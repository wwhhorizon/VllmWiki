# vllm-project/vllm#21731: [Bug]: Assertion `idx_dim >= 0 && idx_dim < index_size && "index out of bounds"` failed.

| 字段 | 值 |
| --- | --- |
| Issue | [#21731](https://github.com/vllm-project/vllm/issues/21731) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;model_support;quantization;sampling_logits;scheduler_memory |
| 子分类 | precision |
| Operator 关键词 | cuda;kernel;operator;quantization;sampling |
| 症状 | build_error;crash;mismatch |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: Assertion `idx_dim >= 0 && idx_dim < index_size && "index out of bounds"` failed.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When I run Llama based bf16 model, Sometimes the framework died with the messages below. I tried on vLLM v0.8.4, vLLM v0.9.2 and both died. ``` /pytorch/aten/src/ATen/native/cuda/ScatterGatherKernel.cu:144: operator(): block: [6,0,0], thread: [64,0,0] Assertion `idx_dim >= 0 && idx_dim = 0 && idx_dim = 0 && idx_dim = 0 && idx_dim = 0 && idx_dim = 0 && idx_dim = 0 && idx_dim = 0 && idx_dim = 0 && idx_dim = 0 && idx_dim , std::allocator >) + 0x98 (0x7f0c249785e8 in /usr/local/lib/python3.12/dist-packages/torch/lib/libc10.so) frame #1: c10::detail::torchCheckFail(char const*, char const*, unsigned int, std::__cxx11::basic_string , std::allocator > const&) + 0xe0 (0x7f0c2490d4a2 in /usr/local/lib/python3.12/dist-packages/torch/lib/libc10.so) frame #2: c10::cuda::c10_cuda_check_implementation(int, char const*, char const*, int, bool) + 0x3c2 (0x7f0c24deb422 in /usr/local/lib/python3.12/dist-packages/torch/lib/libc10_cuda.so) frame #3: c10d::ProcessGroupNCCL::WorkNCCL::finishedGPUExecutionInternal() const + 0x56 (0x7f0bb468b456 in /usr/local/lib/python3.12/dist-packages/torch/lib/libtorch_cuda.so) frame #4: c10d::ProcessGroupNCCL::Work...

## 现有链接修复摘要

#4 Use FlashAttention for `multi_query_kv_attention` | #6 Automatically configure KV cache size | #7 Support beam search & parallel generation

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ight be incorrect. For debugging consider passing CUDA_LAUNCH_BLOCKING=1 Compile with `TORCH_USE_CUDA_DSA` to enable device-side assertions. Exception raised from c10_cuda_check_implementation at /pytorch/c10/cuda/CUDAE...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: r current environment ### 🐛 Describe the bug When I run Llama based bf16 model, Sometimes the framework died with the messages below. I tried on vLLM v0.8.4, vLLM v0.9.2 and both died. ``` /pytorch/aten/src/ATen/native/...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: LM v0.8.4, vLLM v0.9.2 and both died. ``` /pytorch/aten/src/ATen/native/cuda/ScatterGatherKernel.cu:144: operator(): block: [6,0,0], thread: [64,0,0] Assertion `idx_dim >= 0 && idx_dim = 0 && idx_dim = 0 && idx_dim = 0...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: bug ### Your current environment ### 🐛 Describe the bug When I run Llama based bf16 model, Sometimes the framework died with the messages below. I tried on vLLM v0.8.4, vLLM v0.9.2 and both died. ``` /pytorch/aten/src/A...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: gnu/libc.so.6) terminate called after throwing an instance of 'c10::DistBackendError' terminate called after throwing an instance of 'c10::DistBackendError' what(): [PG ID 2 PG GUID 3 Rank 0] Process group watchdog thre...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#4](https://github.com/vllm-project/vllm/pull/4) | mentioned | 0.45 | Use FlashAttention for `multi_query_kv_attention` | 53 (0x7f05c9bb3253 in /usr/lib/x86_64-linux-gnu/libstdc++.so.6) frame #4: <unknown function> + 0x94ac3 (0x7f064a8edac3 in /usr/lib/x86_64-linux-gnu/libc.so.6) frame #5: <unknown f… |
| [#6](https://github.com/vllm-project/vllm/pull/6) | mentioned | 0.45 | Automatically configure KV cache size | /local/lib/python3.12/dist-packages/torch/lib/libtorch_cuda.so) frame #6: c10d::processgroupnccl::ncclcommwatchdog() + 0x14d (0x7f05d989ee8d in /usr/local/lib/python3.12/dist-pack… |
| [#7](https://github.com/vllm-project/vllm/pull/7) | mentioned | 0.45 | Support beam search & parallel generation | /local/lib/python3.12/dist-packages/torch/lib/libtorch_cuda.so) frame #7: <unknown function> + 0xdc253 (0x7f05c9bb3253 in /usr/lib/x86_64-linux-gnu/libstdc++.so.6) frame #8: <unkn… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
