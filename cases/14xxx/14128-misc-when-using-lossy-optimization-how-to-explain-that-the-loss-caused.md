# vllm-project/vllm#14128: [Misc]: When using lossy optimization, how to explain that the loss caused by optimization is within the acceptable range?

| 字段 | 值 |
| --- | --- |
| Issue | [#14128](https://github.com/vllm-project/vllm/issues/14128) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Misc]: When using lossy optimization, how to explain that the loss caused by optimization is within the acceptable range?

### Issue 正文摘录

### Anything you want to discuss about vllm. I’ve noticed that with each version upgrade of vllm, there seems to be some degree of precision loss. How do you determine whether these losses are within an acceptable range? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ## Anything you want to discuss about vllm. I’ve noticed that with each version upgrade of vllm, there seems to be some degree of precision loss. How do you determine whether these losses are within an acceptable range?...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: that with each version upgrade of vllm, there seems to be some degree of precision loss. How do you determine whether these losses are within an acceptable range? ### Before submitting a new issue... - [x] Make sure you...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ge? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ain that the loss caused by optimization is within the acceptable range? stale ### Anything you want to discuss about vllm. I’ve noticed that with each version upgrade of vllm, there seems to be some degree of precision...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
