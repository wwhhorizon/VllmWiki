# vllm-project/vllm#2564: Should the default `length_penalty` be 0?

| 字段 | 值 |
| --- | --- |
| Issue | [#2564](https://github.com/vllm-project/vllm/issues/2564) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Should the default `length_penalty` be 0?

### Issue 正文摘录

I'm wondering if the default value of `length_penalty` in the beam search algorithm should be set to 0. My understanding, based on discussions like [this issue](https://github.com/huggingface/transformers/issues/16930) in the hf transformers repository, is that a `length_penalty` greater than 0 favors shorter sequences, while a penalty less than 0 favors longer ones and 0 means no `length_penalty` In the vLLM project (which has code adapted from Hugging Face), particularly in the file [vllm/sequence.py](https://github.com/vllm-project/vllm/blob/7a0b011dd51e5c6b48e8f8f5424be0995b5cb8ee/vllm/sequence.py#L191), the default value is indeed 0: ```python def get_beam_search_score(self, length_penalty: float = 0.0, seq_len: Optional[int] = None, eos_token_id: Optional[int] = None) -> float: """Calculate the beam search score with length penalty. Adapted from: https://github.com/huggingface/transformers/blob/ccb92be23def445f2afdea94c31286f84b89eb5b/src/transformers/generation/beam_search.py#L938 """ ``` Should we consider setting the default `length_penalty` to 0?

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: understanding, based on discussions like [this issue](https://github.com/huggingface/transformers/issues/16930) in the hf transformers repository, is that a `length_penalty` greater than 0 favors shorter sequences, whil...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 0? I'm wondering if the default value of `length_penalty` in the beam search algorithm should be set to 0. My understanding, based on discussions like [this issue](https://github.com/huggingface/transformers/issues/1693...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
