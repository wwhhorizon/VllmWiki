# vllm-project/vllm#15426: [Usage]: online server requests do not return token usage information in version 0.7.2

| 字段 | 值 |
| --- | --- |
| Issue | [#15426](https://github.com/vllm-project/vllm/issues/15426) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: online server requests do not return token usage information in version 0.7.2

### Issue 正文摘录

### Your current environment - vllm 0.7.2 - vllm 0.4.3 ## In versions >=0.7.2, such as 0.7.2, online server requests do not return token usage information like previous versions 0.4.3. Is it caused by OpenAI client update? - All requests with [OpenAI Completions API with vLLM](https://docs.vllm.ai/en/latest/getting_started/quickstart.html#openai-completions-api-with-vllm) and set **`"stream": true`** ``` curl http://ip:port/v1/chat/completions \ -H "Content-Type: application/json" \ -H "Authorization: Bearer EMPTY" \ -d '{ "model": "Qwen/Qwen2.5-72B-Instruct", "messages": [ { "role": "system", "content": "You are a helpful assistant." }, { "role": "user", "content": "hello" } ], "stream": true }' ``` ## The final json data shows the usage information of the request token in version 0.4.3 but not in 0.7.2. ``` data: {"id":"cmpl-093b1234609a41728005e84a79de3072","object":"chat.completion.chunk","created":1742866542,"model":"Qwen/Qwen2.5-72B-Instruct","choices":[{"index":0,"delta":{"content":""},"finish_reason":"stop"}],"usage":{"prompt_tokens":9,"total_tokens":82,"completion_tokens":73}} data: [DONE] ``` ### How would you like to use vllm I want to run inference of a [specific model...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [Usage]: online server requests do not return token usage information in version 0.7.2 usage;stale ### Your current environment - vllm 0.7.2 - vllm 0.4.3 ## In versions >=0.7.2, such as 0.7.2, online server requests do...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Usage]: online server requests do not return token usage information in version 0.7.2 usage;stale ### Your current environment - vllm 0.7.2 - vllm 0.4.3 ## In versions >=0.7.2, such as 0.7.2, online server requests do...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Usage]: online server requests do not return token usage information in version 0.7.2 usage;stale ### Your current environment - vllm 0.7.2 - vllm 0.4.3 ## In versions >=0.7.2, such as 0.7.2, online server requests do...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: lm. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: quests with [OpenAI Completions API with vLLM](https://docs.vllm.ai/en/latest/getting_started/quickstart.html#openai-completions-api-with-vllm) and set **`"stream": true`** ``` curl http://ip:port/v1/chat/completions \...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
