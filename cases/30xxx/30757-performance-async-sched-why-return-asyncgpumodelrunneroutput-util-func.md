# vllm-project/vllm#30757: [Performance]: Async sched: Why return AsyncGPUModelRunnerOutput util func sample_tokens

| 字段 | 值 |
| --- | --- |
| Issue | [#30757](https://github.com/vllm-project/vllm/issues/30757) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance]: Async sched: Why return AsyncGPUModelRunnerOutput util func sample_tokens

### Issue 正文摘录

### Proposal to improve performance Why is AsyncGPUModelRunnerOutput returned only after sample_tokens, not immediately after execute_model? https://github.com/vllm-project/vllm/blob/0d0c929f2360cde5bae6817ad0f555641329e79d/vllm/v1/engine/core.py#L420-L422 If we defer returning AsyncGPUModelRunnerOutput until after sampling, there's a high chance that the async future completes immediately because `AsyncGPUModelRunnerOutput.get_output` is really light workload. As a result, the batch_queue size may effectively remain at 1, preventing overlap between model forward and scheduling of the next batch. https://github.com/vllm-project/vllm/blob/0d0c929f2360cde5bae6817ad0f555641329e79d/vllm/v1/engine/core.py#L430-L438 ### Report of performance regression _No response_ ### Misc discussion on performance _No response_ ### Your current environment (if you think it is necessary) ```text The output of `python collect_env.py` ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: Why return AsyncGPUModelRunnerOutput util func sample_tokens performance;stale ### Proposal to improve performance Why is AsyncGPUModelRunnerOutput returned only after sample_tokens, not immediately after execute_model?...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: 55641329e79d/vllm/v1/engine/core.py#L430-L438 ### Report of performance regression _No response_ ### Misc discussion on performance _No response_ ### Your current environment (if you think it is necessary) ```text The o...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Performance]: Async sched: Why return AsyncGPUModelRunnerOutput util func sample_tokens performance;stale ### Proposal to improve performance Why is AsyncGPUModelRunnerOutput returned only after sample_tokens, not imme...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
