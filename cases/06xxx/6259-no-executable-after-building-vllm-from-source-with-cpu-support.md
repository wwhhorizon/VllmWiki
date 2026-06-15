# vllm-project/vllm#6259: No executable after building vllm from source with CPU support

| 字段 | 值 |
| --- | --- |
| Issue | [#6259](https://github.com/vllm-project/vllm/issues/6259) |
| 状态 | closed |
| 标签 | installation;stale |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> No executable after building vllm from source with CPU support

### Issue 正文摘录

### Your current environment ```text PyTorch version: 2.3.1+cpu Is debug build: False CUDA used to build PyTorch: None ROCM used to build PyTorch: N/A OS: Ubuntu 24.04 LTS (x86_64) GCC version: (Ubuntu 13.2.0-23ubuntu4) 13.2.0 Clang version: Could not collect CMake version: version 3.29.6 Libc version: glibc-2.39 Python version: 3.9.19 (main, May 6 2024, 19:43:03) [GCC 11.2.0] (64-bit runtime) Python platform: Linux-6.8.0-36-generic-x86_64-with-glibc2.39 Is CUDA available: False CUDA runtime version: No CUDA CUDA_MODULE_LOADING set to: N/A GPU models and configuration: No CUDA Nvidia driver version: No CUDA cuDNN version: No CUDA HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Address sizes: 48 bits physical, 48 bits virtual Byte Order: Little Endian CPU(s): 6 On-line CPU(s) list: 0-5 Vendor ID: AuthenticAMD Model name: AMD Ryzen 5 4500U with Radeon Graphics CPU family: 23 Model: 96 Thread(s) per core: 1 Core(s) per socket: 6 Socket(s): 1 Stepping: 1 Frequency boost: enabled CPU(s) scaling MHz: 73% CPU max MHz: 2375.0000 CPU min MHz: 1400.0000 BogoMIPS: 4741.01 Flags: fpu vme de pse tsc msr pa...

## 现有链接修复摘要

#6422 [ Kernel ] AWQ Fused MoE

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: No executable after building vllm from source with CPU support installation;stale ### Your current environment ```text PyTorch version: 2.3.1+cpu Is debug build: False CUDA used to build PyTorch: None ROCM used to build...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: nt environment ```text PyTorch version: 2.3.1+cpu Is debug build: False CUDA used to build PyTorch: None ROCM used to build PyTorch: N/A OS: Ubuntu 24.04 LTS (x86_64) GCC version: (Ubuntu 13.2.0-23ubuntu4) 13.2.0 Clang...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: False CUDA runtime version: No CUDA CUDA_MODULE_LOADING set to: N/A GPU models and configuration: No CUDA Nvidia driver version: No CUDA cuDNN version: No CUDA HIP runtime version: N/A MIOpen runtime version: N/A Is XNN...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: executable after building vllm from source with CPU support installation;stale ### Your current environment ```text PyTorch version: 2.3.1+cpu Is debug build: False CUDA used to build PyTorch: None ROCM used to build Py...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: perf xsaveerptr rdpru wbnoinvd cppc arat npt lbrv svm_lock nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pausefilter pfthreshold avic v_vmsave_vmload vgif v_spec_ctrl umip rdpid overflow_recov succor smca Vir...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#6422](https://github.com/vllm-project/vllm/pull/6422) | mentioned | 0.6 | [ Kernel ] AWQ Fused MoE | [ Kernel ] AWQ Fused MoE SUMMARY: * Picks up #6259 2761 to support AWQ MoE models via a fused kernel, after the refactor I did in #5970. The kernels for this PR |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
