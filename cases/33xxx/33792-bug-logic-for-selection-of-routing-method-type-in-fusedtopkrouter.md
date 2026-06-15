# vllm-project/vllm#33792: [Bug]: Logic for selection of routing_method_type in FusedTopKRouter

| 字段 | 值 |
| --- | --- |
| Issue | [#33792](https://github.com/vllm-project/vllm/issues/33792) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Logic for selection of routing_method_type in FusedTopKRouter

### Issue 正文摘录

### Your current environment Current environment not relevant, bug affects `main`, currently `f67ee8b859215df4b521c67b9f26e27f30c9739f`. ### 🐛 Describe the bug The logic for the selection of `routing_method_type` in [`fused_topk_router.py`](https://github.com/vllm-project/vllm/blob/main/vllm/model_executor/layers/fused_moe/router/fused_topk_router.py#L137) does not match the definition of the Flashinfer [`RoutingMethodType`](https://github.com/flashinfer-ai/flashinfer/blob/main/flashinfer/fused_moe/core.py#L61)s. Fixing this would allow more models to use the Flashinfer TRTLLMGen kernels, potentially accelerating them. Currently the code reads as follows: ```python @property def routing_method_type(self) -> RoutingMethodType: return ( RoutingMethodType.Renormalize if not self.renormalize else RoutingMethodType.RenormalizeNaive ) ``` To implement the logic from Flashinfer, the logic would be similar to this: ```python @property def routing_method_type(self) -> RoutingMethodType: if self.scoring_func == "sigmoid": if self.top_k == 1: return RoutingMethodType.Llama4 else: return RoutingMethodType.DeepSeekV3 elif self.scoring_func == "softmax": if self.renormalize: return RoutingMetho...

## 候选优化模式

- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 4: [Bug]: Logic for selection of routing_method_type in FusedTopKRouter bug ### Your current environment Current environment not relevant, bug affects `main`, currently `f67ee8b859215df4b521c67b9f26e27f30c9739f`. ### 🐛 Des...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: [Bug]: Logic for selection of routing_method_type in FusedTopKRouter bug ### Your current environment Current environment not relevant, bug affects `main`, currently `f67ee8b859215df4b521c67b9f26e27f30c9739f`. ### 🐛 Des...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ot a vLLM-internal routing type. Although the above changes in code are small, the default backend would change to Flashinfer TRTLLMGen for multiple models, which would need to be validated to prevent bugs. ### Before s...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: gMethodType.Renormalize if not self.renormalize else RoutingMethodType.RenormalizeNaive ) ``` To implement the logic from Flashinfer, the logic would be similar to this: ```python @property def routing_method_type(self)...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: sed_topk_router.py`](https://github.com/vllm-project/vllm/blob/main/vllm/model_executor/layers/fused_moe/router/fused_topk_router.py#L137) does not match the definition of the Flashinfer [`RoutingMethodType`](https://gi...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
