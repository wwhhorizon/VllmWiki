# vllm-project/vllm#8482: [Bug]: crash on Triton backends when start vllm 0.6.1

| 字段 | 值 |
| --- | --- |
| Issue | [#8482](https://github.com/vllm-project/vllm/issues/8482) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;hardware_porting;model_support;quantization |
| 子分类 | env_compat |
| Operator 关键词 | cuda;quantization;triton |
| 症状 | build_error;crash;import_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: crash on Triton backends when start vllm 0.6.1

### Issue 正文摘录

### Your current environment Collecting environment information... PyTorch version: 2.4.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.6 LTS (x86_64) GCC version: (Ubuntu 9.4.0-1ubuntu1~20.04.2) 9.4.0 Clang version: Could not collect CMake version: Could not collect Libc version: glibc-2.31 Python version: 3.12.6 (main, Sep 10 2024, 00:05:17) [GCC 9.4.0] (64-bit runtime) Python platform: Linux-6.8.0-40-generic-x86_64-with-glibc2.31 Is CUDA available: True CUDA runtime version: Could not collect CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA GeForce RTX 4090 Nvidia driver version: 550.54.14 cuDNN version: Could not collect HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True Versions of relevant libraries: [pip3] flashinfer==0.1.6+cu121torch2.4 [pip3] numpy==1.26.4 [pip3] torch==2.4.0 [pip3] torchvision==0.19.0 [pip3] triton==3.0.0 [conda] Could not collect ### Model Input Dumps _No response_ ### 🐛 Describe the bug Traceback (most recent call last): File " ", line 189, in _run_module_as_main File " ", line 112, in _get_module_details File "/usr/local/lib/python3...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: Your current environment Collecting environment information... PyTorch version: 2.4.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.6 LTS (x86_64) GCC vers...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: onment information... PyTorch version: 2.4.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.6 LTS (x86_64) GCC version: (Ubuntu 9.4.0-1ubuntu1~20.04.2) 9.4....
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: [Bug]: crash on Triton backends when start vllm 0.6.1 bug;stale ### Your current environment Collecting environment information... PyTorch version: 2.4.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: m 0.6.1 bug;stale ### Your current environment Collecting environment information... PyTorch version: 2.4.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.6...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: nvironment information... PyTorch version: 2.4.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.6 LTS (x86_64) GCC version: (Ubuntu 9.4.0-1ubuntu1~20.04.2)...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
