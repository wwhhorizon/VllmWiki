# vllm-project/vllm#24029: [Bug]: Outputs always miss responses if n of SamplingParams>1 with AsyncLLM!

| 字段 | 值 |
| --- | --- |
| Issue | [#24029](https://github.com/vllm-project/vllm/issues/24029) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Outputs always miss responses if n of SamplingParams>1 with AsyncLLM!

### Issue 正文摘录

### Your current environment ``` ============================== System Info ============================== OS : Ubuntu 22.04.5 LTS (x86_64) GCC version : (Ubuntu 11.4.0-1ubuntu1~22.04.2) 11.4.0 Clang version : Could not collect CMake version : version 3.22.1 Libc version : glibc-2.35 ============================== PyTorch Info ============================== PyTorch version : 2.7.1+cu126 Is debug build : False CUDA used to build PyTorch : 12.6 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.11.13 (main, Jun 5 2025, 13:12:00) [GCC 11.2.0] (64-bit runtime) Python platform : Linux-5.15.153.1-microsoft-standard-WSL2-x86_64-with-glibc2.35 ============================== CUDA / GPU Info ============================== Is CUDA available : True CUDA runtime version : 12.4.131 CUDA_MODULE_LOADING set to : LAZY GPU models and configuration : GPU 0: NVIDIA GeForce RTX 3060 Laptop GPU Nvidia driver version : 581.08 cuDNN version : Could not collect HIP runtime version : N/A MIOpen runtime version : N/A Is XNNPACK available : True ============================== CPU Info ============================== 架构： x86_64 C...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: ========= OS : Ubuntu 22.04.5 LTS (x86_64) GCC version : (Ubuntu 11.4.0-1ubuntu1~22.04.2) 11.4.0 Clang version : Could not collect CMake version : version 3.22.1 Libc version : glibc-2.35 ===============
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: version : 2.7.1+cu126 Is debug build : False CUDA used to build PyTorch : 12.6 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.11.13 (...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: ntime version : 12.4.131 CUDA_MODULE_LOADING set to : LAZY GPU models and configuration : GPU 0: NVIDIA GeForce RTX 3060 Laptop GPU Nvidia driver version : 581.08 cuDNN version : Could not collect HIP runtime version :...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: cted Vulnerability Meltdown: Not affected Vulnerability Mmio stale data: Not affected Vulnerability Retbleed: Mitigation; Enhanced IBRS Vulnerability Spec rstack overflow: Not affected Vulnerability Spec store bypass: M...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: dio==2.7.1 [pip3] torchvision==0.22.1 [pip3] transformers==4.56.0 [pip3] triton==3.3.1 [conda] numpy 2.2.6 pypi_0 pypi [conda] nvidia-cublas-cu12 12.6.4.1 pypi_0 pypi [conda] nvidia-cuda-cupti-cu12

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
