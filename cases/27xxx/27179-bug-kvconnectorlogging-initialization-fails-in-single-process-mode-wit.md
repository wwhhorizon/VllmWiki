# vllm-project/vllm#27179: [Bug]: KVConnectorLogging initialization fails in single-process mode with LMCache due to has_kv_transfer_group assertion error

| 字段 | 值 |
| --- | --- |
| Issue | [#27179](https://github.com/vllm-project/vllm/issues/27179) |
| 状态 | closed |
| 标签 | bug;stale;kv-connector |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: KVConnectorLogging initialization fails in single-process mode with LMCache due to has_kv_transfer_group assertion error

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I tried running some lmcache examples **in a single process** for debugging with breakpoints. ```shell VLLM_ENABLE_V1_MULTIPROCESSING=0 CUDA_VISIBLE_DEVICES=7 python3 cpu_offload_lmcache.py ``` However, I encountered a KVConnectorLogging initialization failure. ```shell [rank0]: File "/usr/local/lib/python3.12/dist-packages/vllm/v1/metrics/loggers.py", line 65, in __init__ [rank0]: self.kv_transfer_logging = KVConnectorLogging(kv_tranfer_config) [rank0]: ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ [rank0]: File "/usr/local/lib/python3.12/dist-packages/vllm/distributed/kv_transfer/kv_connector/v1/metrics.py", line 54, in __init__ [rank0]: assert not has_kv_transfer_group() [rank0]: ^^^^^^^^^^^^^^^^^^^^^^^^^^^ [rank0]: AssertionError ``` Normally, the worker initializes the **KVConnector** in its own process, preventing this assertion failure. When running in a single process, the worker initializes the **KVConnector** before **KVConnectorLogging**, causing this assertion failure. Currently, I'm working around the issue by commenting out this assertion line. @NickLucche Please help check if there's a better solution ### Before submitting...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. development ci_build;distributed_parallel;frontend_api;hardware_porting;model_support cuda;operator;triton build_error env_dependency Your current environment
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: or debugging with breakpoints. ```shell VLLM_ENABLE_V1_MULTIPROCESSING=0 CUDA_VISIBLE_DEVICES=7 python3 cpu_offload_lmcache.py ``` However, I encountered a KVConnectorLogging initialization failure. ```shell [rank0]: Fi...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: __ [rank0]: self.kv_transfer_logging = KVConnectorLogging(kv_tranfer_config) [rank0]: ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ [rank0]: File "/usr/local/lib/python3.12/dist-packages/vllm/distributed/kv_transfer/kv_connecto...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: buted_parallel;frontend_api;hardware_porting;model_support cuda;operator;triton build_error env_dependency Your current environment
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: hell VLLM_ENABLE_V1_MULTIPROCESSING=0 CUDA_VISIBLE_DEVICES=7 python3 cpu_offload_lmcache.py ``` However, I encountered a KVConnectorLogging initialization failure. ```shell [rank0]: File "/usr/local/lib/python3.12/dist-...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
