# vllm-project/vllm#42625: [Bug]: LMCache cache miss

| 字段 | 值 |
| --- | --- |
| Issue | [#42625](https://github.com/vllm-project/vllm/issues/42625) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: LMCache cache miss

### Issue 正文摘录

### Your current environment vllm 0.19.1 lmcache 0.4.3 ### 🐛 Describe the bug #### LMCache Server ``` export LMCACHE_USE_EXPERIMENTAL=True export LMCACHE_CHUNK_SIZE=256 export LMCACHE_LOCAL_CPU=False export LMCACHE_MAX_LOCAL_CPU_SIZE=5.0 export LMCACHE_REMOTE_URL=lm://localhost:8100 export LMCACHE_REMOTE_SERDE=naive python3 -m lmcache.v1.server localhost 8100 [2026-05-14 09:44:44,209] LMCache INFO: Initializing cpu-only cache server (__init__.py:14:lmcache.v1.server.storage_backend) [2026-05-14 09:44:44,209] LMCache INFO: Server started at localhost:8100 (__main__.py:138:__main__) [2026-05-14 09:45:28,660] LMCache INFO: Connected by ('127.0.0.1', 41688) (__main__.py:142:__main__) [2026-05-14 09:45:33,342] LMCache INFO: Connected by ('127.0.0.1', 41698) (__main__.py:142:__main__) ``` #### Vllm Server1 ``` export LMCACHE_USE_EXPERIMENTAL=True export LMCACHE_CHUNK_SIZE=256 export LMCACHE_LOCAL_CPU=False export LMCACHE_MAX_LOCAL_CPU_SIZE=5.0 export LMCACHE_REMOTE_URL=lm://localhost:8100 export LMCACHE_REMOTE_SERDE=naive vllm serve /models --max-model-len 1024 --gpu-memory-utilization 0.4 --kv-transfer-config '("kv_connector":"LMCacheConnectorV1","kv_role":"kv_both")' --port 8000 (APIS...

## 候选优化模式

- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 3: tils) (EngineCore pid=10974) [2026-05-14 09:45:41,324] LMCache INFO: GPU KV Cache Dimensions: [28][2, 1009, 16, 8, 128] (utils.py:378:lmcache.v1.gpu_connector.utils) (EngineCore pid=10974) [2026-05-14 09:45:41,324] LMCa...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: E_URL=lm://localhost:8100 export LMCACHE_REMOTE_SERDE=naive vllm serve /models --max-model-len 1024 --gpu-memory-utilization 0.4 --kv-transfer-config '("kv_connector":"LMCacheConnectorV1","kv_role":"kv_both")' --port 80...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: ializing cpu-only cache server (__init__.py:14:lmcache.v1.server.storage_backend) [2026-05-14 09:44:44,209] LMCache INFO: Server started at localhost:8100 (__main__.py:138:__main__) [2026-05-14 09:45:28,660] LMCache INF...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: [Bug]: LMCache cache miss bug ### Your current environment vllm 0.19.1 lmcache 0.4.3 ### 🐛 Describe the bug #### LMCache Server ``` export LMCACHE_USE_EXPERIMENTAL=True export LMCACHE_CHUNK_SIZE=256 export LMCACHE_LOCAL...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: PERIMENTAL=True export LMCACHE_CHUNK_SIZE=256 export LMCACHE_LOCAL_CPU=False export LMCACHE_MAX_LOCAL_CPU_SIZE=5.0 export LMCACHE_REMOTE_URL=lm://localhost:8100 export LMCACHE_REMOTE_SERDE=naive python3 -m lmcache.v1.se...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
