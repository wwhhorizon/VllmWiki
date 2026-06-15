# vllm-project/vllm#11050: [Feature]: logging request_id instead of random uuid

| 字段 | 值 |
| --- | --- |
| Issue | [#11050](https://github.com/vllm-project/vllm/issues/11050) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: logging request_id instead of random uuid

### Issue 正文摘录

### 🚀 The feature, motivation and pitch vLLM now supports the x-request-id header, as discussed in this issue: https://github.com/vllm-project/vllm/issues/9593. However, during the completion process, a random ID is still being used. Could we consider using the x-request-id instead? This change would enhance our ability to trace requests more effectively. For reference, see the current implementation here: https://github.com/vllm-project/vllm/blob/main/vllm/entrypoints/openai/serving_completion.py#L89 `request_id = f"cmpl-{random_uuid()}" : ` ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature]: logging request_id instead of random uuid feature request ### 🚀 The feature, motivation and pitch vLLM now supports the x-request-id header, as discussed in this issue: https://github.com/vllm-project/vllm/is...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
