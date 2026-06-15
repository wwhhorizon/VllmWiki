# vllm-project/vllm#33301: [RFC]: Support FP8 LoRA inference

| 字段 | 值 |
| --- | --- |
| Issue | [#33301](https://github.com/vllm-project/vllm/issues/33301) |
| 状态 | open |
| 标签 | RFC;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Support FP8 LoRA inference

### Issue 正文摘录

### Motivation. Currently, vLLM serves LoRA adapters in FP16/BF16 precision. For large-scale serving scenarios with multiple LoRA adapters, this presents several challenges. This RFC proposes adding FP8 LoRA inference support to vLLM. Experimental results(thanks @linitra24 for the execellent work) demonstrate that directly quantizing FP32 LoRA weights to FP8 format results in negligible precision loss, while FP8 weights significantly reduce memory footprint and can potentially improve throughput. Therefore, we propose promoting FP8 LoRA in vLLM. Expected benefits include: - **Memory:** ~2× memory reduction for LoRA weights compared to FP16/BF16 - **Compatibility:** Works with both dense and MoE architectures, supports `text-only` and `multimodal` models - **Potential performance improvements:** FP8 on modern GPUs (SM89+) can accelerate FP8 matrix multiplication ### Proposed Change. To achieve these goals, we need to: 1. Support loading pre-quantized FP8 LoRA weights @jeejeelee @linitra24 2. Implement FP8 LoRA Triton kernels (Linear/MoE) compatible with at least SM80 GPUs @dcmaddix - MoE LoRA kernel: https://github.com/vllm-project/vllm/pull/30286 3. Support online quantization of...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: lent work) demonstrate that directly quantizing FP32 LoRA weights to FP8 format results in negligible precision loss, while FP8 weights significantly reduce memory footprint and can potentially improve throughput. There...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: [RFC]: Support FP8 LoRA inference RFC;stale ### Motivation. Currently, vLLM serves LoRA adapters in FP16/BF16 precision. For large-scale serving scenarios with multiple LoRA adapters, this presents several challenges. T...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: eights significantly reduce memory footprint and can potentially improve throughput. Therefore, we propose promoting FP8 LoRA in vLLM. Expected benefits include: - **Memory:** ~2× memory reduction for LoRA weights compa...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: compared to FP16/BF16 - **Compatibility:** Works with both dense and MoE architectures, supports `text-only` and `multimodal` models - **Potential performance improvements:** FP8 on modern GPUs (SM89+) can accelerate FP...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: quantized FP8 LoRA weights @jeejeelee @linitra24 2. Implement FP8 LoRA Triton kernels (Linear/MoE) compatible with at least SM80 GPUs @dcmaddix - MoE LoRA kernel: https://github.com/vllm-project/vllm/pull/30286 3. Suppo...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
