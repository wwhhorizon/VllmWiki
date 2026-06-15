# vllm-project/vllm#710:  what cause  “assert input_metadata.num_generation_tokens == 0” in vllm/model_executor/layers/attention.py line 200

| 字段 | 值 |
| --- | --- |
| Issue | [#710](https://github.com/vllm-project/vllm/issues/710) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

>  what cause  “assert input_metadata.num_generation_tokens == 0” in vllm/model_executor/layers/attention.py line 200

### Issue 正文摘录

_本地原始数据中没有 issue 正文。_

## 候选优化模式

- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: what cause “assert input_metadata.num_generation_tokens == 0” in vllm/model_executor/layers/attention.py line 200
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: what cause “assert input_metadata.num_generation_tokens == 0” in vllm/model_executor/layers/attention.py line 200

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
