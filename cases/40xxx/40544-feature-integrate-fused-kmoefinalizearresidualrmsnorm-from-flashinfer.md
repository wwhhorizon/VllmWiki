# vllm-project/vllm#40544: [Feature]: Integrate fused `kMoEFinalizeARResidualRMSNorm` from FlashInfer

| 字段 | 值 |
| --- | --- |
| Issue | [#40544](https://github.com/vllm-project/vllm/issues/40544) |
| 状态 | open |
| 标签 | help wanted;feature request |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Integrate fused `kMoEFinalizeARResidualRMSNorm` from FlashInfer

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Available today via FlashInfer 0.6.8, we can leverage this fused MoE Finalize + ResidualAdd + AllReduce + RMSNorm https://github.com/flashinfer-ai/flashinfer/pull/2982. This should be added as a new torch.compile custom pass. I think moe_finalize might still be inside the wrapped fused_moe op so this might require pulling that out. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: [Feature]: Integrate fused `kMoEFinalizeARResidualRMSNorm` from FlashInfer help wanted;feature request ### 🚀 The feature, motivation and pitch Available today via FlashInfer 0.6.8, we can leverage this fused MoE Finaliz...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: flashinfer-ai/flashinfer/pull/2982. This should be added as a new torch.compile custom pass. I think moe_finalize might still be inside the wrapped fused_moe op so this might require pulling that out. ### Alternatives _...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: [Feature]: Integrate fused `kMoEFinalizeARResidualRMSNorm` from FlashInfer help wanted;feature request ### 🚀 The feature, motivation and pitch Available today via FlashInfer 0.6.8, we can leverage this fused MoE Finaliz...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: used `kMoEFinalizeARResidualRMSNorm` from FlashInfer help wanted;feature request ### 🚀 The feature, motivation and pitch Available today via FlashInfer 0.6.8, we can leverage this fused MoE Finalize + ResidualAdd + AllR...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
