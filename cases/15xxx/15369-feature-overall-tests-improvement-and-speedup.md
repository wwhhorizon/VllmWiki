# vllm-project/vllm#15369: [Feature]: Overall tests improvement and speedup

| 字段 | 值 |
| --- | --- |
| Issue | [#15369](https://github.com/vllm-project/vllm/issues/15369) |
| 状态 | closed |
| 标签 | good first issue;feature request;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Overall tests improvement and speedup

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Currently, vLLM test suite are often very expensive and takes a long time to setup and run (approx 1h for the full suite). Majority of these times spent are at our frontend code. Given that API logics are relatively complex (OpenAI vs. API server), we can speed up by mocking and keep e2e to a minimum. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: Feature]: Overall tests improvement and speedup good first issue;feature request;stale ### 🚀 The feature, motivation and pitch Currently, vLLM test suite are often very expensive and takes a long time to setup and run (...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: [Feature]: Overall tests improvement and speedup good first issue;feature request;stale ### 🚀 The feature, motivation and pitch Currently, vLLM test suite are often very expensive and takes a long time to setup and run...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
