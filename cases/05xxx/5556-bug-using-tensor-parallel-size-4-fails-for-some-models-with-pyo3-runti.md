# vllm-project/vllm#5556: [Bug]: Using tensor-parallel-size 4 fails for some models with pyo3_runtime.PanicException: The global thread pool has not been initialized.: ThreadPoolBuildError {"Resource temporarily unavailable" })

| 字段 | 值 |
| --- | --- |
| Issue | [#5556](https://github.com/vllm-project/vllm/issues/5556) |
| 状态 | closed |
| 标签 | installation;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Using tensor-parallel-size 4 fails for some models with pyo3_runtime.PanicException: The global thread pool has not been initialized.: ThreadPoolBuildError {"Resource temporarily unavailable" })

### Issue 正文摘录

### Your current environment ```text Collecting environment information... PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: SUSE Linux Enterprise Server 15 SP5 (x86_64) GCC version: (SUSE Linux) 7.5.0 Clang version: Could not collect CMake version: version 3.29.5 Libc version: glibc-2.31 Python version: 3.10.12 (main, Jul 5 2023, 18:54:27) [GCC 11.2.0] (64-bit runtime) Python platform: Linux-5.14.21-150500.55.49-default-x86_64-with-glibc2.31 Is CUDA available: True CUDA runtime version: 12.4.131 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA A100-SXM4-40GB GPU 1: NVIDIA A100-SXM4-40GB GPU 2: NVIDIA A100-SXM4-40GB GPU 3: NVIDIA A100-SXM4-40GB Nvidia driver version: 535.154.05 cuDNN version: Could not collect HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Address sizes: 48 bits physical, 48 bits virtual Byte Order: Little Endian CPU(s): 64 On-line CPU(s) list: 0-63 Vendor ID: AuthenticAMD Model name: AMD EPYC 7543P 32-Core Processor CPU family: 25 Model: 1 Thread(s) per core: 2 Core(s) per socke...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: icException: The global thread pool has not been initialized.: ThreadPoolBuildError {"Resource temporarily unavailable" }) installation;stale ### Your current environment ```text Collecting environment information... Py...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: onment information... PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: SUSE Linux Enterprise Server 15 SP5 (x86_64) GCC version: (SUSE Linux) 7.5.0...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: veerptr rdpru wbnoinvd amd_ppin brs arat npt lbrv svm_lock nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pausefilter pfthreshold v_vmsave_vmload vgif v_spec_ctrl umip pku ospke vaes vpclmulqdq rdpid overflow_...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: Using tensor-parallel-size 4 fails for some models with pyo3_runtime.PanicException: The global thread pool has not been initialized.: ThreadPoolBuildError {"Resource temporarily unavailable" }) installation;stal...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: ThreadPoolBuildError {"Resource temporarily unavailable" }) installation;stale ### Your current environment ```text Collecting environment information... PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to b...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
