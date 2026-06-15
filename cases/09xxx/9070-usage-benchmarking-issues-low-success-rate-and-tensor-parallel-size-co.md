# vllm-project/vllm#9070: [Usage]: Benchmarking Issues: Low Success Rate and Tensor Parallel Size Constraints on 8x AMD MI300x GPUs

| 字段 | 值 |
| --- | --- |
| Issue | [#9070](https://github.com/vllm-project/vllm/issues/9070) |
| 状态 | closed |
| 标签 | rocm;usage;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;operator;sampling;triton |
| 症状 | build_error;import_error;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: Benchmarking Issues: Low Success Rate and Tensor Parallel Size Constraints on 8x AMD MI300x GPUs

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` Collecting environment information... WARNING 10-04 10:39:09 rocm.py:13] `fork` method is not supported by ROCm. VLLM_WORKER_MULTIPROC_METHOD is overridden to `spawn` instead. WARNING 10-04 10:39:09 _custom_ops.py:18] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'") WARNING 10-04 10:39:09 _custom_ops.py:18] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'") PyTorch version: 2.4.1+rocm6.1 Is debug build: False CUDA used to build PyTorch: N/A ROCM used to build PyTorch: 6.1.40091-a8dbc0c19 OS: Ubuntu 22.04.4 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version: 17.0.0 (https://github.com/RadeonOpenCompute/llvm-project roc-6.1.0 24103 7db7f5e49612030319346f900c08f474b1f9023a) CMake version: version 3.26.4 Libc version: glibc-2.35 Python version: 3.10.14 (main, Mar 21 2024, 16:24:04) [GCC 11.2.0] (64-bit runtime) Python platform: Linux-6.8.0-45-generic-x86_64-with-glibc2.35 Is CUDA available: True CUDA runtime version: Could not collect CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: AMD Instinct MI300X (...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: to `spawn` instead. WARNING 10-04 10:39:09 _custom_ops.py:18] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'") WARNING 10-04 10:39:09 _custom_ops.py:18] Failed to import from vllm._C w...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 7: Issues: Low Success Rate and Tensor Parallel Size Constraints on 8x AMD MI300x GPUs rocm;usage;stale ### Your current environment ```text The output of `python collect_env.py` Collecting environment information... WARNI...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: ```text The output of `python collect_env.py` Collecting environment information... WARNING 10-04 10:39:09 rocm.py:13] `fork` method is not supported by ROCm. VLLM_WORKER_MULTIPROC_METHOD is overridden to `spawn` instea...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 5: [Usage]: Benchmarking Issues: Low Success Rate and Tensor Parallel Size Constraints on 8x AMD MI300x GPUs rocm;usage;stale ### Your current environment ```text The output of `python collect_env.py` Collecting environmen...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: cqm_mbm_total cqm_mbm_local split_lock_detect user_shstk avx_vnni avx512_bf16 wbnoinvd dtherm ida arat pln pts vnmi avx512vbmi umip pku ospke waitpkg avx512_vbmi2 gfni vaes vpclmulqdq avx512_vnni avx512_bitalg tme avx51...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
