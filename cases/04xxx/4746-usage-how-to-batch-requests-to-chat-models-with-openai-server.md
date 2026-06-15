# vllm-project/vllm#4746: [Usage]: How to batch requests to chat models with OpenAI server?

| 字段 | 值 |
| --- | --- |
| Issue | [#4746](https://github.com/vllm-project/vllm/issues/4746) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: How to batch requests to chat models with OpenAI server?

### Issue 正文摘录

### Your current environment ... ### How would you like to use vllm I am serving a chat model (e.g. Llama 3 70B Instruct) using the OpenAI compatible server. However the v1/chat/completions endpoint does not take a batch. In contrast, the v1/completions endpoint takes a batch. Is the proper way to support batching to use multiple threads to send requests to v1/chat/completions or should I apply the chat template myself and then send it to the v1/completions endpoint? Thanks!

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Usage]: How to batch requests to chat models with OpenAI server? usage ### Your current environment ... ### How would you like to use vllm I am serving a chat model (e.g. Llama 3 70B Instruct) using the OpenAI compatib...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Usage]: How to batch requests to chat models with OpenAI server? usage ### Your current environment ... ### How would you like to use vllm I am serving a chat model (e.g. Llama 3 70B Instruct) using the OpenAI compatib...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
