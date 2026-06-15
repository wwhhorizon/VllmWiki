# vllm-project/vllm#15608: [Feature]: In multimodal inference, is it possible to cache textual content and only load images each time to optimize inference efficiency

| 字段 | 值 |
| --- | --- |
| Issue | [#15608](https://github.com/vllm-project/vllm/issues/15608) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: In multimodal inference, is it possible to cache textual content and only load images each time to optimize inference efficiency

### Issue 正文摘录

### 🚀 The feature, motivation and pitch In multimodal inference, is it possible to cache textual content and only load images each time to optimize inference efficiency ### Alternatives _No response_ ### Additional context In multimodal inference, is it possible to cache textual content and only load images each time to optimize inference efficiency ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: and only load images each time to optimize inference efficiency feature request;stale ### 🚀 The feature, motivation and pitch In multimodal inference, is it possible to cache textual content and only load images each ti...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: textual content and only load images each time to optimize inference efficiency feature request;stale ### 🚀 The feature, motivation and pitch In multimodal inference, is it possible to cache textual content and only loa...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ncy ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Feature]: In multimodal inference, is it possible to cache textual content and only load images each time to optimize inference efficiency feature request;stale ### 🚀 The feature, motivation and pitch In multimodal inf...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
