# vllm-project/vllm#34929: [Feature]: Get latency and tpot per request in vLLM benchmark

| 字段 | 值 |
| --- | --- |
| Issue | [#34929](https://github.com/vllm-project/vllm/issues/34929) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Get latency and tpot per request in vLLM benchmark

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Today ttft and itls are provided but I think that some users would prefer to have the end-to-end latency of the request for a more realistic number in their environments. Also, tpot per request should bring a better idea of the performance that happened on a particular request. It's cool to have it for the whole run but per request might bring a more granular perspective and can help debugging ### Alternatives I haven't seen options to get the requested features ### Additional context nothing additional ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: [Feature]: Get latency and tpot per request in vLLM benchmark feature request ### 🚀 The feature, motivation and pitch Today ttft and itls are provided but I think that some users would prefer to have the end-to-end late...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: nal ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature]: Get latency and tpot per request in vLLM benchmark feature request ### 🚀 The feature, motivation and pitch Today ttft and itls are provided but I think that some users would prefer to have the end-to-end late...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
