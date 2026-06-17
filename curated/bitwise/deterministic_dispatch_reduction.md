# Deterministic Dispatch 与 Reduction Control

状态：curated。  
父页：[Bitwise 确定性与数值等价](../bitwise_determinism.md)。  
范围：autotune candidate、backend dispatch、split-K、atomic reduction、fast/deterministic path 和 warmup 状态。

## 问题定义

deterministic mode 必须控制 kernel/backend dispatch 和 reduction geometry。只设置随机种子不够；如果 dispatcher 仍可选择不同 autotune candidate、split-K、atomic reduction、backend fallback 或 warmup 状态，输出仍可能变化。

## 典型触发条件

- autotuner 在数值不等价 candidate 中选择。
- split-K 或 atomic reduction 改变浮点累加顺序。
- fast kernel 使用非 bitwise stable reduction。
- 首次请求触发 JIT、CUDA graph capture 或 allocator/cache warmup。
- hardware-specific dispatcher 从 CSV/heuristic 中选出不同策略。

## 代表证据

| Source | 证据事实 | 炼化结论 |
| --- | --- | --- |
| [#25194](https://github.com/vllm-project/vllm/issues/25194), [#25197](https://github.com/vllm-project/vllm/pull/25197) | Triton `_chunk_cumsum_fwd_kernel` 中 `BLOCK_H=1` 与 `BLOCK_H>1` 输出不同；PR 直接移除 `BLOCK_H=1` autotune config。 | autotune candidate 必须先证明数值等价，不能只按速度进入候选集。 |
| [#35183](https://github.com/vllm-project/vllm/pull/35183) | ROCm skinny GEMM 拆成 deterministic store-then-reduce 与 fast `atomicAdd` path，默认 deterministic，fast path 需显式 opt-in。 | deterministic 与 fast path 应拆开，而不是用同一个 kernel 隐式切换。 |
| [#42240](https://github.com/vllm-project/vllm/pull/42240) | AITER FP8 block-scaled GEMM 的 CSV dispatcher 可能选择 `splitK >= 2`；CK split-K reduction 通过 atomic floating-point adds 累加 partial K products。PR 在 CK path 强制 `splitK=0`。review comment 指出 direct CK call 与 weight group shape / 128x128 block-size 兼容性相关，后续讨论确认 vLLM wrapper 原本也没有真正把 `block_size` 传给 AITER。 | split-K / atomic reduction 是 deterministic contract 的直接控制点；workaround 还必须约束 weight group shape 和 kernel applicability。 |
| [#25404](https://github.com/vllm-project/vllm/issues/25404), [#25603](https://github.com/vllm-project/vllm/pull/25603) | 提供 kernel-level deterministic override plumbing，让 C++/Python kernel 都可接入 deterministic launch。 | deterministic mode 需要 per-kernel override，而不是一个全局模糊开关。 |
| [#33537](https://github.com/vllm-project/vllm/pull/33537) | batch invariant mode 下首次真实请求可能受 CUDA graph、Triton JIT、cache warming 影响；PR 增加 warmup automation。 | first request 与 steady state 都要纳入验证。 |

## 根因机制

这类问题来自“可变但未被 deterministic contract 管住”的执行路径。dispatcher、autotuner、CSV heuristic 或 graph warmup 为了性能选择不同 kernel；这些 kernel 在数学上近似等价，但在浮点累加顺序、atomic interleaving 或低精度 rounding 上不 bitwise 等价。

## 修复方式

1. 枚举 deterministic mode 下所有可变 dispatch 点。
2. 移除数值不等价 autotune candidate，或把它们降为 fast opt-in path。
3. 固定 reduction geometry：split-K、block size、atomic path、store-then-reduce。
4. 为 kernel 提供 deterministic override，而不是让全局开关停留在调度层。
5. 文档中写清 deterministic path 的性能代价和 hardware/backend 边界。
6. 对 workaround 型 fix，显式写清它绕过了哪个 dispatcher/上游 bug，以及哪些 shape/group-size 才允许调用。

## 验证契约

- 对同一输入 back-to-back 调用 kernel，要求 bit-identical 或明确 strict tolerance。
- 对 serving path 覆盖首次请求、warmup 后请求、CUDA graph capture 前后。
- fast opt-in path 不能借用 deterministic path 的 correctness claim。
- 对 split-K/atomic 修复，要记录 hardware、dtype、backend、kernel config、weight group shape 和 dispatcher source。

## 适用边界

- [#42240](https://github.com/vllm-project/vllm/pull/42240) 是 scoped workaround：强制 `splitK=0` 绕过 CK reduction 问题，直到上游修复；不能外推为所有 AITER block-scaled shape 都安全。
- [#35183](https://github.com/vllm-project/vllm/pull/35183) 的 fast path 是显式性能取舍，不应默认承诺 bitwise stability。
- 与 batch invariance 页交叉：当 batch 改变触发不同 dispatch/reduction，最终归因应落到本机制。

## 仍需补证

- 继续复核 `kernel_autotune_reduction` cluster 中只被 benchmark 证明、但没有 exact/token equality 证明的 fast path。
- 补充 `#35183` deterministic/fast path 的性能边界和 opt-in 文档证据。
