# vllm-project/vllm#41938: [Feature]: Opt-in: stop caching KV blocks after thinking start tokens

| 字段 | 值 |
| --- | --- |
| Issue | [#41938](https://github.com/vllm-project/vllm/issues/41938) |
| 状态 | open |
| 标签 | feature request |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Opt-in: stop caching KV blocks after thinking start tokens

### Issue 正文摘录

### 🚀 The feature, motivation and pitch # [Cache] Opt-in: stop caching KV blocks after thinking start tokens ## Motivation Reasoning models (DeepSeek-R1, Qwen3, QwQ, etc.) produce ` ... ` tokens whose content varies across requests even for identical prompts. Under prefix caching, these thinking blocks get hashed, cached, and never reused — pure waste of cache capacity that pressures eviction of actually-reusable prompt blocks. ## Approach Instead of post-hoc cleanup or adding eviction-priority logic, we take the simplest possible path: once the thinking start token sequence is detected during incremental block hashing, we stop computing hashes for subsequent blocks. No hash means `cache_full_blocks` never registers them — they still exist in GPU memory for the current request but don't pollute the shared cache pool. Changes: - `kv_cache_utils.py`: extend `get_request_block_hasher` to accept `thinking_start_token_ids`; the inner closure scans each block and stops hashing once the pattern is found - `request.py`: add `_in_thinking_section` flag per request - `engine/core.py`: wire up token ids from `ReasoningConfig` - `block_pool.py` / `single_type_kv_cache_manager.py`: relax the a...

## 候选优化模式

- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 5: ese thinking blocks get hashed, cached, and never reused — pure waste of cache capacity that pressures eviction of actually-reusable prompt blocks. ## Approach Instead of post-hoc cleanup or adding eviction-priority log...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: caching KV blocks after thinking start tokens ## Motivation Reasoning models (DeepSeek-R1, Qwen3, QwQ, etc.) produce ` ... ` tokens whose content varies across requests even for identical prompts. Under prefix caching,...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: gistered in the cache pool, freeing space for reusable entries. - Prefix cache hit rate is identical (prompt blocks are reused equally in both modes), confirming the feature only affects thinking blocks. - Feature OFF s...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ng blocks get hashed, cached, and never reused — pure waste of cache capacity that pressures eviction of actually-reusable prompt blocks. ## Approach Instead of post-hoc cleanup or adding eviction-priority logic, we tak...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ressure A/B): ```bash # Start server with feature enabled (artificially small cache to create pressure) python -m vllm.entrypoints.openai.api_server \ --model Qwen/Qwen3-14B \ --reasoning-parser qwen3 \ --strip-thinking...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
