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

本地复核队列 `curated/bitwise_review_queue.*` 属于可再生候选材料，不提交到 GitHub。稳定结论进入本页和六个机制页；待复核 claim 进入 [candidates/bitwise_ledger.csv](../../candidates/bitwise_ledger.csv)。

## 炼化条目

| 手段/线索 | 修复对象 | 源证据 | Wiki pattern |
| --- | --- | --- | --- |
| deterministic prefix caching：在最后一个 block 边界拆分 cache-miss prefill | cache miss 使用 `M=N`，cache hit 只算 suffix `M=N % block_size`；不同 `M` 可能选择不同 ROCm/CUDA tiling 并产生 BF16 累加差异 | [#33123](https://github.com/vllm-project/vllm/issues/33123), [#34046](https://github.com/vllm-project/vllm/pull/34046), [#40179](https://github.com/vllm-project/vllm/pull/40179) | scheduler lifecycle; KV cache; bitwise |
| 排除 ROCm gfx950 FP8 FNuz 误归因 | `#33179` PR body 声称 gfx950 应使用 `float8_e4m3fnuz`，但 maintainer 明确指出 Fnuz 只支持 gfx942，MI355/gfx950 使用 CUDA-like FP8 format；该 PR closed/unmerged，不能作为 `#33123` 修复证据 | [#33179](https://github.com/vllm-project/vllm/pull/33179) | dtype/quantization; hardware guard; exclude |
| 移除不稳定 Triton autotune candidate | `_chunk_cumsum_fwd_kernel` 在 `BLOCK_H=1` 与 `BLOCK_H>1` 间输出不同；移除坏 candidate 可消除 Mamba 路径非确定性 | [#25194](https://github.com/vllm-project/vllm/issues/25194), [#25197](https://github.com/vllm-project/vllm/pull/25197) | backend routing; verification |
| 拆分 deterministic 与 fast ROCm skinny GEMM | `atomicAdd` fast reduction 非 bitwise stable；store-then-reduce 可 deterministic | [#35183](https://github.com/vllm-project/vllm/pull/35183), [#34878](https://github.com/vllm-project/vllm/pull/34878) | bitwise; hardware guard |
| 将 `VLLM_BATCH_INVARIANT` 传入 MXFP4 MoE kernel config | MXFP4 MoE 会按 tokens-per-expert 和 SM count 动态选择 `block_m`/`split_k`，batch composition 改变累加顺序 | [#36488](https://github.com/vllm-project/vllm/pull/36488) | MoE/GEMM; dtype/quantization |
| 为 FlashInfer/CUTLASS FP4 MoE 声明 batch-invariant support | invariant code path 已存在但 support gate 返回 false，导致 batch-invariance 模式不可达 | [#42670](https://github.com/vllm-project/vllm/pull/42670) | backend routing; MoE/GEMM |
| 在 batch-invariant mode 下禁用 cascade attention | cascade attention 会按输入 batch 条件性启用，造成 logprob bitwise 差异；merged PR 在 `VLLM_BATCH_INVARIANT=1` 下自动关闭 cascade attention，并用 34/128 prompts fail 到通过的 logprob test 验证 | [#32481](https://github.com/vllm-project/vllm/issues/32481), [#32561](https://github.com/vllm-project/vllm/pull/32561) | batch invariance; attention geometry |
| 清零未初始化 ROCm attention register | inactive lanes 保留 stale `Qlocal`，污染 WMMA attention scores | [#31293](https://github.com/vllm-project/vllm/pull/31293) | metadata/layout; hardware guard |
| 对语义等价要求使用 exact equality | cache/layer identity 应使用 `torch.equal` 或 bit-view equality，而不是宽松 `allclose` | [#29086](https://github.com/vllm-project/vllm/pull/29086) | verification; bitwise |
| 为 fused RoPE + KV cache write 增加 bit-identical tests | 性能优化必须证明 `rtol=0, atol=0`，同时约束 slot mapping，避免 last-write-wins nondeterminism | [#43355](https://github.com/vllm-project/vllm/pull/43355) | metadata/layout; KV cache; verification |
| 把 backend-specific attention score drift 当正确性 bug | ROCm attention 对 Qwen3-VL reranker 有稳定分数偏差；open PR `#39849` 将 gfx9 上已知不稳定的 ROCM_ATTN `mfma4` gqa_ratio 2/4 shapes 路由回 Triton，但它仍是 workaround，不是 native kernel 根因修复 | [#35569](https://github.com/vllm-project/vllm/issues/35569), [#39849](https://github.com/vllm-project/vllm/pull/39849) | backend routing; numerical equivalence |
| 复核 MTP/spec decode 的 kernel selection | MTP eager verification 与普通 decode batch size 不同，issue body 指向 cuBLAS algorithm 与 KV 放大链路；但本地证据缺 linked fix、comments 和 regression test，只能作为待补证线索 | [#42513](https://github.com/vllm-project/vllm/issues/42513) | request lifecycle; backend routing; defer |
| 审计并发/offload 下的 KV cache identity | concurrent prefill、prefix sharing、CPU offload、block allocator pressure 可能返回/恢复错误 KV block | [#37076](https://github.com/vllm-project/vllm/issues/37076), [#39589](https://github.com/vllm-project/vllm/issues/39589), [#31210](https://github.com/vllm-project/vllm/issues/31210) | KV identity; scheduler lifecycle |
| 保持 normalization kernel 的 dtype 语义 | RMSNorm FP8 fusion 需要 FP32 multiply，但 regular RMSNorm 应尊重 weight dtype | [#42325](https://github.com/vllm-project/vllm/issues/42325) | dtype/quantization; activation/norm |
| 把 adapter identity 纳入 cache key | LoRA/adapters 改变 K/V 语义；只按 prompt/base model/name 生成 cache key 会跨 adapter 命中 | [#30931](https://github.com/vllm-project/vllm/issues/30931), [#31069](https://github.com/vllm-project/vllm/pull/31069), [#44250](https://github.com/vllm-project/vllm/issues/44250) | KV cache identity |
| 清零 recycled KV blocks 与 stale metadata tails | 重用 block 或 block-table row 可能保留 stale id/data，导致并发下非确定输出 | [#39146](https://github.com/vllm-project/vllm/issues/39146), [#43741](https://github.com/vllm-project/vllm/pull/43741), [#39589](https://github.com/vllm-project/vllm/issues/39589), [#39591](https://github.com/vllm-project/vllm/pull/39591) | KV identity; metadata layout |
| 增加 per-kernel deterministic dispatch override | deterministic execution 需要 kernel 级 override，因为不同 deterministic 替代方案性能代价差异很大 | [#25404](https://github.com/vllm-project/vllm/issues/25404), [#25603](https://github.com/vllm-project/vllm/pull/25603) | deterministic dispatch |
| 强制 deterministic reduction strategy | split-K 或 atomic reduction 会随 dispatcher choice 改变；deterministic mode 必须固定 reduction geometry | [#42240](https://github.com/vllm-project/vllm/pull/42240), [#35183](https://github.com/vllm-project/vllm/pull/35183) | deterministic dispatch; ROCm kernels |
| 首个真实请求前 warm up deterministic serving | 首次 JIT、CUDA graph capture、allocator/cache warming 会让启动输出不同于 steady state | [#33537](https://github.com/vllm-project/vllm/pull/33537) | verification; dispatch |
| 保持 deterministic weight loading order/lifetime | FP8/NVFP4 权重从共享 streaming buffer 异步加载时，buffer 复用可能造成 corruption | [#38991](https://github.com/vllm-project/vllm/issues/38991) | quant/dtype; loading identity |

## 复核优先级

1. Cache-hit/cache-miss equivalence：#33123、#40179、#34046。
2. MoE/quant kernel 的 batch invariance：#36488、#42670。
3. Triton/ROCm kernel nondeterminism：#25194、#25197、#35183、#31293。
4. 并发/offload 下的 KV identity corruption：#37076、#39589、#31210。
5. Exact verification contracts：#43355、#29086。
6. 新增 gap：#44250/#30931、#39591/#43741、#25404/#25603、#42240、#33537、#38991。

## 抽取规则

- 始终记录比较契约：bit-identical、`torch.equal`、`assert_close`、logprob tolerance 或 semantic answer equivalence。
- 区分 deterministic numerical drift 与 random nondeterminism；两者都是 correctness bug，但指向不同根因。
- 对 cache 相关 case，比较 full-prefill、prefix-hit、prefix-miss、offload-restore 和 concurrent request path。
- 对 quantized kernel，记录 dtype、scale layout、tile shape、`split_k`、`block_m`、TP/EP shape 和 backend。
- 不要只凭 closed state 把 bitwise issue 判定为 solved；必须有 linked PR、maintainer comment 或 reproduced verification。
