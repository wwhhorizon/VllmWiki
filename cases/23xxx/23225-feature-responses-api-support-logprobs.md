# vllm-project/vllm#23225: [Feature][Responses API] Support logprobs

| 字段 | 值 |
| --- | --- |
| Issue | [#23225](https://github.com/vllm-project/vllm/issues/23225) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature][Responses API] Support logprobs

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Current response API returns empty on logprobs like: https://github.com/vllm-project/vllm/blob/0167efe20d3d2280c3da6aea94a6f59afec5099c/vllm/entrypoints/openai/serving_responses.py#L550 https://github.com/vllm-project/vllm/blob/0167efe20d3d2280c3da6aea94a6f59afec5099c/vllm/entrypoints/openai/serving_responses.py#L897 We need to return the logprobs when users need it. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature][Responses API] Support logprobs feature request;stale ### 🚀 The feature, motivation and pitch Current response API returns empty on logprobs like: https://github.com/vllm-project/vllm/blob/0167efe20d3d2280c3da...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
