# vllm-project/vllm#24136: [Feature]: Decoupled Vision-Language Deployment

| 字段 | 值 |
| --- | --- |
| Issue | [#24136](https://github.com/vllm-project/vllm/issues/24136) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Decoupled Vision-Language Deployment

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Support for DvD feature introduced in internvl 3_5 models. Decouples the vision and language models and deploys them on separate servers for faster inference speed ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: The feature, motivation and pitch Support for DvD feature introduced in internvl 3_5 models. Decouples the vision and language models and deploys them on separate servers for faster inference speed ### Alternatives _No...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature]: Decoupled Vision-Language Deployment feature request ### 🚀 The feature, motivation and pitch Support for DvD feature introduced in internvl 3_5 models. Decouples the vision and language models and deploys the...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
