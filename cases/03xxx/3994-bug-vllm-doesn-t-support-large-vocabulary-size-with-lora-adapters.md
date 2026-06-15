# vllm-project/vllm#3994: [Bug]: vLLM doesn't support large vocabulary size with Lora Adapters

| 字段 | 值 |
| --- | --- |
| Issue | [#3994](https://github.com/vllm-project/vllm/issues/3994) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;hardware_porting;model_support |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vLLM doesn't support large vocabulary size with Lora Adapters

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` Collecting environment information... PyTorch version: 2.1.2+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Debian GNU/Linux 10 (buster) (x86_64) GCC version: (Debian 8.3.0-6) 8.3.0 Clang version: Could not collect CMake version: version 3.29.1 Libc version: glibc-2.28 Python version: 3.9.19 (main, Mar 21 2024, 17:11:28) [GCC 11.2.0] (64-bit runtime) Python platform: Linux-4.15.0-197-generic-x86_64-with-glibc2.28 Is CUDA available: True CUDA runtime version: Could not collect CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: Tesla V100-SXM2-32GB Nvidia driver version: 525.78.01 cuDNN version: Could not collect HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Byte Order: Little Endian Address sizes: 46 bits physical, 48 bits virtual CPU(s): 88 On-line CPU(s) list: 0-87 Thread(s) per core: 2 Core(s) per socket: 22 Socket(s): 2 NUMA node(s): 2 Vendor ID: GenuineIntel CPU family: 6 Model: 85 Model name: Intel(R) Xeon(R) Gold 6152 CPU @ 2.10GHz Stepping...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: ython collect_env.py` ``` Collecting environment information... PyTorch version: 2.1.2+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Debian GNU/Linux 10 (buster) (x86_6...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: onment information... PyTorch version: 2.1.2+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Debian GNU/Linux 10 (buster) (x86_64) GCC version: (Debian 8.3.0-6) 8.3.0 Cla...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: text The output of `python collect_env.py` ``` Collecting environment information... PyTorch version: 2.1.2+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Debian GNU/Lin...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: s of relevant libraries: [pip3] numpy==1.26.4 [pip3] torch==2.1.2 [pip3] triton==2.1.0 [conda] numpy 1.26.4 pypi_0 pypi [conda] torch 2.1.2 pypi_0 pypi [conda] triton 2.1.0
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: nvironment information... PyTorch version: 2.1.2+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Debian GNU/Linux 10 (buster) (x86_64) GCC version: (Debian 8.3.0-6) 8.3.0...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
