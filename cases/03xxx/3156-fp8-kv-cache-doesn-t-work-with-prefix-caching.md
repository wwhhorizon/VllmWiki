# vllm-project/vllm#3156: FP8 KV cache doesn't work with prefix caching

| 字段 | 值 |
| --- | --- |
| Issue | [#3156](https://github.com/vllm-project/vllm/issues/3156) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> FP8 KV cache doesn't work with prefix caching

### Issue 正文摘录

FP8 KV cache doesn't work with prefix caching since the Triton kernel does not support KV8 for now.

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ix caching stale FP8 KV cache doesn't work with prefix caching since the Triton kernel does not support KV8 for now.
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: FP8 KV cache doesn't work with prefix caching stale FP8 KV cache doesn't work with prefix caching since the Triton kernel does not support KV8 for now.
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: FP8 KV cache doesn't work with prefix caching stale FP8 KV cache doesn't work with prefix caching since the Triton kernel does not support KV8 for now.
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: FP8 KV cache doesn't work with prefix caching stale FP8 KV cache doesn't work with prefix caching since the Triton kernel does not support KV8 for now.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
