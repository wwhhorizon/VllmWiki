# vllm-project/vllm#26452: [Bug]: vLLM + LMCache Version Compatibility Issues Across Multiple Releases

| 字段 | 值 |
| --- | --- |
| Issue | [#26452](https://github.com/vllm-project/vllm/issues/26452) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;crash;mismatch;nan_inf;oom |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vLLM + LMCache Version Compatibility Issues Across Multiple Releases

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug There is a pattern of compatibility issues between vLLM and LMCache across three different version combinations. Each version pair exhibits a different failure mode during initialization when using LMCache's KV transfer functionality for prefill/decode disaggregation. **Affected Version Combinations:** 1. vLLM 0.10.1.1 + LMCache 0.3.3 → pplx_kernels symbol error 2. vLLM 0.10.2 + LMCache 0.3.6 → StorageManager AssertionError 3. vLLM 0.11.0 + LMCache 0.3.7 → Buffer allocation ValueError --- ## Issue 1: vLLM 0.10.1.1 + LMCache 0.3.3 ### Environment - **vLLM version**: 0.10.1.1 - **LMCache version**: 0.3.3 - **PyTorch**: 2.x with CUDA support - **Python**: 3.11 ### Error ``` OSError: /path/to/libpplx_kernels.so: undefined symbol: _ZN3c104cuda9SetDeviceEab ``` ### Description When initializing vLLM with a quantized model using `gptq_marlin` quantization, the deployment fails with an `OSError` indicating an undefined symbol in the pplx-kernels library. The undefined symbol `_ZN3c104cuda9SetDeviceEab` suggests a C++ ABI mismatch, typically occurring when pplx_kernels was compiled against a different PyTorch/CUDA version. --- ## Issue 2:...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: [Bug]: vLLM + LMCache Version Compatibility Issues Across Multiple Releases bug;stale ### Your current environment ### 🐛 Describe the bug There is a pattern of compatibility issues between vLLM and LMCache across three...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: vLLM + LMCache Version Compatibility Issues Across Multiple Releases bug;stale ### Your current environment ### 🐛 Describe the bug There is a pattern of compatibility issues between vLLM and LMCache across three differe...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: version**: 0.10.1.1 - **LMCache version**: 0.3.3 - **PyTorch**: 2.x with CUDA support - **Python**: 3.11 ### Error ``` OSError: /path/to/libpplx_kernels.so: undefined symbol: _ZN3c104cuda9SetDeviceEab ``` ### Descriptio...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: etDeviceEab ``` ### Description When initializing vLLM with a quantized model using `gptq_marlin` quantization, the deployment fails with an `OSError` indicating an undefined symbol in the pplx-kernels library. The unde...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: *Python**: 3.11 ### Error ``` AssertionError File "lmcache/v1/storage_backend/storage_manager.py", line 153, in _get_allocator_backend assert isinstance(allocator_backend, AllocatorBackendInterface) ``` ### Description...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
