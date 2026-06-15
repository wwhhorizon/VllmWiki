# vllm-project/vllm#19542: [Installation]: CUDA kernel image not available for GTX 1080 Ti (Compute 6.1) using pip-installed vLLM 0.9.1

| 字段 | 值 |
| --- | --- |
| Issue | [#19542](https://github.com/vllm-project/vllm/issues/19542) |
| 状态 | closed |
| 标签 | installation |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;speculative_decoding |
| 子分类 | env_compat |
| Operator 关键词 | cuda;kernel;operator;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Installation]: CUDA kernel image not available for GTX 1080 Ti (Compute 6.1) using pip-installed vLLM 0.9.1

### Issue 正文摘录

### Your current environment ```text INFO 06-12 17:10:51 [__init__.py:244] Automatically detected platform cuda. Collecting environment information... ============================== System Info ============================== OS : Ubuntu 20.04.5 LTS (x86_64) GCC version : (Ubuntu 9.4.0-1ubuntu1~20.04.1) 9.4.0 Clang version : Could not collect CMake version : version 3.27.2 Libc version : glibc-2.31 ============================== PyTorch Info ============================== PyTorch version : 2.7.0+cu126 Is debug build : False CUDA used to build PyTorch : 12.6 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.10.18 | packaged by conda-forge | (main, Jun 4 2025, 14:45:41) [GCC 13.3.0] (64-bit runtime) Python platform : Linux-5.4.0-137-generic-x86_64-with-glibc2.31 ============================== CUDA / GPU Info ============================== Is CUDA available : True CUDA runtime version : 12.8.61 CUDA_MODULE_LOADING set to : LAZY GPU models and configuration : GPU 0: NVIDIA GeForce GTX 1080 Ti GPU 1: NVIDIA GeForce GTX 1080 Ti GPU 2: NVIDIA GeForce GTX 1080 Ti Nvidia driver version : 570.86.10 cuDNN versi...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: [Installation]: CUDA kernel image not available for GTX 1080 Ti (Compute 6.1) using pip-installed vLLM 0.9.1 installation ### Your current environment ```text INFO 06-12 17:10:51 [__init__.py:244] Automatically detected
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: [Installation]: CUDA kernel image not available for GTX 1080 Ti (Compute 6.1) using pip-installed vLLM 0.9.1 installation ### Your current environment ```text INFO 06-12 17:10:51 [__init__.py:244] Automatically detected...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: _.py:244] Automatically detected platform cuda. Collecting environment information... ============================== System Info ============================== OS : Ubuntu 20.04.5 LTS (x86_64) GCC version : (Ubuntu 9.4....
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: able Vulnerability Meltdown: Mitigation; PTI Vulnerability Mmio stale data: Mitigation; Clear CPU buffers; SMT vulnerable Vulnerability Retbleed: Mitigation; IBRS Vulnerability Spec store bypass: Mitigation; Speculative...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: dio==2.7.0 [pip3] torchvision==0.22.0 [pip3] transformers==4.52.4 [pip3] triton==3.3.0 [conda] numpy 2.2.6 pypi_0 pypi [conda] nvidia-cublas-cu12 12.6.4.1 pypi_0 pypi [conda] nvidia-cuda-cupti-cu12 12.6.80

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
