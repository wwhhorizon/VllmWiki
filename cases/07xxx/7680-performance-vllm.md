# vllm-project/vllm#7680: [Performance]: vllm量化和非量化的性能对比

| 字段 | 值 |
| --- | --- |
| Issue | [#7680](https://github.com/vllm-project/vllm/issues/7680) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;hardware_porting;model_support;sampling_logits |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling |
| 症状 | build_error;nan_inf;slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Performance]: vllm量化和非量化的性能对比

### Issue 正文摘录

### Proposal to improve performance _No response_ ### Report of performance regression _No response_ ### Misc discussion on performance 使用qwen32b模型，输入tokens 3000，输出tokens 50左右，在单张A800并发量在11，最大响应时间达到10s，使用awq将qwen32b模型量化为4bit,输入tokens 3000，输出tokens 50左右，无论是显卡利用率设置为0.5还是0.95在单张A800并发量也是在11，最大响应时间达到10s，想知道这是为什么，是什么参数设置不对？理论上量化后显存占用小了，并发数会增加啊 ### Your current environment (if you think it is necessary) Collecting environment information... PyTorch version: 2.2.2+cpu Is debug build: False CUDA used to build PyTorch: Could not collect ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.6 LTS (x86_64) GCC version: (Ubuntu 9.4.0-1ubuntu1~20.04.2) 9.4.0 Clang version: Could not collect CMake version: version 3.16.3 Libc version: glibc-2.31 Python version: 3.10.14 (main, May 6 2024, 19:42:50) [GCC 11.2.0] (64-bit runtime) Python platform: Linux-5.15.0-1050-azure-x86_64-with-glibc2.31 Is CUDA available: False CUDA runtime version: 12.2.140 CUDA_MODULE_LOADING set to: N/A GPU models and configuration: GPU 0: NVIDIA A100 80GB PCIe Nvidia driver version: 550.54.15 cuDNN version: Could not collect HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: Architecture: x86_...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: ou think it is necessary) Collecting environment information... PyTorch version: 2.2.2+cpu Is debug build: False CUDA used to build PyTorch: Could not collect ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.6 LTS (x86_...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: ironment information... PyTorch version: 2.2.2+cpu Is debug build: False CUDA used to build PyTorch: Could not collect ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.6 LTS (x86_64) GCC version: (Ubuntu 9.4.0-1ubuntu1~...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: ormance regression _No response_ ### Misc discussion on performance 使用qwen32b模型，输入tokens 3000，输出tokens 50左右，在单张A800并发量在11，最大响应时间达到10s，使用awq将qwen32b模型量化为4bit,输入tokens 3000，输出tokens 50左右，无论是显卡利用率设置为0.5还是0.95在单张A800并发量也是在1...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: environment information... PyTorch version: 2.2.2+cpu Is debug build: False CUDA used to build PyTorch: Could not collect ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.6 LTS (x86_64) GCC version: (Ubuntu 9.4.0-1ubunt...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Performance]: vllm量化和非量化的性能对比 performance;stale ### Proposal to improve performance _No response_ ### Report of performance regression _No response_ ### Misc discussion on performance 使用qwen32b模型，输入tokens 3000，输出tokens...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
