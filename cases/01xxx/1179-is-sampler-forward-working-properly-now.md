# vllm-project/vllm#1179: Is Sampler forward() working properly now?

| 字段 | 值 |
| --- | --- |
| Issue | [#1179](https://github.com/vllm-project/vllm/issues/1179) |
| 状态 | closed |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Is Sampler forward() working properly now?

### Issue 正文摘录

Hello. I'm using the vLLM very well. But in a recent commit, I find some code that may have bugs. I suspect there is a bug in the way of applying sampling_params in the vllm/model_executor/layers/sampler.py. Watching a _prune_hidden_states function , It seems that logits is sorted by the SamplingType. However, when getting the sampling parameters, those ​​are just ordered by the input_metadata.seq_groups. (e.g. _get_penalties) I can't find a way to match these two in a step of applying parameters. (e.g. _apply_penalties) It may be happened that sampling parameters are applied to wrong logits. Please let me know if I misunderstood anything.

## 候选优化模式

- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: n getting the sampling parameters, those ​​are just ordered by the input_metadata.seq_groups. (e.g. _get_penalties) I can't find a way to match these two in a step of applying parameters. (e.g. _apply_penalties) It may...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: uspect there is a bug in the way of applying sampling_params in the vllm/model_executor/layers/sampler.py. Watching a _prune_hidden_states function , It seems that logits is sorted by the SamplingType. However, when get...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
