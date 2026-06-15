# vllm-project/vllm#14218: [Bug]: Deepseek R1 671B int8 not working on TPU

| 字段 | 值 |
| --- | --- |
| Issue | [#14218](https://github.com/vllm-project/vllm/issues/14218) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;quantization;speculative_decoding |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;quantization |
| 症状 | build_error |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Deepseek R1 671B int8 not working on TPU

### Issue 正文摘录

### Your current environment INFO 03-04 15:53:31 [__init__.py:253] Automatically detected platform tpu. Collecting environment information... PyTorch version: 2.7.0.dev20250304+cpu Is debug build: False CUDA used to build PyTorch: None ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.2 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version: Could not collect CMake version: version 3.31.6 Libc version: glibc-2.35 Python version: 3.10.12 (main, Feb 4 2025, 14:57:36) [GCC 11.4.0] (64-bit runtime) Python platform: Linux-5.19.0-1022-gcp-x86_64-with-glibc2.35 Is CUDA available: False CUDA runtime version: No CUDA CUDA_MODULE_LOADING set to: N/A GPU models and configuration: No CUDA Nvidia driver version: No CUDA cuDNN version: No CUDA HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Address sizes: 48 bits physical, 48 bits virtual Byte Order: Little Endian CPU(s): 240 On-line CPU(s) list: 0-239 Vendor ID: AuthenticAMD Model name: AMD EPYC 7B12 CPU family: 23 Model: 49 Thread(s) per core: 2 Core(s) per socket: 60 Socket(s): 2 Stepping: 0 BogoMIPS: 4500.00 Flags: fpu vme de pse t...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: lly detected platform tpu. Collecting environment information... PyTorch version: 2.7.0.dev20250304+cpu Is debug build: False CUDA used to build PyTorch: None ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.2 LTS (x86_...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: ormation... PyTorch version: 2.7.0.dev20250304+cpu Is debug build: False CUDA used to build PyTorch: None ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.2 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4....
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: __.py:253] Automatically detected platform tpu. Collecting environment information... PyTorch version: 2.7.0.dev20250304+cpu Is debug build: False CUDA used to build PyTorch: None ROCM used to build PyTorch: N/A OS: Ubu...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: Deepseek R1 671B int8 not working on TPU bug;stale ### Your current environment INFO 03-04 15:53:31 [__init__.py:253] Automatically detected platform tpu. Collecting environment information... PyTorch version: 2....
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: development ci_build;distributed_parallel;hardware_porting;model_support;quantization;speculative_decoding cuda;operator;quantization build_error dtype;env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
