# vllm-project/vllm#30694: [Feature]: CompressedTensors: NVFP4A16 not supported for MoE models

| 字段 | 值 |
| --- | --- |
| Issue | [#30694](https://github.com/vllm-project/vllm/issues/30694) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: CompressedTensors: NVFP4A16 not supported for MoE models

### Issue 正文摘录

### 🚀 The feature, motivation and pitch NVFP4A16 (W4A16 FP4) quantization via compressed_tensors works for dense models but fails on MoE models like Qwen3-30B-A3B. Looking at `compressed_tensors_moe.py`, `_is_fp4a16_nvfp4` is checked for Linear layers but not in `get_moe_method()` for FusedMoE. Only W4A4 has a MoE method (`CompressedTensorsW4A4Nvfp4MoEMethod`). Since the Marlin kernel already supports FP4 weights + FP16 activations, is there a plan to add W4A16 MoE support for compressed_tensors? ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Feature]: CompressedTensors: NVFP4A16 not supported for MoE models feature request;stale ### 🚀 The feature, motivation and pitch NVFP4A16 (W4A16 FP4) quantization via compressed_tensors works for dense models but fails...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Feature]: CompressedTensors: NVFP4A16 not supported for MoE models feature request;stale ### 🚀 The feature, motivation and pitch NVFP4A16 (W4A16 FP4) quantization via compressed_tensors works for dense models but fails...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ature]: CompressedTensors: NVFP4A16 not supported for MoE models feature request;stale ### 🚀 The feature, motivation and pitch NVFP4A16 (W4A16 FP4) quantization via compressed_tensors works for dense models but fails on...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: [Feature]: CompressedTensors: NVFP4A16 not supported for MoE models feature request;stale ### 🚀 The feature, motivation and pitch NVFP4A16 (W4A16 FP4) quantization via compressed_tensors works for dense models but fails...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
