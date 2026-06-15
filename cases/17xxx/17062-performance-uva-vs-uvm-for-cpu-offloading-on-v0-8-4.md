# vllm-project/vllm#17062: [Performance]: UVA vs UVM for CPU offloading on v0.8.4+

| 字段 | 值 |
| --- | --- |
| Issue | [#17062](https://github.com/vllm-project/vllm/issues/17062) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;model_support;sampling_logits |
| 子分类 |  |
| Operator 关键词 | cache;cuda;kernel |
| 症状 |  |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Performance]: UVA vs UVM for CPU offloading on v0.8.4+

### Issue 正文摘录

### Proposal to improve performance Referencing the recent implementation on https://github.com/vllm-project/vllm/pull/15354 (v0.8.4+) for CPU offloading @youkaichao, is there any specific reason to pick UVA (`cudaHostAlloc`) over UVM `cudaMallocManaged()`? 1. UVM goes further than UVA to manage data automatically, often using page-faulting hardware to migrate pages on demand. On systems like the GH200, this has potentially additional benefits such as hardware orchestrated frequency based migration. 2. A key benefit of Unified Memory is simplifying the heterogeneous computing memory model by eliminating the need for deep copies when accessing structured data in GPU kernels. [Source](https://developer.nvidia.com/blog/unified-memory-in-cuda-6/#unified_memory_or_unified_virtual_addressing) 3. On several discussion threads, the larger access sizes of CPU offloading makes UVM seems to be the better approach compared to UVA [Source](https://forums.developer.nvidia.com/t/page-fault-profiling/265320/3?u=rajeshshashikumar) Going by [this](https://arxiv.org/pdf/2407.07850), if transparent offloading is desired `cudaMallocManaged()` seems to be desirable for platforms such as the GH200 Alter...

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: ompared to UVA [Source](https://forums.developer.nvidia.com/t/page-fault-profiling/265320/3?u=rajeshshashikumar) Going by [this](https://arxiv.org/pdf/2407.07850), if transparent offloading is desired `cudaMallocManaged...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: CPU offloading @youkaichao, is there any specific reason to pick UVA (`cudaHostAlloc`) over UVM `cudaMallocManaged()`? 1. UVM goes further than UVA to manage data automatically, often using page-faulting hardware to mig...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: [Performance]: UVA vs UVM for CPU offloading on v0.8.4+ performance;stale ### Proposal to improve performance Referencing the recent implementation on https://github.com/vllm-project/vllm/pull/15354 (v0.8.4+) for CPU of...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: on v0.8.4+ performance;stale ### Proposal to improve performance Referencing the recent implementation on https://github.com/vllm-project/vllm/pull/15354 (v0.8.4+) for CPU offloading @youkaichao, is there any specific r...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: efit of Unified Memory is simplifying the heterogeneous computing memory model by eliminating the need for deep copies when accessing structured data in GPU kernels. [Source](https://developer.nvidia.com/blog/unified-me...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
