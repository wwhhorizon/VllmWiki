# vllm-project/vllm#27668: [Feature]: WideEP CI Testing

| 字段 | 值 |
| --- | --- |
| Issue | [#27668](https://github.com/vllm-project/vllm/issues/27668) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: WideEP CI Testing

### Issue 正文摘录

### 🚀 The feature, motivation and pitch We have seen many regressions related to WideEP in `llm-d` due to frequent changes in vLLM, which is creating significant issues in developer velocity We need to get some automated testing in place that can run on a nightly basis, including the following: - DP/EP with deepep ll - DP/EP with deepep ht - EPLB - DBO - Async Scheduling - P/D disagg - multi-gpu setups B200 and H100 ### Alternatives ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: epep ht - EPLB - DBO - Async Scheduling - P/D disagg - multi-gpu setups B200 and H100 ### Alternatives ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for r...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [Feature]: WideEP CI Testing feature request ### 🚀 The feature, motivation and pitch We have seen many regressions related to WideEP in `llm-d` due to frequent changes in vLLM, which is creating significant issues in de...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: [Feature]: WideEP CI Testing feature request ### 🚀 The feature, motivation and pitch We have seen many regressions related to WideEP in `llm-d` due to frequent changes in vLLM, which is creating significant issues in de...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature]: WideEP CI Testing feature request ### 🚀 The feature, motivation and pitch We have seen many regressions related to WideEP in `llm-d` due to frequent changes in vLLM, which is creating significant issues in de...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
