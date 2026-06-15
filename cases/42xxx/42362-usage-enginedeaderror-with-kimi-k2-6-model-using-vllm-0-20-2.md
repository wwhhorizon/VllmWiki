# vllm-project/vllm#42362: [Usage]: EngineDeadError with Kimi-K2.6 model using vLLM 0.20.2

| 字段 | 值 |
| --- | --- |
| Issue | [#42362](https://github.com/vllm-project/vllm/issues/42362) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: EngineDeadError with Kimi-K2.6 model using vLLM 0.20.2

### Issue 正文摘录

### Your current environment ```text Collecting environment information... ============================== System Info ============================== OS : Ubuntu 22.04.5 LTS (aarch64) GCC version : (Ubuntu 11.4.0-1ubuntu1~22.04.3) 11.4.0 Clang version : Could not collect CMake version : Could not collect Libc version : glibc-2.35 ============================== PyTorch Info ============================== PyTorch version : 2.11.0+cu130 Is debug build : False CUDA used to build PyTorch : 13.0 ROCM used to build PyTorch : N/A XPU used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.12.13 (main, May 8 2026, 20:13:21) [GCC 11.4.0] (64-bit runtime) Python platform : Linux-6.8.0-1025-nvidia-64k-aarch64-with-glibc2.35 ============================== CUDA / GPU Info ============================== Is CUDA available : True CUDA runtime version : 13.0.88 CUDA_MODULE_LOADING set to : GPU models and configuration : GPU 0: NVIDIA GB200 GPU 1: NVIDIA GB200 GPU 2: NVIDIA GB200 GPU 3: NVIDIA GB200 Nvidia driver version : 580.126.20 cuDNN version : Could not collect HIP runtime version : N/A MIOpen runtime version : N/A Is XNNPA...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: ======== OS : Ubuntu 22.04.5 LTS (aarch64) GCC version : (Ubuntu 11.4.0-1ubuntu1~22.04.3) 11.4.0 Clang version : Could not collect CMake version : Could not collect Libc version : glibc-2.35 ============
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: ==================== OS : Ubuntu 22.04.5 LTS (aarch64) GCC version : (Ubuntu 11.4.0-1ubuntu1~22.04.3) 11.4.0 Clang version : Could not collect CMake version : Could not collect Libc version : glibc-2.35
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: === Versions of relevant libraries ============================== [pip3] flashinfer-python==0.6.8.post1 [pip3] numpy==2.2.6 [pip3] nvidia-cublas==13.1.0.3 [pip3] nvidia-cuda-cupti==13.0.85 [pip3] nvidia-cuda-nvrtc==13.0...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Usage]: EngineDeadError with Kimi-K2.6 model using vLLM 0.20.2 usage ### Your current environment ```text Collecting environment information... ============================== System Info ==============================...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: ed Vulnerability Meltdown: Not affected Vulnerability Mmio stale data: Not affected Vulnerability Reg file data sampling: Not affected Vulnerability Retbleed: Not affected Vulnerability Spec rstack overflow: Not affecte...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
