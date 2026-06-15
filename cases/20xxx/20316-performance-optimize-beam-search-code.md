# vllm-project/vllm#20316: [Performance]: Optimize beam search code

| 字段 | 值 |
| --- | --- |
| Issue | [#20316](https://github.com/vllm-project/vllm/issues/20316) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance]: Optimize beam search code

### Issue 正文摘录

### Proposal to improve performance Dear vLLM community, I've been analyzing the beam search implementation and have identified potential areas for performance improvement. ## Problem Description The beam search algorithm currently implements candidate expansion by concatenating all candidate tokens with existing sequences. This operation executes beam_width × 2 × beam_width times per decoding step. Through time consumption statistics, it was found that the concatenation operation is highly time-consuming. ## Technical Analysis ### Key Code Locations - Primary logic: [`vllm/engine/protocol.py`](https://github.com/vllm-project/vllm/blob/main/vllm/engine/protocol.py#LXX-YY) The following code uses a double loop to concatenate all candidate tokens with the original token as a BeamSearchSequence, then selects the top-k candidates via the sort method. ![Image](https://github.com/user-attachments/assets/884451fd-2113-4519-9f74-0a0367047688) However, by first selecting the top-k candidate tokens with the highest cumulative probabilities and then performing sorting, we can avoid the time-consuming concatenation operations, thereby improving inference speed. Here’s my revised code: ``` new...

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: all_beams = new_beams ``` Related PR：#19347 ### Performance Profiling Through the optimizations above, the processing time can be reduced by nearly **40%**. I appreciate your review and hope to see these improvements me...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Performance]: Optimize beam search code performance;stale ### Proposal to improve performance Dear vLLM community, I've been analyzing the beam search implementation and have identified potential areas for performance...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: s above, the processing time can be reduced by nearly **40%**. I appreciate your review and hope to see these improvements merged into the main branch soon. ### Report of performance regression _No response_ ### Misc di...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: [Performance]: Optimize beam search code performance;stale ### Proposal to improve performance Dear vLLM community, I've been analyzing the beam search implementation and have identified potential areas for performance...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: if include_stop_str_in_output else current_beam.tokens, logprobs=current_beam.logprobs + [result.outputs[0].logprobs[0]],

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
