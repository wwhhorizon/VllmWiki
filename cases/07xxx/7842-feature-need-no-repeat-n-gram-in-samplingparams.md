# vllm-project/vllm#7842: [Feature]: need no_repeat_n_gram in SamplingParams

| 字段 | 值 |
| --- | --- |
| Issue | [#7842](https://github.com/vllm-project/vllm/issues/7842) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: need no_repeat_n_gram in SamplingParams

### Issue 正文摘录

### 🚀 The feature, motivation and pitch It is very common for large models to encounter infinite loops during inference, and we need some methods to prevent this from happening. If infinite loops during inference are not monitored, it can significantly impact reasoning efficiency. Therefore, I need a parameter `no_repeat_n_gram` to prevent the generation of sequences where *n* consecutive tokens repeat, thus mitigating the occurrence of infinite loops. The specific implementation method is as follows: for a generated token x_i, for each possible value of x_i (in the case of sampling, x_i could have multiple possibilities), we monitor whether generating this token violates the `no_repeat_n_gram_size`. If it does, we set its logit to negative infinity, thereby preventing the generation of *n*-gram repetitions. In practice, I will set *n* as large as possible to act as a punishment for infinite loops without overly affecting the model's normal inference output. The reason I do not use `repeat_penalty` is that it penalizes all tokens that have appeared during inference, which I consider to be an overly harsh penalty, while I only need a mechanism that specifically targets infinite loo...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ich I consider to be an overly harsh penalty, while I only need a mechanism that specifically targets infinite loops. ### Alternatives _No response_ ### Additional context The implementation of `no_repeat_n_gram` from t...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: need no_repeat_n_gram in SamplingParams feature request;stale ### 🚀 The feature, motivation and pitch It is very common for large models to encounter infinite loops during inference, and we need some methods...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: g inference are not monitored, it can significantly impact reasoning efficiency. Therefore, I need a parameter `no_repeat_n_gram` to prevent the generation of sequences where *n* consecutive tokens repeat, thus mitigati...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ale ### 🚀 The feature, motivation and pitch It is very common for large models to encounter infinite loops during inference, and we need some methods to prevent this from happening. If infinite loops during inference ar...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
