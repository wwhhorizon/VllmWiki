# vllm-project/vllm#31821: [Feature]: Change min_capability to is_supported in the kernel abstraction

| 字段 | 值 |
| --- | --- |
| Issue | [#31821](https://github.com/vllm-project/vllm/issues/31821) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Change min_capability to is_supported in the kernel abstraction

### Issue 正文摘录

### 🚀 The feature, motivation and pitch In the `MPLinearKernel` kernel abstraction (marlin, machete), whether a kernel is supported on a platform is determined by querying the `get_min_capability`, e.g. https://github.com/bigPYJ1151/vllm/blob/main/vllm/model_executor/layers/quantization/kernels/mixed_precision/__init__.py#L87-L96 On the other hand, `ScaledMMLinearKernel` (int8) recently (#26668) transitioned to using `is_supported`, which is more extensible to other platforms and reasons for a kernel being supported or not. We should transition the `MPLinearKernel` and also make sure any new uses of the kernel abstraction use `is_supported` instead of `get_min_capability`. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: https://github.com/bigPYJ1151/vllm/blob/main/vllm/model_executor/layers/quantization/kernels/mixed_precision/__init__.py#L87-L96 On the other hand, `ScaledMMLinearKernel` (int8) recently (#26668) transitioned to using `...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Feature]: Change min_capability to is_supported in the kernel abstraction feature request;stale ### 🚀 The feature, motivation and pitch In the `MPLinearKernel` kernel abstraction (marlin, machete), whether a kernel is...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: Change min_capability to is_supported in the kernel abstraction feature request;stale ### 🚀 The feature, motivation and pitch In the `MPLinearKernel` kernel abstraction (marlin, machete), whether a kernel is supported o...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: 151/vllm/blob/main/vllm/model_executor/layers/quantization/kernels/mixed_precision/__init__.py#L87-L96 On the other hand, `ScaledMMLinearKernel` (int8) recently (#26668) transitioned to using `is_supported`, which is mo...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: /vllm/blob/main/vllm/model_executor/layers/quantization/kernels/mixed_precision/__init__.py#L87-L96 On the other hand, `ScaledMMLinearKernel` (int8) recently (#26668) transitioned to using `is_supported`, which is more...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
