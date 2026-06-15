# vllm-project/vllm#32720: [Bug]: More robust 32 bit indexing

| 字段 | 值 |
| --- | --- |
| Issue | [#32720](https://github.com/vllm-project/vllm/issues/32720) |
| 状态 | open |
| 标签 | bug;unstale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: More robust 32 bit indexing

### Issue 正文摘录

### Your current environment NA ### 🐛 Describe the bug 🐛 Describe the bug Recently I submitted a PR that assumed vLLM would always only need 32‑bit indexing. This broke one of our internal models and raised the question of whether that assumption is actually valid in all cases. I’ve since made the assumption configurable to unblock current issues. We discussed several alternatives, and here’s the plan to make this more robust: Turn off assume_32_bit_indexing for backed dynamic shapes. For unbacked models, analyze the Dynamo graph before Inductor to cap the largest tensor size, then set the flag based on that cap. Note that we can leverage the maximum number of tokens for this analysis. Versions NA ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: M would always only need 32‑bit indexing. This broke one of our internal models and raised the question of whether that assumption is actually valid in all cases. I’ve since made the assumption configurable to unblock c...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ote that we can leverage the maximum number of tokens for this analysis. Versions NA ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bot...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: NA ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whi...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: lly valid in all cases. I’ve since made the assumption configurable to unblock current issues. We discussed several alternatives, and here’s the plan to make this more robust: Turn off assume_32_bit_indexing for backed...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: More robust 32 bit indexing bug;unstale ### Your current environment NA ### 🐛 Describe the bug 🐛 Describe the bug Recently I submitted a PR that assumed vLLM would always only need 32‑bit indexing. This broke one...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
