# vllm-project/vllm#8710: [Installation]: vllm CPU mode build failed

| 字段 | 值 |
| --- | --- |
| Issue | [#8710](https://github.com/vllm-project/vllm/issues/8710) |
| 状态 | closed |
| 标签 | installation |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;hardware_porting;model_support;moe;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;import_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Installation]: vllm CPU mode build failed

### Issue 正文摘录

### Your current environment ```text Collecting environment information... WARNING 09-22 20:25:14 _custom_ops.py:18] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'") INFO 09-22 20:25:14 importing.py:10] Triton not installed; certain GPU-related functions will not be available. PyTorch version: 2.4.0+cpu Is debug build: False CUDA used to build PyTorch: None ROCM used to build PyTorch: N/A OS: EndeavourOS Linux (x86_64) GCC version: (GCC) 14.2.1 20240910 Clang version: 18.1.8 CMake version: version 3.30.3 Libc version: glibc-2.40 Python version: 3.12.6 (main, Sep 8 2024, 13:18:56) [GCC 14.2.1 20240805] (64-bit runtime) Python platform: Linux-6.10.10-zen1-1-zen-x86_64-with-glibc2.40 Is CUDA available: False CUDA runtime version: No CUDA CUDA_MODULE_LOADING set to: N/A GPU models and configuration: No CUDA Nvidia driver version: No CUDA cuDNN version: No CUDA HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Address sizes: 43 bits physical, 48 bits virtual Byte Order: Little Endian CPU(s): 16 On-line CPU(s) list: 0-15 Vendor ID: AuthenticAMD Model name: AMD Ryzen...

## 现有链接修复摘要

#8722 [BUGFIX]: fix CPU backend build | #8723 [Bugfix] Fix CPU CMake build

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 11: [Installation]: vllm CPU mode build failed installation ### Your current environment ```text Collecting environment information... WARNING 09-22 20:25:14 _custom_ops.py:18] Failed to import from vllm._C with ModuleNotFou
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: will not be available. PyTorch version: 2.4.0+cpu Is debug build: False CUDA used to build PyTorch: None ROCM used to build PyTorch: N/A OS: EndeavourOS Linux (x86_64) GCC version: (GCC) 14.2.1 20240910 Clang version: 1...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: tallation ### Your current environment ```text Collecting environment information... WARNING 09-22 20:25:14 _custom_ops.py:18] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'") INFO 09-...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: ro irperf xsaveerptr rdpru wbnoinvd arat npt lbrv svm_lock nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pausefilter pfthreshold avic v_vmsave_vmload vgif v_spec_ctrl umip rdpid overflow_recov succor smca sev...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: noinvd arat npt lbrv svm_lock nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pausefilter pfthreshold avic v_vmsave_vmload vgif v_spec_ctrl umip rdpid overflow_recov succor smca sev sev_es Virtualization: AMD-V...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#8722](https://github.com/vllm-project/vllm/pull/8722) | closes_keyword | 0.95 | [BUGFIX]: fix CPU backend build | Fixes: #8710 **BEFORE SUBMITTING, PLEASE READ THE CHECKLIST BELOW AND FILL IN THE DESCRIPTION ABOVE** --- <details> <!-- inside this <details> section, markdown renderin |
| [#8723](https://github.com/vllm-project/vllm/pull/8723) | closes_keyword | 0.95 | [Bugfix] Fix CPU CMake build | FIX #8710 (*link existing issues this PR will resolve*) This PR replaces #8722. **BEFORE SUBMITTING, PLEASE READ THE CHECKLIST BELOW AND FILL IN THE DESCRIPTION ABOVE** -- |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
