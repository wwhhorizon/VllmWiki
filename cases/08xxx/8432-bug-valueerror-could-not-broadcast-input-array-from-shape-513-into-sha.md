# vllm-project/vllm#8432: [Bug]: ValueError: could not broadcast input array from shape (513,) into shape (512,)

| 字段 | 值 |
| --- | --- |
| Issue | [#8432](https://github.com/vllm-project/vllm/issues/8432) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | shape_align |
| Operator 关键词 | attention;cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf;oom |
| 根因提示 | env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: ValueError: could not broadcast input array from shape (513,) into shape (512,)

### Issue 正文摘录

### Your current environment Collecting environment information... /home/miniconda3/envs/vllm/lib/python3.12/site-packages/torch/cuda/init.py:128: UserWarning: CUDA initialization: Unexpected error from cudaGetDeviceCount(). Did you run some cuda functions before calling NumCudaDevices() that might have already set an error? Error 2: out of memory (Triggered internally at ../c10/cuda/CUDAFunctions.cpp:108.) return torch._C._cuda_getDeviceCount() > 0 PyTorch version: 2.4.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version: Could not collect CMake version: version 3.22.1 Libc version: glibc-2.35 Python version: 3.12.4 | packaged by Anaconda, Inc. | (main, Jun 18 2024, 15:12:24) [GCC 11.2.0] (64-bit runtime) Python platform: Linux-5.15.153.1-microsoft-standard-WSL2-x86_64-with-glibc2.35 Is CUDA available: False CUDA runtime version: 12.5.82 CUDA_MODULE_LOADING set to: N/A GPU models and configuration: GPU 0: NVIDIA RTX 4000 Ada Generation GPU 1: NVIDIA RTX 4000 Ada Generation GPU 2: NVIDIA RTX 4000 Ada Generation GPU 3: NVIDIA RTX 4000 Ada Genera...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: DAFunctions.cpp:108.) return torch._C._cuda_getDeviceCount() > 0 PyTorch version: 2.4.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (x86_64) GCC ve...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: rmation... /home/miniconda3/envs/vllm/lib/python3.12/site-packages/torch/cuda/init.py:128: UserWarning: CUDA initialization: Unexpected error from cudaGetDeviceCount(). Did you run some cuda functions before calling Num...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: could not broadcast input array from shape (513,) into shape (512,) bug;stale ### Your current environment Collecting environment information... /home/miniconda3/envs/vllm/lib/python3.12/site-packages/torch/cuda/init.py...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: (512,) bug;stale ### Your current environment Collecting environment information... /home/miniconda3/envs/vllm/lib/python3.12/site-packages/torch/cuda/init.py:128: UserWarning: CUDA initialization: Unexpected error from...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: cuda_getDeviceCount() > 0 PyTorch version: 2.4.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 1...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
