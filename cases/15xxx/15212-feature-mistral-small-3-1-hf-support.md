# vllm-project/vllm#15212: [Feature]: Mistral Small 3.1 HF support

| 字段 | 值 |
| --- | --- |
| Issue | [#15212](https://github.com/vllm-project/vllm/issues/15212) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 23; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Mistral Small 3.1 HF support

### Issue 正文摘录

### 🚀 The feature, motivation and pitch According to https://github.com/vllm-project/vllm/issues/15027, Mistral Small 3.1 is now supported, but only in the Mistral format. Support for the HF format would be great as well. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Feature]: Mistral Small 3.1 HF support feature request ### 🚀 The feature, motivation and pitch According to https://github.com/vllm-project/vllm/issues/15027, Mistral Small 3.1 is now supported, but only in the Mistral...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Feature]: Mistral Small 3.1 HF support feature request ### 🚀 The feature, motivation and pitch According to https://github.com/vllm-project/vllm/issues/15027, Mistral Small 3.1 is now supported, but only in the Mistral...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature]: Mistral Small 3.1 HF support feature request ### 🚀 The feature, motivation and pitch According to https://github.com/vllm-project/vllm/issues/15027, Mistral Small 3.1 is now supported, but only in the Mistral...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
