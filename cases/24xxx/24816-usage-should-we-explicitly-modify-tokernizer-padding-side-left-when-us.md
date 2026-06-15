# vllm-project/vllm#24816: [Usage]: should we explicitly modify `tokernizer.padding_side=left` when using vLLM to do batch infernce?

| 字段 | 值 |
| --- | --- |
| Issue | [#24816](https://github.com/vllm-project/vllm/issues/24816) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: should we explicitly modify `tokernizer.padding_side=left` when using vLLM to do batch infernce?

### Issue 正文摘录

### Your current environment N/A ### How would you like to use vllm As title, I'm confused about whether vLLM handles this internally or not. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: [Usage]: should we explicitly modify `tokernizer.padding_side=left` when using vLLM to do batch infernce? usage;stale ### Your current environment N/A ### How would you like to use vllm As title, I'm confused about whet...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ot. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: okernizer.padding_side=left` when using vLLM to do batch infernce? usage;stale ### Your current environment N/A ### How would you like to use vllm As title, I'm confused about whether vLLM handles this internally or not...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
