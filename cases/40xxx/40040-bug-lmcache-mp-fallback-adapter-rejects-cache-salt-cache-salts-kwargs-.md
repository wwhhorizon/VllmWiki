# vllm-project/vllm#40040: [Bug]: LMCache MP fallback adapter rejects cache_salt/cache_salts kwargs after #39837

| 字段 | 值 |
| --- | --- |
| Issue | [#40040](https://github.com/vllm-project/vllm/issues/40040) |
| 状态 | open |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | distributed_parallel;frontend_api |
| 子分类 | wrong_output |
| Operator 关键词 | cuda;operator |
| 症状 | mismatch |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: LMCache MP fallback adapter rejects cache_salt/cache_salts kwargs after #39837

### Issue 正文摘录

### Your current environment - vLLM checkout: `main` at `3daca38e2279538b420641bd41853c19e5ad01e4` - Python: `3.10.20` - Latest stable checked for comparison: `v0.19.0` (published 2026-04-03) This appears to be a **current `main` regression** rather than a latest-stable regression. ### 🐛 Describe the bug `#39837` added `cache_salt` / `cache_salts` arguments at the LMCache MP connector call sites, but the repo-local fallback/internal adapter copy in `vllm/distributed/kv_transfer/kv_connector/v1/lmcache_integration/multi_process_adapter.py` still has the old method signatures. As a result, the fallback/internal LMCache MP path can raise `TypeError` on current `main`. #### Why this seems real and not intended `cache_salt` is documented as a real cache-isolation feature for shared environments, and `#39837` explicitly extends that support into the LMCache MP connector. Also, `#39837` already had a review comment pointing out that the fallback adapter methods needed to accept the new arguments to avoid `TypeError`, but the merged code still has the old signatures. #### Relevant call sites on current `main` ```python # vllm/distributed/kv_transfer/kv_connector/v1/lmcache_mp_connector.py...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: real cache-isolation feature for shared environments, and `#39837` explicitly extends that support into the LMCache MP connector. Also, `#39837` already had a review comment pointing out that the fallback adapter method...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: request_ids: list[str], ops: list[LoadStoreOp], event: torch.cuda.Event, ): ... def batched_submit_retrieve_requests( self, request_ids: list[str], ops: list[LoadStoreOp], event: torch.cuda.Event, ): ... ``` #### Observ...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: ing a local runtime-oriented repro against the checked-out source, I can reproduce: ```text TypeError: LMCacheMPSchedulerAdapter.maybe_submit_lookup_request() got an unexpected keyword argument 'cache_salt' TypeError: L...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: r/v1/lmcache_mp_connector.py self.worker_adapter.batched_submit_retrieve_requests( request_ids, ops, event, cache_salts=cache_salts ) self.worker_adapter.batched_submit_store_requests( request_ids, ops, event, cache_sal...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: n` at `3daca38e2279538b420641bd41853c19e5ad01e4` - Python: `3.10.20` - Latest stable checked for comparison: `v0.19.0` (published 2026-04-03) This appears to be a **current `main` regression** rather than a latest-stabl...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
