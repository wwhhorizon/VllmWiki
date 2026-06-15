# vllm-project/vllm#8788: [Installation]: Installing vLLM on ROCm - Distro:Gentoo

| 字段 | 值 |
| --- | --- |
| Issue | [#8788](https://github.com/vllm-project/vllm/issues/8788) |
| 状态 | closed |
| 标签 | installation;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;import_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Installation]: Installing vLLM on ROCm - Distro:Gentoo

### Issue 正文摘录

### Your current environment ```text Collecting environment information... WARNING 09-25 07:53:02 _custom_ops.py:18] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'") PyTorch version: 2.6.0.dev20240924+rocm6.1 Is debug build: False CUDA used to build PyTorch: N/A ROCM used to build PyTorch: 6.1.40091-a8dbc0c19 OS: Gentoo Linux (x86_64) GCC version: (Gentoo 13.3.1_p20240614 p17) 13.3.1 20240614 Clang version: 18.1.8 CMake version: version 3.30.2 Libc version: glibc-2.39 Python version: 3.11.9 (main, Apr 19 2024, 16:48:06) [GCC 11.2.0] (64-bit runtime) Python platform: Linux-6.6.38-gentoo-gentoo-dist-x86_64-AMD_Ryzen_7_8700G_w-_Radeon_780M_Graphics-with-glibc2.39 Is CUDA available: True CUDA runtime version: Could not collect CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: AMD Radeon Graphics (gfx1103) Nvidia driver version: Could not collect cuDNN version: Could not collect HIP runtime version: 6.1.40091 MIOpen runtime version: 3.1.0 Is XNNPACK available: True CPU: Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Address sizes: 48 bits physical, 48 bits virtual Byte Order: Little Endian CPU(s): 16 On-line CPU(s) list: 0-15 Vendor...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 10: [Installation]: Installing vLLM on ROCm - Distro:Gentoo installation;stale ### Your current environment ```text Collecting environment information... WARNING 09-25 07:53:02 _custom_ops.py:18] Failed to import from vllm._
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: [Installation]: Installing vLLM on ROCm - Distro:Gentoo installation;stale ### Your current environment ```text Collecting environment information... WARNING 09-25 07:53:02 _custom_ops.py:18] Failed to import from vllm....
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: ion;stale ### Your current environment ```text Collecting environment information... WARNING 09-25 07:53:02 _custom_ops.py:18] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'") PyTorch...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Installation]: Installing vLLM on ROCm - Distro:Gentoo installation;stale ### Your current environment ```text Collecting environment information... WARNING 09-25 07:53:02 _custom_ops.py:18] Failed to import from vllm....
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: aves cqm_llc cqm_occup_llc cqm_mbm_total cqm_mbm_local user_shstk avx512_bf16 clzero irperf xsaveerptr rdpru wbnoinvd cppc arat npt lbrv svm_lock nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pausefilter pfth...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
