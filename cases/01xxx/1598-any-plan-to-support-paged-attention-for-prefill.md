# vllm-project/vllm#1598: Any plan to support paged attention for prefill?

| 字段 | 值 |
| --- | --- |
| Issue | [#1598](https://github.com/vllm-project/vllm/issues/1598) |
| 状态 | closed |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Any plan to support paged attention for prefill?

### Issue 正文摘录

First of all, thank you for the great work and the recent integration for the paged-flash attention v2 kernel! I am wondering if there is any plan to support paged attention for prefill, which can compute multiple tokens in each batch in parallel (like flash_attn_with_kvcache did). I did a quick check over the codebase and found it seems that paged_attention_v2_kernel expects one token for each request. In some cases like speculative decoding and chunked prefill, it would be ideal to compute multiple tokens in each request in parallel.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: Any plan to support paged attention for prefill? First of all, thank you for the great work and the recent integration for the paged-flash attention v2 kernel! I am wondering if there is any plan to support paged attent...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: l, thank you for the great work and the recent integration for the paged-flash attention v2 kernel! I am wondering if there is any plan to support paged attention for prefill, which can compute multiple tokens in each b...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
