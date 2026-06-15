# vllm-project/vllm#44008: [RFC]: Offloading Metrics Redesign

| 字段 | 值 |
| --- | --- |
| Issue | [#44008](https://github.com/vllm-project/vllm/issues/44008) |
| 状态 | open |
| 标签 | RFC |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Offloading Metrics Redesign

### Issue 正文摘录

### Motivation. The offloading connector currently treats metrics as a transfer-specific concern. That worked while the only exposed metrics were load/store bytes, time, and size, but it does not scale well as offloading managers start exposing their own state. The immediate example is `vllm:kv_offload_stores_skipped`, which is emitted by the CPU offloading manager when a store is skipped because the reuse threshold is not reached. A near-term follow-up is a CPU KV offload cache usage gauge. These metrics are not transfer operations, so adding them through the existing hard-coded transfer metrics path would keep expanding special cases in the connector. We need a general offloading metrics path where connector metrics and manager metrics are declared as metadata, registered up front, and observed through the same counter/gauge/histogram machinery. This also makes aggregation semantics explicit: counters are summed, gauges keep the latest value, and histograms accumulate observations. At the same time, offloading metrics are part of vLLM's public Prometheus surface. Existing metrics such as `vllm:kv_offload_total_bytes`, `vllm:kv_offload_total_time`, and `vllm:kv_offload_size` may...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: ion. The offloading connector currently treats metrics as a transfer-specific concern. That worked while the only exposed metrics were load/store bytes, time, and size, but it does not scale well as offloading managers...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ): metric_definitions: dict[str, OffloadingMetricMetadata] @classmethod @abstractmethod def get_manager_cls(cls) -> type[OffloadingManager]: ... ``` During spec initialization: ```python self.metric_definitions = self.g...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: metrics path where connector metrics and manager metrics are declared as metadata, registered up front, and observed through the same counter/gauge/histogram machinery. This also makes aggregation semantics explicit: co...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: or autoscaling rules. The redesign should therefore improve the internal model and introduce clearer flat metrics without silently removing or renaming existing public metrics. ### Proposed Change. ## Summary This RFC p...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: This RFC does not change unrelated metrics such as prefix-cache metrics, request latency metrics, speculative decoding metrics, or KV block sampling metrics. ## Scope In scope: - Offloading connector transfer metrics. -...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
