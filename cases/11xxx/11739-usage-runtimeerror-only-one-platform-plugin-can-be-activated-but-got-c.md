# vllm-project/vllm#11739: [Usage]: RuntimeError: Only one platform plugin can be activated, but got: ['cuda', 'cpu']

| 字段 | 值 |
| --- | --- |
| Issue | [#11739](https://github.com/vllm-project/vllm/issues/11739) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
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

> [Usage]: RuntimeError: Only one platform plugin can be activated, but got: ['cuda', 'cpu']

### Issue 正文摘录

### Your current environment ```text Collecting environment information... PyTorch version: 2.5.1+cpu Is debug build: False CUDA used to build PyTorch: Could not collect ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.5 LTS (x86_64) GCC version: (Ubuntu 12.3.0-1ubuntu1~22.04) 12.3.0 Clang version: Could not collect CMake version: version 3.30.3 Libc version: glibc-2.35 Python version: 3.10.16 (main, Dec 11 2024, 16:24:50) [GCC 11.2.0] (64-bit runtime) Python platform: Linux-6.8.0-49-generic-x86_64-with-glibc2.35 Is CUDA available: False CUDA runtime version: 12.4.99 CUDA_MODULE_LOADING set to: N/A GPU models and configuration: GPU 0: NVIDIA GeForce RTX 3060 Nvidia driver version: 535.183.01 cuDNN version: Could not collect HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Address sizes: 48 bits physical, 48 bits virtual Byte Order: Little Endian CPU(s): 12 On-line CPU(s) list: 0-11 Vendor ID: AuthenticAMD Model name: AMD Ryzen 5 7600 6-Core Processor CPU family: 25 Model: 97 Thread(s) per core: 2 Core(s) per socket: 6 Socket(s): 1 Stepping: 2 CPU max MHz: 5170.0000 CPU min MHz: 400.0000 BogoMIP...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 10: rrent environment ```text Collecting environment information... PyTorch version: 2.5.1+cpu Is debug build: False CUDA used to build PyTorch: Could not collect ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.5 LTS (x86_...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: ge]: RuntimeError: Only one platform plugin can be activated, but got: ['cuda', 'cpu'] usage ### Your current environment ```text Collecting environment information... PyTorch version: 2.5.1+cpu Is debug build: False CU...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: u'] usage ### Your current environment ```text Collecting environment information... PyTorch version: 2.5.1+cpu Is debug build: False CUDA used to build PyTorch: Could not collect ROCM used to build PyTorch: N/A OS: Ubu...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: d cppc arat npt lbrv svm_lock nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pausefilter pfthreshold avic v_vmsave_vmload vgif x2avic v_spec_ctrl vnmi avx512vbmi umip pku ospke avx512_vbmi2 gfni vaes vpclmulqd...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: aves cqm_llc cqm_occup_llc cqm_mbm_total cqm_mbm_local user_shstk avx512_bf16 clzero irperf xsaveerptr rdpru wbnoinvd cppc arat npt lbrv svm_lock nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pausefilter pfth...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
