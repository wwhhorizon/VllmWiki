# vllm-project/vllm#44249: [Bug]: lmcache_connector.start_load_kv asserts on degraded LMCache instead of honoring "recompute" fallback

| 字段 | 值 |
| --- | --- |
| Issue | [#44249](https://github.com/vllm-project/vllm/issues/44249) |
| 状态 | open |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support |
| 子分类 | cold_start |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error;crash |
| 根因提示 | env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: lmcache_connector.start_load_kv asserts on degraded LMCache instead of honoring "recompute" fallback

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When LMCache fails to initialize for any reason, it sets `lmcache_engine = None`, logs `System will operate in degraded mode (recompute)`, and expects callers to fall back to recompute. vLLM's `LMCacheConnectorV1` ignores that signal: it calls `engine.start_load_kv(...)` on every request anyway, and the LMCache adapter then asserts on the `None` handle (`assert self.lmcache_engine is not None`), killing EngineCore on the **first request**. Net effect: any LMCache init failure — for any reason, on any version — turns into a hard crash on first traffic instead of the documented degraded-mode recompute fallback. The container exits with code 0 (the `EngineDeadError` path calls `app.shutdown()` cleanly), so under Kubernetes the pod is restarted indefinitely. Reproduces on two image versions with two **different upstream init failures**, which is the point — the connector-side contract violation is independent of which underlying LMCache failure populated `lmcache_engine = None`: | Image | vLLM | LMCache | Init failure that leaves engine = None | |---|---|---|---| | `ghcr.io/llm-d/llm-d-cuda:v0.6.0` | 0.17.1 | 0.4.1 | ZMQ RPC service-...

## 现有链接修复摘要

#3208 [RFC/WIP] First steps towards FP8 for Mixtral

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: equest**. Net effect: any LMCache init failure — for any reason, on any version — turns into a hard crash on first traffic instead of the documented degraded-mode recompute fallback. The container exits with code 0 (the...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: tart_load_kv asserts on degraded LMCache instead of honoring "recompute" fallback bug ### Your current environment ### 🐛 Describe the bug When LMCache fails to initialize for any reason, it sets `lmcache_engine = None`,...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: type: application/json" \ -d '{"model":"Qwen/Qwen3-30B-A3B","stream":false,"max_tokens":4, "messages":[{"role":"user","content":"hi"}]}' # → HTTP 500, EngineCore exits with code 0 in ~63 ms. ``` Server launched with: ``...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: own()` cleanly), so under Kubernetes the pod is restarted indefinitely. Reproduces on two image versions with two **different upstream init failures**, which is the point — the connector-side contract violation is indep...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ure that leaves engine = None | |---|---|---|---| | `ghcr.io/llm-d/llm-d-cuda:v0.6.0` | 0.17.1 | 0.4.1 | ZMQ RPC service-lookup timeout | | `ghcr.io/llm-d/llm-d-cuda:v0.7.0` | `0.1.dev1+g693c2d11e` | 0.4.4 | `cpuinfo.ge...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#3208](https://github.com/vllm-project/vllm/pull/3208) | mentioned | 0.45 | [RFC/WIP] First steps towards FP8 for Mixtral | se, etc.). lmcache fixed several of these races (lmcache#2808, #2798, #3208) and added reconnect support — but the connector-side contract violation persists across all versions w… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
