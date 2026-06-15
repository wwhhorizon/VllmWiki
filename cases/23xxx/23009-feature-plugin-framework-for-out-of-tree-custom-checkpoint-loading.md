# vllm-project/vllm#23009: [Feature]: Plugin framework for out-of-tree custom checkpoint loading

| 字段 | 值 |
| --- | --- |
| Issue | [#23009](https://github.com/vllm-project/vllm/issues/23009) |
| 状态 | closed |
| 标签 | feature request;stale;rl |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Plugin framework for out-of-tree custom checkpoint loading

### Issue 正文摘录

### 🚀 The feature, motivation and pitch ### Motivation Currently, vLLM primarily supports HuggingFace-format checkpoints along with a few built-in custom loaders such as mistral. However, some proprietary reinforcement learning (RL) systems use custom checkpoint and weight formats along with unique loading mechanisms, which creates challenges for adopting vLLM in these environments. Support is required in two key areas (they share some common path): 1. Initial custom weight loading during rollout engine initialization 2. Loading updated custom weights from the actor ### Our attempt We have developed a heavily modified version of vLLM to enable custom checkpoint loading for a specific proprietary format. While this solution works, a clean and maintainable implementation is necessary for production use. Unfortunately, we cannot open-source the internal implementation details or specifications. ### Proposal We propose to build a fully out-of-tree plugin framework to support custom checkpoint/weights loading. This issue is about this OSS part. On top of the plugin framework, we will develop the actual plugins internally. Based on our experience with the hacked version, the following c...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: motivation and pitch ### Motivation Currently, vLLM primarily supports HuggingFace-format checkpoints along with a few built-in custom loaders such as mistral. However, some proprietary reinforcement learning (RL) syste...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: hts from the actor ### Our attempt We have developed a heavily modified version of vLLM to enable custom checkpoint loading for a specific proprietary format. While this solution works, a clean and maintainable implemen...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: se custom checkpoint and weight formats along with unique loading mechanisms, which creates challenges for adopting vLLM in these environments. Support is required in two key areas (they share some common path): 1. Init...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ure]: Plugin framework for out-of-tree custom checkpoint loading feature request;stale;rl ### 🚀 The feature, motivation and pitch ### Motivation Currently, vLLM primarily supports HuggingFace-format checkpoints along wi...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ling points may be required ### How to measure the success 1. Thorough testing within our proprietary RL system 2. As a proof of concept, we could convert one of the built-in loaders, such as mistral (#8168), into an ou...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
