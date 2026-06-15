# vllm-project/vllm#20223: [Feature]: Any plans to support TokenWeave optimizations in vLLM?

| 字段 | 值 |
| --- | --- |
| Issue | [#20223](https://github.com/vllm-project/vllm/issues/20223) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Any plans to support TokenWeave optimizations in vLLM?

### Issue 正文摘录

### 🚀 The feature, motivation and pitch I recently came across an issue where someone mentioned that TokenWeave achieves performance gains over vLLM by overlapping compute and communication, and by using fused kernels (AllReduce, Residual addition, and RMSNorm). Are there any plans to support these optimizations in vLLM itself? vLLM issue: #19415 TokenWeave Code: [https://github.com/microsoft/tokenweave/tree/main](https://github.com/microsoft/tokenweave/tree/main) TokenWeave Paper: [https://arxiv.org/abs/2505.11329](https://arxiv.org/abs/2505.11329) ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: Feature]: Any plans to support TokenWeave optimizations in vLLM? feature request;stale ### 🚀 The feature, motivation and pitch I recently came across an issue where someone mentioned that TokenWeave achieves performance...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
