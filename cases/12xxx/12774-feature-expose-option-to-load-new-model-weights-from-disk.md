# vllm-project/vllm#12774: [Feature]: Expose option to load new model weights from disk

| 字段 | 值 |
| --- | --- |
| Issue | [#12774](https://github.com/vllm-project/vllm/issues/12774) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Expose option to load new model weights from disk

### Issue 正文摘录

### 🚀 The feature, motivation and pitch In an async RL setting, we often want to perform fast generation with a vllm endpoint on a separate node and occasionally sync model weights from disk. It would be good if this option was available on the vllm endpoint. ### Alternatives SGLang already exposes this option: https://docs.sglang.ai/backend/native_api.html#Update-Weights-From-Disk ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: Expose option to load new model weights from disk feature request;stale ### 🚀 The feature, motivation and pitch In an async RL setting, we often want to perform fast generation with a vllm endpoint on a separ...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: Alternatives SGLang already exposes this option: https://docs.sglang.ai/backend/native_api.html#Update-Weights-From-Disk ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you alre...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Feature]: Expose option to load new model weights from disk feature request;stale ### 🚀 The feature, motivation and pitch In an async RL setting, we often want to perform fast generation with a vllm endpoint on a separ...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
