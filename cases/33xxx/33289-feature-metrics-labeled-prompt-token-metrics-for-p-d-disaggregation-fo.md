# vllm-project/vllm#33289: [Feature]: [Metrics] Labeled prompt token metrics for P/D disaggregation (Follow-up on PR #27569)

| 字段 | 值 |
| --- | --- |
| Issue | [#33289](https://github.com/vllm-project/vllm/issues/33289) |
| 状态 | closed |
| 标签 | feature request;kv-connector |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: [Metrics] Labeled prompt token metrics for P/D disaggregation (Follow-up on PR #27569)

### Issue 正文摘录

### 🚀 The feature, motivation and pitch ## Summary Add labeled Prometheus metrics to distinguish where prompt tokens come from in P/D disaggregated deployments: ``` vllm:prompt_tokens_by_source_total{source="local_compute"} # Tokens prefilled locally vllm:prompt_tokens_by_source_total{source="external_kv_transfer"} # Tokens received via KV transfer vllm:prompt_tokens_by_source_total{source="local_cache_hit"} # Tokens from local prefix cache vllm:prompt_tokens_cached_total # Total cached (local + external, -1 when all cached) ``` > **Note:** The `-1` adjustment is applied by the scheduler when all prompt tokens are cached (from local cache or KV transfer). This forces the model to recompute the last prompt token locally, since the model needs at least one input token to run a forward pass. Related: PR #27569 --- ## Motivation In P/D (Prefill/Decode) disaggregation, decode instances receive KV cache from prefill instances. Currently, decode reports inflated prompt throughput because it counts all prompt tokens as "computed", even though most were transferred. This issue proposed adding labeled metrics so users can understand actual compute work vs transferred work. ## Proposed Imple...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: pt token metrics for P/D disaggregation (Follow-up on PR #27569) feature request;kv-connector ### 🚀 The feature, motivation and pitch ## Summary Add labeled Prometheus metrics to distinguish where prompt tokens come fro...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: okens_by_source_total{source="local_cache_hit"} # Tokens from local prefix cache vllm:prompt_tokens_cached_total # Total cached (local + external, -1 when all cached) ``` > **Note:** The `-1` adjustment is applied by th...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: cache from prefill instances. Currently, decode reports inflated prompt throughput because it counts all prompt tokens as "computed", even though most were transferred. This issue proposed adding labeled metrics so user...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: -- ## Future Work - Add `cache_source` label to distinguish GPU vs CPU cache hits - Add `kv_source` label to distinguish different KV connectors (NIXL, Mooncake, LMCache) - Update CLI logger to show breakdown - Update c...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: king `kv_transfer_params.get("do_remote_decode")`. However, this adds special-case logic and may not be worth the complexity. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a n...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
