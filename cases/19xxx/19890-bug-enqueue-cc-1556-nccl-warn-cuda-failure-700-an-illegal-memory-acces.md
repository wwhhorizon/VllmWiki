# vllm-project/vllm#19890: [Bug]: enqueue.cc:1556 NCCL WARN Cuda failure 700 'an illegal memory access was encountered'

| 字段 | 值 |
| --- | --- |
| Issue | [#19890](https://github.com/vllm-project/vllm/issues/19890) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: enqueue.cc:1556 NCCL WARN Cuda failure 700 'an illegal memory access was encountered'

### Issue 正文摘录

### Your current environment INFO 06-20 10:37:01 [__init__.py:243] Automatically detected platform cuda. Collecting environment information... uv is set ============================== System Info ============================== OS : Ubuntu 24.04.2 LTS (x86_64) GCC version : (Ubuntu 13.3.0-6ubuntu2~24.04) 13.3.0 Clang version : Could not collect CMake version : version 4.0.3 Libc version : glibc-2.39 ============================== PyTorch Info ============================== PyTorch version : 2.7.1+cu128 Is debug build : False CUDA used to build PyTorch : 12.8 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.11.13 (main, Jun 4 2025, 17:37:17) [Clang 20.1.4 ] (64-bit runtime) Python platform : Linux-6.11.0-26-generic-x86_64-with-glibc2.39 ============================== CUDA / GPU Info ============================== Is CUDA available : True CUDA runtime version : 12.8.61 CUDA_MODULE_LOADING set to : LAZY GPU models and configuration : GPU 0: NVIDIA GeForce RTX 5090 GPU 1: NVIDIA GeForce RTX 5090 Nvidia driver version : 570.86.10 cuDNN version : Could not collect HIP runtime version : N/A MIOpen runtime...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: ========= OS : Ubuntu 24.04.2 LTS (x86_64) GCC version : (Ubuntu 13.3.0-6ubuntu2~24.04) 13.3.0 Clang version : Could not collect CMake version : version 4.0.3 Libc version : glibc-2.39 ==================
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: [Bug]: enqueue.cc:1556 NCCL WARN Cuda failure 700 'an illegal memory access was encountered' bug ### Your current environment INFO 06-20 10:37:01 [__init__.py:243] Automatically detected platform cuda. Collecting enviro...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: _.py:243] Automatically detected platform cuda. Collecting environment information... uv is set ============================== System Info ============================== OS : Ubuntu 24.04.2 LTS (x86_64) GCC version : (U...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: enqueue.cc:1556 NCCL WARN Cuda failure 700 'an illegal memory access was encountered' bug ### Your current environment INFO 06-20 10:37:01 [__init__.py:243] Automatically detected platform cuda. Collecting enviro...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: 11.0 [pip3] torchvision==0.22.1+cu128 [pip3] transformers==4.51.3 [pip3] triton==3.3.1 [conda] Could not collect ============================== vLLM Info ============================== ROCM Version : Could not collect N...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
