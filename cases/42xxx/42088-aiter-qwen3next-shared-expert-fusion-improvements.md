# vllm-project/vllm#42088: [aiter] Qwen3Next shared expert fusion improvements

| 字段 | 值 |
| --- | --- |
| Issue | [#42088](https://github.com/vllm-project/vllm/issues/42088) |
| 状态 | open |
| 标签 | feature request |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [aiter] Qwen3Next shared expert fusion improvements

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Related to https://github.com/vllm-project/vllm/pull/39280 To have a PR by 13th of May at the latest. - [ ] Move the gate concatenation to be in the qwen3next specific code rather than additional logic in the MoERunner [vllm/model_executor/layers/fused_moe/runner/moe_runner.py](https://github.com/vllm-project/vllm/pull/39280/files/3f7875d5d2a028354296467bcc8b7c6f573027bb#diff-e4f7854e5c7b372f38317b0886343a226e388c9ffd9851f55d685a6e465b1a84) - [ ] Cleanup saved an unnecessary attributes of FusedMoE that are saved in the constructor and never used. https://github.com/vllm-project/vllm/pull/39280/files/e5c041d0798bf242eb41c3a9ab4b9099e6cbf6d7#diff-eddafffeb6f159f8c75f635d18a502fcfbf662a562b1ae7a8683a9790161a10b - [ ] Move inject_shared_experts_weight to [vllm/model_executor/layers/fused_moe/router/aiter_shared_routed_fused_moe_router.py](https://github.com/vllm-project/vllm/pull/39280/files/e5c041d0798bf242eb41c3a9ab4b9099e6cbf6d7#diff-19717e18d6aa070a2d94709ab2561447651e2ba6e84d5257f7ce4a44d8c73646) - [ ] Audit and prevent breaking uses in the future of `create_fused_moe_router` primarily in relation to shared expert fusion and the scoring fun...

## 候选优化模式

- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: [aiter] Qwen3Next shared expert fusion improvements feature request ### 🚀 The feature, motivation and pitch Related to https://github.com/vllm-project/vllm/pull/39280 To have a PR by 13th of May at the latest. - [ ] Mov...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [aiter] Qwen3Next shared expert fusion improvements feature request ### 🚀 The feature, motivation and pitch Related to https://github.com/vllm-project/vllm/pull/39280 To have a PR by 13th of May at the latest. - [ ] Mov...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: [aiter] Qwen3Next shared expert fusion improvements feature request ### 🚀 The feature, motivation and pitch Related to https://github.com/vllm-project/vllm/pull/39280 To have a PR by 13th of May at the latest. - [ ] Mo
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: the latest. - [ ] Move the gate concatenation to be in the qwen3next specific code rather than additional logic in the MoERunner [vllm/model_executor/layers/fused_moe/runner/moe_runner.py](https://github.com/vllm-projec...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
