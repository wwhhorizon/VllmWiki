# vllm-project/vllm#6445: [Bug]: TypeError: 'NoneType' object is not callable when start Gemma2-27b-it

| 字段 | 值 |
| --- | --- |
| Issue | [#6445](https://github.com/vllm-project/vllm/issues/6445) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;hardware_porting;model_support |
| 子分类 | env_compat |
| Operator 关键词 | attention;cuda;operator;triton |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: TypeError: 'NoneType' object is not callable when start Gemma2-27b-it

### Issue 正文摘录

### Your current environment Collecting environment information... PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: CentOS Linux 7 (Core) (x86_64) GCC version: (GCC) 4.8.5 20150623 (Red Hat 4.8.5-44) Clang version: Could not collect CMake version: version 3.30.0 Libc version: glibc-2.17 Python version: 3.11.4 (main, Jul 5 2023, 13:45:01) [GCC 11.2.0] (64-bit runtime) Python platform: Linux-3.10.0-1160.99.1.el7.x86_64-x86_64-with-glibc2.17 Is CUDA available: True CUDA runtime version: 11.8.89 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA A100-SXM4-40GB GPU 1: NVIDIA A100-SXM4-40GB GPU 2: NVIDIA A100-SXM4-40GB GPU 3: NVIDIA A100-SXM4-40GB Nvidia driver version: 545.23.08 cuDNN version: Could not collect HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Byte Order: Little Endian CPU(s): 192 On-line CPU(s) list: 0-191 Thread(s) per core: 2 Core(s) per socket: 48 Socket(s): 2 NUMA node(s): 2 Vendor ID: AuthenticAMD CPU family: 23 Model: 49 Model name: AMD EPYC 7K62 48-Core Processor Stepping: 0 CPU M...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: Your current environment Collecting environment information... PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: CentOS Linux 7 (Core) (x86_64) GCC v...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: onment information... PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: CentOS Linux 7 (Core) (x86_64) GCC version: (GCC) 4.8.5 20150623 (Red Hat 4.8...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: [Bug]: TypeError: 'NoneType' object is not callable when start Gemma2-27b-it bug;stale ### Your current environment Collecting environment information... PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to b...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: umip overflow_recov succor smca Versions of relevant libraries: [pip3] flashinfer==0.0.8+cu118torch2.3 [pip3] numpy==1.26.4 [pip3] nvidia-nccl-cu12==2.20.5 [pip3] torch==2.3.0 [pip3] torchvision==0.18.0 [pip3] transform...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: nvironment information... PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: CentOS Linux 7 (Core) (x86_64) GCC version: (GCC) 4.8.5 20150623 (Red Hat...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
