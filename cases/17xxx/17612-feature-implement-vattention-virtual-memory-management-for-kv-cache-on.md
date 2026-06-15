# vllm-project/vllm#17612: [Feature]: Implement vAttention: Virtual Memory Management for KV Cache on NVIDIA GPUs

| 字段 | 值 |
| --- | --- |
| Issue | [#17612](https://github.com/vllm-project/vllm/issues/17612) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;frontend_api;sampling_logits;scheduler_memory |
| 子分类 | memory |
| Operator 关键词 | attention;cache;cuda;kernel |
| 症状 | slowdown |
| 根因提示 | env_dependency;memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Feature]: Implement vAttention: Virtual Memory Management for KV Cache on NVIDIA GPUs

### Issue 正文摘录

### 🚀 The feature, motivation and pitch ### Description vAttention is a memory management approach without PagedAttention for managing KV cache in LLM serving. It uses CUDA virtual memory APIs to decouple virtual and physical memory, retaining a contiguous virtual memory layout while mitigating physical memory fragmentation. (Fig 5 source 1) ### Motivation The current vLLm approach of PagedAttention has following issues: 1. **Block Table Management**: Managing the block table is introduces runtime overhead in CPU. 2. **Performance Overhead in Attention Kernels:** Attention kernels must adapt to block-based cache layouts, leading to performance penalties. ### Solution details Utilizing CUDA's VMM API, we propose an improved cache management scheme: 1. **Virtual Memory Reservation:** Reserves a contiguous virtual memory region for each sequence using CUDA’s _cuMemAddressReserve_ API. 2. **Physical Memory Management:** Physical memory is allocated and mapped on demand using _cuMemCreate, cuMemMap_, and _cuMemSetAccess_ 3. **Cache kernel write:** Reshaping decoded outputs and writing them into the KV cache with virtual contiguity. 4. **Metadata and Memory Control:** A block manager tr...

## 候选优化模式

- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 5: virtual memory APIs to decouple virtual and physical memory, retaining a contiguous virtual memory layout while mitigating physical memory fragmentation. (Fig 5 source 1) ### Motivation The current vLLm approach of Page...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: Attention: Virtual Memory Management for KV Cache on NVIDIA GPUs feature request;stale ### 🚀 The feature, motivation and pitch ### Description vAttention is a memory management approach without PagedAttention for managi...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: y up to **1.23×** compared to the use of PagedAttention-based kernels of FlashAttention-2 and FlashInfer. Check sources for more details ### Sources 1. [vAttention: Dynamic Memory Management for Serving LLMs without Pag...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: Benefits 1. Memory management and map is handled by the GPU driver, enhancing flexibility and potentially improving performance. 2. Reduces overhead in the attention kernel due to simplified memory management. ### Resul...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ach without PagedAttention for managing KV cache in LLM serving. It uses CUDA virtual memory APIs to decouple virtual and physical memory, retaining a contiguous virtual memory layout while mitigating physical memory fr...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
