# vllm-project/vllm#8955: [Installation]: vllm ROCm failed to build on Docker.

| 字段 | 值 |
| --- | --- |
| Issue | [#8955](https://github.com/vllm-project/vllm/issues/8955) |
| 状态 | closed |
| 标签 | installation;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Installation]: vllm ROCm failed to build on Docker.

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` OS: Ubuntu 24.04.1 LTS (x86_64) GCC version: (Ubuntu 13.2.0-23ubuntu4) 13.2.0 Clang version: Could not collect CMake version: Could not collect Libc version: glibc-2.39 Python version: 3.12.4 | packaged by Anaconda, Inc. | (main, Jun 18 2024, 15:12:24) [GCC 11.2.0] (64-bit runtime) Python platform: Linux-6.8.0-45-generic-x86_64-with-glibc2.39 Is CUDA available: N/A CUDA runtime version: Could not collect CUDA_MODULE_LOADING set to: N/A GPU models and configuration: Could not collect Nvidia driver version: Could not collect cuDNN version: Could not collect HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: N/A CPU: Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Address sizes: 52 bits physical, 57 bits virtual Byte Order: Little Endian CPU(s): 128 On-line CPU(s) list: 0-127 Vendor ID: AuthenticAMD Model name: AMD EPYC 9334 32-Core Processor CPU family: 25 Model: 17 Thread(s) per core: 2 Core(s) per socket: 32 Socket(s): 2 Stepping: 1 BogoMIPS: 5399.99 Flags: fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 ht syscall nx mmxext fxsr_...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 10: [Installation]: vllm ROCm failed to build on Docker. installation;stale ### Your current environment ```text The output of `python collect_env.py` OS: Ubuntu 24.04.1 LTS (x86_64) GCC version: (Ubuntu 13.2.0-23ubuntu4) 1
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: [Installation]: vllm ROCm failed to build on Docker. installation;stale ### Your current environment ```text The output of `python collect_env.py` OS: Ubuntu 24.04.1 LTS (x86_64) GCC version: (Ubuntu 13.2.0-23ubuntu4) 1...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Installation]: vllm ROCm failed to build on Docker. installation;stale ### Your current environment ```text The output of `python collect_env.py` OS: Ubuntu 24.04.1 LTS (x86_64) GCC version: (Ubuntu 13.2.0-23ubuntu4) 1...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: A runtime version: Could not collect CUDA_MODULE_LOADING set to: N/A GPU models and configuration: Could not collect Nvidia driver version: Could not collect cuDNN version: Could not collect HIP runtime version: N/A MIO...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: aves cqm_llc cqm_occup_llc cqm_mbm_total cqm_mbm_local user_shstk avx512_bf16 clzero irperf xsaveerptr rdpru wbnoinvd amd_ppin cppc arat npt lbrv svm_lock nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pausefi...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
