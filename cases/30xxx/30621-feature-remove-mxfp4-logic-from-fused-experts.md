# vllm-project/vllm#30621: [Feature]: Remove MXFP4 Logic From `fused_experts`

| 字段 | 值 |
| --- | --- |
| Issue | [#30621](https://github.com/vllm-project/vllm/issues/30621) |
| 状态 | closed |
| 标签 | help wanted;good first issue;feature request;stale |
| 评论 | 16; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Remove MXFP4 Logic From `fused_experts`

### Issue 正文摘录

### 🚀 The feature, motivation and pitch SUMMARY: * as part of effort to refactor MoE, trying to reduce cruft * we currently only have MX emulation in vLLM * the logic for this emulation should be moved into quark https://github.com/vllm-project/vllm/blame/main/vllm/model_executor/layers/fused_moe/fused_moe.py#L1866-L1899 ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: [Feature]: Remove MXFP4 Logic From `fused_experts` help wanted;good first issue;feature request;stale ### 🚀 The feature, motivation and pitch SUMMARY: * as part of effort to refactor MoE, trying to reduce cruft * we cur...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: [Feature]: Remove MXFP4 Logic From `fused_experts` help wanted;good first issue;feature request;stale ### 🚀 The feature, motivation and pitch SUMMARY: * as part of effort to refactor MoE, trying to reduce cruft * we cur...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ve MXFP4 Logic From `fused_experts` help wanted;good first issue;feature request;stale ### 🚀 The feature, motivation and pitch SUMMARY: * as part of effort to refactor MoE, trying to reduce cruft * we currently only hav...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: e moved into quark https://github.com/vllm-project/vllm/blame/main/vllm/model_executor/layers/fused_moe/fused_moe.py#L1866-L1899 ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
