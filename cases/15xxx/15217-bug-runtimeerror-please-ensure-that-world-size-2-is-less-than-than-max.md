# vllm-project/vllm#15217: [Bug]: RuntimeError: please ensure that world_size (2) is less than than max local gpu count (1)

| 字段 | 值 |
| --- | --- |
| Issue | [#15217](https://github.com/vllm-project/vllm/issues/15217) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;fp8;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf;oom |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: RuntimeError: please ensure that world_size (2) is less than than max local gpu count (1)

### Issue 正文摘录

### Your current environment ```text Collecting environment information... PyTorch version: 2.7.0a0+git6c0e746 Is debug build: False CUDA used to build PyTorch: N/A ROCM used to build PyTorch: 6.3.42133-1b9c17779 OS: Ubuntu 22.04.5 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version: 18.0.0git (https://github.com/RadeonOpenCompute/llvm-project roc-6.3.1 24491 1e0fda770a2079fbd71e4b70974d74f62fd3af10) CMake version: version 3.31.4 Libc version: glibc-2.35 Python version: 3.12.9 (main, Feb 5 2025, 08:49:00) [GCC 11.4.0] (64-bit runtime) Python platform: Linux-5.14.21-150500.55.83_13.0.62-cray_shasta_c-x86_64-with-glibc2.35 Is CUDA available: True CUDA runtime version: Could not collect CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: AMD Instinct MI250X (gfx90a:sramecc+:xnack-) Nvidia driver version: Could not collect cuDNN version: Could not collect HIP runtime version: 6.3.42133 MIOpen runtime version: 3.3.0 Is XNNPACK available: True CPU: Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Address sizes: 48 bits physical, 48 bits virtual Byte Order: Little Endian CPU(s): 128 On-line CPU(s) list: 0-127 Vendor ID: AuthenticAMD Model name: AMD...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: rrent environment ```text Collecting environment information... PyTorch version: 2.7.0a0+git6c0e746 Is debug build: False CUDA used to build PyTorch: N/A ROCM used to build PyTorch: 6.3.42133-1b9c17779 OS: Ubuntu 22.04....
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 7: ensure that world_size (2) is less than than max local gpu count (1) bug;stale ### Your current environment ```text Collecting environment information... PyTorch version: 2.7.0a0+git6c0e746 Is debug build: False CUDA us...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 6: xsaveerptr rdpru wbnoinvd amd_ppin arat npt lbrv svm_lock nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pausefilter pfthreshold avic v_vmsave_vmload vgif v_spec_ctrl umip pku ospke vaes vpclmulqdq rdpid overf...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: information... PyTorch version: 2.7.0a0+git6c0e746 Is debug build: False CUDA used to build PyTorch: N/A ROCM used to build PyTorch: 6.3.42133-1b9c17779 OS: Ubuntu 22.04.5 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubunt...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: 46 [pip3] torchvision==0.21.0+7af6987 [pip3] transformers==4.49.0 [pip3] triton==3.2.0+gite5be006a [conda] Could not collect ROCM Version: 6.3.42133-1b9c17779 Neuron SDK Version: N/A vLLM Version: 0.7.4.dev49+gc0dd5adf6...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
