# vllm-project/vllm#14724: [RFC]: KV Cache Offloading for Cross-Engine KV Reuse

| 字段 | 值 |
| --- | --- |
| Issue | [#14724](https://github.com/vllm-project/vllm/issues/14724) |
| 状态 | closed |
| 标签 | RFC;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: KV Cache Offloading for Cross-Engine KV Reuse

### Issue 正文摘录

### Introduction and Background In [AIBrix](https://github.com/vllm-project/aibrix), we have implemented a Distributed KV Cache to support high-capacity, cross-engine KV reuse. Our integration with vLLM aligns with the **KV transfer connector** framework introduced by [PR #10502](https://github.com/vllm-project/vllm/pull/10502). Given these similarities and the recent vLLM v1 refactors, we have started refactoring our Distributed KV Cache feature to contribute common functionalities back to the upstream vLLM project. Our goal is to facilitate seamless support for KV cache offloading and cross-engine KV reuse across different cache backends. This RFC aims to enhance vLLM's capability to offload KV cache to external KV cache services by extending the KV transfer connector framework, enabling more memory-efficient and scalable inference workloads. ### Motivation Although the current KV transfer connector framework enables a general way to offloading KV cache to different cache backends, several common functionalities are not provided for KV cache offloading for cross-engine KV reuse use cases: **Tensor Parallelism Aware Management:** When vLLM uses tensor parallelism, each participat...

## 候选优化模式

- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 4: 1. We will enhance the **KV transfer module** by introducing `KVTransferMetadata`, which contains `context_tokens`, `prompt_len`, and `recv_len` for each sequence, enabling the `OffloadingConnector` (described below) to...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 3: [RFC]: KV Cache Offloading for Cross-Engine KV Reuse RFC;stale ### Introduction and Background In [AIBrix](https://github.com/vllm-project/aibrix), we have implemented a Distributed KV Cache to support high-capacity, cr...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: /aibrix), we have implemented a Distributed KV Cache to support high-capacity, cross-engine KV reuse. Our integration with vLLM aligns with the **KV transfer connector** framework introduced by [PR #10502](https://githu...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: V reuse across different cache backends. This RFC aims to enhance vLLM's capability to offload KV cache to external KV cache services by extending the KV transfer connector framework, enabling more memory-efficient and...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ut high-speed interconnects like RDMA, suited for tasks related to 7B/8B models running on 24/32GiB GPU cards. In these setups, GPUs within the same instance (typically 8-16 GPUs) share a single VPC NIC, leading to sign...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
