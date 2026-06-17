# Deterministic Dispatch 与 Reduction Control

状态：curated。  
父页：[Bitwise 确定性与数值等价](../bitwise_determinism.md)。

## 契约

deterministic mode 必须控制 kernel/backend dispatch 和 reduction geometry。只设置随机种子不够；如果 dispatcher 仍可选择不同 autotune candidate、split-K、atomic reduction、backend fallback 或 warmup 状态，输出仍可能变化。

## 机制

常见发散源是“可变但未被 deterministic contract 管住”的执行路径：autotuner 在数值不等价 candidate 中选择；split-K 或 atomic reduction 改变累加顺序；fast kernel 使用非 bitwise stable reduction；首次请求触发 JIT、CUDA graph capture 或 allocator/cache warmup；hardware-specific dispatcher 从 CSV/heuristic 中选出不同策略。

## Source Evidence

| Source | 证据 | 炼化结论 |
| --- | --- | --- |
| [#25194](https://github.com/vllm-project/vllm/issues/25194), [#25197](https://github.com/vllm-project/vllm/pull/25197) | Triton `_chunk_cumsum_fwd_kernel` 中 `BLOCK_H=1` 与 `BLOCK_H>1` 输出不同；PR 直接移除 `BLOCK_H=1` autotune config。 | autotune candidate 必须先证明数值等价，不能只按速度进入候选集。 |
| [#35183](https://github.com/vllm-project/vllm/pull/35183) | ROCm skinny GEMM 拆成 deterministic store-then-reduce 与 fast `atomicAdd` path，默认 deterministic，fast path 需显式 opt-in。 | deterministic 与 fast path 应拆开，而不是用同一个 kernel 隐式切换。 |
| [#42240](https://github.com/vllm-project/vllm/pull/42240) | AITER FP8 block-scaled GEMM 强制 `splitK=0`，绕开 split-K atomic floating-point add 的非结合累加。 | split-K / atomic reduction 是 deterministic contract 的直接控制点。 |
| [#25404](https://github.com/vllm-project/vllm/issues/25404), [#25603](https://github.com/vllm-project/vllm/pull/25603) | 提供 kernel-level deterministic override plumbing，让 C++/Python kernel 都可接入 deterministic launch。 | deterministic mode 需要 per-kernel override，而不是一个全局模糊开关。 |
| [#33537](https://github.com/vllm-project/vllm/pull/33537) | batch invariant mode 下首次真实请求可能受 CUDA graph、Triton JIT、cache warming 影响；PR 增加 warmup automation。 | first request 与 steady state 都要纳入验证。 |

## Fix Pattern

1. 枚举 deterministic mode 下所有可变 dispatch 点。
2. 移除数值不等价 autotune candidate，或把它们降为 fast opt-in path。
3. 固定 reduction geometry：split-K、block size、atomic path、store-then-reduce。
4. 对首次请求、warmup 后请求、CUDA graph capture 前后分别测试。
5. 文档中写清 deterministic path 的性能代价和 hardware/backend 边界。

## Open Review Queue

继续复核 `kernel_autotune_reduction` cluster 中是否存在只被 benchmark 证明、但没有 exact/token equality 证明的 fast path。
