# vllm-project/vllm#28426: [Bug]: RuntimeError: it->second->use_count > 0 INTERNAL ASSERT FAILED at "/pytorch/c10/cuda/CUDACachingAllocator.cpp":2630, please report a bug to PyTorch.

| 字段 | 值 |
| --- | --- |
| Issue | [#28426](https://github.com/vllm-project/vllm/issues/28426) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;scheduler_memory |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: RuntimeError: it->second->use_count > 0 INTERNAL ASSERT FAILED at "/pytorch/c10/cuda/CUDACachingAllocator.cpp":2630, please report a bug to PyTorch.

### Issue 正文摘录

### Your current environment ``` ollecting environment information... ============================== System Info ============================== OS : CentOS Stream 9 (x86_64) GCC version : (GCC) 11.5.0 20240719 (Red Hat 11.5.0-11) Clang version : 20.1.8 (CentOS 20.1.8-1.el9) CMake version : version 4.1.2 Libc version : glibc-2.34 ============================== PyTorch Info ============================== PyTorch version : 2.9.0+cu128 Is debug build : False CUDA used to build PyTorch : 12.8 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.10.19 | packaged by conda-forge | (main, Oct 22 2025, 22:29:10) [GCC 14.3.0] (64-bit runtime) Python platform : Linux-6.9.0-0_fbk10_0_gc5fa564d33e3-x86_64-with-glibc2.34 ============================== CUDA / GPU Info ============================== Is CUDA available : True CUDA runtime version : 12.9.86 CUDA_MODULE_LOADING set to : GPU models and configuration : GPU 0: NVIDIA H100 GPU 1: NVIDIA H100 GPU 2: NVIDIA H100 GPU 3: NVIDIA H100 GPU 4: NVIDIA H100 GPU 5: NVIDIA H100 GPU 6: NVIDIA H100 GPU 7: NVIDIA H100 Nvidia driver version : 535.183.06 cuDNN version : Probab...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: ============ OS : CentOS Stream 9 (x86_64) GCC version : (GCC) 11.5.0 20240719 (Red Hat 11.5.0-11) Clang version : 20.1.8 (CentOS 20.1.8-1.el9) CMake version : version 4.1.2 Libc version : glibc-2.34 ===
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: Error: it->second->use_count > 0 INTERNAL ASSERT FAILED at "/pytorch/c10/cuda/CUDACachingAllocator.cpp":2630, please report a bug to PyTorch. bug ### Your current environment ``` ollecting environment information... ===...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: === Versions of relevant libraries ============================== [pip3] flashinfer-python==0.5.2 [pip3] numpy==2.2.6 [pip3] nvidia-cublas-cu12==12.8.4.1 [pip3] nvidia-cuda-cupti-cu12==12.8.90 [pip3] nvidia-cuda-nvrtc-c...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: o PyTorch. bug ### Your current environment ``` ollecting environment information... ============================== System Info ============================== OS : CentOS Stream 9 (x86_64) GCC version : (GCC) 11.5.0 202...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: n cppc arat npt lbrv svm_lock nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pausefilter pfthreshold avic v_vmsave_vmload vgif x2avic v_spec_ctrl vnmi avx512vbmi umip pku ospke avx512_vbmi2 gfni vaes vpclmulqd...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
