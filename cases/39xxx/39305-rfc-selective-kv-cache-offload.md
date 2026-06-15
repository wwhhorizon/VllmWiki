# vllm-project/vllm#39305: [RFC]: Selective KV Cache offload

| 字段 | 值 |
| --- | --- |
| Issue | [#39305](https://github.com/vllm-project/vllm/issues/39305) |
| 状态 | open |
| 标签 | RFC |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Selective KV Cache offload

### Issue 正文摘录

### Motivation. Implement a "selective offloading" directive in llm-d/vLLM offload path, allowing CPU and FS offloading connectors (and possibly other connectors), to only offload parts of the prompt outside of GPU Memory. ___ At the moment, there is no control available to control KV Cache offloading. It's all (all generated KVCache is offloaded during the forward pass) or nothing (when the connector is disabled). Public traces like Mooncake or Alibaba [show](https://dl.acm.org/doi/pdf/10.1145/3773772) that 40-60% of the KV Cache is stored but never reused. Creating a mechanism to only store some tokens while discarding others can allow vLLM orchestrators (e.g. llm-d) to implement policies that can improve performance or reduce cost in certain scenarios. A few non comprehensive example given: - Long one-off requests in between more common prompts; - KV Cache stored on some remote server with limited bandwidth. See also the [llm-d Context-Aware KVCache retention](https://docs.google.com/document/d/1kRKAZBG7te38tqv9Twxyyc-Pdkk2JZPm7gqHHnNhFpE/edit?tab=t.0#heading=h.p50vcarvctpi). ### Proposed Change. I have implemented a draft in [this fork](https://github.com/ruocco/vllm), adding...

## 候选优化模式

- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 3: [RFC]: Selective KV Cache offload RFC ### Motivation. Implement a "selective offloading" directive in llm-d/vLLM offload path, allowing CPU and FS offloading connectors (and possibly other connectors), to only offload p...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: hat 40-60% of the KV Cache is stored but never reused. Creating a mechanism to only store some tokens while discarding others can allow vLLM orchestrators (e.g. llm-d) to implement policies that can improve performance...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: tps://docs.google.com/document/d/1kRKAZBG7te38tqv9Twxyyc-Pdkk2JZPm7gqHHnNhFpE/edit?tab=t.0#heading=h.p50vcarvctpi). ### Proposed Change. I have implemented a draft in [this fork](https://github.com/ruocco/vllm), adding...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ertain scenarios. A few non comprehensive example given: - Long one-off requests in between more common prompts; - KV Cache stored on some remote server with limited bandwidth. See also the [llm-d Context-Aware KVCache...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: arding others can allow vLLM orchestrators (e.g. llm-d) to implement policies that can improve performance or reduce cost in certain scenarios. A few non comprehensive example given: - Long one-off requests in between m...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
