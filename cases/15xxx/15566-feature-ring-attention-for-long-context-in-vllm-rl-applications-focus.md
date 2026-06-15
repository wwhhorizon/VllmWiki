# vllm-project/vllm#15566: [Feature]: Ring Attention for Long Context in vLLM - RL Applications Focus

| 字段 | 值 |
| --- | --- |
| Issue | [#15566](https://github.com/vllm-project/vllm/issues/15566) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Ring Attention for Long Context in vLLM - RL Applications Focus

### Issue 正文摘录

### 🚀 The feature, motivation and pitch ## Overview I'm interested in implementing Ring Attention (Liu et al., 2023) in vLLM to enable extremely long context windows that scale with device count. This would be particularly beneficial for RL applications with LLMs, where agents need to process extensive histories of interactions and environments. ## Motivation The growing intersection of RL and LLMs creates a significant need for handling very long contexts. RL agents often need to: - Process extensive trial-and-error histories - Maintain memory of past interactions with environments - Learn from sequential decision-making data ## Question @simon-mo Is adding Ring Attention support to vLLM of interest to the project at this time? ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: Ring Attention for Long Context in vLLM - RL Applications Focus feature request;stale ### 🚀 The feature, motivation and pitch ## Overview I'm interested in implementing Ring Attention (Liu et al., 2023) in vLLM to enabl...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: t windows that scale with device count. This would be particularly beneficial for RL applications with LLMs, where agents need to process extensive histories of interactions and environments. ## Motivation The growing i...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: (Liu et al., 2023) in vLLM to enable extremely long context windows that scale with device count. This would be particularly beneficial for RL applications with LLMs, where agents need to process extensive histories of...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
