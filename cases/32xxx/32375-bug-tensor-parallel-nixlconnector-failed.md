# vllm-project/vllm#32375: [Bug]: Tensor Parallel + NixlConnector failed

| 字段 | 值 |
| --- | --- |
| Issue | [#32375](https://github.com/vllm-project/vllm/issues/32375) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | distributed_parallel;frontend_api;model_support |
| 子分类 | runtime_err |
| Operator 关键词 | cuda |
| 症状 | crash |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Tensor Parallel + NixlConnector failed

### Issue 正文摘录

### Your current environment ``` nixl[13]==0.8.0 vllm==0.14.0rc2.dev30+g50632adc5.cu131 ``` ### 🐛 Describe the bug ```python vllm serve Qwen/Qwen3-0.6B -tp 4 --reasoning-parser deepseek_r1 --served-model-name qwen --kv-transfer-config '{"kv_connector":"NixlConnector","kv_role":"kv_both", "kv_buffer_device":"cuda", "kv_connector_extra_config":{"backends":["UCX"]}}' ``` ``` ... (Worker_TP1 pid=54583) INFO 01-15 03:17:56 [nixl_connector.py:114] NIXL is available (Worker_TP2 pid=54584) INFO 01-15 03:17:56 [nixl_connector.py:114] NIXL is available (Worker_TP1 pid=54583) INFO 01-15 03:17:56 [factory.py:64] Creating v1 connector with name: NixlConnector and engine_id: 42513979-f4de-49e4-bad6-139f71aa2ca0 (Worker_TP3 pid=54585) INFO 01-15 03:17:56 [factory.py:64] Creating v1 connector with name: NixlConnector and engine_id: 42513979-f4de-49e4-bad6-139f71aa2ca0 (Worker_TP3 pid=54585) WARNING 01-15 03:17:56 [base.py:166] Initializing KVConnectorBase_V1. This API is experimental and subject to change in the future as we iterate the design. (Worker_TP1 pid=54583) WARNING 01-15 03:17:56 [base.py:166] Initializing KVConnectorBase_V1. This API is experimental and subject to change in the future...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: oop/__init__.py", line 96, in run (APIServer pid=54435) return __asyncio.run( (APIServer pid=54435) ^^^^^^^^^^^^^^ (APIServer pid=54435) File "/usr/lib/python3.12/asyncio/runners.py", line 194, in run (APIServer pid=544...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: {"kv_connector":"NixlConnector","kv_role":"kv_both", "kv_buffer_device":"cuda", "kv_connector_extra_config":{"backends":["UCX"]}}' ``` ``` ... (Worker_TP1 pid=54583) INFO 01-15 03:17:56 [nixl_connector.py:114] NIXL is a...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: dev30+g50632adc5.cu131 ``` ### 🐛 Describe the bug ```python vllm serve Qwen/Qwen3-0.6B -tp 4 --reasoning-parser deepseek_r1 --served-model-name qwen --kv-transfer-config '{"kv_connector":"NixlConnector","kv_role":"kv_bo...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: ole":"kv_both", "kv_buffer_device":"cuda", "kv_connector_extra_config":{"backends":["UCX"]}}' ``` ``` ... (Worker_TP1 pid=54583) INFO 01-15 03:17:56 [nixl_connector.py:114] NIXL is available (Worker_TP2 pid=54584) INFO...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: EngineCore_DP0 pid=54511) ERROR 01-15 03:18:00 [core.py:936] num_gpu_blocks, num_cpu_blocks, kv_cache_config = self._initialize_kv_caches( (EngineCore_DP0 pid=54511) ERROR 01-15 03:18:00 [core.py:936] ^^^^^^^^^^^^^^^^^^...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
