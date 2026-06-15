# vllm-project/vllm#34573: [Installation/Runtime]: Linux ROCM7 /  RuntimeError: No HIP GPUs are available

| 字段 | 值 |
| --- | --- |
| Issue | [#34573](https://github.com/vllm-project/vllm/issues/34573) |
| 状态 | closed |
| 标签 | installation;rocm;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;kernel;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Installation/Runtime]: Linux ROCM7 /  RuntimeError: No HIP GPUs are available

### Issue 正文摘录

### Your current environment AMD Dependency Hell continues - ```text Collecting environment information... PyTorch version: 2.9.0a0+git1c57644 Is debug build: False CUDA used to build PyTorch: N/A ROCM used to build PyTorch: 7.0.51831-a3e329ad8 OS: Ubuntu 22.04.5 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04.2) 11.4.0 Clang version: 20.0.0git (https://github.com/RadeonOpenCompute/llvm-project roc-7.0.0 25314 f4087f6b428f0e6f575ebac8a8a724dab123d06e) CMake version: version 3.31.10 Libc version: glibc-2.35 Python version: 3.12.12 (main, Oct 10 2025, 08:52:57) [GCC 11.4.0] (64-bit runtime) Python platform: Linux-6.18.7-061807-generic-x86_64-with-glibc2.35 Is CUDA available: False CUDA runtime version: No CUDA CUDA_MODULE_LOADING set to: N/A GPU models and configuration: No CUDA Nvidia driver version: No CUDA cuDNN version: No CUDA HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Address sizes: 48 bits physical, 48 bits virtual Byte Order: Little Endian CPU(s): 32 On-line CPU(s) list: 0-31 Vendor ID: AuthenticAMD Model name: AMD RYZEN AI MAX+ PRO 395 w/ Radeon 8060S CPU family: 26 Model:...

## 现有链接修复摘要

#41585 [ROCm] Fix platform detection failures in unprivileged containers

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: [Installation/Runtime]: Linux ROCM7 / RuntimeError: No HIP GPUs are available installation;rocm;stale ### Your current environment AMD Dependency Hell continues - ```text Collecting environment information... PyTorch
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: [Installation/Runtime]: Linux ROCM7 / RuntimeError: No HIP GPUs are available installation;rocm;stale ### Your current environment AMD Dependency Hell continues - ```text Collecting environment information... PyTorch ve...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: ment AMD Dependency Hell continues - ```text Collecting environment information... PyTorch version: 2.9.0a0+git1c57644 Is debug build: False CUDA used to build PyTorch: N/A ROCM used to build PyTorch: 7.0.51831-a3e329ad...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: Linux ROCM7 / RuntimeError: No HIP GPUs are available installation;rocm;stale ### Your current environment AMD Dependency Hell continues - ```text Collecting environment information... PyTorch version: 2.9.0a0+git1c5764...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: llc cqm_occup_llc cqm_mbm_total cqm_mbm_local user_shstk avx_vnni avx512_bf16 clzero irperf xsaveerptr rdpru wbnoinvd cppc arat npt lbrv svm_lock nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pausefilter pfth...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#41585](https://github.com/vllm-project/vllm/pull/41585) | mentioned | 0.6 | [ROCm] Fix platform detection failures in unprivileged containers | g is emitted when amdsmi fails Related issues: #40081, #24576, #34573, #39378 🤖 Generated with [Claude Code](https://claude.ai/code) |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
