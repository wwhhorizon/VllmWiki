# vllm-project/vllm#41611: [Feature]: Close all non gpustack related tickets and route them to provider`s github

| 字段 | 值 |
| --- | --- |
| Issue | [#41611](https://github.com/vllm-project/vllm/issues/41611) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Close all non gpustack related tickets and route them to provider`s github

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Lots of open tickets here blocking real issues with gpustack itself. GPUstack should not be responsible for vLLM, SGlang, llama.cpp backend engines. It should be orchestrator. Can we focus on improving that? :D ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: k itself. GPUstack should not be responsible for vLLM, SGlang, llama.cpp backend engines. It should be orchestrator. Can we focus on improving that? :D ### Alternatives _No response_ ### Additional context _No response_...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: quest ### 🚀 The feature, motivation and pitch Lots of open tickets here blocking real issues with gpustack itself. GPUstack should not be responsible for vLLM, SGlang, llama.cpp backend engines. It should be orchestrato...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: th gpustack itself. GPUstack should not be responsible for vLLM, SGlang, llama.cpp backend engines. It should be orchestrator. Can we focus on improving that? :D ### Alternatives _No response_ ### Additional context _No...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: non gpustack related tickets and route them to provider`s github feature request ### 🚀 The feature, motivation and pitch Lots of open tickets here blocking real issues with gpustack itself. GPUstack should not be respon...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
