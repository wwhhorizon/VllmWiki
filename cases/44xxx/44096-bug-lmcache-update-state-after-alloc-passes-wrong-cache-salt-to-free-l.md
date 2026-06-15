# vllm-project/vllm#44096: [Bug]:  [LMCache] `update_state_after_alloc` passes wrong `cache_salt` to `free_lookup_locks`, leaking server read locks in multi-tenant deployments

| 字段 | 值 |
| --- | --- |
| Issue | [#44096](https://github.com/vllm-project/vllm/issues/44096) |
| 状态 | open |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]:  [LMCache] `update_state_after_alloc` passes wrong `cache_salt` to `free_lookup_locks`, leaking server read locks in multi-tenant deployments

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug In `vllm/distributed/kv_transfer/kv_connector/v1/lmcache_mp_connector.py`: `free_lookup_locks` in `update_state_after_alloc` omits `cache_salt`, so it defaults to "". The lookup was submitted with `cache_salt= `, producing a mismatched ObjectKey — the server cannot find the lock to release, so matched KV chunks remain locked until TTL expiry and cannot be evicted. ```python # update_state_after_alloc — missing cache_salt self.scheduler_adapter.free_lookup_locks( token_ids=list(tracker.all_token_ids), start=0, end=free_end, request_id=request.request_id, # cache_salt missing — defaults to "" ) ``` **Trigger condition** Any request with `cache_salt != ""` where `needs_retrieve() == False` (vLLM already computed all LMCache-cached blocks). **Reproduction** ```python from unittest.mock import MagicMock from lmcache.integration.vllm.lmcache_mp_connector import LMCacheMPConnector, LMCacheMPRequestTracker connector = object.__new__(LMCacheMPConnector) connector.vllm_block_size = 16 connector.scheduler_adapter = MagicMock() req = MagicMock() req.request_id = "req-1" req.all_token_ids = list(range(32)) req.block_hashes = [] req.cache_salt...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: so it defaults to "". The lookup was submitted with `cache_salt= `, producing a mismatched ObjectKey — the server cannot find the lock to release, so matched KV chunks remain locked until TTL expiry and cannot be evicte...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: aults to "". The lookup was submitted with `cache_salt= `, producing a mismatched ObjectKey — the server cannot find the lock to release, so matched KV chunks remain locked until TTL expiry and cannot be evicted. ```pyt...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: tion** Any request with `cache_salt != ""` where `needs_retrieve() == False` (vLLM already computed all LMCache-cached blocks). **Reproduction** ```python from unittest.mock import MagicMock from lmcache.integration.vll...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: evicted. ```python # update_state_after_alloc — missing cache_salt self.scheduler_adapter.free_lookup_locks( token_ids=list(tracker.all_token_ids), start=0, end=free_end, request_id=request.request_id, # cache_salt miss...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: buted_parallel;frontend_api;hardware_porting;model_support cuda;operator;triton build_error;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
