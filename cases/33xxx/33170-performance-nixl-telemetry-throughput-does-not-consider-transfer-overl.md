# vllm-project/vllm#33170: [Performance]: NIXL telemetry throughput does not consider transfer overlapping

| 字段 | 值 |
| --- | --- |
| Issue | [#33170](https://github.com/vllm-project/vllm/issues/33170) |
| 状态 | open |
| 标签 | performance;stale;kv-connector |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance]: NIXL telemetry throughput does not consider transfer overlapping

### Issue 正文摘录

### Proposal to improve performance I encounter a magnificent NIXL throughput drop with the `batch_size` increasing and I think there should be some issues in the telemetry. https://github.com/vllm-project/vllm/blob/main/vllm/distributed/kv_transfer/kv_connector/v1/nixl_connector.py#L2616 here vLLM calculates the throughput by the `sum of bytes transferred /sum the xfer time`, but if there are multiple transfers overlapped, we can not simply sum each xfer time as the total duration. In real case, the total duration should be shorter if multiple transfers can be in parallel. Any thoughts and advices are welcome! ### Report of performance regression _No response_ ### Misc discussion on performance _No response_ ### Your current environment (if you think it is necessary) ```text The output of `python collect_env.py` ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: [Performance]: NIXL telemetry throughput does not consider transfer overlapping performance;stale;kv-connector ### Proposal to improve performance I encounter a magnificent NIXL throughput drop with the `batch_size` inc...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: telemetry throughput does not consider transfer overlapping performance;stale;kv-connector ### Proposal to improve performance I encounter a magnificent NIXL throughput drop with the `batch_size` increasing and I think...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
