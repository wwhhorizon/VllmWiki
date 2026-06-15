# vllm-project/vllm#25310: [Feature]: Proactive, scheduler-bypass pull-KV path to reduce KV-transfer latency

| 字段 | 值 |
| --- | --- |
| Issue | [#25310](https://github.com/vllm-project/vllm/issues/25310) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Proactive, scheduler-bypass pull-KV path to reduce KV-transfer latency

### Issue 正文摘录

### 🚀 The feature, motivation and pitch In the current vLLM implementation, when the Decoder side receives a new request, it must wait for the current scheduling iteration of EngineCore to complete. Only in the next iteration can the scheduler allocate KV blocks and construct kv_connector_metadata, after which the model_runner dispatches the Pull KV task. This waiting introduces latency averaging roughly half of the TPOT, leaving room for performance improvements. ### Alternatives Introduce a fast-path for Pull-KV dispatch that bypasses the current EngineCore scheduling iteration: on request arrival immediately allocate KV blocks, build kv_connector_metadata, and spawn a dedicated thread to issue the Pull-KV task without further delay. ### Additional context This optimization would be particularly beneficial in disaggregated serving setups where KV transfers are frequent and latency-sensitive, as it reduces the latency of newly added requests and improves end-to-end throughput. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/lat...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: [Feature]: Proactive, scheduler-bypass pull-KV path to reduce KV-transfer latency feature request;stale ### 🚀 The feature, motivation and pitch In the current vLLM implementation, when the Decoder side receives a new re...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: Feature]: Proactive, scheduler-bypass pull-KV path to reduce KV-transfer latency feature request;stale ### 🚀 The feature, motivation and pitch In the current vLLM implementation, when the Decoder side receives a new req...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: scheduling iteration: on request arrival immediately allocate KV blocks, build kv_connector_metadata, and spawn a dedicated thread to issue the Pull-KV task without further delay. ### Additional context This optimizatio...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: re to complete. Only in the next iteration can the scheduler allocate KV blocks and construct kv_connector_metadata, after which the model_runner dispatches the Pull KV task. This waiting introduces latency averaging ro...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: blocks and construct kv_connector_metadata, after which the model_runner dispatches the Pull KV task. This waiting introduces latency averaging roughly half of the TPOT, leaving room for performance improvements. ### Al...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
