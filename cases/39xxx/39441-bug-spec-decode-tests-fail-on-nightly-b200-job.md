# vllm-project/vllm#39441: [Bug]: spec decode tests fail on nightly b200 job

| 字段 | 值 |
| --- | --- |
| Issue | [#39441](https://github.com/vllm-project/vllm/issues/39441) |
| 状态 | open |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: spec decode tests fail on nightly b200 job

### Issue 正文摘录

### Your current environment see CI failures in https://github.com/vllm-project/vllm/pull/38577 ### 🐛 Describe the bug CI contains repro and details ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Bug]: spec decode tests fail on nightly b200 job bug ### Your current environment see CI failures in https://github.com/vllm-project/vllm/pull/38577 ### 🐛 Describe the bug CI contains repro and details ### Before submi...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: spec decode tests fail on nightly b200 job bug ### Your current environment see CI failures in https://github.com/vllm-project/vllm/pull/38577 ### 🐛 Describe the bug CI contains repro and details ### Before submi...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ode tests fail on nightly b200 job bug ### Your current environment see CI failures in https://github.com/vllm-project/vllm/pull/38577 ### 🐛 Describe the bug CI contains repro and details ### Before submitting a new iss...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: [Bug]: spec decode tests fail on nightly b200 job bug ### Your current environment see CI failures in https://github.com/vllm-project/vllm/pull/38577 ### 🐛 Describe the bug CI contains repro and details ### Before submi...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
