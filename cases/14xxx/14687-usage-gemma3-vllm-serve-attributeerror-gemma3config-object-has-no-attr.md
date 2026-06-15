# vllm-project/vllm#14687: [Usage]: Gemma3 vllm serve AttributeError: 'Gemma3Config' object has no attribute 'vocab_size'

| 字段 | 值 |
| --- | --- |
| Issue | [#14687](https://github.com/vllm-project/vllm/issues/14687) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf;oom |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: Gemma3 vllm serve AttributeError: 'Gemma3Config' object has no attribute 'vocab_size'

### Issue 正文摘录

### Your current environment ```text PyTorch version: 2.5.1+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A OS: Ubuntu 24.04.1 LTS (x86_64) GCC version: (Ubuntu 13.3.0-6ubuntu2~24.04) 13.3.0 Clang version: Could not collect CMake version: Could not collect Libc version: glibc-2.39 Python version: 3.12.3 (main, Feb 4 2025, 14:48:35) [GCC 13.3.0] (64-bit runtime) Python platform: Linux-6.8.0-52-generic-x86_64-with-glibc2.39 Is CUDA available: True CUDA runtime version: 12.0.140 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA GeForce RTX 4090 GPU 1: NVIDIA GeForce RTX 4090 Nvidia driver version: 550.120 cuDNN version: Could not collect HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Address sizes: 48 bits physical, 48 bits virtual Byte Order: Little Endian CPU(s): 32 On-line CPU(s) list: 0-31 Vendor ID: AuthenticAMD Model name: AMD Ryzen 9 7950X 16-Core Processor CPU family: 25 Model: 97 Thread(s) per core: 2 Core(s) per socket: 16 Socket(s): 1 Stepping: 2 CPU(s) scaling MHz: 41% CPU max MHz: 5881.0000 CPU min MHz: 545.0000...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 9: d cppc arat npt lbrv svm_lock nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pausefilter pfthreshold avic v_vmsave_vmload vgif x2avic v_spec_ctrl vnmi avx512vbmi umip pku ospke avx512_vbmi2 gfni vaes vpclmulqd...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: tribute 'vocab_size' usage ### Your current environment ```text PyTorch version: 2.5.1+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A OS: Ubuntu 24.04.1 LTS (x86_64) GCC ver...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 7: environment ```text PyTorch version: 2.5.1+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A OS: Ubuntu 24.04.1 LTS (x86_64) GCC version: (Ubuntu 13.3.0-6ubuntu2~24.04) 13.3.0...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 6: aves cqm_llc cqm_occup_llc cqm_mbm_total cqm_mbm_local user_shstk avx512_bf16 clzero irperf xsaveerptr rdpru wbnoinvd cppc arat npt lbrv svm_lock nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pausefilter pfth...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Usage]: Gemma3 vllm serve AttributeError: 'Gemma3Config' object has no attribute 'vocab_size' usage ### Your current environment ```text PyTorch version: 2.5.1+cu124 Is debug build: False CUDA used to build PyTorch: 12...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
