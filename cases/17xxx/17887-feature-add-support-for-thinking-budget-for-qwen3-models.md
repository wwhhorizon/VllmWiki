# vllm-project/vllm#17887: [Feature]: Add Support for thinking_budget for Qwen3 Models

| 字段 | 值 |
| --- | --- |
| Issue | [#17887](https://github.com/vllm-project/vllm/issues/17887) |
| 状态 | open |
| 标签 | feature request |
| 评论 | 18; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Add Support for thinking_budget for Qwen3 Models

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Alibaba Documentation [(https://www.alibabacloud.com/help/en/model-studio/deep-thinking)](https://www.alibabacloud.com/help/en/model-studio/deep-thinking) mentions the usage of thinking_budget to control the thinking length hence generation time ! can we please get it added to vllm where /think is hard inserted after thinking_budget number of thinking tokens to stop thinking.. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Feature]: Add Support for thinking_budget for Qwen3 Models feature request ### 🚀 The feature, motivation and pitch Alibaba Documentation [(https://www.alibabacloud.com/help/en/model-studio/deep-thinking)](https://www.a...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature]: Add Support for thinking_budget for Qwen3 Models feature request ### 🚀 The feature, motivation and pitch Alibaba Documentation [(https://www.alibabacloud.com/help/en/model-studio/deep-thinking)](https://www.a...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
