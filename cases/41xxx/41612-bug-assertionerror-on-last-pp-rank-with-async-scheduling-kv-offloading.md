# vllm-project/vllm#41612: [Bug]: AssertionError on last PP rank with async scheduling + KV offloading

| 字段 | 值 |
| --- | --- |
| Issue | [#41612](https://github.com/vllm-project/vllm/issues/41612) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: AssertionError on last PP rank with async scheduling + KV offloading

### Issue 正文摘录

### Your current environment ============================== System Info ============================== OS : Ubuntu 22.04.5 LTS (x86_64) GCC version : (Ubuntu 11.4.0-1ubuntu1~22.04.3) 11.4.0 Clang version : Could not collect CMake version : Could not collect Libc version : glibc-2.35 ============================== PyTorch Info ============================== PyTorch version : 2.11.0+cu130 Is debug build : False CUDA used to build PyTorch : 13.0 ROCM used to build PyTorch : N/A XPU used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.12.13 (main, May 3 2026, 03:30:16) [GCC 11.4.0] (64-bit runtime) Python platform : Linux-6.19.9-arch1-1-x86_64-with-glibc2.35 ============================== CUDA / GPU Info ============================== Is CUDA available : True CUDA runtime version : 13.0.88 CUDA_MODULE_LOADING set to : GPU models and configuration : GPU 0: NVIDIA GeForce RTX 3060 GPU 1: NVIDIA GeForce RTX 3060 GPU 2: NVIDIA GeForce RTX 3060 Nvidia driver version : 595.58.03 cuDNN version : Could not collect HIP runtime version : N/A MIOpen runtime version : N/A Is XNNPACK available : True =======================...

## 现有链接修复摘要

#32618 [Feature] Fully support for async scheduling + PP, 30.8% E2E throughput improvement, 31.8% TPOT improvement

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: ========= OS : Ubuntu 22.04.5 LTS (x86_64) GCC version : (Ubuntu 11.4.0-1ubuntu1~22.04.3) 11.4.0 Clang version : Could not collect CMake version : Could not collect Libc version : glibc-2.35 ============
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: version : 2.11.0+cu130 Is debug build : False CUDA used to build PyTorch : 13.0 ROCM used to build PyTorch : N/A XPU used to build PyTorch : N/A ============================== Python Environment ========================...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: eerptr arat npt lbrv svm_lock nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pausefilter pfthreshold avic v_vmsave_vmload vgif overflow_recov succor smca sev sev_es Virtualization: AMD-V L1d cache: 1 MiB (32 i...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: pt xsavec xgetbv1 clzero xsaveerptr arat npt lbrv svm_lock nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pausefilter pfthreshold avic v_vmsave_vmload vgif overflow_recov succor smca sev sev_es Virtualization:...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: k: self._pp_receive_prev_sampled_token_ids_to_input_batch() ``` ### Regression context | Version | Date | Change | Impact | |---------|------|--------|--------| | v0.13.0 | 2025-12-19 | Before async scheduling default |...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#32618](https://github.com/vllm-project/vllm/pull/32618) | mentioned | 0.45 | [Feature] Fully support for async scheduling + PP, 30.8% E2E throughput improvement, 31.8% TPOT improvement | ally exclusive at this point) \| \| **v0.15.0** \| **2026-01-29** \| **pr #32618: async scheduling + pp support** \| **bug introduced** -- `assert not is_last_rank` reachable on last r… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
