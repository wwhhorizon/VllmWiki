# vllm-project/vllm#3281: unload the model

| 字段 | 值 |
| --- | --- |
| Issue | [#3281](https://github.com/vllm-project/vllm/issues/3281) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 19; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> unload the model

### Issue 正文摘录

Hi, i m sorry, i don't find how unload model. like i load a model, i delete the object and i call the garbage collector but it does nothing. How we are suppose to unload model? I want to load a model do a batch, load an other do a batch, like that for multiple models for comparing them. But for now i must stop python each time.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: unload the model stale Hi, i m sorry, i don't find how unload model. like i load a model, i delete the object and i call the garbage collector but it does nothing. How we are suppose to unload model? I want to load a mo...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: unload the model stale Hi, i m sorry, i don't find how unload model. like i load a model, i delete the object and i call the garbage collector but it does nothing. How we are suppose to unload model? I want to load a mo...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
