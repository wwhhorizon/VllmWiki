# vllm-project/vllm#2606: Beam Search Length Normalization Wrong

| 字段 | 值 |
| --- | --- |
| Issue | [#2606](https://github.com/vllm-project/vllm/issues/2606) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Beam Search Length Normalization Wrong

### Issue 正文摘录

The current implementation of the `get_beam_search_score` method in the vllm/sequence.py seems to incorrectly include the prompt length in the sequence length when calculating the beam score. This deviates from the standard approach used in huggingface and elsewhere. The current implementation is: ``` if seq_len is None: seq_len = self.get_len() # NOTE: HF implementation does not count the EOS token # towards the length, we align with that here for testing. if (eos_token_id is not None and self.get_last_token_id() == eos_token_id): seq_len -= 1 return self.get_cumulative_logprob() / (seq_len**length_penalty) ``` Which I think would be correct if get_len() returned the generated length, but get_len() includes the prompt: ``` def get_len(self) -> int: return len(self.output_token_ids) + len(self.prompt_token_ids) ``` I found this investigating the results returned by a beam search. I was surprised that a short sequence was being returned as the best choice when the second option was much much longer and only had a slightly smaller logprob. The reason, I now realize, is that my prompt is quite long compared to the generation, so the length penalty is not getting correctly applied.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: Beam Search Length Normalization Wrong stale The current implementation of the `get_beam_search_score` method in the vllm/sequence.py seems to incorrectly include the prompt length in the sequence length when calculatin...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ulating the beam score. This deviates from the standard approach used in huggingface and elsewhere. The current implementation is: ``` if seq_len is None: seq_len = self.get_len() # NOTE: HF implementation does not coun...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: score. This deviates from the standard approach used in huggingface and elsewhere. The current implementation is: ``` if seq_len is None: seq_len = self.get_len() # NOTE: HF implementation does not count the EOS token #...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: Beam Search Length Normalization Wrong stale The current implementation of the `get_beam_search_score` method in the vllm/sequence.py seems to incorrectly include the prompt length in the sequence length when calculatin...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: EOS token # towards the length, we align with that here for testing. if (eos_token_id is not None and self.get_last_token_id() == eos_token_id): seq_len -= 1 return self.get_cumulative_logprob() / (seq_len**length_penal...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
