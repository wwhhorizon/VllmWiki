# vllm-project/vllm#33472: [Feature]: default timezone in container should be UTC

| 字段 | 值 |
| --- | --- |
| Issue | [#33472](https://github.com/vllm-project/vllm/issues/33472) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: default timezone in container should be UTC

### Issue 正文摘录

### 🚀 The feature, motivation and pitch The default timezone in the vllm(nightly) container is America/Los_Angeles. This is a personal developer setting, which the developer should set on his own machine with TZ env var or by mounting /etc/localtime and /etc/timezone into the container. For production releases, UTC would be a much better default within the image. ### Alternatives The alternative is for EVERY user outside of the LA timezone to have to configure their system just to get a sane default, or risk mistaken interpretation of log entries. I think it's unacceptable to push this burden onto every user due to developer laziness; it's a reversal of efficiency/burden, in a sense. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: burden onto every user due to developer laziness; it's a reversal of efficiency/burden, in a sense. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot li...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: The alternative is for EVERY user outside of the LA timezone to have to configure their system just to get a sane default, or risk mistaken interpretation of log entries. I think it's unacceptable to push this burden on...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature]: default timezone in container should be UTC feature request ### 🚀 The feature, motivation and pitch The default timezone in the vllm(nightly) container is America/Los_Angeles. This is a personal developer set...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
