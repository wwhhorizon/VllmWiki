# vllm-project/vllm#32270: [Bug]: same `max_seq_len` of flashinfer trtllm decode and prefill.

| 字段 | 值 |
| --- | --- |
| Issue | [#32270](https://github.com/vllm-project/vllm/issues/32270) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: same `max_seq_len` of flashinfer trtllm decode and prefill.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I noticed that in `vllm/v1/attention/backends/flashinfer.py`, both `TRTLLMPrefill` and `TRTLLMDecode` are constructed using the same `max_seq_len`. This seems odd when running hybrid prefill and decode. Is this a bug, or is it intentional? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: same `max_seq_len` of flashinfer trtllm decode and prefill. bug;stale ### Your current environment ### 🐛 Describe the bug I noticed that in `vllm/v1/attention/backends/flashinfer.py`, both `TRTLLMPrefill` and `TR...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: [Bug]: same `max_seq_len` of flashinfer trtllm decode and prefill. bug;stale ### Your current environment ### 🐛 Describe the bug I noticed that in `vllm/v1/attention/backends/flashinfer.py`, both `TRTLLMPrefill` and `TR...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: al? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
