# vllm-project/vllm#6190: [Bug]: AsyncEngineDeadError: Task finished unexpectedly with Gemma2 9B

| 字段 | 值 |
| --- | --- |
| Issue | [#6190](https://github.com/vllm-project/vllm/issues/6190) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: AsyncEngineDeadError: Task finished unexpectedly with Gemma2 9B

### Issue 正文摘录

### Your current environment ```PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version: Could not collect CMake version: version 3.29.6 Libc version: glibc-2.35 Python version: 3.9.19 (main, May 6 2024, 19:43:03) [GCC 11.2.0] (64-bit runtime) Python platform: Linux-5.15.153.1-microsoft-standard-WSL2-x86_64-with-glibc2.35 Is CUDA available: True CUDA runtime version: Could not collect CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA GeForce RTX 3090 Nvidia driver version: 555.85 cuDNN version: Could not collect HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Address sizes: 46 bits physical, 48 bits virtual Byte Order: Little Endian CPU(s): 28 On-line CPU(s) list: 0-27 Vendor ID: GenuineIntel Model name: Intel(R) Core(TM) i7-14700K CPU family: 6 Model: 183 Thread(s) per core: 2 Core(s) per socket: 14 Socket(s): 1 Stepping: 1 BogoMIPS: 6835.19 Flags: fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pa...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: ctedly with Gemma2 9B bug;stale ### Your current environment ```PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (x86_64) GCC ver...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: rrent environment ```PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: AsyncEngineDeadError: Task finished unexpectedly with Gemma2 9B bug;stale ### Your current environment ```PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyT...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: =True, gpu_memory_utilization=0.9, dtype=torch.float16, quantization=quantization, load_format=load_format) self.engine = AsyncLLMEngine.from_engine_args(engine_args) results_generator = self.engine
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: ug]: AsyncEngineDeadError: Task finished unexpectedly with Gemma2 9B bug;stale ### Your current environment ```PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTor...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
