# vllm-project/vllm#32848: [Usage]: Structured output

| 字段 | 值 |
| --- | --- |
| Issue | [#32848](https://github.com/vllm-project/vllm/issues/32848) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: Structured output

### Issue 正文摘录

### Your current environment ```text Collecting environment information... uv is set ============================== System Info ============================== OS : Amazon Linux 2023.9.20251208 (x86_64) GCC version : (GCC) 11.5.0 20240719 (Red Hat 11.5.0-5) Clang version : Could not collect CMake version : version 3.22.2 Libc version : glibc-2.34 ============================== PyTorch Info ============================== PyTorch version : 2.9.1+cu128 Is debug build : False CUDA used to build PyTorch : 12.8 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.12.12 (main, Dec 17 2025, 21:10:06) [Clang 21.1.4 ] (64-bit runtime) Python platform : Linux-6.1.158-180.294.amzn2023.x86_64-x86_64-with-glibc2.34 ============================== CUDA / GPU Info ============================== Is CUDA available : True CUDA runtime version : 12.9.86 CUDA_MODULE_LOADING set to : GPU models and configuration : GPU 0: NVIDIA L40S Nvidia driver version : 580.105.08 cuDNN version : Could not collect HIP runtime version : N/A MIOpen runtime version : N/A Is XNNPACK available : True ============================== CPU Info ====...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: OS : Amazon Linux 2023.9.20251208 (x86_64) GCC version : (GCC) 11.5.0 20240719 (Red Hat 11.5.0-5) Clang version : Could not collect CMake version : version 3.22.2 Libc version : glibc-2.34 ==============
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: version : 2.9.1+cu128 Is debug build : False CUDA used to build PyTorch : 12.8 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.12.12 (...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: === Versions of relevant libraries ============================== [pip3] flashinfer-python==0.5.3 [pip3] numpy==2.2.6 [pip3] nvidia-cublas-cu12==12.8.4.1 [pip3] nvidia-cuda-cupti-cu12==12.8.90 [pip3] nvidia-cuda-nvrtc-c...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: put usage ### Your current environment ```text Collecting environment information... uv is set ============================== System Info ============================== OS : Amazon Linux 2023.9.20251208 (x86_64) GCC ver...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: Vulnerability Meltdown: Not affected Vulnerability Mmio stale data: Not affected Vulnerability Reg file data sampling: Not affected Vulnerability Retbleed: Not affected Vulnerability Spec rstack overflow: Mitigation; sa...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
