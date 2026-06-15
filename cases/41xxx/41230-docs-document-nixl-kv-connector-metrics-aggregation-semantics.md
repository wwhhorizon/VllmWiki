# vllm-project/vllm#41230: [Docs] Document NIXL KV connector metrics aggregation semantics

| 字段 | 值 |
| --- | --- |
| Issue | [#41230](https://github.com/vllm-project/vllm/issues/41230) |
| 状态 | open |
| 标签 | good first issue |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Docs] Document NIXL KV connector metrics aggregation semantics

### Issue 正文摘录

## Summary The NIXL KV connector logs transfer metrics periodically: ``` KV Transfer metrics: Num successful transfers=4, Avg xfer time (ms)=1.381, P90 xfer time (ms)=2.601, Avg post time (ms)=0.672, P90 post time (ms)=0.801, Avg MB per transfer=2.25, Throughput (MB/s)=1629.549, Avg number of descriptors=72.0 ``` Currently there is no documentation explaining what these metrics represent, especially in the context of **multi-rank (TP > 1) deployments**. This has already caused confusion among users. ## Current behavior All metrics are **aggregated across all TP ranks** before summary stats are computed: 1. Each TP rank independently records per-transfer telemetry (`transfer_duration`, `post_duration`, `bytes_transferred`, `num_descriptors`) via `NixlKVConnectorStats.record_transfer()` in [`stats.py`](https://github.com/vllm-project/vllm/blob/main/vllm/distributed/kv_transfer/kv_connector/v1/nixl/stats.py). 2. Stats from all ranks are concatenated via `aggregate()` (`list.extend()`). 3. `reduce()` computes averages, percentiles, and throughput over the **combined** pool of observations from all ranks. This means: - **"Num successful transfers"** is the total count across all ranks,...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: y there is no documentation explaining what these metrics represent, especially in the context of **multi-rank (TP > 1) deployments**. This has already caused confusion among users. ## Current behavior All metrics are *...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: individual rank-level transfers, not the total bytes moved for a single KV cache transfer operation. - **"Throughput (MB/s)"** is `total_MB_all_ranks / total_time_all_ranks` — effectively an average per-rank throughput,...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ost time (ms)=0.672, P90 post time (ms)=0.801, Avg MB per transfer=2.25, Throughput (MB/s)=1629.549, Avg number of descriptors=72.0 ``` Currently there is no documentation explaining what these metrics represent, especi...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
