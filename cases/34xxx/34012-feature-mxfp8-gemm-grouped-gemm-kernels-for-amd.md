# vllm-project/vllm#34012: [Feature]: MXFP8 GEMM / Grouped GEMM Kernels for AMD

| 字段 | 值 |
| --- | --- |
| Issue | [#34012](https://github.com/vllm-project/vllm/issues/34012) |
| 状态 | open |
| 标签 | feature request;rocm;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: MXFP8 GEMM / Grouped GEMM Kernels for AMD

### Issue 正文摘录

### 🚀 The feature, motivation and pitch vLLM does not currently support serving MXFP8 quantized dense/MoE models on AMD gpus. It would be great to to add the required MXFP8 GEMM / Grouped GEMM kernels to enable serving MXFP8 dense and MoE models on AMD gpus. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: [Feature]: MXFP8 GEMM / Grouped GEMM Kernels for AMD feature request;rocm;stale ### 🚀 The feature, motivation and pitch vLLM does not currently support serving MXFP8 quantized dense/MoE models on AMD gpus. It would be g...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: [Feature]: MXFP8 GEMM / Grouped GEMM Kernels for AMD feature request;rocm;stale ### 🚀 The feature, motivation and pitch vLLM does not currently support serving MXFP8 quantized dense/MoE models on AMD gpus. It would be g...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Feature]: MXFP8 GEMM / Grouped GEMM Kernels for AMD feature request;rocm;stale ### 🚀 The feature, motivation and pitch vLLM does not currently support serving MXFP8 quantized dense/MoE models on AMD gpus. It would be g...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: MXFP8 GEMM / Grouped GEMM Kernels for AMD feature request;rocm;stale ### 🚀 The feature, motivation and pitch vLLM does not currently support serving MXFP8 quantized dense/MoE models on AMD gpus. It would be g...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: pitch vLLM does not currently support serving MXFP8 quantized dense/MoE models on AMD gpus. It would be great to to add the required MXFP8 GEMM / Grouped GEMM kernels to enable serving MXFP8 dense and MoE models on AMD...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
