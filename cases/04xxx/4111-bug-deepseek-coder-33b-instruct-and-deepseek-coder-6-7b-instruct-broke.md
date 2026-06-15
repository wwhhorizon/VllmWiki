# vllm-project/vllm#4111: [Bug]: deepseek-coder-33b-instruct and deepseek-coder-6.7b-instruct broken, but deepseek-llm-7b-chat and deepseek-llm-67b-chat work well

| 字段 | 值 |
| --- | --- |
| Issue | [#4111](https://github.com/vllm-project/vllm/issues/4111) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits |
| 子分类 | kernel_eff |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: deepseek-coder-33b-instruct and deepseek-coder-6.7b-instruct broken, but deepseek-llm-7b-chat and deepseek-llm-67b-chat work well

### Issue 正文摘录

### Your current environment ``` Collecting environment information... PyTorch version: 2.0.1+cu117 Is debug build: False CUDA used to build PyTorch: 11.7 ROCM used to build PyTorch: N/A OS: Ubuntu 18.04.6 LTS (x86_64) GCC version: (Ubuntu 7.5.0-3ubuntu1~18.04) 7.5.0 Clang version: Could not collect CMake version: version 3.29.2 Libc version: glibc-2.27 Python version: 3.9.11 (main, Mar 29 2022, 19:08:29) [GCC 7.5.0] (64-bit runtime) Python platform: Linux-3.10.0-514.44.5.10.h254.x86_64-x86_64-with-glibc2.27 Is CUDA available: True CUDA runtime version: 10.2.89 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: Tesla V100-SXM2-32GB GPU 1: Tesla V100-SXM2-32GB GPU 2: Tesla V100-SXM2-32GB GPU 3: Tesla V100-SXM2-32GB GPU 4: Tesla V100-SXM2-32GB GPU 5: Tesla V100-SXM2-32GB GPU 6: Tesla V100-SXM2-32GB GPU 7: Tesla V100-SXM2-32GB Nvidia driver version: 470.57.02 cuDNN version: /usr/lib/x86_64-linux-gnu/libcudnn.so.7.6.5 HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Byte Order: Little Endian CPU(s): 72 On-line CPU(s) list: 0-71 Thread(s) per core: 2 Core(s) per socket: 18 Socket(...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: r current environment ``` Collecting environment information... PyTorch version: 2.0.1+cu117 Is debug build: False CUDA used to build PyTorch: 11.7 ROCM used to build PyTorch: N/A OS: Ubuntu 18.04.6 LTS (x86_64) GCC ver...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: onment information... PyTorch version: 2.0.1+cu117 Is debug build: False CUDA used to build PyTorch: 11.7 ROCM used to build PyTorch: N/A OS: Ubuntu 18.04.6 LTS (x86_64) GCC version: (Ubuntu 7.5.0-3ubuntu1~18.04) 7.5.0...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: ell bug;stale ### Your current environment ``` Collecting environment information... PyTorch version: 2.0.1+cu117 Is debug build: False CUDA used to build PyTorch: 11.7 ROCM used to build PyTorch: N/A OS: Ubuntu 18.04.6...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: nvironment information... PyTorch version: 2.0.1+cu117 Is debug build: False CUDA used to build PyTorch: 11.7 ROCM used to build PyTorch: N/A OS: Ubuntu 18.04.6 LTS (x86_64) GCC version: (Ubuntu 7.5.0-3ubuntu1~18.04) 7....
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: broken, but deepseek-llm-7b-chat and deepseek-llm-67b-chat work well bug;stale ### Your current environment ``` Collecting environment information... PyTorch version: 2.0.1+cu117 Is debug build: False CUDA used to build...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
