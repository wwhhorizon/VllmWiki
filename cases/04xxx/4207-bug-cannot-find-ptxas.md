# vllm-project/vllm#4207: [Bug]: Cannot find ptxas

| 字段 | 值 |
| --- | --- |
| Issue | [#4207](https://github.com/vllm-project/vllm/issues/4207) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Cannot find ptxas

### Issue 正文摘录

### Your current environment PyTorch version: 2.1.2+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version: Could not collect CMake version: version 3.29.2 Libc version: glibc-2.35 Python version: 3.10.12 (main, Nov 20 2023, 15:14:05) [GCC 11.4.0] (64-bit runtime) Python platform: Linux-5.15.133.1-microsoft-standard-WSL2-x86_64-with-glibc2.35 Is CUDA available: True CUDA runtime version: 12.4.131 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA GeForce GTX 1650 Nvidia driver version: 552.22 cuDNN version: Could not collect HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Address sizes: 39 bits physical, 48 bits virtual Byte Order: Little Endian CPU(s): 8 On-line CPU(s) list: 0-7 Vendor ID: GenuineIntel Model name: Intel(R) Core(TM) i5-10300H CPU @ 2.50GHz CPU family: 6 Model: 165 Thread(s) per core: 2 Core(s) per socket: 4 Socket(s): 1 Stepping: 2 BogoMIPS: 4992.01 Flags: fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov p...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: [Bug]: Cannot find ptxas bug ### Your current environment PyTorch version: 2.1.2+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (x86_64) GCC version:...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: [Bug]: Cannot find ptxas bug ### Your current environment PyTorch version: 2.1.2+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (x86_64) GCC version:...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: True CUDA runtime version: 12.4.131 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA GeForce GTX 1650 Nvidia driver version: 552.22 cuDNN version: Could not collect HIP runtime version: N/A M...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: aries: [pip3] mypy-extensions==1.0.0 [pip3] numpy==1.26.4 [pip3] pytorch-triton==3.0.0+989adb9a29 [pip3] torch==2.1.2 [pip3] triton==2.1.0 [conda] Could not collectROCM Version: Could not collect Neuron SDK Version: N/A...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: .llms.vllm import Vllm llm = Vllm( model="microsoft/Orca-2-7b", dtype="float16", max_new_tokens=100, vllm_kwargs={"swap_space": 0, "gpu_memory_utilization": 0.5}, ) ``` On running it, I am encountering the following err...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
