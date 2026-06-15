# vllm-project/vllm#3606: [Feature]: FASTDECODE: High-Throughput GPU-Efficient LLM Serving using Heterogeneous Pipelines

| 字段 | 值 |
| --- | --- |
| Issue | [#3606](https://github.com/vllm-project/vllm/issues/3606) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: FASTDECODE: High-Throughput GPU-Efficient LLM Serving using Heterogeneous Pipelines

### Issue 正文摘录

### 🚀 The feature, motivation and pitch https://arxiv.org/pdf/2403.11421.pdf This paper might be interesting. > Cost of serving large language models (LLM) is high, but the expensive and scarce GPUs are poorly efficient when generating tokens sequentially, unless the batch of sequences is enlarged. However, the batch size is limited by some constantly reused intermediate results, namely KV-Cache. They occupy too much memory to fit more sequences into a GPU simultaneously. While they could be offloaded to host memory, the CPU-GPU bandwidth is an inevitable bottleneck. We find a way to decompose the transformer models into two parts of different characteristics, one of which includes the memory-bound KV-Cache accessing. Our key insight is that the aggregated memory capacity, bandwidth, and computing power of CPUs across multiple nodes is an efficient option to process this part. Performance improvement comes from reduced data transmission overhead and boosted GPU throughput to process the other model part. Moreover, we address efficiency challenges brought by heterogeneity at both temporal and inter-device scopes using scheduling and performance modeling techniques. Evaluation resul...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Feature]: FASTDECODE: High-Throughput GPU-Efficient LLM Serving using Heterogeneous Pipelines feature request;stale ### 🚀 The feature, motivation and pitch https://arxiv.org/pdf/2403.11421.pdf This paper might be inter...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: h size is limited by some constantly reused intermediate results, namely KV-Cache. They occupy too much memory to fit more sequences into a GPU simultaneously. While they could be offloaded to host memory, the CPU-GPU b...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [Feature]: FASTDECODE: High-Throughput GPU-Efficient LLM Serving using Heterogeneous Pipelines feature request;stale ### 🚀 The feature, motivation and pitch https://arxiv.org/pdf/2403.11421.pdf This paper might be inter...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: [Feature]: FASTDECODE: High-Throughput GPU-Efficient LLM Serving using Heterogeneous Pipelines feature request;stale ### 🚀 The feature, motivation and pitch https://arxiv.org/pdf/2403.11421.pdf This paper might be inter...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: o process this part. Performance improvement comes from reduced data transmission overhead and boosted GPU throughput to process the other model part. Moreover, we address efficiency challenges brought by heterogeneity...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
