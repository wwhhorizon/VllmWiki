# vllm-project/vllm#11931: [Bug]: RuntimeError: CUDA error: device-side assert triggered CUDA kernel errors might be asynchronously reported at some other API call, so the stacktrace below might be incorrect.

| 字段 | 值 |
| --- | --- |
| Issue | [#11931](https://github.com/vllm-project/vllm/issues/11931) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 |  |
| Operator 关键词 | attention;cuda;kernel;operator;sampling;triton |
| 症状 | build_error;crash;mismatch |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: RuntimeError: CUDA error: device-side assert triggered CUDA kernel errors might be asynchronously reported at some other API call, so the stacktrace below might be incorrect.

### Issue 正文摘录

### Your current environment ### Model Input Dumps INFO 01-10 21:49:05 model_runner_base.py:120] Writing input of failed execution to /tmp/err_execute_model_input_20250110-214905.pkl... WARNING 01-10 21:49:05 model_runner_base.py:143] Failed to pickle inputs of failed execution: CUDA error: device-side assert triggered WARNING 01-10 21:49:05 model_runner_base.py:143] CUDA kernel errors might be asynchronously reported at some other API call, so the stacktrace below might be incorrect. WARNING 01-10 21:49:05 model_runner_base.py:143] For debugging consider passing CUDA_LAUNCH_BLOCKING=1 WARNING 01-10 21:49:05 model_runner_base.py:143] Compile with `TORCH_USE_CUDA_DSA` to enable device-side assertions. WARNING 01-10 21:49:05 model_runner_base.py:143] ERROR 01-10 21:49:05 engine.py:366] Error in model execution: CUDA error: device-side assert triggered ERROR 01-10 21:49:05 engine.py:366] CUDA kernel errors might be asynchronously reported at some other API call, so the stacktrace below might be incorrect. Process SpawnProcess-1: ERROR 01-10 21:49:05 engine.py:366] For debugging consider passing CUDA_LAUNCH_BLOCKING=1 ERROR 01-10 21:49:05 engine.py:366] Compile with `TORCH_USE_CUDA_DS...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: CUDA_LAUNCH_BLOCKING=1 WARNING 01-10 21:49:05 model_runner_base.py:143] Compile with `TORCH_USE_CUDA_DSA` to enable device-side assertions. WARNING 01-10 21:49:05 model_runner_base.py:143] ERROR 01-10 21:49:05 engine.py...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: RuntimeError: CUDA error: device-side assert triggered CUDA kernel errors might be asynchronously reported at some other API call, so the stacktrace below might be incorrect. bug ### Your current environment ###...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: e.py:366] File "/usr/local/lib/python3.10/dist-packages/vllm/attention/backends/flash_attn.py", line 736, in forward ERROR 01-10 21:49:05 engine.py:366] flash_attn_varlen_func( ERROR 01-10 21:49:05 engine.py:366] File "...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: :05 model_runner_base.py:143] For debugging consider passing CUDA_LAUNCH_BLOCKING=1 WARNING 01-10 21:49:05 model_runner_base.py:143] Compile with `TORCH_USE_CUDA_DSA` to enable device-side assertions. WARNING 01-10 21:4...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: trace below might be incorrect. bug ### Your current environment ### Model Input Dumps INFO 01-10 21:49:05 model_runner_base.py:120] Writing input of failed execution to /tmp/err_execute_model_input_20250110-214905.pkl....

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
