# vllm-project/vllm#41672: [Bug]: thinking_token_budget silently ignored when no penalties are set (inverted condition in gpu_input_batch.py)

| 字段 | 值 |
| --- | --- |
| Issue | [#41672](https://github.com/vllm-project/vllm/issues/41672) |
| 状态 | closed |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: thinking_token_budget silently ignored when no penalties are set (inverted condition in gpu_input_batch.py)

### Issue 正文摘录

## Summary `thinking_token_budget` has no effect for any request that does not also set penalty parameters (`frequency_penalty`, `presence_penalty`, `repetition_penalty`) or `bad_words`. This covers the vast majority of real-world usage. ## Root Cause Introduced in commit `68dd7db81` (ThinkingBudgetStateHolder, April 29), `gpu_input_batch.py` contains an inverted boolean condition when computing `needs_output_token_ids`: ```python # BEFORE (buggy) - vllm/v1/worker/gpu_input_batch.py ~line 879 needs_output_token_ids = ( not self.no_penalties or bool(self.bad_words_token_ids) or self.logitsprocs_need_output_token_ids or not thinking_budget_tracks_reqs # inverted ) ``` When `thinking_budget_tracks_reqs=True` and no penalties are set, the expression evaluates to `False`, so `SamplingMetadata.output_token_ids` is an empty list. `ThinkingBudgetStateHolder.update_state()` iterates zero elements, `_update_think_state()` is never called, `in_end` stays `False`, and `apply_to_logits()` never forces the end token. ## Fix Remove the erroneous `not` (see PR #41674). ## Impact - Severity: **High** - `thinking_token_budget` is completely non-functional for typical usage - Introduced: commit `68d...

## 候选优化模式

- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: acks_reqs=True` and no penalties are set, the expression evaluates to `False`, so `SamplingMetadata.output_token_ids` is an empty list. `ThinkingBudgetStateHolder.update_state()` iterates zero elements, `_update_think_s...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: nput_batch.py) ## Summary `thinking_token_budget` has no effect for any request that does not also set penalty parameters (`frequency_penalty`, `presence_penalty`, `repetition_penalty`) or `bad_words`. This covers the v...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: inking_budget_tracks_reqs=True` and no penalties are set, the expression evaluates to `False`, so `SamplingMetadata.output_token_ids` is an empty list. `ThinkingBudgetStateHolder.update_state()` iterates zero elements,...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
