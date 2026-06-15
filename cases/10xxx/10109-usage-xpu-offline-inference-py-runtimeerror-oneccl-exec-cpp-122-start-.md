# vllm-project/vllm#10109: [Usage]: [XPU] offline_inference.py - RuntimeError: oneCCL: exec.cpp:122 start_workers: EXCEPTION: failed to start worker # 0 

| 字段 | 值 |
| --- | --- |
| Issue | [#10109](https://github.com/vllm-project/vllm/issues/10109) |
| 状态 | closed |
| 标签 | usage;unstale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm;quantization;speculative_decoding |
| 子分类 | env_compat |
| Operator 关键词 | attention;cuda;operator;quantization;triton |
| 症状 | build_error;crash;import_error |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Usage]: [XPU] offline_inference.py - RuntimeError: oneCCL: exec.cpp:122 start_workers: EXCEPTION: failed to start worker # 0 

### Issue 正文摘录

### Your current environment ```text Collecting environment information... [WARNING] Failed to create Level Zero tracer: 2013265921 WARNING 11-07 06:41:13 _logger.py:68] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'") INFO 11-07 06:41:13 importing.py:15] Triton not installed or not compatible; certain GPU-related functions will not be available. PyTorch version: 2.3.1+cxx11.abi Is debug build: False CUDA used to build PyTorch: None ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.2 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version: Could not collect CMake version: version 3.30.5 Libc version: glibc-2.35 Python version: 3.10.15 | packaged by conda-forge | (main, Oct 16 2024, 01:24:24) [GCC 13.3.0] (64-bit runtime) Python platform: Linux-5.15.0-73-generic-x86_64-with-glibc2.35 Is CUDA available: False CUDA runtime version: No CUDA CUDA_MODULE_LOADING set to: N/A GPU models and configuration: No CUDA Nvidia driver version: No CUDA cuDNN version: No CUDA HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Address sizes: 46 bits physical,...

## 现有链接修复摘要

#4 Use FlashAttention for `multi_query_kv_attention` | #6 Automatically configure KV cache size | #7 Support beam search & parallel generation

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: Zero tracer: 2013265921 WARNING 11-07 06:41:13 _logger.py:68] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'") INFO 11-07 06:41:13 importing.py:15] Triton not installed or not compatib...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: e;unstale ### Your current environment ```text Collecting environment information... [WARNING] Failed to create Level Zero tracer: 2013265921 WARNING 11-07 06:41:13 _logger.py:68] Failed to import from vllm._C with Modu...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: not be available. PyTorch version: 2.3.1+cxx11.abi Is debug build: False CUDA used to build PyTorch: None ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.2 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4....
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: dError("No module named 'vllm._C'") INFO 11-07 06:41:13 importing.py:15] Triton not installed or not compatible; certain GPU-related functions will not be available. PyTorch version: 2.3.1+cxx11.abi Is debug build: Fals...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: _occup_llc cqm_mbm_total cqm_mbm_local split_lock_detect avx_vnni avx512_bf16 wbnoinvd dtherm ida arat pln pts avx512vbmi umip pku ospke waitpkg avx512_vbmi2 gfni vaes vpclmulqdq avx512_vnni avx512_bitalg tme avx512_vpo...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#4](https://github.com/vllm-project/vllm/pull/4) | mentioned | 0.45 | Use FlashAttention for `multi_query_kv_attention` | 1100 +-- device #3: intel(r) data center gpu max 1100 +-- device #4: intel(r) data center gpu max 1100 +-- device #5: intel(r) data center gpu max 1100 +-- device #6: intel( |
| [#6](https://github.com/vllm-project/vllm/pull/6) | mentioned | 0.45 | Automatically configure KV cache size | 1100 +-- device #5: intel(r) data center gpu max 1100 +-- device #6: intel(r) data center gpu max 1100 `-- device #7: intel(r) data center gpu max 1100 ``` ### how would y |
| [#7](https://github.com/vllm-project/vllm/pull/7) | mentioned | 0.45 | Support beam search & parallel generation | 1100 +-- device #6: intel(r) data center gpu max 1100 `-- device #7: intel(r) data center gpu max 1100 ``` ### how would you like to use vllm while i'm running [examples/of |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
