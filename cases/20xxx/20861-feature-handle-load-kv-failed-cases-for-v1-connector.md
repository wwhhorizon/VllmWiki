# vllm-project/vllm#20861: [Feature]: handle load kv failed cases for v1 connector

| 字段 | 值 |
| --- | --- |
| Issue | [#20861](https://github.com/vllm-project/vllm/issues/20861) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: handle load kv failed cases for v1 connector

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Currently, we have a kv connector which allowed load kv from other places sync or async, it's a very nice feature! However, how can we handle failed cases while using async load? Such as network issue, remote kv pool server error, or anything could lead to a load fail. To achive this, we might need to add a `get_failed` hook beside `get_finished`, or return more info (such as request id to fetch status, success or failed) in `get_finished`. If a kv load is scheduled and failed to load, we might need to recompute those kvs to avoid wrong infer result. Not sure if this is a good idea to connectors, or am I missing somthing in current connector design which already handle this? ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: handle load kv failed cases for v1 connector feature request;stale ### 🚀 The feature, motivation and pitch Currently, we have a kv connector which allowed load kv from other places sync or async, it's a very...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
