# vllm-project/vllm#21038: [Feature]: Record EPLB metric, can in /metric api get info

| 字段 | 值 |
| --- | --- |
| Issue | [#21038](https://github.com/vllm-project/vllm/issues/21038) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Record EPLB metric, can in /metric api get info

### Issue 正文摘录

### 🚀 The feature, motivation and pitch In https://github.com/vllm-project/vllm/pull/18343#issuecomment-3011349148 this comment, i think we can export some metrics, such as the weight of each expert, to understand the hot and cold distribution of experts, etc. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: Record EPLB metric, can in /metric api get info feature request;stale ### 🚀 The feature, motivation and pitch In https://github.com/vllm-project/vllm/pull/18343#issuecomment-3011349148 this comment, i think w...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: comment, i think we can export some metrics, such as the weight of each expert, to understand the hot and cold distribution of experts, etc. ### Alternatives _No response_ ### Additional context _No response_ ### Before...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
