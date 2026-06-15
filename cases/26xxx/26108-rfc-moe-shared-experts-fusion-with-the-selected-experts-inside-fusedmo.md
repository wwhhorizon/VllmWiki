# vllm-project/vllm#26108: [RFC]: MoE shared_experts fusion with the selected experts inside FusedMoE

| 字段 | 值 |
| --- | --- |
| Issue | [#26108](https://github.com/vllm-project/vllm/issues/26108) |
| 状态 | closed |
| 标签 | RFC;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: MoE shared_experts fusion with the selected experts inside FusedMoE

### Issue 正文摘录

### Motivation. Profile results for DeepSeekR1 show that a significant amount of decode-iteration time is spend in executing the shared_experts of MoE before the "selected_experts" FusedMoE part. To reduce the overhead of shared_experts, their execution can be fused with the selected_experts (by combining the weight matrices) and then executing a single FusedMoE part. ### Proposed Change. Here are the profile results for FP4 and FP8 (we can see operation breakdown for a single transformer decode-iteration) (flags used VLLM_USE_FLASHINFER_MOE_FP8=1 and VLLM_FLASHINFER_MOE_BACKEND="latency"): **DeepSeekR1-FP4 8xB200 batch-size 32** **DeepSeekR1-FP8 8xB200 batch-size 32** From this profile we can see that fusing shared_experts with selected_experts matrix multiplies will have the following benefits: 1. Removes data converts FP16=>FP4/FP8 that we currently do in shared experts, since we will do them in the FusedMoE part anyway. 2. The silu op in shared experts is composed of 2 elementwise ops, and fusion will remove it completely. 3. Willl allow to execute the shared_experts inside the highly optimized FusedMoE part (not using the DeepseekV2MLP class from deepseek_v2.py) Notes/TODOs:...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: FusedMoE part. ### Proposed Change. Here are the profile results for FP4 and FP8 (we can see operation breakdown for a single transformer decode-iteration) (flags used VLLM_USE_FLASHINFER_MOE_FP8=1 and VLLM_FLASHINFER_M...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: ion with the selected experts inside FusedMoE RFC;stale ### Motivation. Profile results for DeepSeekR1 show that a significant amount of decode-iteration time is spend in executing the shared_experts of MoE before the "...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: reakdown for a single transformer decode-iteration) (flags used VLLM_USE_FLASHINFER_MOE_FP8=1 and VLLM_FLASHINFER_MOE_BACKEND="latency"): **DeepSeekR1-FP4 8xB200 batch-size 32** **DeepSeekR1-FP8 8xB200 batch-size 32** F...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: OE_FP8=1 and VLLM_FLASHINFER_MOE_BACKEND="latency"): **DeepSeekR1-FP4 8xB200 batch-size 32** **DeepSeekR1-FP8 8xB200 batch-size 32** From this profile we can see that fusing shared_experts with selected_experts matrix m...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: [RFC]: MoE shared_experts fusion with the selected experts inside FusedMoE RFC;stale ### Motivation. Profile results for DeepSeekR1 show that a significant amount of decode-iteration time is spend in executing the share...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
