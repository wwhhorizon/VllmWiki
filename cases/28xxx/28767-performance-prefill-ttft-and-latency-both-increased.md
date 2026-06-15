# vllm-project/vllm#28767: [Performance]: Prefill TTFT and latency both increased

| 字段 | 值 |
| --- | --- |
| Issue | [#28767](https://github.com/vllm-project/vllm/issues/28767) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance]: Prefill TTFT and latency both increased

### Issue 正文摘录

### Proposal to improve performance _No response_ ### Report of performance regression With the following commands: ```bash python benchmark_long_document_qa_throughput.py \ --model meta-llama/Llama-3.2-1B-Instruct ``` The first round (no cache hit) performance degrades from > `TTFT=0.770s` and `round time=1.575s` with nightly version on Nov 13 to > `TTFT=0.899s` and `round time=1.832s` with nightly version on Nov 14 ### Misc discussion on performance _No response_ ### Your current environment (if you think it is necessary) ```text The output of `python collect_env.py` ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 5: [Performance]: Prefill TTFT and latency both increased performance;stale ### Proposal to improve performance _No response_ ### Report of performance regression With the following commands: ```bash python benchmark_long_...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ommands: ```bash python benchmark_long_document_qa_throughput.py \ --model meta-llama/Llama-3.2-1B-Instruct ``` The first round (no cache hit) performance degrades from > `TTFT=0.770s` and `round time=1.575s` with night...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Performance]: Prefill TTFT and latency both increased performance;stale ### Proposal to improve performance _No response_ ### Report of performance regression With the following commands: ```bash python benchmark_long_...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: y \ --model meta-llama/Llama-3.2-1B-Instruct ``` The first round (no cache hit) performance degrades from > `TTFT=0.770s` and `round time=1.575s` with nightly version on Nov 13 to > `TTFT=0.899s` and `round time=1.832s`...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: nce degrades from > `TTFT=0.770s` and `round time=1.575s` with nightly version on Nov 13 to > `TTFT=0.899s` and `round time=1.832s` with nightly version on Nov 14 ### Misc discussion on performance _No response_ ### You...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
