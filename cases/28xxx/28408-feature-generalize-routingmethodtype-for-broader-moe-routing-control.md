# vllm-project/vllm#28408: [Feature]: Generalize RoutingMethodType for broader MoE routing control

| 字段 | 值 |
| --- | --- |
| Issue | [#28408](https://github.com/vllm-project/vllm/issues/28408) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Generalize RoutingMethodType for broader MoE routing control

### Issue 正文摘录

### 🚀 The feature, motivation and pitch PR #27492 introduced `RoutingMethodType` to support different routing methods for FP8 flashinfer TRTLLM MOE (DeepSeekV3, Llama4, Renormalize, etc.). While this was implemented to support Qwen3 and Qwen3-next models, the review discussion revealed opportunities to use this more broadly across the codebase to simplify MoE routing configuration. ### Motivation: Currently, MoE routing behavior is controlled through multiple fragmented parameters (scoring_func, renormalize, use_grouped_topk, custom routing functions, etc.). This creates several issues: 1. Lack of clarity: The routing method isn't explicitly defined in one place 2. Code duplication: Each model must explicitly specify routing parameters 3. Maintenance burden: Adding new routing methods requires updates across multiple locations 4. Tight coupling: Current implementation is tied to flashinfer's specific enum values As noted by @mgoin: "I like the idea of having a routing method type so we can reduce the need for hacks like checking the llama 4 custom routing function within the quant method... I think if we do this right, we can actually remove other arguments we have in FusedMoE suc...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: ort different routing methods for FP8 flashinfer TRTLLM MOE (DeepSeekV3, Llama4, Renormalize, etc.). While this was implemented to support Qwen3 and Qwen3-next models, the review discussion revealed opportunities to use...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 4: [Feature]: Generalize RoutingMethodType for broader MoE routing control feature request;stale ### 🚀 The feature, motivation and pitch PR #27492 introduced `RoutingMethodType` to support different routing methods for FP8...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: [Feature]: Generalize RoutingMethodType for broader MoE routing control feature request;stale ### 🚀 The feature, motivation and pitch PR #27492 introduced `RoutingMethodType` to support different routing methods for FP8...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Feature]: Generalize RoutingMethodType for broader MoE routing control feature request;stale ### 🚀 The feature, motivation and pitch PR #27492 introduced `RoutingMethodType` to support different routing methods for FP8...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: e]: Generalize RoutingMethodType for broader MoE routing control feature request;stale ### 🚀 The feature, motivation and pitch PR #27492 introduced `RoutingMethodType` to support different routing methods for FP8 flashi...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
