# vllm-project/vllm#29722: [RFC]: Add Balance Scheduling

| 字段 | 值 |
| --- | --- |
| Issue | [#29722](https://github.com/vllm-project/vllm/issues/29722) |
| 状态 | closed |
| 标签 | RFC;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Add Balance Scheduling

### Issue 正文摘录

### Motivation. **Limitations of the current vLLM v1 scheduling strategy** vLLM v1 scheduling currently enables chunkedprefill by default, which processes prefill and decode requests simultaneously in a single scheduling session. This can impact the overall system throughput and performance in some scenarios. Balance scheduling addresses this issue by synchronizing the number of running queues across all schedulers to delay the scheduling of new requests, thereby improving the overall system's steady-state decoding time. This achieves: ✅Adding `balance_gather` to the scheduler synchronizes the number of requests in the running queues between DPs. ✅Balance scheduling improves the decode steady-state time, thereby increasing the overall output throughput of the inference system. ### Proposed Change. **1.Feature Overview** In the vLLM scheduler, running requests (i.e., requests that are already undergoing pre-filled computation) have the highest priority, followed by waiting requests (i.e., requests that have not yet been computed). As shown in the diagram above, when the entire inference system exits from a steady state, the scheduler will schedule a batch of new requests for prefil...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 7: [RFC]: Add Balance Scheduling RFC;stale ### Motivation. **Limitations of the current vLLM v1 scheduling strategy** vLLM v1 scheduling currently enables chunkedprefill by default, which processes prefill and decode reque...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: ously in a single scheduling session. This can impact the overall system throughput and performance in some scenarios. Balance scheduling addresses this issue by synchronizing the number of running queues across all sch...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: nse ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: operations and then synchronize them among the dynamic programming (DP) models. This can cause some DP models that are entirely decoded to synchronize with the number of prefilled tokens. Frequent prefill scheduling by...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
