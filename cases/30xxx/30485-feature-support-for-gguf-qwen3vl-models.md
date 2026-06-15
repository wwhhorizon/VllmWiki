# vllm-project/vllm#30485: [Feature]: Support for GGUF qwen3vl models

| 字段 | 值 |
| --- | --- |
| Issue | [#30485](https://github.com/vllm-project/vllm/issues/30485) |
| 状态 | open |
| 标签 | feature request;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Support for GGUF qwen3vl models

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Currently, GGUF models that use the qwen3vl architecture fail with the error `ValueError: GGUF model with architecture qwen3vl is not supported yet.`. Could support for GGUF models using qwen3vl be implemented? ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Feature]: Support for GGUF qwen3vl models feature request;stale ### 🚀 The feature, motivation and pitch Currently, GGUF models that use the qwen3vl architecture fail with the error `ValueError: GGUF model with architec...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: Support for GGUF qwen3vl models feature request;stale ### 🚀 The feature, motivation and pitch Currently, GGUF models that use the qwen3vl architecture fail with the error `ValueError: GGUF model with architec...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ature, motivation and pitch Currently, GGUF models that use the qwen3vl architecture fail with the error `ValueError: GGUF model with architecture qwen3vl is not supported yet.`. Could support for GGUF models using qwen...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
