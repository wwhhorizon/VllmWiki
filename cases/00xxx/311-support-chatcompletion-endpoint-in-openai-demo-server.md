# vllm-project/vllm#311: Support `ChatCompletion` Endpoint in OpenAI demo server

| 字段 | 值 |
| --- | --- |
| Issue | [#311](https://github.com/vllm-project/vllm/issues/311) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Support `ChatCompletion` Endpoint in OpenAI demo server

### Issue 正文摘录

@infwinston Feel free to use FastChat's completion template to implement a chat completion endpoint in our demo server. You can use the completion API as a reference: https://github.com/vllm-project/vllm/blob/9d27b09d12767de775a92d765e177a61f8477189/vllm/entrypoints/openai/api_server.py#L88-L101

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: Support `ChatCompletion` Endpoint in OpenAI demo server feature request @infwinston Feel free to use FastChat's completion template to implement a chat completion endpoint in our demo server. You can use the completion...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
