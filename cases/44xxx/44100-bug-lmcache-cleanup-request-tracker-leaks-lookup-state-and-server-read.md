# vllm-project/vllm#44100: [Bug]: [LMCache] `_cleanup_request_tracker` leaks lookup state and server read locks when request is aborted before allocation

| 字段 | 值 |
| --- | --- |
| Issue | [#44100](https://github.com/vllm-project/vllm/issues/44100) |
| 状态 | open |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;scheduler_memory |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: [LMCache] `_cleanup_request_tracker` leaks lookup state and server read locks when request is aborted before allocation

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug **Problem** When a request is aborted after `get_num_new_matched_tokens` submits a lookup but before `update_state_after_alloc` is called, `_cleanup_request_tracker` is the only cleanup path. It only pops the tracker — it never calls `cleanup_lookup_result` or `free_lookup_locks`. `_pending_lookups` retains the request_id and read locks on matched KV chunks are never released until TTL expiry, blocking eviction. Root cause: `update_state_after_alloc` correctly calls both on the normal path. `_cleanup_request_tracker` calls neither. **Trigger condition** Request submitted a lookup (`maybe_submit_lookup_request` → enters `_pending_lookups`), then aborted before `update_state_after_alloc` — client disconnect, request timeout. **Reproduction** ```python from unittest.mock import MagicMock from vllm.distributed.kv_transfer.kv_connector.v1.lmcache_mp_connector import ( LMCacheMPConnectorUpstream as LMCacheMPConnector, LMCacheMPRequestTracker, ) connector = object.__new__(LMCacheMPConnector) connector.vllm_block_size = 16 connector.scheduler_adapter = MagicMock() connector.scheduler_adapter._pending_lookups = {"req-1"} connector.schedul...

## 现有链接修复摘要

#44129 fix: release LMCache lookup locks on abort

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: onnect, request timeout. **Reproduction** ```python from unittest.mock import MagicMock from vllm.distributed.kv_transfer.kv_connector.v1.lmcache_mp_connector import ( LMCacheMPConnectorUpstream as LMCacheMPConnector, L...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: [LMCache] `_cleanup_request_tracker` leaks lookup state and server read locks when request is aborted before allocation bug ### Your current environment ### 🐛 Describe the bug **Problem** When a request is aborte...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ed. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: and read locks on matched KV chunks are never released until TTL expiry, blocking eviction. Root cause: `update_state_after_alloc` correctly calls both on the normal path. `_cleanup_request_tracker` calls neither. **Tri...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ontend_api;hardware_porting;model_support;scheduler_memory cuda;operator;triton build_error;nan_inf env_dependency #44129 fix: release LMCache lookup locks on abort Your current environment

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#44129](https://github.com/vllm-project/vllm/pull/44129) | closes_keyword | 0.95 | fix: release LMCache lookup locks on abort | Fixes #44100 ### How this was tested - `python -m pytest --confcutdir=tests\v1\kv_connector\unit tests\v1\kv_connector\unit\test_lmcache_mp_connector.py -q` - `python -m ruff che |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
