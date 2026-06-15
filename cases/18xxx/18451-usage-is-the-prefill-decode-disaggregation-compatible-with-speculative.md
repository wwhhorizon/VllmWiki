# vllm-project/vllm#18451: [Usage]: Is the Prefill Decode Disaggregation compatible with Speculative Decoding in vLLM?

| 字段 | 值 |
| --- | --- |
| Issue | [#18451](https://github.com/vllm-project/vllm/issues/18451) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Is the Prefill Decode Disaggregation compatible with Speculative Decoding in vLLM?

### Issue 正文摘录

### How would you like to use vllm I would like to know if Prefill Decode Disaggregation and Speculative Decoding are compatible in vllm, and if there is a corresponding roadmap for this. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Usage]: Is the Prefill Decode Disaggregation compatible with Speculative Decoding in vLLM? usage;stale ### How would you like to use vllm I would like to know if Prefill Decode Disaggregation and Speculative Decoding a...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: is. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
