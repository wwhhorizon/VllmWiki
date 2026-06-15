# vllm-project/vllm#3635: [Usage]: Is it possible to generate without detokenizing?

| 字段 | 值 |
| --- | --- |
| Issue | [#3635](https://github.com/vllm-project/vllm/issues/3635) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;hardware_porting;model_support |
| 子分类 |  |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: Is it possible to generate without detokenizing?

### Issue 正文摘录

### Your current environment ```text Collecting environment information... PyTorch version: 2.1.2+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Rocky Linux release 8.7 (Green Obsidian) (x86_64) GCC version: (GCC) 8.5.0 20210514 (Red Hat 8.5.0-16) Clang version: 14.0.6 (Red Hat 14.0.6-1.module+el8.7.0+1080+d88dc670) CMake version: version 3.28.4 Libc version: glibc-2.28 Python version: 3.11.6 | packaged by conda-forge | (main, Oct 3 2023, 10:40:35) [GCC 12.3.0] (64-bit runtime) Python platform: Linux-4.18.0-425.10.1.el8_7.x86_64-x86_64-with-glibc2.28 Is CUDA available: True CUDA runtime version: 12.2.91 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA A100-SXM4-80GB GPU 1: NVIDIA A100-SXM4-80GB GPU 2: NVIDIA A100-SXM4-80GB GPU 3: NVIDIA A100-SXM4-80GB Nvidia driver version: 545.23.08 cuDNN version: Could not collect HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Byte Order: Little Endian CPU(s): 64 On-line CPU(s) list: 0-63 Thread(s) per core: 1 Core(s) per socket: 32 Socket(s): 2 NUMA node(s): 2 Vendor ID: GenuineI...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: rrent environment ```text Collecting environment information... PyTorch version: 2.1.2+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Rocky Linux release 8.7 (Green Obsi...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: onment information... PyTorch version: 2.1.2+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Rocky Linux release 8.7 (Green Obsidian) (x86_64) GCC version: (GCC) 8.5.0 20...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: ng? usage ### Your current environment ```text Collecting environment information... PyTorch version: 2.1.2+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Rocky Linux re...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: udio==2.2.1 [pip3] torchmetrics==1.3.1 [pip3] torchvision==0.17.1 [pip3] triton==2.1.0 [conda] numpy 1.26.2 pypi_0 pypi [conda] torch 2.1.2 pypi_0 pypi [conda] torchaudio 2.2.1
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: nvironment information... PyTorch version: 2.1.2+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Rocky Linux release 8.7 (Green Obsidian) (x86_64) GCC version: (GCC) 8.5....

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
