# vllm-project/vllm#22966: [Feature]: any way to config the prefix of chatcmpl-tool?

| 字段 | 值 |
| --- | --- |
| Issue | [#22966](https://github.com/vllm-project/vllm/issues/22966) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: any way to config the prefix of chatcmpl-tool?

### Issue 正文摘录

### 🚀 The feature, motivation and pitch When using vllm generated tool_call message, then send the response to OpenAI, it report: ``` messages[2].tool_calls[0].id': string too long. Expected a string with maximum length 40, but got a string with length 46 instead. ``` This because of the random_tool_id using format: `chatcmpl-tool-{uuid}`, any way to config the prefix? ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Feature]: any way to config the prefix of chatcmpl-tool? feature request;stale ### 🚀 The feature, motivation and pitch When using vllm generated tool_call message, then send the response to OpenAI, it report: ``` messa...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: any way to config the prefix of chatcmpl-tool? feature request;stale ### 🚀 The feature, motivation and pitch When using vllm generated tool_call message, then send the response to OpenAI, it report: ``` messa...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
