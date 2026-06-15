# vllm-project/vllm#2080: System prompt not working with Mistral-7B-Instruct-v0.1

| 字段 | 值 |
| --- | --- |
| Issue | [#2080](https://github.com/vllm-project/vllm/issues/2080) |
| 状态 | closed |
| 标签 |  |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> System prompt not working with Mistral-7B-Instruct-v0.1

### Issue 正文摘录

Following the example https://docs.vllm.ai/en/latest/getting_started/quickstart.html#using-openai-chat-api-with-vllm I tried ``` curl http://$BASE_URL/chat/completions \ -H "Content-Type: application/json" \ -d '{ "model": "mistralai/Mistral-7B-Instruct-v0.1", "messages": [ {"role": "system", "content": "You are a helpful assistant."}, {"role": "user", "content": "Who won the world series in 2020?"} ] }' ``` gives error `BadRequestError: Error code: 400 - {'object': 'error', 'message': 'Conversation roles must alternate user/assistant/user/assistant/...', 'type': 'invalid_request_error', 'param': None, 'code': None} ` Without system prompt it works fine. I also tried with OpenHermes-2.5-Mistral-7B ``` curl http://$BASE_URL/chat/completions \ -H "Content-Type: application/json" \ -d '{ "model": "teknium/OpenHermes-2.5-Mistral-7B", "messages": [ {"role": "system", "content": "You are a helpful assistant."}, {"role": "user", "content": "Who won the world series in 2020?"} ] }' ``` and it works fine with system prompt.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: mpletions \ -H "Content-Type: application/json" \ -d '{ "model": "mistralai/Mistral-7B-Instruct-v0.1", "messages": [ {"role": "system", "content": "You are a helpful assistant."}, {"role": "user", "content": "Who won th...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: o won the world series in 2020?"} ] }' ``` gives error `BadRequestError: Error code: 400 - {'object': 'error', 'message': 'Conversation roles must alternate user/assistant/user/assistant/...', 'type': 'invalid_request_e...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: Mistral-7B-Instruct-v0.1 Following the example https://docs.vllm.ai/en/latest/getting_started/quickstart.html#using-openai-chat-api-with-vllm I tried ``` curl http://$BASE_URL/chat/completions \ -H "Content-Type: applic...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
