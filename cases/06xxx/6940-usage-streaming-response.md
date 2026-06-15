# vllm-project/vllm#6940: [Usage]: Streaming response

| 字段 | 值 |
| --- | --- |
| Issue | [#6940](https://github.com/vllm-project/vllm/issues/6940) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;frontend_api;hardware_porting;model_support;sampling_logits |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: Streaming response

### Issue 正文摘录

### Your current environment ```text PyTorch version: N/A Is debug build: N/A CUDA used to build PyTorch: N/A ROCM used to build PyTorch: N/A OS: Ubuntu 24.04 LTS (x86_64) GCC version: (Ubuntu 13.2.0-23ubuntu4) 13.2.0 Clang version: Could not collect CMake version: Could not collect Libc version: glibc-2.39 Python version: 3.12.3 (main, Apr 10 2024, 05:33:47) [GCC 13.2.0] (64-bit runtime) Python platform: Linux-6.8.0-1012-aws-x86_64-with-glibc2.39 Is CUDA available: N/A CUDA runtime version: 12.0.140 CUDA_MODULE_LOADING set to: N/A GPU models and configuration: GPU 0: Tesla T4 GPU 1: Tesla T4 GPU 2: Tesla T4 GPU 3: Tesla T4 Nvidia driver version: 555.42.06 cuDNN version: Could not collect HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: N/A CPU: Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Address sizes: 46 bits physical, 48 bits virtual Byte Order: Little Endian CPU(s): 48 On-line CPU(s) list: 0-47 Vendor ID: GenuineIntel Model name: Intel(R) Xeon(R) Platinum 8259CL CPU @ 2.50GHz CPU family: 6 Model: 85 Thread(s) per core: 2 Core(s) per socket: 24 Socket(s): 1 Stepping: 7 BogoMIPS: 4999.98 Flags: fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pg...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: aming response usage;stale ### Your current environment ```text PyTorch version: N/A Is debug build: N/A CUDA used to build PyTorch: N/A ROCM used to build PyTorch: N/A OS: Ubuntu 24.04 LTS (x86_64) GCC version: (Ubuntu...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: ur current environment ```text PyTorch version: N/A Is debug build: N/A CUDA used to build PyTorch: N/A ROCM used to build PyTorch: N/A OS: Ubuntu 24.04 LTS (x86_64) GCC version: (Ubuntu 13.2.0-23ubuntu4) 13.2.0 Clang v...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: : N/A CUDA runtime version: 12.0.140 CUDA_MODULE_LOADING set to: N/A GPU models and configuration: GPU 0: Tesla T4 GPU 1: Tesla T4 GPU 2: Tesla T4 GPU 3: Tesla T4 Nvidia driver version: 555.42.06 cuDNN version: Could no...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: 024) llm = LLM(MODEL_NAME, tensor_parallel_size=4, dtype="half", gpu_memory_utilization=0.5, max_model_len=27_000) message = SYSTEM_PROMPT + "\n\n" + f"Question: {question}\n\nDocument: {document}" response = llm.genera...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Usage]: Streaming response usage;stale ### Your current environment ```text PyTorch version: N/A Is debug build: N/A CUDA used to build PyTorch: N/A ROCM used to build PyTorch: N/A OS: Ubuntu 24.04 LTS (x86_64) GCC ver...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
