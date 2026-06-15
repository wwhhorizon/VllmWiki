# vllm-project/vllm#36804: [Feature]: FA4 Attention Sinks

| 字段 | 值 |
| --- | --- |
| Issue | [#36804](https://github.com/vllm-project/vllm/issues/36804) |
| 状态 | open |
| 标签 | feature request |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: FA4 Attention Sinks

### Issue 正文摘录

### 🚀 The feature, motivation and pitch In order to run GPT-OSS-120b efficiently on the blackwell architecture it requires attention sink support in FA4 ### Alternatives Eager attention :( ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: e, motivation and pitch In order to run GPT-OSS-120b efficiently on the blackwell architecture it requires attention sink support in FA4 ### Alternatives Eager attention :( ### Additional context _No response_ ### Befor...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ## 🚀 The feature, motivation and pitch In order to run GPT-OSS-120b efficiently on the blackwell architecture it requires attention sink support in FA4 ### Alternatives Eager attention :( ### Additional context _No resp...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: feature request ### 🚀 The feature, motivation and pitch In order to run GPT-OSS-120b efficiently on the blackwell architecture it requires attention sink support in FA4 ### Alternatives Eager attention :( ### Additional...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature]: FA4 Attention Sinks feature request ### 🚀 The feature, motivation and pitch In order to run GPT-OSS-120b efficiently on the blackwell architecture it requires attention sink support in FA4 ### Alternatives Ea...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
