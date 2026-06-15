# vllm-project/vllm#38069: [RFC]: Can we implement n-gram and suffix speculative decoding in model_runner_v2?

| 字段 | 值 |
| --- | --- |
| Issue | [#38069](https://github.com/vllm-project/vllm/issues/38069) |
| 状态 | open |
| 标签 | RFC |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Can we implement n-gram and suffix speculative decoding in model_runner_v2?

### Issue 正文摘录

### Motivation. I noticed that Eagle has been implemented in model_runner_v2. Can we introduce the n-gram and suffix speculative inference methods into v2? Compared with model-based methods, these two should be easier to implement. ### Proposed Change. Implement n-gram and suffix speculative decoding based on model_runner_v2. ### Feedback Period. 1–2 weeks for initial feedback. ### CC List. @WoosukKwon @TheEpicDolphin ### Any Other Things. _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [RFC]: Can we implement n-gram and suffix speculative decoding in model_runner_v2? RFC ### Motivation. I noticed that Eagle has been implemented in model_runner_v2. Can we introduce the n-gram and suffix speculative inf...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [RFC]: Can we implement n-gram and suffix speculative decoding in model_runner_v2? RFC ### Motivation. I noticed that Eagle has been implemented in model_runner_v2. Can we introduce the n-gram and suffix speculative inf...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
