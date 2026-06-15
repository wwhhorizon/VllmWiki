# vllm-project/vllm#13020: [RFC]: Async KV Cache Transfer for Disaggregated Inference

| 字段 | 值 |
| --- | --- |
| Issue | [#13020](https://github.com/vllm-project/vllm/issues/13020) |
| 状态 | closed |
| 标签 | RFC;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Async KV Cache Transfer for Disaggregated Inference

### Issue 正文摘录

### Motivation. Hello vLLM community, We're from the AWS Neuron inference team and are actively working on P/D disaggregated inference. We'd like to share our initial PoC for achieving **asynchronous KV cache transfer** (mentioned in roadmap #10818), to make decode continue execution while receiving KV cache from prefill workers. Developed based on the current KVCacheTransferAgent (introduced in v0.7.0) and v0 scheduler. ### Proposed Change. **KVCacheTransferAgent (KVLookupBuffer level)** at Decode Worker: * Create and maintain a `receiver_buffer` containing entries for `{input_ids, roi, keys, caches, hidden}` in decode workers, rather than only for prefill workers. * Introduce the `async_drop_select` API. Unlike `drop_select` (which triggers immediate blocking lookups that stall current process), this method queues `drop_select_request` and returns immediately. * Implement a dedicated `drop_select_requester` thread to process queued `drop_select_request`. This thread initiates lookups and data transfers via the `drop_select_handler` from prefill worker, then inserts results into the `receiver_buffer` upon completion. **Scheduler** at Decode Worker: * Add a new `transfer queue` an...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 7: [RFC]: Async KV Cache Transfer for Disaggregated Inference RFC;stale ### Motivation. Hello vLLM community, We're from the AWS Neuron inference team and are actively working on P/D disaggregated inference. We'd like to s...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ### Any Other Things. We have conducted initial validation using Neuron backend ([neuronx-distributed-inference](https://github.com/aws-neuron/neuronx-distributed-inference)) on AWS Trn1/Trn2 instances. We'll share perf...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: es. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: [RFC]: Async KV Cache Transfer for Disaggregated Inference RFC;stale ### Motivation. Hello vLLM community, We're from the AWS Neuron inference team and are actively working on P/D disaggregated inference. We'd like to s...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: `async_drop_select` API. Unlike `drop_select` (which triggers immediate blocking lookups that stall current process), this method queues `drop_select_request` and returns immediately. * Implement a dedicated `drop_selec...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
