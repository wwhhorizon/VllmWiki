# vllm-project/vllm#13188: [Usage]: Usage of tensor_parallel_size

| 字段 | 值 |
| --- | --- |
| Issue | [#13188](https://github.com/vllm-project/vllm/issues/13188) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: Usage of tensor_parallel_size

### Issue 正文摘录

### Your current environment INFO 02-13 10:47:30 __init__.py:190] Automatically detected platform cuda. WARNING 02-13 10:47:30 cuda.py:336] Detected different devices in the system: WARNING 02-13 10:47:30 cuda.py:336] NVIDIA GeForce RTX 3090 WARNING 02-13 10:47:30 cuda.py:336] NVIDIA A100-SXM4-80GB WARNING 02-13 10:47:30 cuda.py:336] Tesla T4 WARNING 02-13 10:47:30 cuda.py:336] NVIDIA GeForce RTX 3090 WARNING 02-13 10:47:30 cuda.py:336] Please make sure to set `CUDA_DEVICE_ORDER=P CI_BUS_ID` to avoid unexpected behavior. Collecting environment information... PyTorch version: 2.5.1+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A OS: CentOS Linux 7 (Core) (x86_64) GCC version: (GCC) 4.8.5 20150623 (Red Hat 4.8.5-44) Clang version: Could not collect CMake version: Could not collect Libc version: glibc-2.17 Python version: 3.10.4 (main, Mar 6 2023, 10:28:01) [GCC 4.8.5 20150623 (Red Ha t 4.8.5-44)] (64-bit runtime) Python platform: Linux-3.10.0-1160.90.1.el7.x86_64-x86_64-with-glibc2.17 Is CUDA available: True CUDA runtime version: 11.8.89 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA GeForce RTX 3090 GPU 1: N...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: CI_BUS_ID` to avoid unexpected behavior. Collecting environment information... PyTorch version: 2.5.1+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A OS: CentOS Linux 7 (Core
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 7: nt INFO 02-13 10:47:30 __init__.py:190] Automatically detected platform cuda. WARNING 02-13 10:47:30 cuda.py:336] Detected different devices in the system: WARNING 02-13 10:47:30 cuda.py:336] NVIDIA GeForce RTX 3090 WAR...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: CI_BUS_ID` to avoid unexpected behavior. Collecting environment information... PyTorch version: 2.5.1+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A OS: CentOS Linux 7 (Core...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: dio==2.5.1 [pip3] torchvision==0.20.1 [pip3] transformers==4.48.3 [pip3] triton==3.1.0 [conda] Could not collect ROCM Version: Could not collect Neuron SDK Version: N/A vLLM Version: 0.7.2 vLLM Build Flags: CUDA Archs:...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: nvironment information... PyTorch version: 2.5.1+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A OS: CentOS Linux 7 (Core) (x86_64) GCC version: (GCC) 4.8.5 20150623 (Red Hat...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
