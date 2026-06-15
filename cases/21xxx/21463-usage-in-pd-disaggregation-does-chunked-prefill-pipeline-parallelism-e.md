# vllm-project/vllm#21463: [Usage]: In pd disaggregation,  does chunked prefill + pipeline parallelism equal to chunked pipeline parallelism proposed by mooncake?

| 字段 | 值 |
| --- | --- |
| Issue | [#21463](https://github.com/vllm-project/vllm/issues/21463) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: In pd disaggregation,  does chunked prefill + pipeline parallelism equal to chunked pipeline parallelism proposed by mooncake?

### Issue 正文摘录

I want to know in pd disaggregation, if enable chunked prefill and pipeline parallelism, it equals to chunked pipeline parallelism proposed by mooncake or not, which is truly useful for long context. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Usage]: In pd disaggregation, does chunked prefill + pipeline parallelism equal to chunked pipeline parallelism proposed by mooncake? usage;stale I want to know in pd disaggregation, if enable chunked prefill and pipel...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Usage]: In pd disaggregation, does chunked prefill + pipeline parallelism equal to chunked pipeline parallelism proposed by mooncake? usage;stale I want to know in pd disaggregation, if enable chunked prefill and pipel...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
