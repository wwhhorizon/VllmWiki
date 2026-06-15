# vllm-project/vllm#3870: Can you guys give the implementation for chat conversation based on current chat and chat history using vllm and llama-2-13B model

| 字段 | 值 |
| --- | --- |
| Issue | [#3870](https://github.com/vllm-project/vllm/issues/3870) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Can you guys give the implementation for chat conversation based on current chat and chat history using vllm and llama-2-13B model

### Issue 正文摘录

### How would you like to use vllm - Basically we need to implement chat conversation similar to chatgpt , like AI chat conversation based on the current chat and previous chat history. - we have to use vllm and llama-2-13B model to do this feature can you guys help me on this!

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: chat conversation based on current chat and chat history using vllm and llama-2-13B model usage;stale ### How would you like to use vllm - Basically we need to implement chat conversation similar to chatgpt , like AI ch...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: on current chat and chat history using vllm and llama-2-13B model usage;stale ### How would you like to use vllm - Basically we need to implement chat conversation similar to chatgpt , like AI chat conversation based on...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
