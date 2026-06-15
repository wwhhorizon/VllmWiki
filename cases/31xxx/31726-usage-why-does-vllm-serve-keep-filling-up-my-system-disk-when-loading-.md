# vllm-project/vllm#31726: [Usage]: Why does `vllm serve` keep filling up my system disk when loading a model from a network mount?

| 字段 | 值 |
| --- | --- |
| Issue | [#31726](https://github.com/vllm-project/vllm/issues/31726) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error;nan_inf;slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: Why does `vllm serve` keep filling up my system disk when loading a model from a network mount?

### Issue 正文摘录

### Your current environment ``` Collecting environment information... ============================== System Info ============================== OS : Ubuntu 22.04.5 LTS (x86_64) GCC version : (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version : Could not collect CMake version : version 3.22.1 Libc version : glibc-2.35 ============================== PyTorch Info ============================== PyTorch version : 2.9.0+cu128 Is debug build : False CUDA used to build PyTorch : 12.8 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.11.10 (main, Oct 3 2024, 07:29:13) [GCC 11.2.0] (64-bit runtime) Python platform : Linux-5.10.134-18.0.5.lifsea8.x86_64-x86_64-with-glibc2.35 ============================== CUDA / GPU Info ============================== Is CUDA available : True CUDA runtime version : 12.4.131 CUDA_MODULE_LOADING set to : GPU models and configuration : GPU 0: NVIDIA H20 GPU 1: NVIDIA H20 GPU 2: NVIDIA H20 GPU 3: NVIDIA H20 GPU 4: NVIDIA H20 GPU 5: NVIDIA H20 GPU 6: NVIDIA H20 GPU 7: NVIDIA H20 Nvidia driver version : 560.35.03 cuDNN version : Probably one of the following: /usr/lib/x86_64-linux...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: ========= OS : Ubuntu 22.04.5 LTS (x86_64) GCC version : (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version : Could not collect CMake version : version 3.22.1 Libc version : glibc-2.35 =================
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: version : 2.9.0+cu128 Is debug build : False CUDA used to build PyTorch : 12.8 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.11.10 (...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: ge]: Why does `vllm serve` keep filling up my system disk when loading a model from a network mount? usage;stale ### Your current environment ``` Collecting environment information... ============================== Syst...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: nt libraries ============================== [pip3] botorch==0.8.5 [pip3] flashinfer-python==0.5.3 [pip3] gpytorch==1.10 [pip3] msgpack-numpy==0.4.8 [pip3] numpy==1.26.4 [pip3] nvidia-cublas-cu12==12.8.4.1 [pip3] nvidia-...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: 1 NVIDIA_DRIVER_CAPABILITIES=compute,utility NCCL_DEBUG=TRACE VLLM_TORCH_PROFILER_DIR=/bucket/serve/benchmark/profile_result/vllm NVIDIA_PRODUCT_NAME=CUDA CUDA_VERSION=12.1.1 VLLM_ALLREDUCE_USE_SYMM_MEM=0 LD_LIBRARY_PAT...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
