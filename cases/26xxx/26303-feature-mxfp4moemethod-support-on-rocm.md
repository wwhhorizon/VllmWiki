# vllm-project/vllm#26303: [Feature]: `Mxfp4MoEMethod` support on ROCm

| 字段 | 值 |
| --- | --- |
| Issue | [#26303](https://github.com/vllm-project/vllm/issues/26303) |
| 状态 | closed |
| 标签 | feature request;rocm;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: `Mxfp4MoEMethod` support on ROCm

### Issue 正文摘录

### 🚀 The feature, motivation and pitch As per title. ROCm supports MXFP4 models quantized with Quark quantizer in https://github.com/vllm-project/vllm/blob/main/vllm/model_executor/layers/quantization/quark/schemes/quark_w4a4_mxfp4.py, but AFAIK the logic in https://github.com/vllm-project/vllm/blob/main/vllm/model_executor/layers/quantization/mxfp4.py is not tested on amd gpus. Should be interesting to support, might do sometime ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Feature]: `Mxfp4MoEMethod` support on ROCm feature request;rocm;stale ### 🚀 The feature, motivation and pitch As per title. ROCm supports MXFP4 models quantized with Quark quantizer in https://github.com/vllm-project/v...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Feature]: `Mxfp4MoEMethod` support on ROCm feature request;rocm;stale ### 🚀 The feature, motivation and pitch As per title. ROCm supports MXFP4 models quantized with Quark quantizer in https://github.com/vllm-project/v...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: `Mxfp4MoEMethod` support on ROCm feature request;rocm;stale ### 🚀 The feature, motivation and pitch As per title. ROCm supports MXFP4 models quantized with Quark quantizer in https://github.com/vllm-project/v...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: 🚀 The feature, motivation and pitch As per title. ROCm supports MXFP4 models quantized with Quark quantizer in https://github.com/vllm-project/vllm/blob/main/vllm/model_executor/layers/quantization/quark/schemes/quark_w...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: [Feature]: `Mxfp4MoEMethod` support on ROCm feature request;rocm;stale ### 🚀 The feature, motivation and pitch As per title. ROCm supports MXFP4 models quantized with Quark quantizer in https://github.com/vllm-project/v...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
