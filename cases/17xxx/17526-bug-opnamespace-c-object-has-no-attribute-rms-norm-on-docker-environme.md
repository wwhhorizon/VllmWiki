# vllm-project/vllm#17526: [Bug]: '_OpNamespace' '_C' object has no attribute 'rms_norm' on docker environment

| 字段 | 值 |
| --- | --- |
| Issue | [#17526](https://github.com/vllm-project/vllm/issues/17526) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | activation_norm;attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;import_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: '_OpNamespace' '_C' object has no attribute 'rms_norm' on docker environment

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I installed the new commit 88ad9ec6b23b79c358ce279b02a67e7c96e2c8b9 on MI300x. This occurs for any model. I've seen the issue has been raised couple of times last year. And the solution was to do a fresh install on vLLM. In any case I removed all of the docker cache and tried again, that didn't workout. ``` # vllm serve meta-llama/Llama-3.1-8B-Instruct --download-dir /app/data/models INFO 05-01 10:06:16 [__init__.py:239] Automatically detected platform rocm. WARNING 05-01 10:06:16 [rocm.py:29] Failed to import from vllm._C with ImportError('/usr/local/lib/python3.12/dist-packages/vllm/_C.abi3.so: undefined symbol: _Z18cutlass_mla_decodeRKN2at6TensorES2_S2_S2_S2_S2_d') WARNING 05-01 10:06:16 [_custom_ops.py:21] Failed to import from vllm._C with ImportError('/usr/local/lib/python3.12/dist-packages/vllm/_C.abi3.so: undefined symbol: _Z18cutlass_mla_decodeRKN2at6TensorES2_S2_S2_S2_S2_d') INFO 05-01 10:06:25 [api_server.py:1043] vLLM API server version 0.8.5.dev331+g88ad9ec6b.d20250430 INFO 05-01 10:06:25 [api_server.py:1044] args: Namespace(subparser='serve', model_tag='meta-llama/Llama-3.1-8B-Instruct', config='', host=None, port=8...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: [Bug]: '_OpNamespace' '_C' object has no attribute 'rms_norm' on docker environment bug;stale ### Your current environment ### 🐛 Describe the bug I installed the new commit 88ad9ec6b23b79c358ce279b02a67e7c96e2c8b9 on MI...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: space' '_C' object has no attribute 'rms_norm' on docker environment bug;stale ### Your current environment ### 🐛 Describe the bug I installed the new commit 88ad9ec6b23b79c358ce279b02a67e7c96e2c8b9 on MI300x. This occu...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: I installed the new commit 88ad9ec6b23b79c358ce279b02a67e7c96e2c8b9 on MI300x. This occurs for any model. I've seen the issue has been raised couple of times last year. And the solution was to do a fresh install on vLLM...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: 88ad9ec6b23b79c358ce279b02a67e7c96e2c8b9 on MI300x. This occurs for any model. I've seen the issue has been raised couple of times last year. And the solution was to do a fresh install on vLLM. In any case I removed all...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: ocal/lib/python3.12/dist-packages/vllm/_C.abi3.so: undefined symbol: _Z18cutlass_mla_decodeRKN2at6TensorES2_S2_S2_S2_S2_d') WARNING 05-01 10:06:16 [_custom_ops.py:21] Failed to import from vllm._C with ImportError('/usr...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
