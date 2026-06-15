# vllm-project/vllm#12839: [Usage]: How to make use of vLLM tools functionality

| 字段 | 值 |
| --- | --- |
| Issue | [#12839](https://github.com/vllm-project/vllm/issues/12839) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: How to make use of vLLM tools functionality

### Issue 正文摘录

### Your current environment Doc : https://docs.vllm.ai/en/stable/features/tool_calling.html ### How would you like to use vllm I'm willing to make use of vLLM tools and tool_choice parameter in OpenAI /v1/chat/completions request. The doc attached below shows multiple ways of using `tools` and `tool_choice` but it turns out bit misleading. - One of the way is to pass --chat-template provided in `examples` folder of vLLM. But these templates are present only for llama-3.1, 3.2 and mistral models. We have bunch of other OpenAI compatible models, how can we use it for them. I want to know is there any way where we can simply pass `tools` and `tool_choice` parameter in the payload and model honors it to generate the response. I don't want to specify --chat-template at the time of spinning up the container. I urgently need this confirmation to give a logical conclusion to my analysis. https://docs.vllm.ai/en/stable/features/tool_calling.html https://docs.vllm.ai/en/latest/getting_started/examples/openai_chat_completion_client_with_tools.html ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right c...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: d in `examples` folder of vLLM. But these templates are present only for llama-3.1, 3.2 and mistral models. We have bunch of other OpenAI compatible models, how can we use it for them. I want to know is there any way wh...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: payload and model honors it to generate the response. I don't want to specify --chat-template at the time of spinning up the container. I urgently need this confirmation to give a logical conclusion to my analysis. http...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: tml ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: e of vLLM tools and tool_choice parameter in OpenAI /v1/chat/completions request. The doc attached below shows multiple ways of using `tools` and `tool_choice` but it turns out bit misleading. - One of the way is to pas...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: s.vllm.ai/en/stable/features/tool_calling.html https://docs.vllm.ai/en/latest/getting_started/examples/openai_chat_completion_client_with_tools.html ### Before submitting a new issue... - [x] Make sure you already searc...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
