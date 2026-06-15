# vllm-project/vllm#3447: [Bug]: TypeError: endswith first arg must be str or a tuple of str, not bytes

| 字段 | 值 |
| --- | --- |
| Issue | [#3447](https://github.com/vllm-project/vllm/issues/3447) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;frontend_api;hardware_porting;model_support;sampling_logits |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: TypeError: endswith first arg must be str or a tuple of str, not bytes

### Issue 正文摘录

### Your current environment ```text Collecting environment information... PyTorch version: 2.1.2+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: CentOS Linux 7 (Core) (x86_64) GCC version: (GCC) 4.8.5 20150623 (Red Hat 4.8.5-44) Clang version: Could not collect CMake version: Could not collect Libc version: glibc-2.17 Python version: 3.10.13 (main, Sep 11 2023, 13:44:35) [GCC 11.2.0] (64-bit runtime) Python platform: Linux-5.15.146.1-microsoft-standard-WSL2-x86_64-with-glibc2.17 Is CUDA available: True CUDA runtime version: 12.3.107 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA GeForce RTX 4090 Nvidia driver version: 551.52 cuDNN version: Could not collect HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Byte Order: Little Endian CPU(s): 24 On-line CPU(s) list: 0-23 Thread(s) per core: 2 Core(s) per socket: 12 Socket(s): 1 Vendor ID: GenuineIntel CPU family: 6 Model: 183 Model name: 13th Gen Intel(R) Core(TM) i7-13700F Stepping: 1 CPU MHz: 2111.998 BogoMIPS: 4223.99 Virtualization: VT-x Hypervisor vendor: Microsoft...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: rrent environment ```text Collecting environment information... PyTorch version: 2.1.2+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: CentOS Linux 7 (Core) (x86_64) GCC...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: onment information... PyTorch version: 2.1.2+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: CentOS Linux 7 (Core) (x86_64) GCC version: (GCC) 4.8.5 20150623 (Red Hat 4.8...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: bytes bug ### Your current environment ```text Collecting environment information... PyTorch version: 2.1.2+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: CentOS Linux 7...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ip3] numpy==1.26.4 [pip3] torch==2.1.2 [pip3] torchvision==0.16.2 [pip3] triton==2.1.0 [conda] numpy 1.26.4 pypi_0 pypi [conda] torch 2.1.2 pypi_0 pypi [conda] torchvision 0.16.2
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: nvironment information... PyTorch version: 2.1.2+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: CentOS Linux 7 (Core) (x86_64) GCC version: (GCC) 4.8.5 20150623 (Red Hat...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
