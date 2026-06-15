# vllm-project/vllm#11276: [Usage]: How to set a dynamic temperature when sampling? (decrease gradually as more tokens generated)

| 字段 | 值 |
| --- | --- |
| Issue | [#11276](https://github.com/vllm-project/vllm/issues/11276) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: How to set a dynamic temperature when sampling? (decrease gradually as more tokens generated)

### Issue 正文摘录

### How would you like to use vllm I want to set a dynamic temperature when sampling. Specifically, I need to dynamically adjust the temperature coefficient based on the length of the currently generated token each time the logits are processed. It seems that `sampling_params` cannot achieve this feature. Which part of the code should I modify? ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: like to use vllm I want to set a dynamic temperature when sampling. Specifically, I need to dynamically adjust the temperature coefficient based on the length of the currently generated token each time the logits are pr...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: fy? ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ature when sampling? (decrease gradually as more tokens generated) usage;stale ### How would you like to use vllm I want to set a dynamic temperature when sampling. Specifically, I need to dynamically adjust the tempera...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
