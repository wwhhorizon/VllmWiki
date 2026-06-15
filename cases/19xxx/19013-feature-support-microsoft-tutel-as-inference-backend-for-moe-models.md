# vllm-project/vllm#19013: [Feature]: support Microsoft Tutel as inference backend for Moe models

| 字段 | 值 |
| --- | --- |
| Issue | [#19013](https://github.com/vllm-project/vllm/issues/19013) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: support Microsoft Tutel as inference backend for Moe models

### Issue 正文摘录

### 🚀 The feature, motivation and pitch https://github.com/microsoft/Tutel it can speed up Deepseek-R1 inference to 80TPS in single request on 8*a100s, it is awesome. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: el it can speed up Deepseek-R1 inference to 80TPS in single request on 8*a100s, it is awesome. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: re]: support Microsoft Tutel as inference backend for Moe models feature request;stale ### 🚀 The feature, motivation and pitch https://github.com/microsoft/Tutel it can speed up Deepseek-R1 inference to 80TPS in single...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: [Feature]: support Microsoft Tutel as inference backend for Moe models feature request;stale ### 🚀 The feature, motivation and pitch https://github.com/microsoft/Tutel it can speed up Deepseek-R1 inference to 80TPS in s...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Feature]: support Microsoft Tutel as inference backend for Moe models feature request;stale ### 🚀 The feature, motivation and pitch https://github.com/microsoft/Tutel it can speed up Deepseek-R1 inference to 80TPS in s...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: [Feature]: support Microsoft Tutel as inference backend for Moe models feature request;stale ### 🚀 The feature, motivation and pitch https://github.com/microsoft/Tutel it can speed up Deepseek-R1 inference to 80TPS in s...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
