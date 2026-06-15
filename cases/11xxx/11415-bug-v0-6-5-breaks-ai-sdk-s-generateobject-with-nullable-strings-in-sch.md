# vllm-project/vllm#11415: [Bug]: v0.6.5 breaks AI SDK's `generateObject` with nullable strings in schema (`"type mismatch! call is<type>() before get<type>()" && is<std::string>()`)

| 字段 | 值 |
| --- | --- |
| Issue | [#11415](https://github.com/vllm-project/vllm/issues/11415) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: v0.6.5 breaks AI SDK's `generateObject` with nullable strings in schema (`"type mismatch! call is<type>() before get<type>()" && is<std::string>()`)

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug The same request works perfectly fine in 0.6.4-post1 but fails in 0.6.5. It looks like the requests are failing if there's any nullable string in the provided schema. ``` [AI_APICallError]: Bad Request at /app/node_modules/@ai-sdk/provider-utils/dist/index.js:516:14 at process.processTicksAndRejections (node:internal/process/task_queues:95:5) at async postToApi (/app/node_modules/@ai-sdk/provider-utils/dist/index.js:409:28) at async OpenAIChatLanguageModel.doGenerate (/app/node_modules/@ai-sdk/openai/dist/index.js:520:50) at async fn (/app/node_modules/ai/dist/index.js:2341:33) at async /app/node_modules/ai/dist/index.js:343:22 at async _retryWithExponentialBackoff (/app/node_modules/ai/dist/index.js:171:12) at async fn (/app/node_modules/ai/dist/index.js:2309:34) at async /app/node_modules/ai/dist/index.js:343:22 cause: undefined, url: 'http://vllm:8000/v1/chat/completions', requestBodyValues: { model: 'casperhansen/llama-3.3-70b-instruct-awq', logit_bias: undefined, logprobs: undefined, top_logprobs: undefined, user: undefined, parallel_tool_calls: undefined, max_tokens: 1000, temperature: 0....

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: mismatch! call is<type>() before get<type>()" && is<std::string>()`) bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug The same request works perfectly fine in 0.6.4-post1...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 3: breaks AI SDK's `generateObject` with nullable strings in schema (`"type mismatch! call is<type>() before get<type>()" && is<std::string>()`) bug;stale ### Your current environment ### Model Input Dumps _No response_ ##...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: .ai.error.AI_APICallError)]: true } ``` ## How to reproduce this issue Install the necessary dependencies: ````console npm i ai @ai-sdk/openai zod ```` Start a vLLM server, I used the following parameters: ``` --host 0....
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: )" && is<std::string>()`) bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug The same request works perfectly fine in 0.6.4-post1 but fails in 0.6.5. It looks like the requ...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: eaks AI SDK's `generateObject` with nullable strings in schema (`"type mismatch! call is<type>() before get<type>()" && is<std::string>()`) bug;stale ### Your current environment ### Model Input Dumps _No response_ ###...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
