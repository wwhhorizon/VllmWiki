# vllm-project/vllm#27700: [Feature]: Thresholds for enabling Sequence Parallelism + Async TP

| 字段 | 值 |
| --- | --- |
| Issue | [#27700](https://github.com/vllm-project/vllm/issues/27700) |
| 状态 | closed |
| 标签 | feature request;keep-open |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Thresholds for enabling Sequence Parallelism + Async TP

### Issue 正文摘录

### 🚀 The feature, motivation and pitch SP + Async TP is beneficial on long prefills / big batches but can be detrimental below a certain threshold. With the enable of dynamic sizes in https://github.com/vllm-project/vllm/pull/26681 , this introduces regressions for decode. Therefore, if SP + Async TP is to be enabled by default, we should have some sort of thresholding for when it is active / inactive. ### Alternatives _No response_ ### Additional context Data: ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: eature]: Thresholds for enabling Sequence Parallelism + Async TP feature request;keep-open ### 🚀 The feature, motivation and pitch SP + Async TP is beneficial on long prefills / big batches but can be detrimental below...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Feature]: Thresholds for enabling Sequence Parallelism + Async TP feature request;keep-open ### 🚀 The feature, motivation and pitch SP + Async TP is beneficial on long prefills / big batches but can be detrimental belo...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: zes in https://github.com/vllm-project/vllm/pull/26681 , this introduces regressions for decode. Therefore, if SP + Async TP is to be enabled by default, we should have some sort of thresholding for when it is active /...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: eep-open ### 🚀 The feature, motivation and pitch SP + Async TP is beneficial on long prefills / big batches but can be detrimental below a certain threshold. With the enable of dynamic sizes in https://github.com/vllm-p...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
