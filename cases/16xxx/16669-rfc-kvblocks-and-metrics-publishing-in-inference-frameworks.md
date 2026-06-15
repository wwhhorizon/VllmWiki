# vllm-project/vllm#16669: [RFC]: KVBlocks and Metrics Publishing In Inference Frameworks

| 字段 | 值 |
| --- | --- |
| Issue | [#16669](https://github.com/vllm-project/vllm/issues/16669) |
| 状态 | closed |
| 标签 | RFC;stale |
| 评论 | 12; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: KVBlocks and Metrics Publishing In Inference Frameworks

### Issue 正文摘录

### Motivation. To do effective planning and routing for distributed LLM inference, we need mechanisms to publish information about the state of the inference engine to other pieces of the distributed system. Examples include: - Publishing events when blocks are added and removed from the local prefix tree so that a router can create a global prefix tree with data from all the workers. - Publishing real-time metrics so a router can load balance between workers if a worker is starting to queue requests. ### Proposed Change. ## Metrics In vLLM there is already a methodology to publish Metrics using classes that inherit StatsLoggerBase. For example PrometheusStatLogger. We would add a method to relevant engine classes which would accept 3rd party StatLoggers that conform to the StatsLoggerBase interface. In this way an inference framework that wraps vLLM (such as dynamo) has a way to inject custom logic for publishing Metric events. ```python def add_stats_logger(self, name, logger: StatsLoggerBase): self.engine.add_logger(name, logger) ``` or ```python class AsyncLLM(EngineClient): def __init__( self, vllm_config: VllmConfig, executor_class: type[Executor], log_stats: bool, usage_co...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: d routing for distributed LLM inference, we need mechanisms to publish information about the state of the inference engine to other pieces of the distributed system. Examples include: - Publishing events when blocks are...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [RFC]: KVBlocks and Metrics Publishing In Inference Frameworks RFC;stale ### Motivation. To do effective planning and routing for distributed LLM inference, we need mechanisms to publish information about the state of t...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ctive planning and routing for distributed LLM inference, we need mechanisms to publish information about the state of the inference engine to other pieces of the distributed system. Examples include: - Publishing event...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: izable msgspec @dataclass class KVCacheEvent: """Base class for all KV cache-related events""" pass @dataclass class BlockStored(KVCacheEvent): block_hashes: List[int] parent_block_hash: Optional[int] token_ids: List[in...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: [RFC]: KVBlocks and Metrics Publishing In Inference Frameworks RFC;stale ### Motivation. To do effective planning and routing for distributed LLM inference, we need mechanisms to publish information about the state of t...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
