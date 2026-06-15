# vllm-project/vllm#24171: [MM processor]: Benchmark mm processor's performance

| 字段 | 值 |
| --- | --- |
| Issue | [#24171](https://github.com/vllm-project/vllm/issues/24171) |
| 状态 | closed |
| 标签 | help wanted;good first issue;feature request;multi-modality |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [MM processor]: Benchmark mm processor's performance

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Currently, we haven't had scripts to benchmark mm_processor's performance under complicated deploy environments (DP, multiple instances etc). Therefore, we should add some benchmark script to simulate it and identify the potential bottlenecks. ### Alternatives _No response_ ### Additional context cc @DarkLight1337 @ywang96 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [MM processor]: Benchmark mm processor's performance help wanted;good first issue;feature request;multi-modality ### 🚀 The feature, motivation and pitch Currently, we haven't had scripts to benchmark mm_processor's perf...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 96 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whi...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: enchmark mm processor's performance help wanted;good first issue;feature request;multi-modality ### 🚀 The feature, motivation and pitch Currently, we haven't had scripts to benchmark mm_processor's performance under com...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
