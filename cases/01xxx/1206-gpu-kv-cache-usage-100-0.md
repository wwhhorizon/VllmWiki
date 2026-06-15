# vllm-project/vllm#1206: GPU KV cache usage: 100.0%以后就卡住

| 字段 | 值 |
| --- | --- |
| Issue | [#1206](https://github.com/vllm-project/vllm/issues/1206) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 21; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> GPU KV cache usage: 100.0%以后就卡住

### Issue 正文摘录

GPU KV cache usage: 100.0%以后就卡住，GPU使用率也将为0，无法继续提供服务，请问有什么解决办法吗？

## 候选优化模式

- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: GPU KV cache usage: 100.0%以后就卡住 bug;stale GPU KV cache usage: 100.0%以后就卡住，GPU使用率也将为0，无法继续提供服务，请问有什么解决办法吗？
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: GPU KV cache usage: 100.0%以后就卡住 bug;stale GPU KV cache usage: 100.0%以后就卡住，GPU使用率也将为0，无法继续提供服务，请问有什么解决办法吗？

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
