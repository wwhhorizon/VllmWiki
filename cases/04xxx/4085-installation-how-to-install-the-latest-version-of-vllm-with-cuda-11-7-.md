# vllm-project/vllm#4085: [Installation]:  How to install the latest version of vLLM with CUDA 11.7 and PyTorch 2.0.1 ？

| 字段 | 值 |
| --- | --- |
| Issue | [#4085](https://github.com/vllm-project/vllm/issues/4085) |
| 状态 | closed |
| 标签 | installation;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;hardware_porting |
| 子分类 | env_compat |
| Operator 关键词 | cuda;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Installation]:  How to install the latest version of vLLM with CUDA 11.7 and PyTorch 2.0.1 ？

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` PyTorch version: 2.0.1+cu117 Is debug build: False CUDA used to build PyTorch: 11.7 ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.6 LTS (x86_64) GCC version: (Ubuntu 9.4.0-1ubuntu1~20.04.2) 9.4.0 Clang version: Could not collect CMake version: version 3.28.3 Libc version: glibc-2.31 Python version: 3.10.13 (main, Sep 11 2023, 13:44:35) [GCC 11.2.0] (64-bit runtime) Python platform: Linux-5.4.0-144-generic-x86_64-with-glibc2.31 Is CUDA available: True CUDA runtime version: 11.7.99 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA A100 80GB PCIe GPU 1: NVIDIA A100 80GB PCIe Nvidia driver version: 470.57.02 cuDNN version: Could not collect HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True Versions of relevant libraries: [pip3] numpy==1.23.4 [pip3] pytorch-lightning==2.2.1 [pip3] torch==2.0.1 [pip3] torchmetrics==1.3.2 [pip3] torchvision==0.15.2 [pip3] triton==2.0.0 [conda] numpy 1.23.4 pypi_0 pypi [conda] pytorch-lightning 2.2.1 pypi_0 pypi [conda] torch 2.0.1 pypi_0 pypi [conda] torchmetrics 1.3.2 pypi_0 pypi [conda] torchvision 0.15.2 pypi_0 pyp...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: [Installation]: How to install the latest version of vLLM with CUDA 11.7 and PyTorch 2.0.1 ？ installation;stale ### Your current environment ```text The output of `python collect_env.py` ```
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: [Installation]: How to install the latest version of vLLM with CUDA 11.7 and PyTorch 2.0.1 ？ installation;stale ### Your current environment ```text The output of `python collect_env.py` ```
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: GPU models and configuration: GPU 0: NVIDIA A100 80GB PCIe
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: orch==2.0.1 [pip3] torchmetrics==1.3.2 [pip3] torchvision==0.15.2 [pip3] triton==2.0.0 [conda] numpy 1.23.4 pypi_0 pypi [conda] pytorch-lightning 2.2.1 pypi_0 pypi [conda] torch 2.0.1
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: Is debug build: False CUDA used to build PyTorch: 11.7

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
