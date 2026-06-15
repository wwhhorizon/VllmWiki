# vllm-project/vllm#413: bloom loading KeyError

| 字段 | 值 |
| --- | --- |
| Issue | [#413](https://github.com/vllm-project/vllm/issues/413) |
| 状态 | closed |
| 标签 |  |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> bloom loading KeyError

### Issue 正文摘录

codes from vllm.model_executor.models.bloom.BloomForCausalLM this part will add 'transformer.' prefix to the lm_head which does not match the huggingface bloom key:

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: bloom loading KeyError codes from vllm.model_executor.models.bloom.BloomForCausalLM this part will add 'transformer.' prefix to the lm_head which does not match the huggingface bloom key:
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: bloom loading KeyError codes from vllm.model_executor.models.bloom.BloomForCausalLM this part will add 'transformer.' prefix to the lm_head which does not match the huggingface bloom key:

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
