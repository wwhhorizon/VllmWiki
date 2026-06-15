# vllm-project/vllm#38260: [RFC]: Multi-tier KV offloading via the vLLM offloading connector

| 字段 | 值 |
| --- | --- |
| Issue | [#38260](https://github.com/vllm-project/vllm/issues/38260) |
| 状态 | open |
| 标签 | RFC |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Multi-tier KV offloading via the vLLM offloading connector

### Issue 正文摘录

### Motivation. To date, vLLM offers native KV offloading to CPU memory but does not support further offloading from CPU memory to other tiers such as storage. Implementations for storage offload should either work directly with storage or implement their own CPU offloading as an additional tier. This document describes a high level design to natively support multi-tier KV offloading in vLLM. The architecture supports a single primary tier, in most cases CPU DRAM, and multiple secondary tiers. ## Goals - Allow simple and native integration of the current vLLM CPU offloading with secondary tiers such as storage, or connection with other vLLM nodes for PD disaggregation settings or P2P communication of KV data. - Utilize async gpu cpu transfers for primary tier and async lookup for secondary tier loads - Support for HMA models out of the box - Seamless support for cross TP offloading and transfers - Simple, clean and performant implementation of PD communication via the CPU tier What we don't intend to support - Direct GPU access (neither GPU-storage or GPU-GPU communication) - Limited flexibility for variance in block size. While we allow vLLM block size to vary, CPU block size mus...

## 候选优化模式

- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 4: storage or GPU-GPU communication) - Limited flexibility for variance in block size. While we allow vLLM block size to vary, CPU block size must be constant across all vLLM nodes (and a multiple of the underlying vLLM bl...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 3: [RFC]: Multi-tier KV offloading via the vLLM offloading connector RFC ### Motivation. To date, vLLM offers native KV offloading to CPU memory but does not support further offloading from CPU memory to other tiers such a...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: level design to natively support multi-tier KV offloading in vLLM. The architecture supports a single primary tier, in most cases CPU DRAM, and multiple secondary tiers. ## Goals - Allow simple and native integration of...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: CPU to CPU implementation while introduces more hops and therefore more latency, has several benefits: - Quicker offloading on the P node, once moved to local CPU can release GPU memory. - Shorter time GPU memory requir...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: V1 connector API and translates it to a simpler more abstract API for a backend. The multi-tier offloading has several key changes to this framework: - It designates a single (CPU DRAM) backend as the primary tier but a...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
