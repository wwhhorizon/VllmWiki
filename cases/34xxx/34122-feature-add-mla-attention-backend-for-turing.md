# vllm-project/vllm#34122: [Feature]: Add MLA attention backend for Turing

| 字段 | 值 |
| --- | --- |
| Issue | [#34122](https://github.com/vllm-project/vllm/issues/34122) |
| 状态 | open |
| 标签 | feature request;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Add MLA attention backend for Turing

### Issue 正文摘录

### 🚀 The feature, motivation and pitch The TRITON_MLA attention backend is used by MLA models (such as GLM-4.7-FLASH) if GPU is Turing, but it Using FlashAttention prefill for MLA. NoTRITON or other prefill is implementd in TRITON_MLA to supported turing. Please help to support MLA on Turing. Thanks. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: [Feature]: Add MLA attention backend for Turing feature request;stale ### 🚀 The feature, motivation and pitch The TRITON_MLA attention backend is used by MLA models (such as GLM-4.7-FLASH) if GPU is Turing, but it Using...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Feature]: Add MLA attention backend for Turing feature request;stale ### 🚀 The feature, motivation and pitch The TRITON_MLA attention backend is used by MLA models (such as GLM-4.7-FLASH) if GPU is Turing, but it Using...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: e, motivation and pitch The TRITON_MLA attention backend is used by MLA models (such as GLM-4.7-FLASH) if GPU is Turing, but it Using FlashAttention prefill for MLA. NoTRITON or other prefill is implementd in TRITON_MLA...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
