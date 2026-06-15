# vllm-project/vllm#30075: [Feature]: Default eplb num_redundant_experts to the lowest valid value if unspecified

| 字段 | 值 |
| --- | --- |
| Issue | [#30075](https://github.com/vllm-project/vllm/issues/30075) |
| 状态 | open |
| 标签 | help wanted;good first issue;feature request;unstale |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Default eplb num_redundant_experts to the lowest valid value if unspecified

### Issue 正文摘录

### 🚀 The feature, motivation and pitch EPLB requires the number of experts to be chosen up front and there is a known minimum valid value that can be derived from the vllm startup configuration. Since extra EPLB experts trades kv cache memory for potential performance improvements, but that is not guaranteed to pay off, having the EPLB value default to the minimum valid value would reduce friction on enabling EPLB the first time until users are ready to tune. As a consequence, it would also streamline templating the same config to work across multiple EP sizes for the default case. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: e lowest valid value if unspecified help wanted;good first issue;feature request;unstale ### 🚀 The feature, motivation and pitch EPLB requires the number of experts to be chosen up front and there is a known minimum val...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: e]: Default eplb num_redundant_experts to the lowest valid value if unspecified help wanted;good first issue;feature request;unstale ### 🚀 The feature, motivation and pitch EPLB requires the number of experts to be chos...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: ed from the vllm startup configuration. Since extra EPLB experts trades kv cache memory for potential performance improvements, but that is not guaranteed to pay off, having the EPLB value default to the minimum valid v...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: is a known minimum valid value that can be derived from the vllm startup configuration. Since extra EPLB experts trades kv cache memory for potential performance improvements, but that is not guaranteed to pay off, havi...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
