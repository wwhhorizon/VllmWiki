# vllm-project/vllm#1747: client get error response

| 字段 | 值 |
| --- | --- |
| Issue | [#1747](https://github.com/vllm-project/vllm/issues/1747) |
| 状态 | closed |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> client get error response

### Issue 正文摘录

I'm sending requests using multiple clients.(using locust). When the user num is low, all requests get right response. When the user num is high, say 60, some requests get error response. But I can't see any error log on the server. How could I debug it? The GPU KV cache usage is at most 66%, I think it's far from vllm's limit.

## 候选优化模式

- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: I can't see any error log on the server. How could I debug it? The GPU KV cache usage is at most 66%, I think it's far from vllm's limit.
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: client get error response I'm sending requests using multiple clients.(using locust). When the user num is low, all requests get right response. When the user num is high, say 60, some requests get error response. But I...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
