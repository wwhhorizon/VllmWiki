# vllm-project/vllm#11372: [Feature]: Will vLLM support flash-attention 3 ?

| 字段 | 值 |
| --- | --- |
| Issue | [#11372](https://github.com/vllm-project/vllm/issues/11372) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Will vLLM support flash-attention 3 ?

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Flash attention 3 seems very promising for running efficient LLM inference on NVIDIA Hopper cards. Are there any plans to support it in the future ? https://github.com/Dao-AILab/flash-attention ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ion 3 seems very promising for running efficient LLM inference on NVIDIA Hopper cards. Are there any plans to support it in the future ? https://github.com/Dao-AILab/flash-attention ### Alternatives _No response_ ### Ad...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: h-attention 3 ? feature request ### 🚀 The feature, motivation and pitch Flash attention 3 seems very promising for running efficient LLM inference on NVIDIA Hopper cards. Are there any plans to support it in the future...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: vation and pitch Flash attention 3 seems very promising for running efficient LLM inference on NVIDIA Hopper cards. Are there any plans to support it in the future ? https://github.com/Dao-AILab/flash-attention ### Alte...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature]: Will vLLM support flash-attention 3 ? feature request ### 🚀 The feature, motivation and pitch Flash attention 3 seems very promising for running efficient LLM inference on NVIDIA Hopper cards. Are there any p...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
