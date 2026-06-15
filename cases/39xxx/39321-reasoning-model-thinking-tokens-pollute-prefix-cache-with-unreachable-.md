# vllm-project/vllm#39321: Reasoning model thinking tokens pollute prefix cache with unreachable entries

| 字段 | 值 |
| --- | --- |
| Issue | [#39321](https://github.com/vllm-project/vllm/issues/39321) |
| 状态 | closed |
| 标签 |  |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Reasoning model thinking tokens pollute prefix cache with unreachable entries

### Issue 正文摘录

When serving reasoning models (DeepSeek-R1, QwQ, etc.) with `--reasoning-parser`, all output tokens — including ` ` tokens — are hashed and cached via Automatic Prefix Caching (APC). If the user does not include thinking tokens when constructing the next turn's prompt (e.g., [DeepSeek's API docs](https://api-docs.deepseek.com/guides/thinking_mode) explicitly say not to), these cached blocks will never be matched by any future prefix, becoming dead weight that wastes GPU memory until LRU eviction. ## Code path In `request.py`, `append_output_token_ids` adds output tokens to `all_token_ids` and calls `update_block_hashes()`, which hashes them into blocks eligible for prefix caching. When the request finishes, these blocks are freed (ref count decremented) but remain in `cached_block_hash_to_block` as eviction candidates — not deleted. Since each block's hash depends on `parent_block_hash` (see `hash_block_tokens` in `kv_cache_utils.py`), the hash chain means blocks after the thinking tokens encode the entire prefix including thinking. A future request without thinking tokens computes different hashes — no match. ## Why this causes wasted cache and recomputation Consider a multi-turn...

## 候选优化模式

- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 3: Reasoning model thinking tokens pollute prefix cache with unreachable entries When serving reasoning models (DeepSeek-R1, QwQ, etc.) with `--reasoning-parser`, all output tokens — including ` ` tokens — are hashed and c...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: eek's API docs](https://api-docs.deepseek.com/guides/thinking_mode) explicitly say not to), these cached blocks will never be matched by any future prefix, becoming dead weight that wastes GPU memory until LRU eviction....
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: .deepseek.com/guides/thinking_mode) explicitly say not to), these cached blocks will never be matched by any future prefix, becoming dead weight that wastes GPU memory until LRU eviction. ## Code path In `request.py`, `...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: Reasoning model thinking tokens pollute prefix cache with unreachable entries When serving reasoning models (DeepSeek-R1, QwQ, etc.) with `--reasoning-parser`, all output tokens — including ` ` tokens — are hashed and c...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ead weight that wastes GPU memory until LRU eviction. ## Code path In `request.py`, `append_output_token_ids` adds output tokens to `all_token_ids` and calls `update_block_hashes()`, which hashes them into blocks eligib...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
