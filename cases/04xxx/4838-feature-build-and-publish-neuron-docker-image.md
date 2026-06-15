# vllm-project/vllm#4838: [Feature]: Build and publish Neuron docker image

| 字段 | 值 |
| --- | --- |
| Issue | [#4838](https://github.com/vllm-project/vllm/issues/4838) |
| 状态 | open |
| 标签 | feature request;keep-open |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Build and publish Neuron docker image

### Issue 正文摘录

### 🚀 The feature, motivation and pitch It seems like the current docker images don't support Neuron (Inferentia). It would be very helpful if there was a tested, managed Neuron docker image to use. While at the same subject, it would be even better if some documentation would be added on running vLlm Neuron using containers. ### Alternatives DJL? ### Additional context _No response_

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [Feature]: Build and publish Neuron docker image feature request;keep-open ### 🚀 The feature, motivation and pitch It seems like the current docker images don't support Neuron (Inferentia). It would be very helpful if t...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature]: Build and publish Neuron docker image feature request;keep-open ### 🚀 The feature, motivation and pitch It seems like the current docker images don't support Neuron (Inferentia). It would be very helpful if t...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: n't support Neuron (Inferentia). It would be very helpful if there was a tested, managed Neuron docker image to use. While at the same subject, it would be even better if some documentation would be added on running vLl...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
