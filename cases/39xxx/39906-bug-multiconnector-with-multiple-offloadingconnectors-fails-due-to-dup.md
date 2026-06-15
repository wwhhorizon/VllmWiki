# vllm-project/vllm#39906: [Bug]: MultiConnector with multiple OffloadingConnectors fails due to duplicate Prometheus metrics registration

| 字段 | 值 |
| --- | --- |
| Issue | [#39906](https://github.com/vllm-project/vllm/issues/39906) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;distributed_parallel;frontend_api;model_support |
| 子分类 | install |
| Operator 关键词 | cuda |
| 症状 | crash |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: MultiConnector with multiple OffloadingConnectors fails due to duplicate Prometheus metrics registration

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When using `MultiConnector` with **two `OffloadingConnector` instances** (one for CPU offloading, one for shared storage offloading), the server crashes on startup with a duplicate Prometheus metrics registration error. **Configuration:** ```python --kv-transfer-config '{ "kv_connector":"MultiConnector", "kv_role":"kv_both", "kv_connector_extra_config": { "connectors": [ { "kv_connector": "OffloadingConnector", "kv_role": "kv_both", "kv_connector_extra_config": { "cpu_bytes_to_use": 64424509440 } }, { "kv_connector": "OffloadingConnector", "kv_role": "kv_both", "kv_connector_extra_config": { "spec_name": "SharedStorageOffloadingSpec", "shared_storage_path": "/mnt/files-storage/", "block_size": 256, "threads_per_gpu": 64, "spec_module_path": "llmd_fs_backend.spec" } } ] } }' ``` **Error:** ``` (APIServer pid=1) ValueError: Duplicated timeseries in CollectorRegistry: {'vllm:kv_offload_total_bytes_created', 'vllm:kv_offload_total_bytes', 'vllm:kv_offload_total_bytes_total'} ``` **Root cause analysis:** `MultiConnector.build_prom_metrics()` iterates over all sub-connectors and calls each one's `build_prom_metrics()`. When two sub-con...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: fload_total_bytes_total'} ``` **Root cause analysis:** `MultiConnector.build_prom_metrics()` iterates over all sub-connectors and calls each one's `build_prom_metrics()`. When two sub-connectors are both `OffloadingConn...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: 515 ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: [Bug]: MultiConnector with multiple OffloadingConnectors fails due to duplicate Prometheus metrics registration ### Your current environment ### 🐛 Describe the bug When using `MultiConnector` with **two `OffloadingConne...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: es on startup with a duplicate Prometheus metrics registration error. **Configuration:** ```python --kv-transfer-config '{ "kv_connector":"MultiConnector", "kv_role":"kv_both", "kv_connector_extra_config": { "connectors...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: "threads_per_gpu": 64, "spec_module_path": "llmd_fs_backend.spec" } } ] } }' ``` **Error:** ``` (APIServer pid=1) ValueError: Duplicated timeseries in CollectorRegistry: {'vllm:kv_offload_total_bytes_created', 'vllm:kv_...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
