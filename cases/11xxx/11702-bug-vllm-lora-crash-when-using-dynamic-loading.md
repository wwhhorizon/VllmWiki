# vllm-project/vllm#11702: [Bug]: vLLM LoRA Crash when using Dynamic Loading

| 字段 | 值 |
| --- | --- |
| Issue | [#11702](https://github.com/vllm-project/vllm/issues/11702) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;moe;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vLLM LoRA Crash when using Dynamic Loading

### Issue 正文摘录

### Your current environment ``` root@mistral-7b-lora-7946cc6459-jqx4h:/vllm-workspace# python3 collect_env.py Collecting environment information... PyTorch version: 2.5.0+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version: Could not collect CMake version: Could not collect Libc version: glibc-2.35 Python version: 3.12.7 (main, Oct 1 2024, 08:52:12) [GCC 11.4.0] (64-bit runtime) Python platform: Linux-6.6.41-amd64-x86_64-with-glibc2.35 Is CUDA available: True CUDA runtime version: Could not collect CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA H100 80GB HBM3 Nvidia driver version: 535.86.10 cuDNN version: Could not collect HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Address sizes: 46 bits physical, 57 bits virtual Byte Order: Little Endian CPU(s): 192 On-line CPU(s) list: 0-191 Vendor ID: GenuineIntel Model name: Intel(R) Xeon(R) Platinum 8468 CPU family: 6 Model: 143 Thread(s) per core: 2 Core(s) per socket: 48 Socket(s):...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: e# python3 collect_env.py Collecting environment information... PyTorch version: 2.5.0+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (x86_64) GCC ver...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: onment information... PyTorch version: 2.5.0+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4....
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: ed Vulnerability Meltdown: Not affected Vulnerability Mmio stale data: Not affected Vulnerability Reg file data sampling: Not affected Vulnerability Retbleed: Not affected Vulnerability Spec rstack overflow: Not affecte...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: async abort: Not affected Versions of relevant libraries: [pip3] flashinfer==0.1.6+cu121torch2.4 [pip3] numpy==1.26.4 [pip3] nvidia-cublas-cu12==12.4.5.8 [pip3] nvidia-cuda-cupti-cu12==12.4.127 [pip3] nvidia-cuda-nvrtc-...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: -jqx4h:/vllm-workspace# python3 collect_env.py Collecting environment information... PyTorch version: 2.5.0+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
