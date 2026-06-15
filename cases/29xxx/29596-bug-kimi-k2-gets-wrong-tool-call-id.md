# vllm-project/vllm#29596: [Bug]: kimi-k2 gets wrong tool_call_id

| 字段 | 值 |
| --- | --- |
| Issue | [#29596](https://github.com/vllm-project/vllm/issues/29596) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: kimi-k2 gets wrong tool_call_id

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug in [v0.11.1rc2], kimi-k2 / kimi-k2 think gets correct tool_call_id, like: ``` ChatCompletionMessageFunctionToolCall(id='functions.get_weather:0',... ``` in [v0.11.2] and maybe also in few previous versions, we got: ``` ChatCompletionMessageFunctionToolCall(id='chatcmpl-tool-a12b7e6c67d74489899e6780a1930f3b',... ``` which significantly reduce the reliability of upcoming tool calls. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: tions.get_weather:0',... ``` in [v0.11.2] and maybe also in few previous versions, we got: ``` ChatCompletionMessageFunctionToolCall(id='chatcmpl-tool-a12b7e6c67d74489899e6780a1930f3b',... ``` which significantly reduce...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ls. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: kimi-k2 gets wrong tool_call_id bug;stale ### Your current environment ### 🐛 Describe the bug in [v0.11.1rc2], kimi-k2 / kimi-k2 think gets correct tool_call_id, like: ``` ChatCompletionMessageFunctionToolCall(id...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
