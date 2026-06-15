# vllm-project/vllm#25486: [Feature]: Support BF16/FP16 FlashInfer CUTLASS MoE for SM90/SM100

| 字段 | 值 |
| --- | --- |
| Issue | [#25486](https://github.com/vllm-project/vllm/issues/25486) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Support BF16/FP16 FlashInfer CUTLASS MoE for SM90/SM100

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Currently when running unquantized mixture of experts models, vLLM only has the option of a Triton-based fused_moe kernel https://github.com/vllm-project/vllm/blob/a903669e10cc98507fa5c2ae099b7161f7140cf7/vllm/model_executor/layers/fused_moe/fused_moe.py#L270-L271 This Triton fused_moe requires extensive tuning for good performance, with the configs tuned for each hardware device X num_experts X hidden_dim X batch_size stored in https://github.com/vllm-project/vllm/tree/main/vllm/model_executor/layers/fused_moe/configs FlashInfer has a `cutlass_fused_moe` implementation (https://github.com/flashinfer-ai/flashinfer/blob/main/flashinfer/fused_moe/core.py) for SM90+SM100 that we currently use for FP8, NVFP4, and MXFP4 models that is performant. However it has support for many other dtypes, such as bfloat16 for unquantized models. ```python input : torch.Tensor Input tensor of shape [num_tokens, hidden_size]. Support float, float16, bfloat16, float8_e4m3fn and nvfp4. For FP8, the input must be quantized. For NVFP4, both quantized and non-quantized inputs are supported. ``` I think we should investigate integrating FlashInfer MoE as an option for...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 9: [Feature]: Support BF16/FP16 FlashInfer CUTLASS MoE for SM90/SM100 feature request;stale ### 🚀 The feature, motivation and pitch Currently when running unquantized mixture of experts models, vLLM only has the option of...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: [Feature]: Support BF16/FP16 FlashInfer CUTLASS MoE for SM90/SM100 feature request;stale ### 🚀 The feature, motivation and pitch Currently when running unquantized mixture of experts models, vLLM only has the option of...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Feature]: Support BF16/FP16 FlashInfer CUTLASS MoE for SM90/SM100 feature request;stale ### 🚀 The feature, motivation and pitch Currently when running unquantized mixture of experts models, vLLM only has the option of...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ivation and pitch Currently when running unquantized mixture of experts models, vLLM only has the option of a Triton-based fused_moe kernel https://github.com/vllm-project/vllm/blob/a903669e10cc98507fa5c2ae099b7161f7140...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: [Feature]: Support BF16/FP16 FlashInfer CUTLASS MoE for SM90/SM100 feature request;stale ### 🚀 The feature, motivation and pitch Currently when running unquantized mixture of experts models, vLLM only has the option of...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
