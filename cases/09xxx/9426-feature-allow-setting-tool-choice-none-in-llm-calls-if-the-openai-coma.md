# vllm-project/vllm#9426: [Feature]: Allow setting tool_choice="none" in LLM calls if the OpenAI comaptible vllm server is started with --enable-auto-tool-choice

| 字段 | 值 |
| --- | --- |
| Issue | [#9426](https://github.com/vllm-project/vllm/issues/9426) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Allow setting tool_choice="none" in LLM calls if the OpenAI comaptible vllm server is started with --enable-auto-tool-choice

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Apparently, when starting the (OpenAI compatible) vllm server with the option `--enable-auto-tool-choice` to handle function calls, it is not possible to prevent tool calls when calling the model. According to the OpenAI API, this should be possible by setting `tool_choice='none'`. However, setting tool_choice to "none" seems to be not yet supported by vllm. Currently, an ValueError is thrown: Call: ``` client=OpenAI(...) completion = client.chat.completions.create( messages=[ {"role": "user", "content": "Write a poem"}], model="meta-llama-3.1", tool_choice='none' ) ``` Error Message: ```openai.BadRequestError: Error code: 400 - {'object': 'error', 'message': "[{'type': 'value_error', 'loc': ('body',), 'msg': 'Value error, When using `tool_choice`, `tools` must be set.', 'input': {'messages': [{'role': 'user', 'content': 'Write a poem'}], 'model': 'meta-llama-3.1', 'tool_choice': 'none'}, 'ctx': {'error': ValueError('When using `tool_choice`, `tools` must be set.')}}]", 'type': 'BadRequestError', 'param': None, 'code': 400}``` ### Alternatives The only alternative would be hosting two models in parallel. One for function calls and one for ge...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: unction calls, it is not possible to prevent tool calls when calling the model. According to the OpenAI API, this should be possible by setting `tool_choice='none'`. However, setting tool_choice to "none" seems to be no...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: comaptible vllm server is started with --enable-auto-tool-choice feature request ### 🚀 The feature, motivation and pitch Apparently, when starting the (OpenAI compatible) vllm server with the option `--enable-auto-tool-...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
