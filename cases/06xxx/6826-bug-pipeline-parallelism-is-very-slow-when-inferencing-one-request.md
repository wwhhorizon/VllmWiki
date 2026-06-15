# vllm-project/vllm#6826: [Bug]: Pipeline parallelism is very slow when inferencing one request

| 字段 | 值 |
| --- | --- |
| Issue | [#6826](https://github.com/vllm-project/vllm/issues/6826) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf;slowdown |
| 根因提示 | env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Pipeline parallelism is very slow when inferencing one request

### Issue 正文摘录

### Your current environment ```text Collecting environment information... PyTorch version: 2.3.1+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Debian GNU/Linux 11 (bullseye) (x86_64) GCC version: (Spack GCC) 10.2.0 Clang version: Could not collect CMake version: version 3.29.5 Libc version: glibc-2.31 Python version: 3.10.10 (main, Aug 15 2023, 10:11:04) [GCC 7.5.0] (64-bit runtime) Python platform: Linux-5.10.0-26-amd64-x86_64-with-glibc2.31 Is CUDA available: True CUDA runtime version: 12.3.52 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA A100-PCIE-40GB GPU 1: NVIDIA A100-PCIE-40GB GPU 2: NVIDIA A100-PCIE-40GB GPU 3: NVIDIA A100-PCIE-40GB Nvidia driver version: 555.42.06 cuDNN version: Could not collect HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Byte Order: Little Endian Address sizes: 43 bits physical, 48 bits virtual CPU(s): 256 On-line CPU(s) list: 0-254 Off-line CPU(s) list: 255 Thread(s) per core: 1 Core(s) per socket: 64 Socket(s): 2 NUMA node(s): 2 Vendor ID: AuthenticAMD CPU family: 23 Model: 49 M...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: [Bug]: Pipeline parallelism is very slow when inferencing one request bug ### Your current environment ```text Collecting environment information... PyTorch version: 2.3.1+cu121 Is debug build: False CUDA used to build...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: [Bug]: Pipeline parallelism is very slow when inferencing one request bug ### Your current environment ```text Collecting environment information... PyTorch version: 2.3.1+cu121 Is debug build: False CUDA used to build...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: [Bug]: Pipeline parallelism is very slow when inferencing one request bug ### Your current environment ```text Collecting environment information... PyTorch version: 2.3.1+cu121 Is debug build: False CUDA used to build...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: quest bug ### Your current environment ```text Collecting environment information... PyTorch version: 2.3.1+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Debian GNU/Lin...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: nvironment information... PyTorch version: 2.3.1+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Debian GNU/Linux 11 (bullseye) (x86_64) GCC version: (Spack GCC) 10.2.0 C...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
