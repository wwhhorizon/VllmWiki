# vllm-project/vllm#42912: [Bug]: vllm-glm5.1 with llmcache with glm-5-fp8 failed

| 字段 | 值 |
| --- | --- |
| Issue | [#42912](https://github.com/vllm-project/vllm/issues/42912) |
| 状态 | open |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: vllm-glm5.1 with llmcache with glm-5-fp8 failed

### Issue 正文摘录

### Your current environment ubuntu22.04 vllm/vllm-openai:glm51 ### 🐛 Describe the bug [Bug]: vllm-glm5.1 with llmcache with glm-5-fp8 failed [31;20m[2026-05-16 13:54:01,727] LMCache ERROR:[0m LMCacheEngine marked as init failed: Traceback (most recent call last): (Worker_TP0 pid=120) File "/usr/local/lib/python3.12/dist-packages/lmcache/v1/manager.py", line 208, in post_init (Worker_TP0 pid=120) self._lmcache_engine.post_init(async_lookup_server=async_lookup_server) (Worker_TP0 pid=120) File "/usr/local/lib/python3.12/dist-packages/lmcache/v1/cache_engine.py", line 301, in post_init (Worker_TP0 pid=120) self.storage_manager = StorageManager( (Worker_TP0 pid=120) ^^^^^^^^^^^^^^^ (Worker_TP0 pid=120) File "/usr/local/lib/python3.12/dist-packages/lmcache/v1/storage_backend/storage_manager.py", line 246, in __init__ (Worker_TP0 pid=120) self.create_backends() (Worker_TP0 pid=120) File "/usr/local/lib/python3.12/dist-packages/lmcache/v1/storage_backend/storage_manager.py", line 1224, in create_backends (Worker_TP0 pid=120) new_backends = CreateStorageBackends( (Worker_TP0 pid=120) ^^^^^^^^^^^^^^^^^^^^^^ (Worker_TP0 pid=120) File "/usr/local/lib/python3.12/dist-packages/lmcache/v1/sto...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ^^^^^^^^^^^^^^^^^^^^^^^^^^^ (Worker_TP0 pid=120) RuntimeError: cudaHostAlloc failed: 2 (Worker_TP0 pid=120) [3m(cache_engine.py:277:lmcache.v1.cache_engine)[0m (Worker_TP0 pid=120) [31;20m[2026-05-16 13:54:01,728] LM...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: , in __init__ (Worker_TP0 pid=120) self.initialize_allocator(config, metadata) # type: ignore (Worker_TP0 pid=120) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ (Worker_TP0 pid=120) File "/usr/local/lib/python3.12/dist-pa...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: =120) File "/usr/local/lib/python3.12/dist-packages/lmcache/v1/storage_backend/storage_manager.py", line 246, in __init__ (Worker_TP0 pid=120) self.create_backends() (Worker_TP0 pid=120) File "/usr/local/lib/python3.12/...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: [Bug]: vllm-glm5.1 with llmcache with glm-5-fp8 failed bug ### Your current environment ubuntu22.04 vllm/vllm-openai:glm51 ### 🐛 Describe the bug [Bug]: vllm-glm5.1 with llmcache with glm-5-fp8 failed [31;20m[2026-05-16...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: line 67, in __init__ (Worker_TP0 pid=120) self.initialize_allocator(config, metadata) # type: ignore (Worker_TP0 pid=120) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ (Worker_TP0 pid=120) File "/usr/local/lib/python3.12/...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
