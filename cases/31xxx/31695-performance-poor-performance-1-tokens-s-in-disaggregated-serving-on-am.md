# vllm-project/vllm#31695: [Performance]: Poor performance (1 tokens/s) in Disaggregated Serving on AMD MI325X

| 字段 | 值 |
| --- | --- |
| Issue | [#31695](https://github.com/vllm-project/vllm/issues/31695) |
| 状态 | closed |
| 标签 | performance;rocm |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;distributed_parallel;hardware_porting;model_support;scheduler_memory |
| 子分类 | latency_reg |
| Operator 关键词 | cache |
| 症状 | slowdown |
| 根因提示 |  |
| 硬件范围 | amd |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Performance]: Poor performance (1 tokens/s) in Disaggregated Serving on AMD MI325X

### Issue 正文摘录

### Proposal to improve performance We suspect the current SharedStorageConnector might not be fully optimized for ROCm memory mapping, potentially falling back to slower I/O paths. ### Report of performance regression We are testing Disaggregated Serving (PD separation) using vLLM V1 engine and SharedStorageConnector on AMD MI325X. Despite a successful end-to-end setup, we are seeing a significant performance bottleneck. Current Performance Metrics: - Avg prompt throughput: 1.0 tokens/s - Avg generation throughput: 5.0 tokens/s - Hardware: AMD MI325X (Multi-GPU) - Model: Llama-3.1-8B-Instruct `Engine 000: Avg prompt throughput: 1.0 tokens/s, Avg generation throughput: 5.0 tokens/s, Running: 0 reqs, Waiting: 0 reqs, GPU KV cache usage: 0.0%, Prefix cache hit rate: 0.0%, External prefix cache hit rate: 0.0%` ### Misc discussion on performance Here is the doc for reproducing it: [Steps for Prefill-Decode Disaggregation](https://docs.google.com/document/d/1k762zbqXtmPal_BsV7qcKMHjd6MWMpcakSNw4i095eA/edit?tab=t.0) We also attempted to use high-performance connectors: - P2pNcclConnector: Consistently deadlocks or hangs during the handshake on MI325X. - LMCacheConnectorV1: Unusable due...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: 1.0 tokens/s, Avg generation throughput: 5.0 tokens/s, Running: 0 reqs, Waiting: 0 reqs, GPU KV cache usage: 0.0%, Prefix cache hit rate: 0.0%, External prefix cache hit rate: 0.0%` ### Misc discussion on performance He...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: formance (1 tokens/s) in Disaggregated Serving on AMD MI325X performance;rocm ### Proposal to improve performance We suspect the current SharedStorageConnector might not be fully optimized for ROCm memory mapping, poten...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: potentially falling back to slower I/O paths. ### Report of performance regression We are testing Disaggregated Serving (PD separation) using vLLM V1 engine and SharedStorageConnector on AMD MI325X. Despite a successful...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: e: 0.0%` ### Misc discussion on performance Here is the doc for reproducing it: [Steps for Prefill-Decode Disaggregation](https://docs.google.com/document/d/1k762zbqXtmPal_BsV7qcKMHjd6MWMpcakSNw4i095eA/edit?tab=t.0) We...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: neration throughput: 5.0 tokens/s, Running: 0 reqs, Waiting: 0 reqs, GPU KV cache usage: 0.0%, Prefix cache hit rate: 0.0%, External prefix cache hit rate: 0.0%` ### Misc discussion on performance Here is the doc for re...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
