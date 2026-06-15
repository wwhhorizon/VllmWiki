# vllm-project/vllm#3059: Can I send a termination signal before the service inference ends？

| 字段 | 值 |
| --- | --- |
| Issue | [#3059](https://github.com/vllm-project/vllm/issues/3059) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Can I send a termination signal before the service inference ends？

### Issue 正文摘录

I used some models (say 10) for the classification task that were deployed as openai servers using vllm, that is, 10 servers in total. Each request requests the inference services of these servers in parallel, and whenever one server returns a result, the service returns a result. To save GPU resources, is there a way to terminate the inferencing of the other 9 services by passing a signal (context cancel)?

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: a result. To save GPU resources, is there a way to terminate the inferencing of the other 9 services by passing a signal (context cancel)?
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: send a termination signal before the service inference ends？ I used some models (say 10) for the classification task that were deployed as openai servers using vllm, that is, 10 servers in total. Each request requests t...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: eployed as openai servers using vllm, that is, 10 servers in total. Each request requests the inference services of these servers in parallel, and whenever one server returns a result, the service returns a result. To s...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
