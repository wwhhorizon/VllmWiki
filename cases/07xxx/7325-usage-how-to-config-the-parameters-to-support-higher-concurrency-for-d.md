# vllm-project/vllm#7325: [Usage]: How to config the parameters to support higher concurrency for deploying the qwen2-7b model as an API at 8-GPU A800 (80G) server?

| 字段 | 值 |
| --- | --- |
| Issue | [#7325](https://github.com/vllm-project/vllm/issues/7325) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support |
| 子分类 | env_compat |
| Operator 关键词 | cuda |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: How to config the parameters to support higher concurrency for deploying the qwen2-7b model as an API at 8-GPU A800 (80G) server?

### Issue 正文摘录

### Your current environment ```text PyTorch version: 2.4.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.3 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version: Could not collect CMake version: version 3.30.2 Libc version: glibc-2.35 Python version: 3.11.9 (main, Apr 19 2024, 16:48:06) [GCC 11.2.0] (64-bit runtime) Python platform: Linux-5.15.0-78-generic-x86_64-with-glibc2.35 Is CUDA available: True CUDA runtime version: Could not collect CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA A800-SXM4-80GB GPU 1: NVIDIA A800-SXM4-80GB GPU 2: NVIDIA A800-SXM4-80GB GPU 3: NVIDIA A800-SXM4-80GB GPU 4: NVIDIA A800-SXM4-80GB GPU 5: NVIDIA A800-SXM4-80GB GPU 6: NVIDIA A800-SXM4-80GB GPU 7: NVIDIA A800-SXM4-80GB Nvidia driver version: 550.90.07 cuDNN version: Could not collect HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True ``` ### How would you like to use vllm I have one GPU server with 8-GPU A800 (80G). And I want to serve the model qwen2-7b as OpenAI API. The qwen2-7b can be run one GPU. I want to run 8 models paralleling as 8 instances to...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: U A800 (80G) server? usage ### Your current environment ```text PyTorch version: 2.4.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.3 LTS (x86_64) GCC ver...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: environment ```text PyTorch version: 2.4.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.3 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Usage]: How to config the parameters to support higher concurrency for deploying the qwen2-7b model as an API at 8-GPU A800 (80G) server? usage ### Your current environment ```text PyTorch version: 2.4.0+cu121 Is debug...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: rent environment ```text PyTorch version: 2.4.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.3 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: want to run 8 models paralleling as 8 instances to support multiple API requests concurrently. The basic requirement is as below pic shows. ![image](https://github.com/user-attachments/assets/99555837-e1cd-4134-aa64-a88...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
