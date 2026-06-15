# vllm-project/vllm#10489: [Feature]: Support outlines versions > v0.1.0

| 字段 | 值 |
| --- | --- |
| Issue | [#10489](https://github.com/vllm-project/vllm/issues/10489) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Support outlines versions > v0.1.0

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Outlines (used for guided decoding) has had a minor upgrade on 7th of Oct (ref below). This has improved their internal workings and should have a good impact on the performance downstream (on vllm). At the moment the version used by vllm is pinned but we have successfully spinned up vllm ourselves internally with just upgrading this dependency (there are no _relevant_ breaking changes for vllm) and it works out of the box. https://github.com/dottxt-ai/outlines/releases/tag/0.1.0 ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [Feature]: Support outlines versions > v0.1.0 feature request ### 🚀 The feature, motivation and pitch Outlines (used for guided decoding) has had a minor upgrade on 7th of Oct (ref below). This has improved their intern...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature]: Support outlines versions > v0.1.0 feature request ### 🚀 The feature, motivation and pitch Outlines (used for guided decoding) has had a minor upgrade on 7th of Oct (ref below). This has improved their intern...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
