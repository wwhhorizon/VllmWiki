# vllm-project/vllm#26300: [Feature]: Improve vLLM CUDA Memory Utilization and Estimation

| 字段 | 值 |
| --- | --- |
| Issue | [#26300](https://github.com/vllm-project/vllm/issues/26300) |
| 状态 | open |
| 标签 | feature request |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;frontend_api;scheduler_memory |
| 子分类 | memory |
| Operator 关键词 | cache;cuda |
| 症状 | build_error;oom |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Feature]: Improve vLLM CUDA Memory Utilization and Estimation

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Thanks @houseroad for the context! It’s a general problem, 1) we do CUDA graph with memory allocation for KV cache, 2) we run the torch.compile. Since we may do memory profiling in torch.compile which may consume a lot of memory, either we may need to reserve less memory for KV cache (with some HBM wasted at the end), or we run into OOM. To solve this problem, the idea is described in https://github.com/vllm-project/vllm/issues/19480#issuecomment-3121169375, @yinghai , which looks resonable to me. 1. Reserve a big range of memory address but allocate a small amount of KV memory using subset of those memory address so that we can do the profile and cudagraph capturing. 2. Deallocate the KV memory but hold the KV memory address. Estimate how much KV we can build now that we have information of cudagraph memory usage 3. Allocate the KV memory and map to the same reserved memory address for KV. The CUDA memory allocation, deallocation, pause and resume can be found in https://github.com/fzyzcjy/torch_memory_saver/blob/0fa8e036b9f5f21d63bb1a06f70102b11f0b6743/csrc/core.cpp I think this is an important problem to solve since a lot of Cuda memory i...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: e do CUDA graph with memory allocation for KV cache, 2) we run the torch.compile. Since we may do memory profiling in torch.compile which may consume a lot of memory, either we may need to reserve less memory for KV cac...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Feature]: Improve vLLM CUDA Memory Utilization and Estimation feature request ### 🚀 The feature, motivation and pitch Thanks @houseroad for the context! It’s a general problem, 1) we do CUDA graph with memory allocatio...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: cation for KV cache, 2) we run the torch.compile. Since we may do memory profiling in torch.compile which may consume a lot of memory, either we may need to reserve less memory for KV cache (with some HBM wasted at the...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: It’s a general problem, 1) we do CUDA graph with memory allocation for KV cache, 2) we run the torch.compile. Since we may do memory profiling in torch.compile which may consume a lot of memory, either we may need to re...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: Improve vLLM CUDA Memory Utilization and Estimation feature request ### 🚀 The feature, motivation and pitch Thanks @houseroad for the context! It’s a general problem, 1) we do CUDA graph with memory allocatio...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
