# vllm-project/vllm#8370: [Performance]: INFO 09-11 12:41:50 spec_decode_worker.py:790] SpecDecodeWorker scoring_time_ms is slow

| 字段 | 值 |
| --- | --- |
| Issue | [#8370](https://github.com/vllm-project/vllm/issues/8370) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance]: INFO 09-11 12:41:50 spec_decode_worker.py:790] SpecDecodeWorker scoring_time_ms is slow

### Issue 正文摘录

### Proposal to improve performance _No response_ ### Report of performance regression INFO 09-11 12:41:50 spec_decode_worker.py:790] SpecDecodeWorker stage times: average_time_per_proposal_tok_ms=4.96 scoring_time_ms=54.92 verification_time_ms=1.20 The proportion of scoretime in decde is too large. The draft model only requires 5ms for each decode, but it takes 50ms for each score calculation. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Performance]: INFO 09-11 12:41:50 spec_decode_worker.py:790] SpecDecodeWorker scoring_time_ms is slow performance;stale ### Proposal to improve performance _No response_ ### Report of performance regression INFO 09-11...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: roposal to improve performance _No response_ ### Report of performance regression INFO 09-11 12:41:50 spec_decode_worker.py:790] SpecDecodeWorker stage times: average_time_per_proposal_tok_ms=4.96 scoring_time_ms=54.92...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: on. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: me_ms=1.20 The proportion of scoretime in decde is too large. The draft model only requires 5ms for each decode, but it takes 50ms for each score calculation. ### Before submitting a new issue... - [X] Make sure you alr...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
