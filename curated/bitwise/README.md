# Bitwise 确定性与数值等价

状态：curated seed page，基于代表性 raw issue/PR body 生成并持续复核。  
范围：bitwise invariance、deterministic output、batch-size invariance、prefix-cache equivalence，以及可能翻转 greedy decoding 的 numerical drift。

## 核心 Lesson

在 vLLM 中，bitwise issue 很少只是“浮点噪声”。它们通常暴露的是 request state、KV cache identity、backend routing、GEMM tiling、quantization scale/layout 或 kernel launch geometry 之间的契约不一致。单个 kernel test 里 1 ULP 的差异可能看似无害，但一旦写入 KV cache 或 logits，就可能在后续层中放大，并在 `temperature=0` 时翻转 `argmax`。

## 机制页

- [Prefix Cache 等价](prefix_cache_equivalence.md)
- [Batch Invariance 与 Kernel Geometry](batch_invariance_kernel_geometry.md)
- [并发下的 KV Cache Identity](kv_cache_identity_concurrency.md)
- [量化与 Dtype 数值语义](quant_dtype_numerical_semantics.md)
- [Bitwise 工作的验证契约](verification_contracts.md)
- [Deterministic Dispatch 与 Reduction Control](deterministic_dispatch_reduction.md)
- [对 Kernel 优化的约束](implications_for_kernels.md)

本地复核队列 `curated/bitwise_review_queue.*` 属于可再生候选材料，不提交到 GitHub。稳定结论进入本页、机制页和必要的桥接页；待复核 claim 进入 [candidates/bitwise_ledger.csv](../../candidates/bitwise_ledger.csv)。

## 稳定机制族

本页只保留机制族级入口，避免把专题入口变成长表。具体 issue/PR、patch、验证和适用边界维护在各机制页；仍是 `include_with_boundary`、`defer` 或 `unresolved_review_risk` 的条目只进入 [next.md](next.md) 或机制页边界段。

| 机制族 | 已稳定结论 | 机制页 |
| --- | --- | --- |
| dispatch / reduction | autotune candidate、split-K、atomic reduction、cuBLAS/workspace 和 backend selector 都必须进入 deterministic contract；fast path 不能借用 deterministic path 的 correctness claim。 | [Deterministic Dispatch 与 Reduction Control](deterministic_dispatch_reduction.md) |
| batch / kernel geometry | batch composition 不能改变同一请求的 kernel geometry、attention path、MoE tile 或 quantized matmul config；BI mode 必须能真正到达固定几何路径。 | [Batch Invariance 与 Kernel Geometry](batch_invariance_kernel_geometry.md) |
| KV / metadata identity | KV block、block table、persistent buffer、offload store、LoRA adapter 和 external cache key 都必须携带足够身份维度，不能跨请求或跨生命周期复用错误内容。 | [并发下的 KV Cache Identity](kv_cache_identity_concurrency.md) |
| quant / dtype semantics | 低精度路径的 dtype guard、scale layout、fusion math dtype、LoRA activation 和 loading lifetime 都是数值语义的一部分，不能只按“kernel 能跑”判断。 | [量化与 Dtype 数值语义](quant_dtype_numerical_semantics.md) |
| prefix-cache equivalence | cache miss、cache hit、cache bypass 与 Mamba metadata replay 要保持 token/logprob/metadata identity；open 的默认 exact reproducibility 问题先按契约边界维护。 | [Prefix Cache 等价](prefix_cache_equivalence.md) |
| verification contracts | 每条结论必须声明保护对象和比较契约：bit-identical、strict tolerance、logprob ranking、token equality、KV identity、metadata identity 或 semantic only。 | [Bitwise 工作的验证契约](verification_contracts.md) |

## 主线核心缺口

- runtime same-name LoRA reload 已接近内容派生的本地 prefix-cache version identity 修法闭环；截至 2026-06-21，[#45981](https://github.com/vllm-project/vllm/pull/45981) 仍 open，reviewers 仍处于 awaiting requested review，尚无 maintainer/reviewer 的实质反馈，因此当前缺口更准确地说是 merge 与 source/deployment 边界被上游接受：[#42125](https://github.com/vllm-project/vllm/issues/42125)、[#45981](https://github.com/vllm-project/vllm/pull/45981)。
- external KV connector 仍缺跨仓统一的 adapter identity/version schema；截至 2026-06-21，[#45549](https://github.com/vllm-project/vllm/pull/45549) 与 [LMCache #2962](https://github.com/LMCache/LMCache/pull/2962) 都仍 open，且没有新的 acceptance signal，因此当前不只是“还没合并”，而是 schema 应由哪一层 key 充当 single source of truth 仍在收敛：[#44250](https://github.com/vllm-project/vllm/issues/44250)、[#45549](https://github.com/vllm-project/vllm/pull/45549)、[LMCache #2962](https://github.com/LMCache/LMCache/pull/2962)。
- loading-lifetime 主线的 family closure 已基本收敛为“iterator-side `clone()` 保 correctness、eager loader 改 streaming 收 memory/perf”；从当前 main 代码路径看，原始 shared-buffer alias 链在默认加载路径上已被 `clone()` 机械切断，但截至 2026-06-21，[#38991](https://github.com/vllm-project/vllm/issues/38991) 本体仍 open/0 comments，且没有 direct issue-level closure 或 exact unified-memory regression coverage。

## 辅助边界

- prefix-cache 默认 exact reproducibility 契约、same-step sharing 假说、eager-vs-BI contract，以及 open workaround、support-gate、selector fallback、warmup、test-soundness 等辅助项，统一维护在 [next.md](next.md)。
- 这些条目只有在出现 linked fix、maintainer closure、changed files 或 regression test，并且会直接改变主线判断时，才升回专题入口。

## 反例 / 排除项

- [#33179](https://github.com/vllm-project/vllm/pull/33179)：closed/unmerged 且被 maintainer 直接反驳的 gfx950 FP8 FNuz 归因，不得继续当作 `#33123` 的 dtype 修复证据。

## 抽取规则

- 始终记录比较契约：bit-identical、`torch.equal`、`assert_close`、logprob tolerance 或 semantic answer equivalence。
- 区分 deterministic numerical drift 与 random nondeterminism；两者都是 correctness bug，但指向不同根因。
- 对 cache 相关 case，比较 full-prefill、prefix-hit、prefix-miss、offload-restore 和 concurrent request path。
- 对 quantized kernel，记录 dtype、scale layout、tile shape、`split_k`、`block_m`、TP/EP shape 和 backend。
- 不要只凭 closed state 把 bitwise issue 判定为 solved；必须有 linked PR、maintainer comment 或 reproduced verification。
