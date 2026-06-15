# vllm-project/vllm#38279: [Feature]: PagedEviction: Structured Block-wise KV Cache Pruning for Efficient Large Language Model Inference

| 字段 | 值 |
| --- | --- |
| Issue | [#38279](https://github.com/vllm-project/vllm/issues/38279) |
| 状态 | open |
| 标签 | feature request |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: PagedEviction: Structured Block-wise KV Cache Pruning for Efficient Large Language Model Inference

### Issue 正文摘录

### 🚀 The feature, motivation and pitch here is reference paper for it , https://arxiv.org/pdf/2509.04377 ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: [Feature]: PagedEviction: Structured Block-wise KV Cache Pruning for Efficient Large Language Model Inference feature request ### 🚀 The feature, motivation and pitch here is reference paper for it , https://arxiv.org/pd...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: [Feature]: PagedEviction: Structured Block-wise KV Cache Pruning for Efficient Large Language Model Inference feature request ### 🚀 The feature, motivation and pitch here is reference paper for it , https://arxiv.org/pd...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: [Feature]: PagedEviction: Structured Block-wise KV Cache Pruning for Efficient Large Language Model Inference feature request ### 🚀 The feature, motivation and pitch here is reference paper for it , https://arxiv.org/pd...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ion: Structured Block-wise KV Cache Pruning for Efficient Large Language Model Inference feature request ### 🚀 The feature, motivation and pitch here is reference paper for it , https://arxiv.org/pdf/2509.04377 ### Alte...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
