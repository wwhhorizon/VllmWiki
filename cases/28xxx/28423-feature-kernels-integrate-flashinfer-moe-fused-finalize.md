# vllm-project/vllm#28423: [Feature][Kernels]: Integrate FlashInfer MoE Fused Finalize

| 字段 | 值 |
| --- | --- |
| Issue | [#28423](https://github.com/vllm-project/vllm/issues/28423) |
| 状态 | closed |
| 标签 | feature request;torch.compile |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature][Kernels]: Integrate FlashInfer MoE Fused Finalize

### Issue 正文摘录

### 🚀 The feature, motivation and pitch We are working on fusing all small ops in DSR1 and other popular models. There are open work streams on a couple of these: - RMSNorm + BlockFP8 - ROPE+KV Insert - All Reduce + RMSNorm One other one that is possible is fusing the MoE finalize reduction. Here is an op in FlashInfer: - https://github.com/flashinfer-ai/flashinfer/blob/d42fb90ee59d269b77b218a93467f8af58756eba/flashinfer/comm/trtllm_ar.py#L349 - So this would fuse the application + reduction of the topk weights onto the shared and routed experts in MoE layers - Here's an example trace cc @ProExpertProg ### Alternatives none ### Additional context https://vllm-dev.slack.com/archives/C08NFPURQ1F/p1762802402502609 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: [Feature][Kernels]: Integrate FlashInfer MoE Fused Finalize feature request;torch.compile ### 🚀 The feature, motivation and pitch We are working on fusing all small ops in DSR1 and other popular models. There are open w...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: le ### 🚀 The feature, motivation and pitch We are working on fusing all small ops in DSR1 and other popular models. There are open work streams on a couple of these: - RMSNorm + BlockFP8 - ROPE+KV Insert - All Reduce +...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: [Feature][Kernels]: Integrate FlashInfer MoE Fused Finalize feature request;torch.compile ### 🚀 The feature, motivation and pitch We are working on fusing all small ops in DSR1 and other popular models. There are open w...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: [Kernels]: Integrate FlashInfer MoE Fused Finalize feature request;torch.compile ### 🚀 The feature, motivation and pitch We are working on fusing all small ops in DSR1 and other popular models. There are open work strea...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: els. There are open work streams on a couple of these: - RMSNorm + BlockFP8 - ROPE+KV Insert - All Reduce + RMSNorm One other one that is possible is fusing the MoE finalize reduction. Here is an op in FlashInfer: - htt...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
