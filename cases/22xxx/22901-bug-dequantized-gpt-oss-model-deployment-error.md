# vllm-project/vllm#22901: [Bug]: Dequantized GPT-OSS Model Deployment Error

| 字段 | 值 |
| --- | --- |
| Issue | [#22901](https://github.com/vllm-project/vllm/issues/22901) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Dequantized GPT-OSS Model Deployment Error

### Issue 正文摘录

### Your current environment ============================== System Info ============================== OS : Ubuntu 24.04.2 LTS (x86_64) GCC version : (Ubuntu 13.3.0-6ubuntu2~24.04) 13.3.0 Clang version : Could not collect CMake version : Could not collect Libc version : glibc-2.39 ============================== PyTorch Info ============================== PyTorch version : 2.9.0.dev20250804+cu128 Is debug build : False CUDA used to build PyTorch : 12.8 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.12.3 (main, Jun 18 2025, 17:59:45) [GCC 13.3.0] (64-bit runtime) Python platform : Linux-6.8.0-60-generic-x86_64-with-glibc2.39 ============================== CUDA / GPU Info ============================== Is CUDA available : True CUDA runtime version : Could not collect CUDA_MODULE_LOADING set to : GPU models and configuration : GPU 0: NVIDIA H100 80GB HBM3 GPU 1: NVIDIA H100 80GB HBM3 GPU 2: NVIDIA H100 80GB HBM3 GPU 3: NVIDIA H100 80GB HBM3 GPU 4: NVIDIA H100 80GB HBM3 GPU 5: NVIDIA H100 80GB HBM3 GPU 6: NVIDIA H100 80GB HBM3 GPU 7: NVIDIA H100 80GB HBM3 Nvidia driver version : 535.216.03 cuDNN versi...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 10: ========= OS : Ubuntu 24.04.2 LTS (x86_64) GCC version : (Ubuntu 13.3.0-6ubuntu2~24.04) 13.3.0 Clang version : Could not collect CMake version : Could not collect Libc version : glibc-2.39 ==============
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: : 2.9.0.dev20250804+cu128 Is debug build : False CUDA used to build PyTorch : 12.8 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.12....
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: Dequantized GPT-OSS Model Deployment Error bug;stale ### Your current environment ============================== System Info ============================== OS : Ubuntu 24.04.2 LTS (x86_64) GCC vers
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Bug]: Dequantized GPT-OSS Model Deployment Error bug;stale ### Your current environment ============================== System Info ============================== OS : Ubuntu 24.04.2 LTS (x86_
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: Dequantized GPT-OSS Model Deployment Error bug;stale ### Your current environment ============================== System Info ============================== OS : Ubuntu 24.04.2 LTS (x86_64) GCC version : (Ubuntu 1...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
