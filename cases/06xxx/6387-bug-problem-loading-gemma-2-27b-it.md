# vllm-project/vllm#6387: [Bug]: Problem loading Gemma 2 27b-it

| 字段 | 值 |
| --- | --- |
| Issue | [#6387](https://github.com/vllm-project/vllm/issues/6387) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;scheduler_memory;speculative_decoding |
| 子分类 | race_cond |
| Operator 关键词 | cuda;kernel;operator;triton |
| 症状 | build_error;crash;mismatch;oom |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Problem loading Gemma 2 27b-it

### Issue 正文摘录

### Your current environment ```text PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Red Hat Enterprise Linux 9.1 (Plow) (x86_64) GCC version: (GCC) 11.3.0 Clang version: Could not collect CMake version: version 3.30.0 Libc version: glibc-2.34 Python version: 3.10.4 (main, Apr 29 2023, 13:32:24) [GCC 11.3.0] (64-bit runtime) Python platform: Linux-5.14.0-162.6.1.el9_1.x86_64-x86_64-with-glibc2.34 Is CUDA available: True CUDA runtime version: 12.1.105 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA A100-SXM4-40GB GPU 1: NVIDIA A100-SXM4-40GB Nvidia driver version: 525.85.12 cuDNN version: Could not collect HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Address sizes: 46 bits physical, 57 bits virtual Byte Order: Little Endian CPU(s): 48 On-line CPU(s) list: 0-47 Vendor ID: GenuineIntel Model name: Intel(R) Xeon(R) Gold 5317 CPU @ 3.00GHz CPU family: 6 Model: 106 Thread(s) per core: 2 Core(s) per socket: 12 Socket(s): 2 Stepping: 6 CPU max MHz: 3600.0000 CPU min MHz: 800.0000 BogoMIPS: 6000.00 F...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: g Gemma 2 27b-it bug;stale ### Your current environment ```text PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Red Hat Enterprise Linux 9.1 (Plow)...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: environment ```text PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Red Hat Enterprise Linux 9.1 (Plow) (x86_64) GCC version: (GCC) 11.3.0 Clang ve...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: Problem loading Gemma 2 27b-it bug;stale ### Your current environment ```text PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Red Hat Enterp...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: Tsx async abort: Not affected Versions of relevant libraries: [pip3] flashinfer==0.0.8+cu121torch2.3 [pip3] numpy==1.26.4 [pip3] nvidia-nccl-cu12==2.20.5 [pip3] torch==2.3.0 [pip3] torchvision==0.18.0 [pip3] transformer...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: Problem loading Gemma 2 27b-it bug;stale ### Your current environment ```text PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Red Hat Enterp...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
