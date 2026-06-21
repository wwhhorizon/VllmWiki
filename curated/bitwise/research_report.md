# Bitwise / Deterministic 调研报告

状态：组会汇报稿。  
范围：基于当前 VllmWiki 已精读和炼化的 bitwise / deterministic 主线，不新增未复核结论。  
时间：2026-06-21。

## 一、VllmWiki 方法论

VllmWiki 的目标不是把 vLLM issue 自动分类成表格，而是把 issue、PR、review comment、patch diff 和测试信息炼化成可复用的工程知识。它参考 KernelWiki 的组织方式：原始证据留在 source layer，公开仓库只保留经过复核的结论层、候选 ledger 和维护契约。

当前 bitwise 主线的处理流程是：

1. 先从全量 issue/PR 语料中筛选候选。早期 source snapshot 覆盖约 15,818 个 unique issues、8,931 个 unique PRs 和 145,553 条 pattern evidence rows，但全量层评论正文缺口较大，因此不能只凭关键词或表格字段下结论。
2. 对 bitwise / deterministic 主线定向补抓 issue comments、PR files、review comments、reviews、timeline 等证据。
3. 每个 claim 进入 `candidates/bitwise_ledger.csv`，标注 `include`、`defer`、`exclude` 以及 `stable`、`include_with_boundary`、`unresolved_review_risk`、`defer_blocked` 等风险状态。
4. promotion 必须读原始内容：issue body、PR body、changed files、review comments 和测试。只有 root cause、fix、verification、scope boundary 都被证据支撑，才进入机制页。
5. review comment 暴露但尚未被 patch/test/maintainer resolution 闭环的问题，只写成 boundary 或 risk，不写成已修复事实。
6. 稳定结论下沉到 `curated/bitwise/*.md`；待复核内容留在 ledger 和 `next.md`，避免专题入口变成未闭环问题堆叠。

分类本身也遵循开放 taxonomy。当前 6 类机制族是对已精读证据的阶段性稳定压缩，不宣称覆盖未来所有 bitwise 问题。如果新的 claim 不能自然映射到现有机制，且有独立 root cause、fix pattern 和 verification contract，就先保持 `defer` 并记录分类缺口，而不是为了目录稳定硬塞进旧类。

因此，VllmWiki 的核心产物不是“issue 列表”，而是机制化知识：某类 bitwise 问题为什么发生、修复方式是什么、验证应该保护什么对象、适用边界在哪里。

## 二、Bitwise 调研结果

### 2.1 总结论

vLLM 的 bitwise / deterministic 问题通常不是普通浮点噪声，也不只是随机种子没有固定。它们更常见的根因是 execution contract 缺失：同一个请求在不同 cache 状态、batch composition、backend path、kernel config、dtype path 或 metadata 生命周期下，实际执行了不同的计算。

这类差异在单个 kernel 里可能只是 1 ULP 或 `1e-5` 级 logprob drift，但一旦写入 KV cache、logits 或 beam ranking，就可能在后续 decode 中放大，并在 `temperature=0` 下翻转 `argmax`。因此 bitwise 调研的重点不是“数值误差有多小”，而是“这个误差是否改变了 serving 语义”。

当前结果已经收敛成 6 类稳定机制族。这里的“稳定”指它们能覆盖当前已炼化的 bitwise 主线证据，并不表示这是永久封闭全集：

| 机制族 | 调研结论 |
| --- | --- |
| deterministic dispatch / reduction | autotune candidate、split-K、atomic reduction、cuBLAS workspace、backend selector 和 metadata builder 都必须进入 deterministic contract。 |
| batch invariance / kernel geometry | 同一请求不能因为旁路请求改变 kernel geometry、attention path、MoE tile、quantized matmul config 或 compile/graph support gate。 |
| KV / metadata identity | KV block、block table、persistent buffer、offload store、LoRA adapter、external KV key 都必须携带足够身份维度。 |
| quant / dtype semantics | 低精度路径中的 dtype guard、scale layout、fusion math dtype、LoRA activation、loading lifetime 都是数值语义的一部分。 |
| prefix-cache equivalence | cache miss、cache hit、cache bypass 与 Mamba metadata replay 必须保持 token、logprob 和 metadata identity。 |
| verification contracts | 每条 bitwise claim 必须声明保护对象：bit equality、strict tolerance、logprob ranking、token equality、KV identity、metadata identity 或 semantic equivalence。 |

### 2.2 Deterministic dispatch / reduction：确定性首先要管住执行路径

最直接的发现是：deterministic 不是“设置 seed”就结束，而是必须控制 dispatcher、autotuner、backend selector 和 reduction geometry。

代表案例：

| Source | 现象 | 结论 |
| --- | --- | --- |
| [#25194](https://github.com/vllm-project/vllm/issues/25194) / [#25197](https://github.com/vllm-project/vllm/pull/25197) | Triton `_chunk_cumsum_fwd_kernel` 的不同 autotune candidate 会产生不同数值输出，最终修复是移除不稳定 candidate。 | autotune 空间不是纯性能空间，candidate 进入前必须证明数值等价。 |
| [#35183](https://github.com/vllm-project/vllm/pull/35183) | ROCm skinny GEMM 拆成 deterministic store-then-reduce path 和 fast `atomicAdd` path。 | fast path 可以存在，但必须和 deterministic path 明确分离，不能复用 deterministic correctness claim。 |
| [#27660](https://github.com/vllm-project/vllm/pull/27660) | `torch.compile` 路径需要显式控制 cuBLAS reduced-precision、split-K、workspace 和 AOT compile 边界。 | compile/eager 不是判断标准；真正要管的是 reduction order、workspace algorithm 和 trace side effect。 |
| [#41651](https://github.com/vllm-project/vllm/issues/41651) / [#42650](https://github.com/vllm-project/vllm/pull/42650) | FlashInfer/Triton metadata builder 用 model-wide head count 做 plan/scratch allocation，但 runtime 用 per-layer Q-head。 | metadata builder 也是 dispatch contract；plan-time 和 runtime shape 必须同源。 |

这一类问题对后续 kernel 优化的约束是：优化时可以保留 fast kernel，但必须给 deterministic path 单独的入口、验证和边界。只看吞吐或宽松 `allclose` 不足以证明该 kernel 可以进入 deterministic candidate set。

### 2.3 Batch invariance / kernel geometry：同一请求不能被旁路请求改变

batch invariance 的核心问题是：同一个请求单独运行、与其他请求混 batch、并发 prefill/decode、first request 和 warmup 后运行时，用户可见输出应保持一致。很多失败并不在 sampler，而在 kernel geometry。

代表案例：

| Source | 现象 | 结论 |
| --- | --- | --- |
| [#36488](https://github.com/vllm-project/vllm/pull/36488) | MXFP4 MoE 的 `block_m` / `split_k` 会随 tokens-per-expert 和 SM count 改变。 | batch-invariant mode 必须传到实际 kernel config 层。 |
| [#32481](https://github.com/vllm-project/vllm/issues/32481) / [#32561](https://github.com/vllm-project/vllm/pull/32561) | cascade attention 会随 batch 条件性启用，造成 logprob 数值差异。 | 条件性 attention 优化在 BI mode 下必须被 gate 掉或证明不依赖旁路请求。 |
| [#29581](https://github.com/vllm-project/vllm/issues/29581) / [#38670](https://github.com/vllm-project/vllm/pull/38670) | AWQ 在 BI mode 下仍自动转到 AWQ_Marlin，绕开 deterministic matmul override。 | quantization auto-conversion 也是 BI contract 的一部分；必要时要牺牲 fused kernel 性能回到可控路径。 |
| [#33688](https://github.com/vllm-project/vllm/pull/33688) | TRITON_ATTN 在 BI mode 下强制 2D kernel，避免 decode path 随 batch shape 在 2D/3D kernel 间切换。 | backend support gate 不能只声明“可运行”，还要证明最终 kernel family 固定。 |
| [#40408](https://github.com/vllm-project/vllm/pull/40408) | Cutlass FP8 direct path 可以进入 BI mode，但要求 config independent of `M`。 | fast low-precision path 可以保留，前提是固定 config 并用多 batch/M 维测试证明。 |

关键 insight 是：BI mode 不是简单“走慢路径”。有些 fast path 可以被纳入 BI，有些 fused path 必须绕开，分界线是 kernel geometry、dispatch selector 和 support gate 是否真正固定。

### 2.4 KV / metadata identity：cache 正确性是身份建模问题

KV cache 相关 issue 的共同特征是：错误很容易表现成 nondeterministic token，但根因往往不是随机性，而是请求读到了不属于自己的 KV、metadata 或旧生命周期内容。

代表案例：

| Source | 现象 | 结论 |
| --- | --- | --- |
| [#30931](https://github.com/vllm-project/vllm/issues/30931) / [#31069](https://github.com/vllm-project/vllm/pull/31069) | LoRA prefix cache hash 使用 `lora_name`，同名不同 ID adapter 可能错误共享 cache block。 | adapter identity 是 KV cache key 的必填维度。 |
| [#35219](https://github.com/vllm-project/vllm/pull/35219) | hybrid Mamba/attention 共享 block pool 时，旧 fp32 SSM state 被解释成 fp8/fp16 attention KV，传播 NaN/Inf。 | KV block identity 还包括上一生命周期的 dtype 解释方式；fresh attention block 需要清零。 |
| [#31210](https://github.com/vllm-project/vllm/issues/31210) / [#31341](https://github.com/vllm-project/vllm/pull/31341) | CPU KV offload 在 compute 尚未结束或 copy engine 争用时搬走 KV，导致 restore 后内容错误。 | KV identity 不只看 key/ownership，也包括 copy stream 和 engine-step 时序。 |
| [#39589](https://github.com/vllm-project/vllm/issues/39589) / [#39591](https://github.com/vllm-project/vllm/pull/39591) | variable-length concurrent prefill 暴露 block table tail stale 问题。 | `append_row`、`move_row`、`clear_row` 需要维护“逻辑长度之后必须为零”的 metadata invariant。 |

这一类机制把 KV identity 扩展成一个完整结构：prompt/token range、base model、adapter、dtype、layout、backend、cache group、rank/world、copy stream、生命周期都可能是 key 的一部分。缺任何一维，都可能让请求稳定地读到错误内容。

### 2.5 Quant / dtype semantics：低精度路径要声明 reference boundary

低精度 issue 的共同点是：实现细节往往就是数值语义本身。dtype guard、scale layout、fusion multiply dtype、LoRA activation path 和 weight loading lifetime 都会改变 deterministic 输出。

代表案例：

| Source | 现象 | 结论 |
| --- | --- | --- |
| [#42007](https://github.com/vllm-project/vllm/issues/42007) / [#42120](https://github.com/vllm-project/vllm/pull/42120) | FP8 MoE + LoRA 中，base GEMM 需要量化 activation，LoRA delta 需要原始精度 activation；无 active LoRA 时还要避免 stale mapping。 | LoRA + MoE + FP8 需要同时维护 base path、adapter path 和 token mapping 生命周期。 |
| [#42325](https://github.com/vllm-project/vllm/issues/42325) / [#42379](https://github.com/vllm-project/vllm/pull/42379) | RMSNorm fused path 与 regular path 的 multiply dtype 不一致，造成 BF16 场景明显差异。 | reference boundary 要说清楚是 native dtype、FP32 还是 composite path；更高精度不自动等价。 |
| [#33179](https://github.com/vllm-project/vllm/pull/33179) | PR body 把 gfx950 归为 FP8 Fnuz，但 maintainer 明确反驳，PR closed/unmerged。 | hardware dtype guard 不能只凭 PR body promotion；反例也要进入 wiki，防止错误归因污染后续结论。 |
| [#38991](https://github.com/vllm-project/vllm/issues/38991) 及 [#43163](https://github.com/vllm-project/vllm/issues/43163) / [#43464](https://github.com/vllm-project/vllm/pull/43464) | shared numpy buffer view 与 CUDA async copy 会破坏 weight loading lifetime；iterator-side `clone()` 能切断 alias 链。 | weight loading lifetime 也是 dtype/quant correctness 的一部分；`clone()` 是 correctness fix，streaming loader 是 memory/perf 收口。 |

这一类结果对后续优化很重要：优化一个 fused/quantized kernel 时，不能只证明它更快或更接近 FP32，还要声明它要对齐哪条 reference path。否则“更高精度”也可能破坏既有 serving 语义。

### 2.6 Prefix-cache equivalence：cache hit/miss 的等价要拆成两类根因

prefix cache 相关问题目前收敛成两类：

第一类是计算几何变化。cache miss 通常 full prefill，cache hit 只计算 suffix；不同 `M` 会触发不同 GEMM tiling、backend path 或 accumulation order。第二类是 metadata identity 错误，尤其在 CUDA graph 和 Mamba metadata caching 下，问题可能不是值错了，而是 persistent buffer 地址错了。

代表案例：

| Source | 现象 | 结论 |
| --- | --- | --- |
| [#33123](https://github.com/vllm-project/vllm/issues/33123) | ROCm 上 prefix cache miss 与 hit 在 `temperature=0` 下生成不同 token。 | prefix cache divergence 是用户可见 correctness 问题，不只是 cache 性能问题。 |
| [#40179](https://github.com/vllm-project/vllm/pull/40179) | patch 试图把 cache-miss prefill 拆到 cached block boundary，使 suffix GEMM geometry 与 cache-hit path 对齐。 | 方向成立，但 resumed request、block-aligned prompt、final-token scheduler 约束仍需 follow-up patch。 |
| [#34865](https://github.com/vllm-project/vllm/issues/34865) / [#34874](https://github.com/vllm-project/vllm/pull/34874) | Mamba `"all"` mode 多 cache group 共享 metadata 时，CUDA graph replay 读取的 persistent buffer 仍指向旧 builder。 | prefix metadata identity 不只是 block table 值，还包括 graph replay 会读取的 buffer 地址。 |
| [#42699](https://github.com/vllm-project/vllm/issues/42699) / [#40896](https://github.com/vllm-project/vllm/issues/40896) | open issue 显示 prefix-read/no-prefix-read 或 cold/warm cache 有差异，但 `fp32` 或 `VLLM_BATCH_INVARIANT=1` 可让输出收敛。 | 当前更适合作为默认 prefix-cache exact reproducibility 的契约边界，而不是直接 promotion 为独立 KV corruption。 |

这里最重要的结果是：prefix-cache 问题不能一概归因到 cache key 或 KV state。需要先判断是 suffix GEMM geometry 变化，还是 metadata/persistent-buffer identity 错误。

### 2.7 Verification contracts：先定义保护对象，再谈测试通过

当前调研里反复出现的一个问题是：测试通过不等于 bitwise claim 成立。测试必须先声明保护对象。

| 验证层级 | 适用对象 | 合格证据 |
| --- | --- | --- |
| bit-identical | KV cache、slot mapping、fused write、exact deterministic path | `torch.equal`、bit-view equality、`rtol=0, atol=0` |
| strict numeric tolerance | backend math drift | 明确 tolerance，并记录 dtype/backend/hardware |
| logprob/token equality | deterministic decoding 可见行为 | `temperature=0` token 一致，必要时检查 logprob ranking |
| metadata identity | CUDA graph persistent buffer、block table、slot mapping | storage/data pointer 指向当前生命周期对象，且逻辑值正确 |
| token-prefix identity | decode/prefill consistency、logprob replay | 使用 token ids，而不是 decode 后文本再 encode |
| semantic equivalence | 高层 eval 或非确定 sampling | 只能作为补充，不能单独支撑 bitwise claim |

代表证据：

- [#29086](https://github.com/vllm-project/vllm/pull/29086)：`torch.allclose` 被 revert 回 `torch.equal`，说明 layer/cache identity 不能用近似相等替代。
- [#34874](https://github.com/vllm-project/vllm/pull/34874)：Mamba metadata test 断言 storage/persistent-buffer identity，而不是只比较值。
- [#43317](https://github.com/vllm-project/vllm/pull/43317)：decode/prefill consistency 如果用文本 roundtrip 重建 prefix，会因为 tokenizer 改写 token ids 产生误报。
- [#43355](https://github.com/vllm-project/vllm/pull/43355)：fused RoPE + KV cache write 的 bit-identical test 有价值，但 FP8 conversion 和 NHD/HND layout risk 未闭环前只能作为 verification boundary。

### 2.8 当前主线缺口

当前未闭环问题并不是“完全不知道根因”，而是证据闭环程度不同：

| Source | 当前判断 | 缺口 |
| --- | --- | --- |
| [#38991](https://github.com/vllm-project/vllm/issues/38991) | shared-buffer lifetime 机制很强；同宗 `#43163/#43464` 已支持 iterator-side `clone()` 作为 accepted correctness fix。 | `#38991` 本体仍缺 direct linked fix / maintainer closure，也缺 exact unified-memory + async copy 的 dedicated regression。 |
| [#42125](https://github.com/vllm-project/vllm/issues/42125) / [#45981](https://github.com/vllm-project/vllm/pull/45981) | runtime same-name LoRA reload 已收敛到 content-derived `lora_cache_key`，并形成 identity 计算、request 传播、block-hash 消费三层闭环。 | PR 仍 open；HF Hub、remote path、rolling upgrade、external KV、TOCTOU 等 deployment boundary 需要上游接受。 |
| [#44250](https://github.com/vllm-project/vllm/issues/44250) / [#45549](https://github.com/vllm-project/vllm/pull/45549) / [LMCache #2962](https://github.com/LMCache/LMCache/pull/2962) | external KV 至少必须携带 adapter 维度，但跨仓 schema 还没统一。 | 需要确认 LoRA 维度最终落在 `CacheEngineKey.tags` 之类的 single source of truth，还是继续多处镜像。 |
| [#40179](https://github.com/vllm-project/vllm/pull/40179) | deterministic prefix caching split 的方向成立。 | 需要 resumed request、block-aligned prompt、final-token-aware boundary 的 follow-up patch 和 regression。 |
| [#42240](https://github.com/vllm-project/vllm/pull/42240) | AITER FP8 `splitK=0` 是 scoped workaround。 | PR merge 状态和上游 AITER deterministic split-K 根因修复仍需追踪；当前不外推到非 128x128 shape。 |
| [#43355](https://github.com/vllm-project/vllm/pull/43355) | verification contract 样例有价值。 | FP8 `qk_t` conversion、NHD layout gate、key/value row guard 需要最终 patch 或 maintainer resolution。 |

### 2.9 对 kernel 优化的直接启示

这次 bitwise 调研对后续 kernel 优化最直接的价值，是把“优化时不能破坏什么”抽成不变量：

| Kernel 优化不变量 | 含义 |
| --- | --- |
| 固定 reduction order | split-K、atomicAdd、store-then-reduce、cuBLAS workspace 都会影响 bitwise；fast reduction 要和 deterministic path 分开。 |
| 固定 batch-sensitive geometry | `block_m`、`split_k`、tokens-per-expert、attention 2D/3D path、FA2 split count 不能随旁路请求改变同一请求输出。 |
| autotune candidate 先证等价 | benchmark 更快不能成为 deterministic candidate 的充分条件。 |
| metadata 来源单一 | plan-time scratch、head count、block table tail、CUDA graph persistent buffer 必须来自 runtime 实际使用的同一语义来源。 |
| cache identity 完整 | 不同 adapter、不同 dtype 生命周期、不同 cache group 或不同请求不能共享同一逻辑 KV 身份。 |
| dtype/reference boundary 明确 | fused/quantized kernel 要声明 reference 是 native dtype、FP32 还是 composite path。 |
| selector/support gate 同步 | 有 deterministic kernel 不够，selector/oracle/support gate 必须让它在目标模式下可达。 |
| 测试保护对象明确 | 不能只用 semantic output 或宽松 `allclose` 支撑 bitwise claim；beam/ranking/cache identity 需要更强契约。 |

整体来看，bitwise 调研已经把 vLLM 的确定性问题从“零散 bug”炼化成了几组工程不变量。后续做 kernel 优化时，性能指标之外必须同步回答：是否改变了同一请求的 reduction order、batch geometry、metadata source、cache identity、dtype reference，以及测试到底保护了什么对象。
