# vllm-project/vllm#499: LogProbs - Incorrect?

| 字段 | 值 |
| --- | --- |
| Issue | [#499](https://github.com/vllm-project/vllm/issues/499) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> LogProbs - Incorrect?

### Issue 正文摘录

Hi, I am working on some multi-choice tasks in LM_evaluation_harness, where I find your results inconsistent with existing results. - So I have some questions regarding your LogProbs specified in your SamplingParams. - Is that correct as the log_softmax(logits)?

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: existing results. - So I have some questions regarding your LogProbs specified in your SamplingParams. - Is that correct as the log_softmax(logits)?
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: LogProbs - Incorrect? Hi, I am working on some multi-choice tasks in LM_evaluation_harness, where I find your results inconsistent with existing results. - So I have some questions regarding your LogProbs specified in y...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
