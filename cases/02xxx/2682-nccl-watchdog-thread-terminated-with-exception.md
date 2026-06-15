# vllm-project/vllm#2682: NCCL watchdog thread terminated with exception

| 字段 | 值 |
| --- | --- |
| Issue | [#2682](https://github.com/vllm-project/vllm/issues/2682) |
| 状态 | closed |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api |
| 子分类 |  |
| Operator 关键词 | cuda;kernel;operator |
| 症状 | build_error;mismatch |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> NCCL watchdog thread terminated with exception

### Issue 正文摘录

I got this error when running llama2-7b on tp=8. The engine succeeded for the first few prompts and then stuck into this exception. ``` (RayWorkerVllm pid=5304) [E ProcessGroupNCCL.cpp:916] [Rank 7] NCCL watchdog thread terminated with exception: CUDA error: unknown error (RayWorkerVllm pid=5304) CUDA kernel errors might be asynchronously reported at some other API call, so the stacktrace below might be incorrect.(RayWorkerVllm pid=5304) For debugging consider passing CUDA_LAUNCH_BLOCKING=1. (RayWorkerVllm pid=5304) Compile with `TORCH_USE_CUDA_DSA` to enable device-side assertions. (RayWorkerVllm pid=5304) (RayWorkerVllm pid=5304) Exception raised from c10_cuda_check_implementation at ../c10/cuda/CUDAException.cpp:44 (most recent call first): (RayWorkerVllm pid=5304) frame #0: c10::Error::Error(c10::SourceLocation, std::string) + 0x57 (0x7fdc6810f617 in /usr/local/lib/python3.10/dist-packages/torch/lib/libc10.so) (RayWorkerVllm pid=5304) frame #1: c10::detail::torchCheckFail(char const*, char const*, unsigned int, std::string const&) + 0x64 (0x7fdc680ca98d in /usr/local/lib/python3.10/dist-packages/torch/lib/libc10.so) (RayWorkerVllm pid=5304) frame #2: c10::cuda::c10_cuda_check_...

## 现有链接修复摘要

#4 Use FlashAttention for `multi_query_kv_attention` | #6 Automatically configure KV cache size | #7 Support beam search & parallel generation

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: ugging consider passing CUDA_LAUNCH_BLOCKING=1. (RayWorkerVllm pid=5304) Compile with `TORCH_USE_CUDA_DSA` to enable device-side assertions. (RayWorkerVllm pid=5304) (RayWorkerVllm pid=5304) Exception raised from c10_cu...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: upNCCL.cpp:916] [Rank 7] NCCL watchdog thread terminated with exception: CUDA error: unknown error (RayWorkerVllm pid=5304) CUDA kernel errors might be asynchronously reported at some other API call, so the stacktrace b...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: watchdog thread terminated with exception I got this error when running llama2-7b on tp=8. The engine succeeded for the first few prompts and then stuck into this exception. ``` (RayWorkerVllm pid=5304) [E ProcessGroupN...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: tend_api cuda;kernel;operator build_error;mismatch env_dependency #4 Use FlashAttention for `multi_query_kv_attention` | #6 Automatically configure KV cache size | #7 Support beam search & parallel generation I got this...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: build;distributed_parallel;frontend_api cuda;kernel;operator build_error;mismatch env_dependency #4 Use FlashAttention for `multi_query_kv_attention` | #6 Automatically configure KV cache size | #7 Support beam search &...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#4](https://github.com/vllm-project/vllm/pull/4) | mentioned | 0.45 | Use FlashAttention for `multi_query_kv_attention` | -packages/torch/lib/libtorch_cuda.so) (rayworkervllm pid=5304) frame #4: c10d::processgroupnccl::worknccl::iscompleted() + 0x58 (0x7fd8d5ec8078 in /usr/local/lib/python3.10/dist-p… |
| [#6](https://github.com/vllm-project/vllm/pull/6) | mentioned | 0.45 | Automatically configure KV cache size | -packages/torch/lib/libtorch_cuda.so) (rayworkervllm pid=5304) frame #6: c10d::processgroupnccl::ncclcommwatchdog() + 0x78 (0x7fd8d5edec18 in /usr/local/lib/python3.10/dist-packag… |
| [#7](https://github.com/vllm-project/vllm/pull/7) | mentioned | 0.45 | Support beam search & parallel generation | -packages/torch/lib/libtorch_cuda.so) (rayworkervllm pid=5304) frame #7: <unknown function> + 0xdc2b3 (0x7fdc6b63e2b3 in /usr/lib/x86_64-linux-gnu/libstdc++.so.6) (rayworkervllm pi |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
