# vllm-project/vllm#7231: [Bug]: vllm serve get me "command not found"

| 字段 | 值 |
| --- | --- |
| Issue | [#7231](https://github.com/vllm-project/vllm/issues/7231) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vllm serve get me "command not found"

### Issue 正文摘录

### Your current environment ```text PyTorch version: 2.0.1+cu117 Is debug build: False CUDA used to build PyTorch: 11.7 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.3 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version: Could not collect CMake version: version 3.30.2 Libc version: glibc-2.35 Python version: 3.10.12 (main, Jul 29 2024, 16:56:48) [GCC 11.4.0] (64-bit runtime) Python platform: Linux-5.15.133.1-microsoft-standard-WSL2-x86_64-with-glibc2.35 Is CUDA available: True CUDA runtime version: 11.5.119 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA GeForce GTX 1080 Nvidia driver version: 545.84 cuDNN version: Could not collect HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Address sizes: 39 bits physical, 48 bits virtual Byte Order: Little Endian CPU(s): 12 On-line CPU(s) list: 0-11 Vendor ID: GenuineIntel Model name: 11th Gen Intel(R) Core(TM) i5-11400 @ 2.60GHz CPU family: 6 Model: 167 Thread(s) per core: 2 Core(s) per socket: 6 Socket(s): 1 Stepping: 1 BogoMIPS: 5183.99 Flags: fpu vme de pse tsc msr pae mce cx8 apic sep mtrr...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: me "command not found" bug ### Your current environment ```text PyTorch version: 2.0.1+cu117 Is debug build: False CUDA used to build PyTorch: 11.7 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.3 LTS (x86_64) GCC ver...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: environment ```text PyTorch version: 2.0.1+cu117 Is debug build: False CUDA used to build PyTorch: 11.7 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.3 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: True CUDA runtime version: 11.5.119 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA GeForce GTX 1080 Nvidia driver version: 545.84 cuDNN version: Could not collect HIP runtime version: N/A M...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: cted Vulnerability Meltdown: Not affected Vulnerability Mmio stale data: Vulnerable: Clear CPU buffers attempted, no microcode; SMT Host state unknown Vulnerability Retbleed: Mitigation; Enhanced IBRS Vulnerability Spec...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: rch==2.0.1 [pip3] torchvision==0.15.2 [pip3] transformers==4.42.3 [pip3] triton==2.0.0 [conda] Could not collect ROCM Version: Could not collect Neuron SDK Version: N/A vLLM Version: 0.2.1.post1 vLLM Build Flags: CUDA A...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
