# vllm-project/vllm#10137: [Feature]: Support for predicted outputs

| 字段 | 值 |
| --- | --- |
| Issue | [#10137](https://github.com/vllm-project/vllm/issues/10137) |
| 状态 | closed |
| 标签 | help wanted;feature request;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Support for predicted outputs

### Issue 正文摘录

### 🚀 The feature, motivation and pitch https://platform.openai.com/docs/guides/latency-optimization#use-predicted-outputs Reminds me on: https://github.com/FasterDecoding/REST https://arxiv.org/html/2311.08252v2 ### Alternatives _No response_ ### Additional context I could give it a try to implement it based on ngram speculation ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: Support for predicted outputs help wanted;feature request;stale ### 🚀 The feature, motivation and pitch https://platform.openai.com/docs/guides/latency-optimization#use-predicted-outputs Reminds me on: https:...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: e feature, motivation and pitch https://platform.openai.com/docs/guides/latency-optimization#use-predicted-outputs Reminds me on: https://github.com/FasterDecoding/REST https://arxiv.org/html/2311.08252v2 ### Alternativ...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: on ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whi...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
