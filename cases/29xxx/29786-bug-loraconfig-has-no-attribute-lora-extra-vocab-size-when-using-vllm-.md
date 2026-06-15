# vllm-project/vllm#29786: [Bug]: LoRAConfig has no attribute 'lora_extra_vocab_size' when using vLLM + verl GRPO LoRA

| 字段 | 值 |
| --- | --- |
| Issue | [#29786](https://github.com/vllm-project/vllm/issues/29786) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: LoRAConfig has no attribute 'lora_extra_vocab_size' when using vLLM + verl GRPO LoRA

### Issue 正文摘录

### Your current environment ============================== System Info ============================== OS : Ubuntu 24.04.3 LTS (aarch64) GCC version : (Ubuntu 13.3.0-6ubuntu2~24.04) 13.3.0 Clang version : Could not collect CMake version : version 4.1.2 Libc version : glibc-2.39 ============================== PyTorch Info ============================== PyTorch version : 2.9.1+cu130 Is debug build : False CUDA used to build PyTorch : 13.0 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.12.3 (main, Nov 6 2025, 13:44:16) [GCC 13.3.0] (64-bit runtime) Python platform : Linux-6.14.0-1013-nvidia-aarch64-with-glibc2.39 ============================== CUDA / GPU Info ============================== Is CUDA available : True CUDA runtime version : 13.0.88 CUDA_MODULE_LOADING set to : GPU models and configuration : GPU 0: NVIDIA GB10 Nvidia driver version : 580.95.05 cuDNN version : Could not collect HIP runtime version : N/A MIOpen runtime version : N/A Is XNNPACK available : True ============================== CPU Info ============================== Architecture: aarch64 CPU Operating Mode: 64-bit Byte Order:...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 10: ======== OS : Ubuntu 24.04.3 LTS (aarch64) GCC version : (Ubuntu 13.3.0-6ubuntu2~24.04) 13.3.0 Clang version : Could not collect CMake version : version 4.1.2 Libc version : glibc-2.39 ==================
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: ==================== OS : Ubuntu 24.04.3 LTS (aarch64) GCC version : (Ubuntu 13.3.0-6ubuntu2~24.04) 13.3.0 Clang version : Could not collect CMake version : version 4.1.2 Libc version : glibc-2.39 ======
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: LoRAConfig has no attribute 'lora_extra_vocab_size' when using vLLM + verl GRPO LoRA bug ### Your current environment ============================== System Info ============================== OS
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: === Versions of relevant libraries ============================== [pip3] flashinfer-python==0.5.2 [pip3] jupyterlab_nvidia_nsight==0.8.0 [pip3] numpy==1.26.4 [pip3] nvidia-cublas==13.0.0.19 [pip3] nvidia-cublas-cu12==12...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: ulnerability Meltdown: Not affected Vulnerability Mmio stale data: Not affected Vulnerability Reg file data sampling: Not affected Vulnerability Retbleed: Not affected Vulnerability Spec rstack overflow: Not affected Vu...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
