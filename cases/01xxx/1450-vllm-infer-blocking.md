# vllm-project/vllm#1450: vllm Infer blocking

| 字段 | 值 |
| --- | --- |
| Issue | [#1450](https://github.com/vllm-project/vllm/issues/1450) |
| 状态 | closed |
| 标签 |  |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> vllm Infer blocking

### Issue 正文摘录

I use vllm 0.2.0 for model reasoning, the first request can return the result normally, the second request can see the request entered the vllm, but there is no result, and the subsequent request feels blocked. Can you help me? Analyze what the reason is. However, this does not happen when I use vllm 0.1.4.

## 候选优化模式

- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: vllm Infer blocking I use vllm 0.2.0 for model reasoning, the first request can return the result normally, the second request can see the request entered the vllm, but there is no result, and the subsequent request fee...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: vllm Infer blocking I use vllm 0.2.0 for model reasoning, the first request can return the result normally, the second request can see the request entered the vllm, but there is no result, and the subsequent request fee...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: vllm Infer blocking I use vllm 0.2.0 for model reasoning, the first request can return the result normally, the second request can see the request entered the vllm, but there is no result, and the subsequent request fee...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
