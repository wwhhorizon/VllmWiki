# vllm-project/vllm#41045: [Feature] [NVFP4]: Unfused global scales for microscale quantization

| 字段 | 值 |
| --- | --- |
| Issue | [#41045](https://github.com/vllm-project/vllm/issues/41045) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature] [NVFP4]: Unfused global scales for microscale quantization

### Issue 正文摘录

### 🚀 The feature, motivation and pitch ## Background ## Currently, FP4 kernels in vLLM require that global scales from different partitions are fused into a single global scale for the fused weight ([source](https://github.com/vllm-project/vllm/blob/main/vllm/model_executor/layers/quantization/compressed_tensors/schemes/compressed_tensors_w4a4_nvfp4.py#L105-L113)). This is a reasonable ask from a performance perspective, but complicates upstream PTQ flows such as LLM Compressor and may lead to unnecessary accuracy loss. Specifically, LLM Compressor has to take a performance hit in order to calculate global scales before local scales, and could see better accuracy recovery from more granular global scales (with minimal runtime cost). ## Proposed Changes ## I propose supporting unfused global scales by utilizing the `Sm90RowOrScalarBroadcast` cutlass template. Each column has a alpha value which are populated from the partition global scales. https://github.com/vllm-project/vllm/compare/main...neuralmagic:vllm:kylesayrs/nvfp4-unfused-global-scale?expand=1 ## Remaining Questions ## * What is the performance cost of loading per-column global scales? * What is the accuracy improve fro...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: [Feature] [NVFP4]: Unfused global scales for microscale quantization feature request ### 🚀 The feature, motivation and pitch ## Background ## Currently, FP4 kernels in vLLM require that global scales from different part...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: Changes ## I propose supporting unfused global scales by utilizing the `Sm90RowOrScalarBroadcast` cutlass template. Each column has a alpha value which are populated from the partition global scales. https://github.com/...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: es upstream PTQ flows such as LLM Compressor and may lead to unnecessary accuracy loss. Specifically, LLM Compressor has to take a performance hit in order to calculate global scales before local scales, and could see b...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: orting unfused global scales by utilizing the `Sm90RowOrScalarBroadcast` cutlass template. Each column has a alpha value which are populated from the partition global scales. https://github.com/vllm-project/vllm/compare...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: es upstream PTQ flows such as LLM Compressor and may lead to unnecessary accuracy loss. Specifically, LLM Compressor has to take a performance hit in order to calculate global scales before local scales, and could see b...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
