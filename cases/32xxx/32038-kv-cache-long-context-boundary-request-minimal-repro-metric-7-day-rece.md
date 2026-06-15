# vllm-project/vllm#32038: KV-cache / long-context boundary request (minimal repro + metric) — 7-day receipts eval

| 字段 | 值 |
| --- | --- |
| Issue | [#32038](https://github.com/vllm-project/vllm/issues/32038) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> KV-cache / long-context boundary request (minimal repro + metric) — 7-day receipts eval

### Issue 正文摘录

### Proposal to improve performance I’m looking for the smallest vLLM boundary where KV-cache / long-context becomes the bottleneck (memory traffic + tail latency). I want a runnable repro + the metric you care about, then I can return a receipts-backed before/after within 7 days. The candidate improvement class is topology: replace scan-like access patterns with structured traversal / layout on a declared boundary (with SHA256-indexed receipts), but I won’t speculate until we lock the minimal repro and acceptance metric. ### Report of performance regression Not reporting a regression. I’m requesting the smallest reproducible KV-cache / long-context perf boundary and the preferred metric, so I can return a receipts-backed before/after. ### Misc discussion on performance Routing ask: who owns KV-cache / paged-attention performance triage in vLLM? I need the smallest reproducible repro that exposes KV-cache / long-context pain: - model + context length - batch/concurrency - backend (flash-attn / triton / etc.) - exact command/config to run - the metric you want as acceptance currency (tokens/s, p99 latency, OOM threshold, etc.) What I will return in 7 days once the boundary is defin...

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: long-context boundary request (minimal repro + metric) — 7-day receipts eval performance;stale ### Proposal to improve performance I’m looking for the smallest vLLM boundary where KV-cache / long-context becomes the bot...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: urn a receipts-backed before/after. ### Misc discussion on performance Routing ask: who owns KV-cache / paged-attention performance triage in vLLM? I need the smallest reproducible repro that exposes KV-cache / long-con...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: rformance;stale ### Proposal to improve performance I’m looking for the smallest vLLM boundary where KV-cache / long-context becomes the bottleneck (memory traffic + tail latency). I want a runnable repro + the metric y...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: KV-cache / long-context boundary request (minimal repro + metric) — 7-day receipts eval performance;stale ### Proposal to improve performance I’m looking for the smallest vLLM boundary where KV-cache / long-context beco
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: smallest reproducible repro that exposes KV-cache / long-context pain: - model + context length - batch/concurrency - backend (flash-attn / triton / etc.) - exact command/config to run - the metric you want as acceptanc...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
