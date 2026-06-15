# vllm-project/vllm#3997: [Usage]: flash_attn vs xformers

| 字段 | 值 |
| --- | --- |
| Issue | [#3997](https://github.com/vllm-project/vllm/issues/3997) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: flash_attn vs xformers

### Issue 正文摘录

### Your current environment I found that "Using FlashAttention backend" or "Using XFormers backend", the throughput is the same ### How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm.

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: s xformers usage;stale ### Your current environment I found that "Using FlashAttention backend" or "Using XFormers backend", the throughput is the same ### How would you like to use vllm I want to run inference of a [sp...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: me ### How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm.
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: # How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm.
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Usage]: flash_attn vs xformers usage;stale ### Your current environment I found that "Using FlashAttention backend" or "Using XFormers backend", the throughput is the same ### How would you like to use vllm I want to r...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: und that "Using FlashAttention backend" or "Using XFormers backend", the throughput is the same ### How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integr...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
