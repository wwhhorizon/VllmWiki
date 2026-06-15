# vllm-project/vllm#43015: [RFC]: Add support for Cohere's /v2/chat HTTP API entry point

| 字段 | 值 |
| --- | --- |
| Issue | [#43015](https://github.com/vllm-project/vllm/issues/43015) |
| 状态 | open |
| 标签 | RFC |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Add support for Cohere's /v2/chat HTTP API entry point

### Issue 正文摘录

### Motivation. vLLM does not currently support the [Cohere Chat v2 api](https://docs.cohere.com/reference/chat). While similar to chat completions, this api has a number of different fields, including notably, citations present within the assistant messages which should then be rendered into the prompt. This functionality is important to many of our users and so it would be needed for them to be able to use cohere models with vLLM directly. ### Proposed Change. The proposed change is to add a cohere/v2/chat entry point that renders the request using the Melody library's prompt rendering functions. The flow would be very similar to the create_chat_completion function, but with render_chat calling the melody library to produce the rendered chat template prompt. Common logic could also be potentially refactored into a shared class. Output parsing logic is already in place and would not need to change. ### Feedback Period. _No response_ ### CC List. _No response_ ### Any Other Things. _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://d...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: mpletions, this api has a number of different fields, including notably, citations present within the assistant messages which should then be rendered into the prompt. This functionality is important to many of our user...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: of our users and so it would be needed for them to be able to use cohere models with vLLM directly. ### Proposed Change. The proposed change is to add a cohere/v2/chat entry point that renders the request using the Melo...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: proposed change is to add a cohere/v2/chat entry point that renders the request using the Melody library's prompt rendering functions. The flow would be very similar to the create_chat_completion function, but with rend...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
