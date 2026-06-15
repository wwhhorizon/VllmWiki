# vllm-project/vllm#13914: [Bug]: running deepseek-r1 14B with 2*5090D

| 字段 | 值 |
| --- | --- |
| Issue | [#13914](https://github.com/vllm-project/vllm/issues/13914) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;import_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: running deepseek-r1 14B with 2*5090D

### Issue 正文摘录

### Your current environment pytorch==2.7 vllm==0.7.3 cuda==12.8 gpu==5090Droot@lam-MU72-SU0-00:/opt# python3 collect_env.py Collecting environment information... PyTorch version: 2.7.0.dev20250226+cu128 Is debug build: False CUDA used to build PyTorch: 12.8 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (x86_64) GCC version: (Ubuntu 12.3.0-1ubuntu1~22.04) 12.3.0 Clang version: Could not collect CMake version: Could not collect Libc version: glibc-2.35 Python version: 3.10.12 (main, Feb 4 2025, 14:57:36) [GCC 11.4.0] (64-bit runtime) Python platform: Linux-6.8.0-52-generic-x86_64-with-glibc2.35 Is CUDA available: True CUDA runtime version: Could not collect CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA GeForce RTX 5090 D GPU 1: NVIDIA GeForce RTX 5090 D Nvidia driver version: 570.86.10 cuDNN version: Could not collect HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Address sizes: 46 bits physical, 57 bits virtual Byte Order: Little Endian CPU(s): 40 On-line CPU(s) list: 0-39 Vendor ID: GenuineIntel Model name: Intel(R) Xeon(R) Silver 4316 CPU @ 2.30GHz CP...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 10: t# python3 collect_env.py Collecting environment information... PyTorch version: 2.7.0.dev20250226+cu128 Is debug build: False CUDA used to build PyTorch: 12.8 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (x86...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: 2*5090D bug;stale ### Your current environment pytorch==2.7 vllm==0.7.3 cuda==12.8 gpu==5090Droot@lam-MU72-SU0-00:/opt# python3 collect_env.py Collecting environment information... PyTorch version: 2.7.0.dev20250226+cu1...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: t@lam-MU72-SU0-00:/opt# python3 collect_env.py Collecting environment information... PyTorch version: 2.7.0.dev20250226+cu128 Is debug build: False CUDA used to build PyTorch: 12.8 ROCM used to build PyTorch: N/A OS: Ub...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: running deepseek-r1 14B with 2*5090D bug;stale ### Your current environment pytorch==2.7 vllm==0.7.3 cuda==12.8 gpu==5090Droot@lam-MU72-SU0-00:/opt# python3 collect_env.py Collecting environment information... Py...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: -nvjitlink-cu12==12.8.61 [pip3] nvidia-nvtx-cu12==12.8.55 [pip3] pytorch-triton==3.2.0+git4b3bb1f8 [pip3] pyzmq==26.2.1 [pip3] torch==2.7.0.dev20250226+cu128 [pip3] torchaudio==2.6.0.dev20250226+cu128 [pip3] torchvision...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
