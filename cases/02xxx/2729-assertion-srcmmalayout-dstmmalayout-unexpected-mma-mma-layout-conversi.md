# vllm-project/vllm#2729: Assertion `!(srcMmaLayout && dstMmaLayout) && "Unexpected mma -> mma layout conversion"' failed.

| 字段 | 值 |
| --- | --- |
| Issue | [#2729](https://github.com/vllm-project/vllm/issues/2729) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 28; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | gemm_linear;scheduler_memory |
| 子分类 | env_compat |
| Operator 关键词 | cuda;triton |
| 症状 |  |
| 根因提示 | env_dependency;memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> Assertion `!(srcMmaLayout && dstMmaLayout) && "Unexpected mma -> mma layout conversion"' failed.

### Issue 正文摘录

When executing script `examples/offline_inference_with_prefix.py`, it will call `context_attention_fwd` from `vllm.model_executor.layers.triton_kernel.prefix_prefill`, which triggered the following error ``` python: /project/lib/Analysis/Allocation.cpp:40: std::pair , llvm::SmallVector > mlir::triton::getCvtOrder(mlir::Attribute, mlir::Attribute): Assertion `!(srcMmaLayout && dstMmaLayout) && "Unexpected mma -> mma layout conversion"' failed. ``` Platform : - V100 - CUDA 12.0 - python 3.11.6 - vllm 0.3.0+cu120 - triton 2.1.0 - torch 2.1.2 related to #1669

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: t && dstMmaLayout) && "Unexpected mma -> mma layout conversion"' failed. stale When executing script `examples/offline_inference_with_prefix.py`, it will call `context_attention_fwd` from `vllm.model_executor.layers.tri...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ion `!(srcMmaLayout && dstMmaLayout) && "Unexpected mma -> mma layout conversion"' failed. stale When executing script `examples/offline_inference_with_prefix.py`, it will call `context_attention_fwd` from `vllm.model_e...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: r ``` python: /project/lib/Analysis/Allocation.cpp:40: std::pair , llvm::SmallVector > mlir::triton::getCvtOrder(mlir::Attribute, mlir::Attribute): Assertion `!(srcMmaLayout && dstMmaLayout) && "Unexpected mma -> mma la...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: `, it will call `context_attention_fwd` from `vllm.model_executor.layers.triton_kernel.prefix_prefill`, which triggered the following error ``` python: /project/lib/Analysis/Allocation.cpp:40: std::pair , llvm::SmallVec...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: Assertion `!(srcMmaLayout && dstMmaLayout) && "Unexpected mma -> mma layout conversion"' failed. stale When executing script `examples/offline_inference_with_prefix.py`, it will call `context_attention_fwd` from `vllm.m...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
