# vllm-project/vllm#12878: [RFC]: Is IntermediateTensors shared across all request_ids or different for each request_id?

| 字段 | 值 |
| --- | --- |
| Issue | [#12878](https://github.com/vllm-project/vllm/issues/12878) |
| 状态 | closed |
| 标签 | RFC;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Is IntermediateTensors shared across all request_ids or different for each request_id?

### Issue 正文摘录

### Motivation. Hi, I have a unique usecase where for each new request (unique request_id), at decoding step i, I want to store hidden_states returned by model at step i and use them when decoding the output tokens for step i+1 and so on.. ### Proposed Change. Given that for different prompts/request, hidden_states can be different, I was wondering whether using IntermediateTenors is the best data structure to use? Or do you have suggestions for a more simplified storage structure: something which stores the current hidden state for each request id and then deletes that from memory once that request has been served fully. ### Feedback Period. _No response_ ### CC List. _No response_ ### Any Other Things. _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [RFC]: Is IntermediateTensors shared across all request_ids or different for each request_id? RFC;stale ### Motivation. Hi, I have a unique usecase where for each new request (unique request_id), at decoding step i, I w...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: quest_id), at decoding step i, I want to store hidden_states returned by model at step i and use them when decoding the output tokens for step i+1 and so on.. ### Proposed Change. Given that for different prompts/reques...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
