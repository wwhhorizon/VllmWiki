# vllm-project/vllm#3872: [Bug]: Does vLLM support Qwen/Qwen1.5-32B-Chat-AWQ? It works for the first time then stops generating responses.

| 字段 | 值 |
| --- | --- |
| Issue | [#3872](https://github.com/vllm-project/vllm/issues/3872) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 16; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Does vLLM support Qwen/Qwen1.5-32B-Chat-AWQ? It works for the first time then stops generating responses.

### Issue 正文摘录

### Your current environment vllm docker image: vllm/vllm-openai:latest ### 🐛 Describe the bug It works for the first time then stops generating responses, as shown below. ChatCompletion(id='cmpl-19b57e1ef1dc41edb57f37fa9bb66151', choices=[Choice(finish_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content='\n\n', role='assistant', function_call=None, tool_calls=None), stop_reason=None)], created=1712343257, model='Qwen/Qwen1.5-32B-Chat-AWQ', object='chat.completion', system_fingerprint=None, usage=CompletionUsage(completion_tokens=2, prompt_tokens=78, total_tokens=80))

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Does vLLM support Qwen/Qwen1.5-32B-Chat-AWQ? It works for the first time then stops generating responses. bug;stale ### Your current environment vllm docker image: vllm/vllm-openai:latest ### 🐛 Describe the bug I...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: stops generating responses. bug;stale ### Your current environment vllm docker image: vllm/vllm-openai:latest ### 🐛 Describe the bug It works for the first time then stops generating responses, as shown below. ChatCompl...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: at-AWQ? It works for the first time then stops generating responses. bug;stale ### Your current environment vllm docker image: vllm/vllm-openai:latest ### 🐛 Describe the bug It works for the first time then stops genera...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: tale ### Your current environment vllm docker image: vllm/vllm-openai:latest ### 🐛 Describe the bug It works for the first time then stops generating responses, as shown below. ChatCompletion(id='cmpl-19b57e1ef1dc41edb5...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
