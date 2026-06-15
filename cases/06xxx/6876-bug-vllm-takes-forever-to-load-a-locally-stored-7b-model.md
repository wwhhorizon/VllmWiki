# vllm-project/vllm#6876: [Bug]: vLLM takes forever to load a locally stored 7B model

| 字段 | 值 |
| --- | --- |
| Issue | [#6876](https://github.com/vllm-project/vllm/issues/6876) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 20; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support |
| 子分类 |  |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vLLM takes forever to load a locally stored 7B model

### Issue 正文摘录

### Your current environment ``` PyTorch version: 2.3.1+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Amazon Linux 2 (x86_64) GCC version: (GCC) 7.3.1 20180712 (Red Hat 7.3.1-17) Clang version: Could not collect CMake version: version 3.30.1 Libc version: glibc-2.26 Python version: 3.10.14 | packaged by conda-forge | (main, Mar 20 2024, 12:45:18) [GCC 12.3.0] (64-bit runtime) Python platform: Linux-5.10.217-205.860.amzn2.x86_64-x86_64-with-glibc2.26 Is CUDA available: True CUDA runtime version: 12.1.105 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA A10G Nvidia driver version: 535.183.01 cuDNN version: Could not collect HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Byte Order: Little Endian CPU(s): 8 On-line CPU(s) list: 0-7 Thread(s) per core: 2 Core(s) per socket: 4 Socket(s): 1 NUMA node(s): 1 Vendor ID: AuthenticAMD CPU family: 23 Model: 49 Model name: AMD EPYC 7R32 Stepping: 0 CPU MHz: 3130.445 BogoMIPS: 5599.99 Hypervisor vendor: KVM Virtualization type: full L1d cache: 32K L1i cache: 32K L2 cache: 512K L3...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: ally stored 7B model bug;stale ### Your current environment ``` PyTorch version: 2.3.1+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Amazon Linux 2 (x86_64) GCC version...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: rent environment ``` PyTorch version: 2.3.1+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Amazon Linux 2 (x86_64) GCC version: (GCC) 7.3.1 20180712 (Red Hat 7.3.1-17) C...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: vLLM takes forever to load a locally stored 7B model bug;stale ### Your current environment ``` PyTorch version: 2.3.1+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: xt==0.17.0 [pip3] torchvision==0.18.1 [pip3] transformers==4.43.3 [pip3] triton==2.3.1 [conda] aws-ofi-nccl 1.9.1 aws_efa1.26.1_0 https://aws-ml-conda.s3.us-west-2.amazonaws.com [conda] blas 2.116 mkl conda-forge [conda]
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: hardware_porting;model_support cuda;operator;triton build_error;slowdown dtype;env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
