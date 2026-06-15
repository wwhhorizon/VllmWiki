# vllm-project/vllm#21571: [Usage]: Qwen  tool_call response type problem

| 字段 | 值 |
| --- | --- |
| Issue | [#21571](https://github.com/vllm-project/vllm/issues/21571) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Qwen  tool_call response type problem

### Issue 正文摘录

### Your current environment 通过vllm部署Qwen_Coder，参数配置--enable-auto-tool-choice --tool-call-parser hermes，调用工具返回格式是：Choice(finish_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content=' \n \n \n1024\n\n\n ', refusal=None, role='assistant', annotations=None, audio=None, function_call=None, tool_calls=[], reasoning_content=None), stop_reason=None) tool_call在content里边，而不是在tool_call里边 如何可以才能实现这种标准的openai的工具调用，ChatCompletion(id='chatcmpl-cd0e10d2-57fa-98c2-a6a2-f7d621218fb7', choices=[Choice(finish_reason='tool_calls', index=0, logprobs=None, message=ChatCompletionMessage(content='', refusal=None, role='assistant', annotations=None, audio=None, function_call=None, tool_calls=[ChatCompletionMessageToolCall(id='call_f9aca388535744f0b27facf1', function=Function(arguments='{"input_num": 1024}', name='square_the_number'), type='function', index=0)]))], created=1753410311, model='qwen3-coder-plus', object='chat.completion', service_tier=None, system_fingerprint=None, usage=CompletionUsage(completion_tokens=26, prompt_tokens=300, total_tokens=326, completion_tokens_details=None, prompt_tokens_details=PromptTokensDetails(audio_tokens=None, cached_tokens=0))) ### How would...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: )) ### How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm. ### Before submitting a new issue... - [x] Make sure you already searched f...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Usage]: Qwen tool_call response type problem usage;stale ### Your current environment 通过vllm部署Qwen_Coder，参数配置--enable-auto-tool-choice --tool-call-parser hermes，调用工具返回格式是：Choice(finish_reason='stop', index=0, logprobs=...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: lm. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Usage]: Qwen tool_call response type problem usage;stale ### Your current environment 通过vllm部署Qwen_Coder，参数配置--enable-auto-tool-choice --tool-call-parser hermes，调用工具返回格式是：Choice(finish_reason='stop', index=0, logprobs=...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
