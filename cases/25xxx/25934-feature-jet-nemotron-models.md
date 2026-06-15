# vllm-project/vllm#25934: [Feature]: Jet nemotron models

| 字段 | 值 |
| --- | --- |
| Issue | [#25934](https://github.com/vllm-project/vllm/issues/25934) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Jet nemotron models

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Hi, I was wondering if jet nemotron models can be supported in VLLM. They have a new attention implementation called JetBlock which is linear or more efficient. Is this planned to be supported or not inthe scope? I am just wondering, because I would like to train my custom jet nemotron models and I am using VLLM currently. https://github.com/NVlabs/Jet-Nemotron Thanks ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: Jet nemotron models feature request;stale ### 🚀 The feature, motivation and pitch Hi, I was wondering if jet nemotron models can be supported in VLLM. They have a new attention implementation called JetBlock...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: new attention implementation called JetBlock which is linear or more efficient. Is this planned to be supported or not inthe scope? I am just wondering, because I would like to train my custom jet nemotron models and I...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: be supported in VLLM. They have a new attention implementation called JetBlock which is linear or more efficient. Is this planned to be supported or not inthe scope? I am just wondering, because I would like to train my...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Feature]: Jet nemotron models feature request;stale ### 🚀 The feature, motivation and pitch Hi, I was wondering if jet nemotron models can be supported in VLLM. They have a new attention implementation called JetBlock...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
