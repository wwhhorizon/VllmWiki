# vllm-project/vllm#7283: [Bug]: Empty prompt kills vllm server (AsyncEngineDeadError: Background loop is stopped.)

| 字段 | 值 |
| --- | --- |
| Issue | [#7283](https://github.com/vllm-project/vllm/issues/7283) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf;slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Empty prompt kills vllm server (AsyncEngineDeadError: Background loop is stopped.)

### Issue 正文摘录

### Your current environment ```text python3 collect_env.py Collecting environment information... PyTorch version: 2.3.1+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.6 LTS (x86_64) GCC version: (Ubuntu 9.4.0-1ubuntu1~20.04.2) 9.4.0 Clang version: Could not collect CMake version: version 3.30.1 Libc version: glibc-2.31 Python version: 3.10.14 (main, Apr 6 2024, 18:45:05) [GCC 9.4.0] (64-bit runtime) Python platform: Linux-5.15.138.1-4.cm2-x86_64-with-glibc2.31 Is CUDA available: True CUDA runtime version: Could not collect CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA A100-SXM4-80GB Nvidia driver version: 525.85.12 cuDNN version: Could not collect HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Byte Order: Little Endian Address sizes: 48 bits physical, 48 bits virtual CPU(s): 256 On-line CPU(s) list: 0-255 Thread(s) per core: 2 Core(s) per socket: 64 Socket(s): 2 NUMA node(s): 8 Vendor ID: AuthenticAMD CPU family: 25 Model: 1 Model name: AMD EPYC 7763 64-Core Processor Stepping: 1 Frequency boost: en...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: xt python3 collect_env.py Collecting environment information... PyTorch version: 2.3.1+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.6 LTS (x86_64) GCC ver...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 7: cted Vulnerability Meltdown: Not affected Vulnerability Mmio stale data: Not affected Vulnerability Retbleed: Not affected Vulnerability Spec rstack overflow: Mitigation; safe RET, no microcode Vulnerability Spec store...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: onment information... PyTorch version: 2.3.1+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.6 LTS (x86_64) GCC version: (Ubuntu 9.4.0-1ubuntu1~20.04.2) 9.4....
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: nt environment ```text python3 collect_env.py Collecting environment information... PyTorch version: 2.3.1+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.6...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: rdpid overflow_recov succor smca Versions of relevant libraries: [pip3] flashinfer==0.0.9+cu121torch2.3 [pip3] numpy==1.26.4 [pip3] nvidia-nccl-cu12==2.20.5 [pip3] pyzmq==26.0.3 [pip3] torch==2.3.1 [pip3] torchvision==0...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
