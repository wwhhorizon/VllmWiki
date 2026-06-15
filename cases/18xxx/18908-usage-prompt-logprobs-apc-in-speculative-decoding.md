# vllm-project/vllm#18908: [Usage]: prompt logprobs + APC in speculative decoding

| 字段 | 值 |
| --- | --- |
| Issue | [#18908](https://github.com/vllm-project/vllm/issues/18908) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;speculative_decoding |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: prompt logprobs + APC in speculative decoding

### Issue 正文摘录

### Your current environment ```text ============================== System Info ============================== OS : Ubuntu 20.04.2 LTS (x86_64) GCC version : (Ubuntu 9.3.0-17ubuntu1~20.04) 9.3.0 Clang version : Could not collect CMake version : version 3.16.3 Libc version : glibc-2.31 ============================== PyTorch Info ============================== PyTorch version : 2.6.0+cu124 Is debug build : False CUDA used to build PyTorch : 12.4 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.10.16 (main, Dec 11 2024, 16:24:50) [GCC 11.2.0] (64-bit runtime) Python platform : Linux-5.4.0-42-generic-x86_64-with-glibc2.31 ============================== CUDA / GPU Info ============================== Is CUDA available : True CUDA runtime version : 11.8.89 CUDA_MODULE_LOADING set to : LAZY GPU models and configuration : GPU 0: NVIDIA GeForce RTX 4090 GPU 1: NVIDIA GeForce RTX 4090 GPU 2: NVIDIA GeForce RTX 4090 GPU 3: NVIDIA GeForce RTX 4090 GPU 4: NVIDIA GeForce RTX 4090 GPU 5: NVIDIA GeForce RTX 4090 GPU 6: NVIDIA GeForce RTX 4090 GPU 7: NVIDIA GeForce RTX 4090 Nvidia driver version : 525.105.17 cuDNN v...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: ========= OS : Ubuntu 20.04.2 LTS (x86_64) GCC version : (Ubuntu 9.3.0-17ubuntu1~20.04) 9.3.0 Clang version : Could not collect CMake version : version 3.16.3 Libc version : glibc-2.31 ==================
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: version : 2.6.0+cu124 Is debug build : False CUDA used to build PyTorch : 12.4 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.10.16 (...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Usage]: prompt logprobs + APC in speculative decoding usage;stale ### Your current environment ```text ============================== System Info ============================== OS : Ubuntu 20.04.2 LTS (x86_64) GCC vers
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: untime version : 11.8.89 CUDA_MODULE_LOADING set to : LAZY GPU models and configuration : GPU 0: NVIDIA GeForce RTX 4090 GPU 1: NVIDIA GeForce RTX 4090 GPU 2: NVIDIA GeForce RTX 4090 GPU 3: NVIDIA GeForce RTX 4090 GPU 4...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: u124 [pip3] torchvision==0.21.0+cu124 [pip3] transformers==4.52.3 [pip3] triton==3.2.0 [conda] numpy 2.1.2 pypi_0 pypi [conda] nvidia-cublas-cu12 12.4.5.8 pypi_0 pypi [conda] nvidia-cuda-cupti-cu12 12.4.127

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
