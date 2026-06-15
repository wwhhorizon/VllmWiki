# vllm-project/vllm#19541: [Bug]: Disaggregated prefill memory leak

| 字段 | 值 |
| --- | --- |
| Issue | [#19541](https://github.com/vllm-project/vllm/issues/19541) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Disaggregated prefill memory leak

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Prefill nodes might leak memory if the decode process unexpectedly exits without pulling the cache. For example, if the user's prompt is short (e.g., 4KB), but the `max_tokens` is much larger (e.g., 64KB). If the proxy ignores the max tokens limit and forces it to 1 before forwarding to prefill, prefill will accept the request and run normally. The proxy then restores the user's max tokens setting before sending to decode. Decode rejects the request because the token limit is too high, returning a 400 error. This leaves prefill's cache will not be pulled by the decode node forever, causing a memory leak. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Bug]: Disaggregated prefill memory leak bug;stale ### Your current environment ### 🐛 Describe the bug Prefill nodes might leak memory if the decode process unexpectedly exits without pulling the cache. For example, if...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ak. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
