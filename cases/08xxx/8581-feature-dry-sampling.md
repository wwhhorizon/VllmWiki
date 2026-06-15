# vllm-project/vllm#8581: [Feature]: DRY Sampling

| 字段 | 值 |
| --- | --- |
| Issue | [#8581](https://github.com/vllm-project/vllm/issues/8581) |
| 状态 | open |
| 标签 | feature request;unstale |
| 评论 | 27; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: DRY Sampling

### Issue 正文摘录

### 🚀 The feature, motivation and pitch DRY is a sampler that completely mitigates repetitions. This is especially important for small models which tend to slop in large contexts. Here's an explanation of DRY from the author himself https://github.com/oobabooga/text-generation-webui/pull/5677 Along with oobabooga, koboldcpp also has an implementation of DRY which according to author IIRC is better than oobabooga's DRY has been a completely game changer for me and from what I have seen several others. It completely removes need for other samplers like top_p, top_k, repetition_penalty. It is recommended to be used with min_p and produces great coherent results. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: tch DRY is a sampler that completely mitigates repetitions. This is especially important for small models which tend to slop in large contexts. Here's an explanation of DRY from the author himself https://github.com/oob...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: that completely mitigates repetitions. This is especially important for small models which tend to slop in large contexts. Here's an explanation of DRY from the author himself https://github.com/oobabooga/text-generatio...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: DRY Sampling feature request;unstale ### 🚀 The feature, motivation and pitch DRY is a sampler that completely mitigates repetitions. This is especially important for small models which tend to slop in large c...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: completely mitigates repetitions. This is especially important for small models which tend to slop in large contexts. Here's an explanation of DRY from the author himself https://github.com/oobabooga/text-generation-web...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
