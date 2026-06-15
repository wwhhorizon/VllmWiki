# vllm-project/vllm#9584: [Feature]: LoRA support for Qwen model

| 字段 | 值 |
| --- | --- |
| Issue | [#9584](https://github.com/vllm-project/vllm/issues/9584) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: LoRA support for Qwen model

### Issue 正文摘录

### 🚀 The feature, motivation and pitch [rank0]: ValueError: Model QWenLMHeadModel does not support LoRA, but LoRA is enabled. Support for this model may be added in the future. If this is important to you, please open an issue on github. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Feature]: LoRA support for Qwen model feature request ### 🚀 The feature, motivation and pitch [rank0]: ValueError: Model QWenLMHeadModel does not support LoRA, but LoRA is enabled. Support for this model may be added i...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: s enabled. Support for this model may be added in the future. If this is important to you, please open an issue on github. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature]: LoRA support for Qwen model feature request ### 🚀 The feature, motivation and pitch [rank0]: ValueError: Model QWenLMHeadModel does not support LoRA, but LoRA is enabled. Support for this model may be added i...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
