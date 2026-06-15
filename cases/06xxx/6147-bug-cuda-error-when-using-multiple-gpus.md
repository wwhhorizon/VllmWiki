# vllm-project/vllm#6147: [Bug]: CUDA error when using multiple GPUs

| 字段 | 值 |
| --- | --- |
| Issue | [#6147](https://github.com/vllm-project/vllm/issues/6147) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf;oom;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: CUDA error when using multiple GPUs

### Issue 正文摘录

### Your current environment ```text (vllm) nd600@PC-7C610BFD7B:~$ python collect_env.py Collecting environment information... /home/nd600/miniconda3/envs/vllm/lib/python3.10/site-packages/torch/cuda/__init__.py:118: UserWarning: CUDA initialization: Unexpected error from cudaGetDeviceCount(). Did you run some cuda functions before calling NumCudaDevices() that might have already set an error? Error 2: out of memory (Triggered internally at ../c10/cuda/CUDAFunctions.cpp:108.) return torch._C._cuda_getDeviceCount() > 0 PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version: Could not collect CMake version: version 3.30.0 Libc version: glibc-2.35 Python version: 3.10.14 (main, May 6 2024, 19:42:50) [GCC 11.2.0] (64-bit runtime) Python platform: Linux-5.15.153.1-microsoft-standard-WSL2-x86_64-with-glibc2.35 Is CUDA available: False CUDA runtime version: 12.1.66 CUDA_MODULE_LOADING set to: N/A GPU models and configuration: GPU 0: NVIDIA RTX 4000 Ada Generation GPU 1: NVIDIA RTX 4000 Ada Generation GPU 2: NVIDIA RTX 4000 Ada Gener...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: Functions.cpp:108.) return torch._C._cuda_getDeviceCount() > 0 PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (x86_64) GCC vers...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 7: [Bug]: CUDA error when using multiple GPUs bug;stale ### Your current environment ```text (vllm) nd600@PC-7C610BFD7B:~$ python collect_env.py Collecting environment information... /home/nd600/miniconda3/envs/vllm/lib/py...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 7: [Bug]: CUDA error when using multiple GPUs bug;stale ### Your current environment ```text (vllm) nd600@PC-7C610BFD7B:~$ python collect_env.py Collecting environment information... /home/nd600/miniconda3/envs/vllm/lib/py...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 6: avx512cd sha_ni avx512bw avx512vl xsaveopt xsavec xgetbv1 xsaves avx512_bf16 clzero xsaveerptr arat npt nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pausefilter pfthreshold v_vmsave_vmload avx512vbmi umip av...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: m) nd600@PC-7C610BFD7B:~$ python collect_env.py Collecting environment information... /home/nd600/miniconda3/envs/vllm/lib/python3.10/site-packages/torch/cuda/__init__.py:118: UserWarning: CUDA initialization: Unexpecte...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
