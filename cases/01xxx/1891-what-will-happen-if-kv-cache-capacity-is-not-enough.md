# vllm-project/vllm#1891: What will happen if kv cache capacity is not enough?

| 字段 | 值 |
| --- | --- |
| Issue | [#1891](https://github.com/vllm-project/vllm/issues/1891) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> What will happen if kv cache capacity is not enough?

### Issue 正文摘录

When the request concurrency and input lengths are high, the capacity of kv cache usage will boost. So I am wondering what will happen when this condition is met? An OOM error is thrown or part of the kv cache will be offloaded to cpu?

## 候选优化模式

- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 4: What will happen if kv cache capacity is not enough? When the request concurrency and input lengths are high, the capacity of kv cache usage will boost. So I am wondering what will happen when this condition is met? An...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: What will happen if kv cache capacity is not enough? When the request concurrency and input lengths are high, the capacity of kv cache usage will boost. So I am wondering what will happen when this condition is met? An...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: What will happen if kv cache capacity is not enough? When the request concurrency and input lengths are high, the capacity of kv cache usage will boost. So I am wondering what will happen when this condition is met? An...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
