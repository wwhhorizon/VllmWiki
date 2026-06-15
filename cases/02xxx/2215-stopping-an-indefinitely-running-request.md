# vllm-project/vllm#2215: Stopping an indefinitely running request

| 字段 | 值 |
| --- | --- |
| Issue | [#2215](https://github.com/vllm-project/vllm/issues/2215) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Stopping an indefinitely running request

### Issue 正文摘录

I am using Mixtral-8x7B-Instruct-v0.1 to generate JSONs from some given text, but in some cases the generation does not follow the given JSON format, and starts generating a very large (5k+ tokens) output. This causes the server to slow down massively. Is there a way to stop the generation of a particular request?

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: Stopping an indefinitely running request feature request;stale I am using Mixtral-8x7B-Instruct-v0.1 to generate JSONs from some given text, but in some cases the generation does not follow the given JSON format, and st...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: en text, but in some cases the generation does not follow the given JSON format, and starts generating a very large (5k+ tokens) output. This causes the server to slow down massively. Is there a way to stop the generati...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
