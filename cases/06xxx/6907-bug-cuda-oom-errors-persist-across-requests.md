# vllm-project/vllm#6907: [Bug]: cuda OOM errors persist across requests.

| 字段 | 值 |
| --- | --- |
| Issue | [#6907](https://github.com/vllm-project/vllm/issues/6907) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support |
| 子分类 | memory |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error;oom |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: cuda OOM errors persist across requests.

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` Collecting environment information... PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Amazon Linux 2 (x86_64) GCC version: (GCC) 7.3.1 20180712 (Red Hat 7.3.1-17) Clang version: Could not collect CMake version: version 3.27.7 Libc version: glibc-2.26 Python version: 3.10.9 | packaged by conda-forge | (main, Feb 2 2023, 20:20:04) [GCC 11.3.0] (64-bit runtime) Python platform: Linux-5.10.219-208.866.amzn2.x86_64-x86_64-with-glibc2.26 Is CUDA available: True CUDA runtime version: 12.1.105 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA A10G Nvidia driver version: 550.54.14 cuDNN version: Could not collect HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Byte Order: Little Endian CPU(s): 4 On-line CPU(s) list: 0-3 Thread(s) per core: 2 Core(s) per socket: 2 Socket(s): 1 NUMA node(s): 1 Vendor ID: AuthenticAMD CPU family: 23 Model: 49 Model name: AMD EPYC 7R32 Stepping: 0 CPU MHz: 3257.105 BogoMIPS: 5600.00 Hypervisor vendor:...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: f `python collect_env.py` Collecting environment information... PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Amazon Linux 2 (x86_64) GCC version...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: [Bug]: cuda OOM errors persist across requests. bug;stale ### Your current environment ```text The output of `python collect_env.py` Collecting environment information... PyTorch version: 2.3.0+cu121 Is debug build: Fal...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: ```text The output of `python collect_env.py` Collecting environment information... PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Amazon Linux 2...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: [Bug]: cuda OOM errors persist across requests. bug;stale ### Your current environment ```text The output of `python collect_env.py` Collecting environment information... PyTorch version: 2.3.0+cu121 Is debug build: Fal...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: cuda OOM errors persist across requests. bug;stale ### Your current environment ```text The output of `python collect_env.py` Collecting environment information... PyTorch version: 2.3.0+cu121 Is debug build: Fal...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
