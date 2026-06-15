# vllm-project/vllm#21313: [Feature]: Support Anthropic API `/v1/messages` endpoint

| 字段 | 值 |
| --- | --- |
| Issue | [#21313](https://github.com/vllm-project/vllm/issues/21313) |
| 状态 | closed |
| 标签 | good first issue;feature request |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Support Anthropic API `/v1/messages` endpoint

### Issue 正文摘录

### 🚀 The feature, motivation and pitch We need to add support for Anthropic API, at least for the [`/v1/messages` endpoint](https://docs.anthropic.com/en/api/messages), in order to support applications that depend on it like [Claude Code](https://github.com/anthropics/claude-code). There are routers that implement the endpoint by wrapping the OpenAI api server from vLLM, like https://github.com/musistudio/claude-code-router and https://github.com/1rgs/claude-code-proxy I'm not sure the difficulty, but I think it shouldn't be difficult and hopefully should be able to be added as a new endpoint within `vllm serve` ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: ike [Claude Code](https://github.com/anthropics/claude-code). There are routers that implement the endpoint by wrapping the OpenAI api server from vLLM, like https://github.com/musistudio/claude-code-router and https://...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: : Support Anthropic API `/v1/messages` endpoint good first issue;feature request ### 🚀 The feature, motivation and pitch We need to add support for Anthropic API, at least for the [`/v1/messages` endpoint](https://docs....
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
