# vllm-project/vllm#30392: [Bug]: Docker image v0.12.0 Fail to serve via Docker image

| 字段 | 值 |
| --- | --- |
| Issue | [#30392](https://github.com/vllm-project/vllm/issues/30392) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Docker image v0.12.0 Fail to serve via Docker image

### Issue 正文摘录

### Your current environment ```text Collecting environment information... ============================== System Info ============================== OS : Ubuntu 22.04.5 LTS (x86_64) GCC version : (Ubuntu 11.4.0-1ubuntu1~22.04.2) 11.4.0 Clang version : Could not collect CMake version : Could not collect Libc version : glibc-2.35 ============================== PyTorch Info ============================== PyTorch version : 2.9.0+cu129 Is debug build : False CUDA used to build PyTorch : 12.9 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.12.12 (main, Oct 10 2025, 08:52:57) [GCC 11.4.0] (64-bit runtime) Python platform : Linux-6.6.87.2-microsoft-standard-WSL2-x86_64-with-glibc2.35 ============================== CUDA / GPU Info ============================== Is CUDA available : True CUDA runtime version : 12.9.86 CUDA_MODULE_LOADING set to : GPU models and configuration : GPU 0: NVIDIA RTX A4000 GPU 1: NVIDIA RTX A4000 Nvidia driver version : 581.15 cuDNN version : Could not collect HIP runtime version : N/A MIOpen runtime version : N/A Is XNNPACK available : True ============================== CPU Info...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: [Bug]: Docker image v0.12.0 Fail to serve via Docker image usage;stale ### Your current environment ```text Collecting environment information... ============================== System Info =============================
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: version : 2.9.0+cu129 Is debug build : False CUDA used to build PyTorch : 12.9 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.12.12 (...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 5: === Versions of relevant libraries ============================== [pip3] flashinfer-python==0.5.3 [pip3] numpy==2.2.0 [pip3] nvidia-cublas-cu12==12.9.1.4 [pip3] nvidia-cuda-cupti-cu12==12.9.79 [pip3] nvidia-cuda-nvrtc-c...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: age;stale ### Your current environment ```text Collecting environment information... ============================== System Info ============================== OS : Ubuntu 22.04.5 LTS (x86_64) GCC version : (Ubuntu 11.4....
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Bug]: Docker image v0.12.0 Fail to serve via Docker image usage;stale ### Your current environment ```text Collecting environment information... ============================== System Info ==============================...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
