# vllm-project/vllm#24059: [Feature][KV Connector]: Async lookup policy support for MultiConnector

| 字段 | 值 |
| --- | --- |
| Issue | [#24059](https://github.com/vllm-project/vllm/issues/24059) |
| 状态 | closed |
| 标签 | feature request;stale;v1 |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature][KV Connector]: Async lookup policy support for MultiConnector

### Issue 正文摘录

### 🚀 The feature, motivation and pitch This is a follow-up feature after #23620 . In #23620 , we introduced a new semantics in the connector's api to support "async remote lookup". The goal of this feature request is to make MultiConnector flexible enough to deal with the new semantics. For example, it should support at least the following policies: - Wait for the longest matching - Wait for the first available matching ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: e][KV Connector]: Async lookup policy support for MultiConnector feature request;stale;v1 ### 🚀 The feature, motivation and pitch This is a follow-up feature after #23620 . In #23620 , we introduced a new semantics in t...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: new semantics. For example, it should support at least the following policies: - Wait for the longest matching - Wait for the first available matching ### Alternatives _No response_ ### Additional context _No response_...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
