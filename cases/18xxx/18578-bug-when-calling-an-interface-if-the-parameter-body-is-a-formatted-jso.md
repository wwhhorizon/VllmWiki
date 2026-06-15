# vllm-project/vllm#18578: [Bug]: When calling an interface, if the parameter 'body' is a formatted JSON parameter, an error message 'missing body' will be reported

| 字段 | 值 |
| --- | --- |
| Issue | [#18578](https://github.com/vllm-project/vllm/issues/18578) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: When calling an interface, if the parameter 'body' is a formatted JSON parameter, an error message 'missing body' will be reported

### Issue 正文摘录

### Your current environment java langchain ### 🐛 Describe the bug { "model": "xxx", "messages": [{ "role": "system", "content": "hello" }], "temperature": 0.0, "stream": "false" } java langchain ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: When calling an interface, if the parameter 'body' is a formatted JSON parameter, an error message 'missing body' will be reported bug;stale ### Your current environment java langchain ### 🐛 Describe the bug { "m...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ain ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: : "system", "content": "hello" }], "temperature": 0.0, "stream": "false" } java langchain ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at th...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ted JSON parameter, an error message 'missing body' will be reported bug;stale ### Your current environment java langchain ### 🐛 Describe the bug { "model": "xxx", "messages": [{ "role": "system", "content": "hello" }],...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
