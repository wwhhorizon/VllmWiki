# vllm-project/vllm#30368: [CI] Test target determination using LLM

| 字段 | 值 |
| --- | --- |
| Issue | [#30368](https://github.com/vllm-project/vllm/issues/30368) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI] Test target determination using LLM

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Our conditional testing strategy is outdated and need to be updated manually for each test. It eventually led to a lot of leaks, PRs don't run the right tests or not enough test coverage before merging. An idea to improve this is to use LLM to take the codebase, PR diff, and context to determine which job should run in CI. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [CI] Test target determination using LLM feature request;stale ### 🚀 The feature, motivation and pitch Our conditional testing strategy is outdated and need to be updated manually for each test. It eventually led to a l...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: [CI] Test target determination using LLM feature request;stale ### 🚀 The feature, motivation and pitch Our conditional testing strategy is outdated and need to be updated manually for each test. It eventually led to a lo
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: [CI] Test target determination using LLM feature request;stale ### 🚀 The feature, motivation and pitch Our conditional testing strategy is outdated and need to be updated manually for each test. It eventually led to a l...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
