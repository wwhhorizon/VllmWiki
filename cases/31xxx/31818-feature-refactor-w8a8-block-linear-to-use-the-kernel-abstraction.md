# vllm-project/vllm#31818: [Feature]: Refactor W8A8 Block Linear to use the kernel abstraction

| 字段 | 值 |
| --- | --- |
| Issue | [#31818](https://github.com/vllm-project/vllm/issues/31818) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Refactor W8A8 Block Linear to use the kernel abstraction

### Issue 正文摘录

### 🚀 The feature, motivation and pitch #27814 refactors per-tensor and per-token fp8 scaled mm to use the kernel abstraction (finally, thanks @vllmellm and @tjtanaa for the hard work). We should also add the group quantization to that as a follow up and make sure it is included in the same kernel picker to reduce complexity (`QuantKey` is already used to distinguish quantization types). ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: feature, motivation and pitch #27814 refactors per-tensor and per-token fp8 scaled mm to use the kernel abstraction (finally, thanks @vllmellm and @tjtanaa for the hard work). We should also add the group quantization t...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ature]: Refactor W8A8 Block Linear to use the kernel abstraction feature request;stale ### 🚀 The feature, motivation and pitch #27814 refactors per-tensor and per-token fp8 scaled mm to use the kernel abstraction (final...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: [Feature]: Refactor W8A8 Block Linear to use the kernel abstraction feature request;stale ### 🚀 The feature, motivation and pitch #27814 refactors per-tensor and per-token fp8 scaled mm to use the kernel abstraction (fi...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
