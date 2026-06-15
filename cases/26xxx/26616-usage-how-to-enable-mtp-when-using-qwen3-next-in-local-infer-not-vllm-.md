# vllm-project/vllm#26616: [Usage]: How to enable MTP when using Qwen3-Next in local infer ( not vllm serve)

| 字段 | 值 |
| --- | --- |
| Issue | [#26616](https://github.com/vllm-project/vllm/issues/26616) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;speculative_decoding |
| 子分类 | kernel_eff |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: How to enable MTP when using Qwen3-Next in local infer ( not vllm serve)

### Issue 正文摘录

### Your current environment ```text Collecting environment information... ============================== System Info ============================== OS : Ubuntu 22.04.2 LTS (x86_64) GCC version : (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version : Could not collect CMake version : Could not collect Libc version : glibc-2.35 ============================== PyTorch Info ============================== PyTorch version : 2.8.0+cu128 Is debug build : False CUDA used to build PyTorch : 12.8 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.12.11 | packaged by Anaconda, Inc. | (main, Jun 5 2025, 13:09:17) [GCC 11.2.0] (64-bit runtime) Python platform : Linux-4.18.0-2.6.8.kwai.x86_64-x86_64-with-glibc2.35 ============================== CUDA / GPU Info ============================== Is CUDA available : True CUDA runtime version : 11.8.89 CUDA_MODULE_LOADING set to : LAZY GPU models and configuration : GPU 0: NVIDIA A100 80GB PCIe GPU 1: NVIDIA A100 80GB PCIe GPU 2: NVIDIA A100 80GB PCIe GPU 3: NVIDIA A100 80GB PCIe Nvidia driver version : 550.54.14 cuDNN version : Probably one of the following: /usr/lib/x86_...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: ========= OS : Ubuntu 22.04.2 LTS (x86_64) GCC version : (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version : Could not collect CMake version : Could not collect Libc version : glibc-2.35 ==============
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: version : 2.8.0+cu128 Is debug build : False CUDA used to build PyTorch : 12.8 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.12.11 |...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Usage]: How to enable MTP when using Qwen3-Next in local infer ( not vllm serve) usage;stale ### Your current environment ```text Collecting environment information... ============================== System Info =======...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: enable MTP when using Qwen3-Next in local infer ( not vllm serve) usage;stale ### Your current environment ```text Collecting environment information... ============================== System Info =======================...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: dio==2.8.0 [pip3] torchvision==0.23.0 [pip3] transformers==4.57.0 [pip3] triton==3.4.0 [conda] numpy 2.2.6 pypi_0 pypi [conda] nvidia-cublas-cu12 12.8.4.1 pypi_0 pypi [conda] nvidia-cuda-cupti-cu12

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
