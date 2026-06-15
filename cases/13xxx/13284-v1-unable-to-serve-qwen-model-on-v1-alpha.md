# vllm-project/vllm#13284: [V1]: Unable to serve Qwen model on V1 alpha.

| 字段 | 值 |
| --- | --- |
| Issue | [#13284](https://github.com/vllm-project/vllm/issues/13284) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 21; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [V1]: Unable to serve Qwen model on V1 alpha.

### Issue 正文摘录

### Your current environment ```text INFO 02-14 01:40:48 __init__.py:190] Automatically detected platform cuda. Collecting environment information... PyTorch version: 2.5.1+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.3 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version: Could not collect CMake version: version 3.31.4 Libc version: glibc-2.35 Python version: 3.12.9 (main, Feb 5 2025, 08:49:00) [GCC 11.4.0] (64-bit runtime) Python platform: Linux-5.15.0-107-generic-x86_64-with-glibc2.35 Is CUDA available: True CUDA runtime version: 12.1.105 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA RTX 6000 Ada Generation Nvidia driver version: 535.171.04 cuDNN version: Could not collect HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Address sizes: 48 bits physical, 48 bits virtual Byte Order: Little Endian CPU(s): 128 On-line CPU(s) list: 0-127 Vendor ID: AuthenticAMD Model name: AMD EPYC 75F3 32-Core Processor CPU family: 25 Model: 1 Thread(s) per core: 2 Core(s) per socket: 32 Socke...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: ly detected platform cuda. Collecting environment information... PyTorch version: 2.5.1+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.3 LTS (x86_64) GCC ve...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 8: [V1]: Unable to serve Qwen model on V1 alpha. bug;stale ### Your current environment ```text INFO 02-14 01:40:48 __init__.py:190] Automatically detected platform cuda. Collecting environment information... PyTorch versi...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 6: xsaveerptr rdpru wbnoinvd amd_ppin arat npt lbrv svm_lock nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pausefilter pfthreshold v_vmsave_vmload vgif v_spec_ctrl umip pku ospke vaes vpclmulqdq rdpid overflow_r...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: ext INFO 02-14 01:40:48 __init__.py:190] Automatically detected platform cuda. Collecting environment information... PyTorch version: 2.5.1+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 5: dio==2.5.1 [pip3] torchvision==0.20.1 [pip3] transformers==4.48.2 [pip3] triton==3.1.0 [conda] Could not collect ROCM Version: Could not collect Neuron SDK Version: N/A vLLM Version: 0.7.2 vLLM Build Flags: CUDA Archs:...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
