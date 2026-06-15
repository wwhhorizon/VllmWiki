# vllm-project/vllm#15948: [Feature]: Add Maximum Output Length Limitation at Request Level

| 字段 | 值 |
| --- | --- |
| Issue | [#15948](https://github.com/vllm-project/vllm/issues/15948) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Add Maximum Output Length Limitation at Request Level

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Currently, when a request is made, the system only checks that the sum of input token length and max_tokens doesn't exceed the model's maximum length. This allows requests with extremely large max_tokens values to be accepted, which can lead to: - Resource starvation for other concurrent requests - Increased latency across the system Add a new engine parameter: max_output_len This parameter would be enforced during request validation ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions. PR: https://github.com/vllm-project/vllm/pull/14553

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: Add Maximum Output Length Limitation at Request Level feature request;stale ### 🚀 The feature, motivation and pitch Currently, when a request is made, the system only checks that the sum of input token length...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: ead to: - Resource starvation for other concurrent requests - Increased latency across the system Add a new engine parameter: max_output_len This parameter would be enforced during request validation ### Additional cont...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: cks that the sum of input token length and max_tokens doesn't exceed the model's maximum length. This allows requests with extremely large max_tokens values to be accepted, which can lead to: - Resource starvation for o...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
