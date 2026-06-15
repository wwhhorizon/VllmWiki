# vllm-project/vllm#30620: [Feature]: Remove Chunking From FusedMoE

| 字段 | 值 |
| --- | --- |
| Issue | [#30620](https://github.com/vllm-project/vllm/issues/30620) |
| 状态 | closed |
| 标签 | help wanted;good first issue;feature request |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Remove Chunking From FusedMoE

### Issue 正文摘录

### 🚀 The feature, motivation and pitch * we have some chunking logic in the triton kernels to avoid IMA: https://github.com/vllm-project/vllm/blob/main/vllm/model_executor/layers/fused_moe/fused_moe.py#L1807 * we chunk in ~65k tokens * this case does not happen anymore because of chunked prefill We should remove this ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ure]: Remove Chunking From FusedMoE help wanted;good first issue;feature request ### 🚀 The feature, motivation and pitch * we have some chunking logic in the triton kernels to avoid IMA: https://github.com/vllm-project/...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: The feature, motivation and pitch * we have some chunking logic in the triton kernels to avoid IMA: https://github.com/vllm-project/vllm/blob/main/vllm/model_executor/layers/fused_moe/fused_moe.py#L1807 * we chunk in ~6...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ernels to avoid IMA: https://github.com/vllm-project/vllm/blob/main/vllm/model_executor/layers/fused_moe/fused_moe.py#L1807 * we chunk in ~65k tokens * this case does not happen anymore because of chunked prefill We sho...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: [Feature]: Remove Chunking From FusedMoE help wanted;good first issue;feature request ### 🚀 The feature, motivation and pitch * we have some chunking logic in the triton kernels to avoid IMA: https://github.com/vllm-pro...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
