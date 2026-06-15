# vllm-project/vllm#26778: [Feature]: Configure the kv_event endpoint to clarify user behavior

| 字段 | 值 |
| --- | --- |
| Issue | [#26778](https://github.com/vllm-project/vllm/issues/26778) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Configure the kv_event endpoint to clarify user behavior

### Issue 正文摘录

### 🚀 The feature, motivation and pitch When set different style `endpoint` value, different effects will appear; when i set this value is `tcp://localhost:5557` it to connect this zmq, but when it set this value is `tcp://*:5557` it to bind this zmq. This behavior is a bit confusing. My idea is to use bind by default, but the user can control it to connect. Or, at worst, print a log message notifying the user that the current behavior has changed from bind to connect. @njhill what do you think? https://github.com/vllm-project/vllm/blob/fd85c9f4263de8cf9bc9f51bef9471344436614c/vllm/distributed/kv_events.py#L227-L235 ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Feature]: Configure the kv_event endpoint to clarify user behavior feature request ### 🚀 The feature, motivation and pitch When set different style `endpoint` value, different effects will appear; when i set this value...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ature]: Configure the kv_event endpoint to clarify user behavior feature request ### 🚀 The feature, motivation and pitch When set different style `endpoint` value, different effects will appear; when i set this value is...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
