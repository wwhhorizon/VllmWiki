# vllm-project/vllm#809: Qwen-7B, set max_num_batched_tokens=4096, then output role is null and content is empty string

| 字段 | 值 |
| --- | --- |
| Issue | [#809](https://github.com/vllm-project/vllm/issues/809) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Qwen-7B, set max_num_batched_tokens=4096, then output role is null and content is empty string

### Issue 正文摘录

Qwen-7B, which "max_position_embeddings": 8192. When I set max_num_batched_tokens=4096, then it outputs role is null and content is empty: ``` Message received 0.11 seconds after request: { "role": "assistant" } Message received 0.59 seconds after request: { "role": null, "content": "" } Message received 0.59 seconds after request: { "role": null, "content": "" } Full response received 0.59 seconds after request Full conversation received: Process finished with exit code 0 ``` when I cut prompt text shorter( less than 2560), it runs ok. But Qwen-7B, it support longer prompt, up to 8K. now it can only use 2560(max_num_batched_tokens value), when set bigger value than 2560, and send token than 2560 it return error result.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: Qwen-7B, set max_num_batched_tokens=4096, then output role is null and content is empty string Qwen-7B, which "max_position_embeddings": 8192. When I set max_num_batched_tokens=4096, then it outputs role is null and c
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: e is null and content is empty: ``` Message received 0.11 seconds after request: { "role": "assistant" } Message received 0.59 seconds after request: { "role": null, "content": "" } Message received 0.59 seconds after r...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
