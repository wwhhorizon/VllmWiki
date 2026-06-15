# vllm-project/vllm#7578: [Usage]: 请问vllm怎么开启并发推理

| 字段 | 值 |
| --- | --- |
| Issue | [#7578](https://github.com/vllm-project/vllm/issues/7578) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: 请问vllm怎么开启并发推理

### Issue 正文摘录

### Your current environment PyTorch version: 2.4.0 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version: Could not collect CMake version: version 3.29.5 Libc version: glibc-2.35 Python version: 3.11.9 (main, Apr 19 2024, 16:48:06) [GCC 11.2.0] (64-bit runtime) Python platform: Linux-6.8.0-40-generic-x86_64-with-glibc2.35 Is CUDA available: True CUDA runtime version: 12.1.105 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA RTX A6000 GPU 1: NVIDIA RTX A6000 GPU 2: NVIDIA RTX A6000 GPU 3: NVIDIA RTX A6000 Nvidia driver version: 560.28.03 cuDNN version: Could not collect HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: 架构： x86_64 CPU 运行模式： 32-bit, 64-bit Address sizes: 43 bits physical, 48 bits virtual 字节序： Little Endian CPU: 256 在线 CPU 列表： 0-255 厂商 ID： AuthenticAMD 型号名称： AMD EPYC 7H12 64-Core Processor CPU 系列： 23 型号： 49 每个核的线程数： 2 每个座的核数： 64 座： 2 步进： 0 Frequency boost: enabled CPU 最大 MHz： 2600.0000 CPU 最小 MHz： 1500.0000 BogoMIPS： 5190.46 标记： fpu vme de pse tsc msr pae mce cx8 apic sep mtrr...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: Usage]: 请问vllm怎么开启并发推理 usage;stale ### Your current environment PyTorch version: 2.4.0 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (x86_64) GCC version:...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: # Your current environment PyTorch version: 2.4.0 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: True CUDA runtime version: 12.1.105 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA RTX A6000 GPU 1: NVIDIA RTX A6000 GPU 2: NVIDIA RTX A6000 GPU 3: NVIDIA RTX A6000 Nvidia driver version: 5...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Usage]: 请问vllm怎么开启并发推理 usage;stale ### Your current environment PyTorch version: 2.4.0 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (x86_64) GCC version:...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: .4.0.post0 [pip3] torchvision==0.19.0 [pip3] transformers==4.43.2 [pip3] triton==2.3.1 [conda] blas 1.0 mkl [conda] ffmpeg 4.3 hf484d3e_0 pytorch [conda] libjpeg-turbo 2.0.0 h9bf14

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
