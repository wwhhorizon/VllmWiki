# vllm-project/vllm#5863: [Bug]: A bug when running examples/llava_example.py with image_features as input and multiple GPUs enabled

| 字段 | 值 |
| --- | --- |
| Issue | [#5863](https://github.com/vllm-project/vllm/issues/5863) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 14; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;multimodal_vlm |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: A bug when running examples/llava_example.py with image_features as input and multiple GPUs enabled

### Issue 正文摘录

### Your current environment ```text Collecting environment information... PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Amazon Linux 2 (x86_64) GCC version: (GCC) 7.3.1 20180712 (Red Hat 7.3.1-17) Clang version: Could not collect CMake version: version 3.29.6 Libc version: glibc-2.26 Python version: 3.10.14 | packaged by conda-forge | (main, Mar 20 2024, 12:45:18) [GCC 12.3.0] (64-bit runtime) Python platform: Linux-5.10.209-198.812.amzn2.x86_64-x86_64-with-glibc2.26 Is CUDA available: True CUDA runtime version: 12.1.105 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA A10G GPU 1: NVIDIA A10G GPU 2: NVIDIA A10G GPU 3: NVIDIA A10G GPU 4: NVIDIA A10G GPU 5: NVIDIA A10G GPU 6: NVIDIA A10G GPU 7: NVIDIA A10G Nvidia driver version: 535.104.12 cuDNN version: Could not collect HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Byte Order: Little Endian CPU(s): 192 On-line CPU(s) list: 0-191 Thread(s) per core: 2 Core(s) per socket: 48 Socket(s): 2 NUMA node(s): 2 Vendor ID: AuthenticAMD CPU family: 23...

## 现有链接修复摘要

#5880 [VLM][Bugfix] Make sure that `multi_modal_kwargs` is broadcasted properly

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: rrent environment ```text Collecting environment information... PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Amazon Linux 2 (x86_64) GCC version...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: abled bug ### Your current environment ```text Collecting environment information... PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Amazon Linux 2...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: onment information... PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Amazon Linux 2 (x86_64) GCC version: (GCC) 7.3.1 20180712 (Red Hat 7.3.1-17)...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: nvironment information... PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Amazon Linux 2 (x86_64) GCC version: (GCC) 7.3.1 20180712 (Red Hat 7.3.1-...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: nccl-cu12==2.20.5 [pip3] torch==2.3.0 [pip3] transformers==4.41.2 [pip3] triton==2.3.0 [conda] numpy 1.26.4 pypi_0 pypi [conda] nvidia-nccl-cu12 2.20.5 pypi_0 pypi [conda] torch 2.3.0

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#5880](https://github.com/vllm-project/vllm/pull/5880) | closes_keyword | 0.95 | [VLM][Bugfix] Make sure that `multi_modal_kwargs` is broadcasted properly | Fix #5863 The current broadcasting logic only supports first level tensors. For `multi_modal_kwargs`, tensors can be nested under. The PR extends tensor_dict flatten and unfla |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
