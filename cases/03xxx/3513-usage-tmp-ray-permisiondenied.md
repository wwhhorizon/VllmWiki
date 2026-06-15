# vllm-project/vllm#3513: [Usage]: /tmp/ray PermisionDenied

| 字段 | 值 |
| --- | --- |
| Issue | [#3513](https://github.com/vllm-project/vllm/issues/3513) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: /tmp/ray PermisionDenied

### Issue 正文摘录

### Your current environment ```text Collecting environment information... PyTorch version: N/A Is debug build: N/A CUDA used to build PyTorch: N/A ROCM used to build PyTorch: N/A OS: Amazon Linux 2 (x86_64) GCC version: Could not collect Clang version: Could not collect CMake version: Could not collect Libc version: glibc-2.26 Python version: 3.11.8 (main, Mar 17 2024, 20:06:37) [GCC 7.3.1 20180712 (Red Hat 7.3.1-17)] (64-bit runtime) Python platform: Linux-4.14.336-256.559.amzn2.x86_64-x86_64-with-glibc2.26 Is CUDA available: N/A CUDA runtime version: Could not collect CUDA_MODULE_LOADING set to: N/A GPU models and configuration: Could not collect Nvidia driver version: Could not collect cuDNN version: Could not collect HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: N/A CPU: Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Byte Order: Little Endian CPU(s): 48 On-line CPU(s) list: 0-47 Thread(s) per core: 2 Core(s) per socket: 24 Socket(s): 1 NUMA node(s): 1 Vendor ID: GenuineIntel CPU family: 6 Model: 85 Model name: Intel(R) Xeon(R) Platinum 8259CL CPU @ 2.50GHz Stepping: 7 CPU MHz: 1544.802 BogoMIPS: 5000.00 Hypervisor vendor: KVM Virtualization t...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: rrent environment ```text Collecting environment information... PyTorch version: N/A Is debug build: N/A CUDA used to build PyTorch: N/A ROCM used to build PyTorch: N/A OS: Amazon Linux 2 (x86_64) GCC version: Could not...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: ting environment information... PyTorch version: N/A Is debug build: N/A CUDA used to build PyTorch: N/A ROCM used to build PyTorch: N/A OS: Amazon Linux 2 (x86_64) GCC version: Could not collect Clang version: Could no...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: age;stale ### Your current environment ```text Collecting environment information... PyTorch version: N/A Is debug build: N/A CUDA used to build PyTorch: N/A ROCM used to build PyTorch: N/A OS: Amazon Linux 2 (x86_64) G...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Usage]: /tmp/ray PermisionDenied usage;stale ### Your current environment ```text Collecting environment information... PyTorch version: N/A Is debug build: N/A CUDA used to build PyTorch: N/A ROCM used to build PyTorc...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
