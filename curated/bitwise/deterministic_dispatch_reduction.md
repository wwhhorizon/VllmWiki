# Deterministic Dispatch 与 Reduction Control

状态：reviewed seed page。  
父页：[Bitwise 确定性与数值等价](../bitwise_determinism.md)

## 契约

deterministic mode 必须控制 kernel/backend dispatch 和 reduction geometry。只设置随机种子不够；如果 dispatcher 仍可选择 split-K、atomic reduction、不同 autotune candidate 或不同 backend，输出仍可能变化。

## 机制

常见发散源：

- autotune 在多个数值不等价 candidate 中选择。
- split-K 或 atomic reduction 改变累加顺序。
- fast kernel 使用非 bitwise stable reduction。
- backend fallback 因硬件/shape/capability 改变。
- 首次请求触发 JIT、graph capture 或 cache warmup，后续请求走不同路径。

## Curated Case

| Case | 观察 | 优化/修复 |
| --- | --- | --- |
| [#25194](https://github.com/vllm-project/vllm/issues/25194), [#25197](https://github.com/vllm-project/vllm/pull/25197) | Triton `_chunk_cumsum_fwd_kernel` 的 `BLOCK_H=1` candidate 输出不同 | 移除不稳定 autotune candidate |
| [#35183](https://github.com/vllm-project/vllm/pull/35183) | ROCm skinny GEMM fast reduction 使用 `atomicAdd` | 拆分 deterministic store-then-reduce 与 fast opt-in kernel |
| [#25404](https://github.com/vllm-project/vllm/issues/25404), [#25603](https://github.com/vllm-project/vllm/pull/25603) | 需要 per-kernel deterministic override | 暴露 kernel-level deterministic dispatch 控制 |
| [#42240](https://github.com/vllm-project/vllm/pull/42240) | reduction strategy 需要固定 | candidate：继续确认 split-K/dispatch 细节 |
| [#33537](https://github.com/vllm-project/vllm/pull/33537) | 首次请求 warmup 影响 deterministic serving | 在真实请求前稳定 JIT/graph/cache 状态 |

## Fix Pattern

1. 枚举 deterministic mode 下所有可变 dispatch 点。
2. 去掉数值不等价 autotune candidate，或把它们移到 fast opt-in path。
3. 固定 reduction geometry：split-K、block size、atomic path、store-then-reduce。
4. 对首次请求与 steady state 分别测试。
5. 在文档中写清性能代价与开关边界。

## Open Review Queue

使用 [bitwise_review_queue.csv](../bitwise_review_queue.csv) 中 cluster 为 `kernel_autotune_reduction` 或 deterministic dispatch 相关的行。
