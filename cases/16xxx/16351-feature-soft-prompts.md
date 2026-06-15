# vllm-project/vllm#16351: [Feature]: Soft Prompts?

| 字段 | 值 |
| --- | --- |
| Issue | [#16351](https://github.com/vllm-project/vllm/issues/16351) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Soft Prompts?

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Soft prompts would be similar to Loras in that they are artifacts from a parameter efficient training process that live on the server where vLLM is running. But unlike Loras, which require being set or unset as a global state that affects all requests, soft prompts could be part of the `generate` call. This would allow a single vLLM server to respond to many different fine tuned tasks I see someone tried something a long time ago but abandoned it. (PR #815 https://github.com/vllm-project/vllm/pull/815) ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: Soft Prompts? feature request;stale ### 🚀 The feature, motivation and pitch Soft prompts would be similar to Loras in that they are artifacts from a parameter efficient training process that live on the serve...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ould be similar to Loras in that they are artifacts from a parameter efficient training process that live on the server where vLLM is running. But unlike Loras, which require being set or unset as a global state that af...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
