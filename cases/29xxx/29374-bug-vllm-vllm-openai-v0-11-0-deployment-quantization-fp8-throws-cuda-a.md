# vllm-project/vllm#29374: [Bug]: vllm/vllm-openai:v0.11.0 deployment --quantization fp8 throws cuda and tensor errors

| 字段 | 值 |
| --- | --- |
| Issue | [#29374](https://github.com/vllm-project/vllm/issues/29374) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;model_support;quantization;scheduler_memory |
| 子分类 | env_compat |
| Operator 关键词 | cuda;fp8;quantization |
| 症状 |  |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: vllm/vllm-openai:v0.11.0 deployment --quantization fp8 throws cuda and tensor errors

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Please help me to quantize the model,and mention which flag should i use for quantization. Please find my deployment spec Model - meta-llama/Llama-3.3-70B-Instruct: - --quantization - fp8 - --kv-cache-dtype - fp8 Enabling "quantization fp8" is failing deployment. Spec: NVIDIA-SMI 550.127.08 Driver Version: 550.127.08 CUDA Version: 12.9 Error: Exception raised from c10_cuda_check_implementation at /pytorch/c10/cuda/CUDAException.cpp:42 (most recent call first): frame #0: c10::Error::Error(c10::SourceLocation, std::__cxx11::basic_string , std::allocator >) + 0x80 (0x7f9b9b4d9eb0 in /usr/local/lib/python3.12/dist-packages/torch/lib/libc10.so) frame #1: + 0x111c7 (0x7f9b9b56c1c7 in /usr/local/lib/python3.12/dist-packages/torch/lib/libc10_cuda.so) frame #2: c10d::symmetric_memory::AllocationRef::~AllocationRef() + 0xce (0x7f9b3eb25ece in /usr/local/lib/python3.12/dist-packages/torch/lib/libtorch_cuda.so) frame #3: c10d::symmetric_memory::Block::~Block() + 0x1d2 (0x7f9b3eb2cc92 in /usr/local/lib/python3.12/dist-packages/torch/lib/libtorch_cuda.so) frame #4: c10d::symmetric_memory::CUDASymmetricMemoryAllocator::free(void*) + 0x1de (0x7f...

## 现有链接修复摘要

#4 Use FlashAttention for `multi_query_kv_attention` | #6 Automatically configure KV cache size | #7 Support beam search & parallel generation | #12 Implement preemption via recomputation & Refactor scheduling logic

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Bug]: vllm/vllm-openai:v0.11.0 deployment --quantization fp8 throws cuda and tensor errors bug;stale ### Your current environment ### 🐛 Describe the bug Please help me to quantize the model,and mention which flag shoul...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: vllm/vllm-openai:v0.11.0 deployment --quantization fp8 throws cuda and tensor errors bug;stale ### Your current environment ### 🐛 Describe the bug Please help me to quantize the model,and mention which flag shoul...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: t environment ### 🐛 Describe the bug Please help me to quantize the model,and mention which flag should i use for quantization. Please find my deployment spec Model - meta-llama/Llama-3.3-70B-Instruct: - --quantization...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: " is failing deployment. Spec: NVIDIA-SMI 550.127.08 Driver Version: 550.127.08 CUDA Version: 12.9 Error: Exception raised from c10_cuda_check_implementation at /pytorch/c10/cuda/CUDAException.cpp:42 (most recent call f...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: ama-3.3-70B-Instruct: - --quantization - fp8 - --kv-cache-dtype - fp8 Enabling "quantization fp8" is failing deployment. Spec: NVIDIA-SMI 550.127.08 Driver Version: 550.127.08 CUDA Version: 12.9 Error: Exception raised...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#4](https://github.com/vllm-project/vllm/pull/4) | mentioned | 0.45 | Use FlashAttention for `multi_query_kv_attention` | /local/lib/python3.12/dist-packages/torch/lib/libtorch_cuda.so) frame #4: c10d::symmetric_memory::cudasymmetricmemoryallocator::free(void*) + 0x1de (0x7f9b3eb247fe in /usr/local/l… |
| [#6](https://github.com/vllm-project/vllm/pull/6) | mentioned | 0.45 | Automatically configure KV cache size | in /usr/local/lib/python3.12/dist-packages/torch/lib/libc10.so) frame #6: <unknown function> + 0x434a5f (0x7f9b8e172a5f in /usr/local/lib/python3.12/dist-packages/torch/lib/libtor… |
| [#7](https://github.com/vllm-project/vllm/pull/7) | mentioned | 0.45 | Support beam search & parallel generation | ocal/lib/python3.12/dist-packages/torch/lib/libtorch_python.so) frame #7: c10::tensorimpl::~tensorimpl() + 0x9 (0x7f9b9b4b7179 in /usr/local/lib/python3.12/dist-packages/torch/lib… |
| [#12](https://github.com/vllm-project/vllm/pull/12) | mentioned | 0.45 | Implement preemption via recomputation & Refactor scheduling logic | orker_tp6() [0x59b914] frame #11: vllm::worker_tp6() [0x59b914] frame #12: vllm::worker_tp6() [0x53be84] frame #13: vllm::worker_tp6() [0x59bded] frame #14: vllm::worker_tp6() [0x… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
