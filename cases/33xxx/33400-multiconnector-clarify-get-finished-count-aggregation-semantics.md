# vllm-project/vllm#33400: MultiConnector: Clarify get_finished_count aggregation semantics

| 字段 | 值 |
| --- | --- |
| Issue | [#33400](https://github.com/vllm-project/vllm/issues/33400) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> MultiConnector: Clarify get_finished_count aggregation semantics

### Issue 正文摘录

## Summary `MultiConnector.get_finished_count()` currently returns `None` because the correct aggregation strategy is unclear. This issue tracks clarifying and implementing proper semantics. ## Background `get_finished_count()` returns the expected number of workers that will report send/receive completion for each request. It's used by `KVOutputAggregator` to track when all workers have finished: ```python # vllm/distributed/kv_transfer/kv_connector/utils.py class KVOutputAggregator: def __init__(self, expected_finished_count: int): self._expected_finished_count = expected_finished_count @classmethod def from_connector(cls, connector, world_size: int): return cls(connector.get_finished_count() or world_size) ``` Currently **all connectors return `None`** (base class, lmcache_mp_connector), so the aggregator falls back to `world_size`. ## The Problem For `MultiConnector` wrapping multiple sub-connectors, if sub-connectors start returning non-None values, the correct aggregation is unclear: | Strategy | Description | When it makes sense | |----------|-------------|---------------------| | **Sum** | Add counts from all connectors | Sub-connectors have independent completion tracking...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: MultiConnector: Clarify get_finished_count aggregation semantics stale ## Summary `MultiConnector.get_finished_count()` currently returns `None` because the correct aggregation strategy is unclear. This issue tracks cla...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: self._expected_finished_count = expected_finished_count @classmethod def from_connector(cls, connector, world_size: int): return cls(connector.get_finished_count() or world_size) ``` Currently **all connectors return `N...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
