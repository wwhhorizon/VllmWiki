# vllm-project/vllm#26298: [RFC]: Per-request metrics for the offline API.

| 字段 | 值 |
| --- | --- |
| Issue | [#26298](https://github.com/vllm-project/vllm/issues/26298) |
| 状态 | closed |
| 标签 | RFC;stale |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Per-request metrics for the offline API.

### Issue 正文摘录

### Motivation. In V0 when calling `LLM.generate()` the `metrics` field of the `RequestOutput` object was set to a `RequestMetrics` object: ``` @dataclass class RequestMetrics: """Metrics associated with a request. Attributes: arrival_time: The time when the request arrived. first_scheduled_time: The time when the request was first scheduled. first_token_time: The time when the first token was generated. time_in_queue: The time the request spent in the queue. finished_time: The time when the request was finished. scheduler_time: The time spent in the scheduler when this request was being considered by the scheduler. model_forward_time: The time spent in the model forward pass when this request was in the batch. model_execute_time: The time spent in the model execute function. This will include model forward, block/sync across workers, cpu-gpu sync time and sampling time. """ arrival_time: float last_token_time: float first_scheduled_time: Optional[float] first_token_time: Optional[float] time_in_queue: Optional[float] finished_time: Optional[float] = None scheduler_time: Optional[float] = None model_forward_time: Optional[float] = None model_execute_time: Optional[float] = None ``...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [RFC]: Per-request metrics for the offline API. RFC;stale ### Motivation. In V0 when calling `LLM.generate()` the `metrics` field of the `RequestOutput` object was set to a `RequestMetrics` object: ``` @dataclass class...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: m/vllm-project/vllm/pull/24947 added stats back, but now as a `RequestStateStats` object: ``` class RequestStateStats: """Stats that need to be tracked across delta updates.""" num_generation_tokens: int = 0 # This is a...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: etrics` object: ``` @dataclass class RequestMetrics: """Metrics associated with a request. Attributes: arrival_time: The time when the request arrived. first_scheduled_time: The time when the request was first scheduled...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 394 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: e function. This will include model forward, block/sync across workers, cpu-gpu sync time and sampling time. """ arrival_time: float last_token_time: float first_scheduled_time: Optional[float] first_token_time: Opti

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
