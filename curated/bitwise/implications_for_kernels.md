# 对 Kernel 优化的约束

状态：curated bridge。  
父页：[Bitwise 确定性与数值等价](README.md)。
范围：把 bitwise / deterministic 结论翻译成后续 kernel 优化时必须保留的不变量；本文不是 kernel 优化方法论，也不替代各机制页的证据。

## 问题定义

很多 bitwise issue 最后都落到 kernel dispatch、tiling、reduction、metadata 或 dtype path。后续做 kernel 优化时，不能只比较吞吐和宽松 tolerance，还要明确优化是否改变了同一请求的执行几何、累加顺序、cache 身份或验证契约。

## 优化不变量

| 约束 | 来自哪类 bitwise 结论 | 对 kernel 优化的含义 |
| --- | --- | --- |
| 固定 reduction order | split-K、atomicAdd、store-then-reduce、cuBLAS workspace | fast reduction 可以存在，但 deterministic path 必须固定累加顺序；fast opt-in 不能复用 deterministic correctness claim。 |
| 固定 batch-sensitive geometry | `block_m`、`split_k`、tokens-per-expert、attention 2D/3D path、FA2 split count | 同一请求在 batch=1、混 batch、并发 prefill/decode 下不能因为旁路请求改变 tile 或 backend path。 |
| autotune candidate 先证数值等价 | Triton autotune、CSV/heuristic selector、hardware-specific backend fallback | 候选 kernel 进入 autotune 前要有 exact 或明确 strict-tolerance 证据；只按 benchmark 更快不能进入 deterministic candidate set。 |
| metadata 来源单一 | per-layer Q-head、plan-time scratch、CUDA graph persistent buffer、block table tail | kernel launch 前的 plan/scratch/tile budget 必须来自 runtime 实际使用的同一语义来源；不能用 model-wide config 代替 served layer shape。 |
| cache identity 完整 | KV block、LoRA adapter、external KV key、offload store、block reuse | 优化不能让不同请求、adapter、dtype 生命周期或 cache group 共享同一个逻辑 KV 身份；如果复用物理 block，必须清理 stale data 和 metadata。 |
| dtype/reference boundary 明确 | FP8/FP4/MXFP4 scale layout、RMSNorm multiply dtype、LoRA original activation | fused/quantized kernel 要声明 reference 是 native dtype、FP32 还是 composite path；更高精度或更快都不能自动等价。 |
| selector 和 support gate 同步 | BI mode backend list、FlashInfer/CUTLASS support gate、known-bad shape fallback | 有 deterministic kernel 不够，selector/oracle 必须让它在目标模式下可达；workaround 要写清硬件、shape 和 fallback path。 |
| 测试保护对象明确 | bit equality、logprob ranking、token equality、metadata identity、semantic answer | kernel test 不能只用 semantic output 或宽松 `allclose` 支撑 bitwise claim；beam/ranking/cache identity 需要更强契约。 |

## 代表证据

| Source | 约束事实 | 对 kernel 优化的含义 |
| --- | --- | --- |
| [#25194](https://github.com/vllm-project/vllm/issues/25194), [#25197](https://github.com/vllm-project/vllm/pull/25197) | `_chunk_cumsum_fwd_kernel` 的不同 autotune candidate 会给出不同数值输出，最终修复是移除不稳定 candidate。 | autotune 空间不是纯性能空间；候选加入前必须先证明数值等价。 |
| [#35183](https://github.com/vllm-project/vllm/pull/35183) | ROCm skinny GEMM 将 deterministic store-then-reduce 与 fast `atomicAdd` path 拆开。 | 优化可以保留 fast path，但 deterministic path 要独立命名、独立验证、独立 opt-in/opt-out 语义。 |
| [#36488](https://github.com/vllm-project/vllm/pull/36488), [#40408](https://github.com/vllm-project/vllm/pull/40408) | MXFP4 MoE 和 Cutlass FP8 都要求 batch-invariant mode 下 kernel config 不随 `M`、tokens-per-expert 或 batch composition 改变。 | 低精度 fast kernel 能进入 BI mode 的前提是 fixed-config；后续 tuning 一旦重新依赖 shape，就要重跑 bitwise 验证。 |
| [#41651](https://github.com/vllm-project/vllm/issues/41651), [#42650](https://github.com/vllm-project/vllm/pull/42650) | FlashInfer/Triton attention metadata 使用 model-wide head count，和 runtime per-layer Q-head 不一致，导致 plan/scratch 错误。 | kernel 优化中的 metadata builder 必须和实际 served layer shape 同源；否则 kernel 本身再 deterministic 也会稳定地读写错误几何。 |

## 机制映射

- [Deterministic Dispatch 与 Reduction Control](deterministic_dispatch_reduction.md)：负责 reduction order、autotune、selector、compile/cuBLAS 和 metadata launch contract。
- [Batch Invariance 与 Kernel Geometry](batch_invariance_kernel_geometry.md)：负责 batch composition 是否改变 kernel config、attention path、MoE tile 或 quantized matmul path。
- [量化与 Dtype 数值语义](quant_dtype_numerical_semantics.md)：负责 dtype guard、scale layout、fusion math dtype、FP8/FP4 fast path 和 loading lifetime。
- [并发下的 KV Cache Identity](kv_cache_identity_concurrency.md)：负责 KV block、adapter、external cache、offload 和 reuse 的身份边界。
- [Bitwise 工作的验证契约](verification_contracts.md)：负责把优化目标翻译成 exact equality、strict tolerance、logprob/token equality 或 metadata identity。

## 适用边界

本文只总结已经在 bitwise 主线中反复出现的约束，不新增独立 claim。若后续 kernel 优化发现新约束，应先进入对应机制页和 ledger；只有证据稳定后，再把不变量抽到本文。

对性能优化而言，允许存在更快但非 bitwise 的路径，但必须显式分离：默认 deterministic / batch-invariant 路径保持可验证，fast path 需要 opt-in、边界说明和独立测试。
