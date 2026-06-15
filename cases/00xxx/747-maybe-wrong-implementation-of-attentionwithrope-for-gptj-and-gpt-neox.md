# vllm-project/vllm#747: Maybe Wrong implementation of AttentionWithRoPE for GPTJ and GPT-NeoX?

| 字段 | 值 |
| --- | --- |
| Issue | [#747](https://github.com/vllm-project/vllm/issues/747) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Maybe Wrong implementation of AttentionWithRoPE for GPTJ and GPT-NeoX?

### Issue 正文摘录

I think there may be a wrong implementation for GPTJ and GPT-NeoX when doing 'apply rotary embedding'. Currently implemented `PagedAttentionWithRoPE` always use the whole `query` and `key`, which is compatible with models like `llama` and `baichuan`, however for GPTJ and GPT-NeoX they may only use part of query and key when doing rope. If current implementation does not compatible with those two models, I would suggest for those models that not using the whole query and key when applying rotary embeddings, can have another attention class that inherit from `PagedAttentionWithRoPE` and do something like: ```python query_rot, query_pass = self._prepare_tensor_for_rope(query, self.rotary_dim) key_rot, key_pass = self._prepare_tensor_for_rope(key, self.rotary_dim) pos_encoding_ops.rotary_embedding_neox( positions, query_rot, key_rot, self.rotary_dim, self.cos_sin_cache, ) query = self._cat_tensor_after_rope(query_rot, query_pass) key = self._cat_tensor_after_rope(key_rot, key_pass) ```

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: thRoPE` always use the whole `query` and `key`, which is compatible with models like `llama` and `baichuan`, however for GPTJ and GPT-NeoX they may only use part of query and key when doing rope. If current implementati...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
