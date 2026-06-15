# vllm-project/vllm#28096: [Feature]: Enable DeepSeek-OCR pluginization

| 字段 | 值 |
| --- | --- |
| Issue | [#28096](https://github.com/vllm-project/vllm/issues/28096) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Enable DeepSeek-OCR pluginization

### Issue 正文摘录

### 🚀 The feature, motivation and pitch I’ve noticed that DeepSeek-OCR (which depends on DeepSeekV1) currently uses `fused_topk` and `fused_experts` implemented under Triton. Since vllm-ascend hasn’t fully integrated Triton yet, would it make sense to consider making these two ops plugin-enabled? In addition, I saw that there’s already a `FusedMoE` module capable of supporting operator registration downstream. Would it be feasible to directly use `FusedMoE` as a replacement for `fused_topk` and `fused_experts`? I’ve done some initial experiments, though not fully successful yet. If you could provide some guidance, I’d be happy to submit a PR to help implement this. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: ed that DeepSeek-OCR (which depends on DeepSeekV1) currently uses `fused_topk` and `fused_experts` implemented under Triton. Since vllm-ascend hasn’t fully integrated Triton yet, would it make sense to consider making t...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: eekV1) currently uses `fused_topk` and `fused_experts` implemented under Triton. Since vllm-ascend hasn’t fully integrated Triton yet, would it make sense to consider making these two ops plugin-enabled? In addition, I...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature]: Enable DeepSeek-OCR pluginization feature request ### 🚀 The feature, motivation and pitch I’ve noticed that DeepSeek-OCR (which depends on DeepSeekV1) currently uses `fused_topk` and `fused_experts` implement...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
