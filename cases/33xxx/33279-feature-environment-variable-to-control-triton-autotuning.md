# vllm-project/vllm#33279: [Feature]: Environment Variable to Control Triton Autotuning

| 字段 | 值 |
| --- | --- |
| Issue | [#33279](https://github.com/vllm-project/vllm/issues/33279) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Environment Variable to Control Triton Autotuning

### Issue 正文摘录

### Motivation - Triton kernel parameters are **not one-size-fits-all** across hardware platforms. Fixed defaults can result in **very slow out-of-the-box performance** on certain systems. - Runtime autotuning is required for performance portability, but it can introduce **non-determinism, increased startup time, and incompatibilities** with static execution paths. These issues have surfaced repeatedly in the project: - Non-deterministic behavior caused by Triton autotuning: [#25194](https://github.com/vllm-project/vllm/issues/25194) - Slow startup time: [#19824](https://github.com/vllm-project/vllm/issues/19824), [#20342](https://github.com/vllm-project/vllm/issues/20342) - Backend instability and crashes involving Triton kernels: [#26381](https://github.com/vllm-project/vllm/issues/26381) Currently, autotuning behavior is implicit and not user-controllable, making it difficult to balance performance, stability, and reproducibility. ### Proposal Introduce an environment variable (e.g., `VLLM_TRITON_AUTOTUNE`) to explicitly enable or disable Triton autotuning, **defaulting to disabled**. The intended workflow is: - Enable autotuning intentionally for benchmarking or calibration -...

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: tion paths. These issues have surfaced repeatedly in the project: - Non-deterministic behavior caused by Triton autotuning: [#25194](https://github.com/vllm-project/vllm/issues/25194) - Slow startup time: [#19824](https...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: [Feature]: Environment Variable to Control Triton Autotuning feature request;stale ### Motivation - Triton kernel parameters are **not one-size-fits-all** across hardware platforms. Fixed defaults can result in **very s...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: xecution paths. These issues have surfaced repeatedly in the project: - Non-deterministic behavior caused by Triton autotuning: [#25194](https://github.com/vllm-project/vllm/issues/25194) - Slow startup time: [#19824](h...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: equired for performance portability, but it can introduce **non-determinism, increased startup time, and incompatibilities** with static execution paths. These issues have surfaced repeatedly in the project: - Non-deter...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: Environment Variable to Control Triton Autotuning feature request;stale ### Motivation - Triton kernel parameters are **not one-size-fits-all** across hardware platforms. Fixed defaults can result in **very s...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
