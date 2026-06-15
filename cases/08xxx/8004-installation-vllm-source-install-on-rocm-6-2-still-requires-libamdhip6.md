# vllm-project/vllm#8004: [Installation]: vLLM source install on rocm 6.2 still requires libamdhip64.so.6

| 字段 | 值 |
| --- | --- |
| Issue | [#8004](https://github.com/vllm-project/vllm/issues/8004) |
| 状态 | closed |
| 标签 | installation;rocm |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;import_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Installation]: vLLM source install on rocm 6.2 still requires libamdhip64.so.6

### Issue 正文摘录

### Your current environment ```text Collecting environment information... WARNING 08-29 12:39:01 _custom_ops.py:18] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'") PyTorch version: 2.5.0.dev20240821+rocm6.2 Is debug build: False CUDA used to build PyTorch: N/A ROCM used to build PyTorch: 6.2.41133-dd7f95766 OS: SUSE Linux Enterprise Server 15 SP5 (x86_64) GCC version: (SUSE Linux) 12.3.0 Clang version: Could not collect CMake version: version 3.30.2 Libc version: glibc-2.31 Python version: 3.11.8 (main, Feb 26 2024, 21:39:34) [GCC 11.2.0] (64-bit runtime) Python platform: Linux-5.14.21-150500.55.49_13.0.57-cray_shasta_c-x86_64-with-glibc2.31 Is CUDA available: True CUDA runtime version: Could not collect CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: AMD Instinct MI210 (gfx90a:sramecc+:xnack-) Nvidia driver version: Could not collect cuDNN version: Could not collect HIP runtime version: 6.2.41133 MIOpen runtime version: 3.2.0 Is XNNPACK available: True CPU: Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Address sizes: 48 bits physical, 48 bits virtual Byte Order: Little Endian CPU(s): 128 On-line CPU(s) list: 0-127 Vendor I...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: [Installation]: vLLM source install on rocm 6.2 still requires libamdhip64.so.6 installation;rocm ### Your current environment ```text Collecting environment information... WARNING 08-29 12:39:01 _custom_ops.py:18] Faile
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: [Installation]: vLLM source install on rocm 6.2 still requires libamdhip64.so.6 installation;rocm ### Your current environment ```text Collecting environment information... WARNING 08-29 12:39:01 _custom_ops.py:18] Fail...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: tion;rocm ### Your current environment ```text Collecting environment information... WARNING 08-29 12:39:01 _custom_ops.py:18] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'") PyTorch...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: in brs arat npt lbrv svm_lock nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pausefilter pfthreshold v_vmsave_vmload vgif v_spec_ctrl umip pku ospke vaes vpclmulqdq rdpid overflow_recov succor smca fsrm L1d ca...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [pip3] pyzmq==26.1.1 [pip3] torch==2.5.0.dev20240821+rocm6.2 [pip3] torcheval==0.0.7 [pip3] torchmetrics==1.4.1 [pip3] transformers==4.44.1 [conda] numpy 1.26.4 pypi_0 pypi [conda] nvidia-ml-py 12.560.30 pypi_0 pypi [co...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
