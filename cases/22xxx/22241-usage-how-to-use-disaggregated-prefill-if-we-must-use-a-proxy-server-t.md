# vllm-project/vllm#22241: [Usage]: How to use disaggregated_prefill? If we must use a proxy server to transfer request from user to prefill instance and then transfer request to decode instance?

| 字段 | 值 |
| --- | --- |
| Issue | [#22241](https://github.com/vllm-project/vllm/issues/22241) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: How to use disaggregated_prefill? If we must use a proxy server to transfer request from user to prefill instance and then transfer request to decode instance?

### Issue 正文摘录

### Your current environment ## vllm 0.8.5 use PyNcclConnector or mooncakeConnector ### How would you like to use vllm Can we send a request to prefill instance and then the prefill instance transfer request to decode instance. Meanwhile, if we have multi-prefill instances or multi-decode instances, how proxy server work? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Usage]: How to use disaggregated_prefill? If we must use a proxy server to transfer request from user to prefill instance and then transfer request to decode instance? usage;stale ### Your current environment ## vllm 0...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: rk? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
