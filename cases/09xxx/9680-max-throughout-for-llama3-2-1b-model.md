# vllm-project/vllm#9680: Max throughout for llama3.2 1B model

| 字段 | 值 |
| --- | --- |
| Issue | [#9680](https://github.com/vllm-project/vllm/issues/9680) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Max throughout for llama3.2 1B model

### Issue 正文摘录

### benchmark that targets high througput small llm use case my use case does not care about latency, but need extremely high throughput at minimum price (cheap t4 gpu or just cpu), i.e. run 1 billion requests every week (avg 100k input tokens, 20k output tokens per request). i didnt find any benchmark targeting this type of usecase, would love some pointers.

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: Max throughout for llama3.2 1B model stale ### benchmark that targets high througput small llm use case my use case does not care about latency, but need extremely high throughput at minimum price (cheap t4 gpu or just...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: Max throughout for llama3.2 1B model stale ### benchmark that targets high througput small llm use case my use case does not care about latency, but need extremely high throughput at minimum price (cheap t4 gpu or just...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: Max throughout for llama3.2 1B model stale ### benchmark that targets high througput small llm use case my use case does not care about latency, but need extremely high throughput at minimum price (cheap t4 gpu or just...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ut for llama3.2 1B model stale ### benchmark that targets high througput small llm use case my use case does not care about latency, but need extremely high throughput at minimum price (cheap t4 gpu or just cpu), i.e. r...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
