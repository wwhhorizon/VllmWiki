# vllm-project/vllm#12262: [Feature]: Is it possible to run a 2:4 sparse fp8 quantized model on L20 GPUs?

| 字段 | 值 |
| --- | --- |
| Issue | [#12262](https://github.com/vllm-project/vllm/issues/12262) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Is it possible to run a 2:4 sparse fp8 quantized model on L20 GPUs?

### Issue 正文摘录

### 🚀 The feature, motivation and pitch I've found that the current 2:4 sparse fp8 quantized model requires CUDA Compute Capability of >=9.0, but fp8 quantized model can run on L20, which has CUDA Compute Capability of 8.9. Is it possible to run the 2:4 sparse fp8 quantized model on L20? If it can be achieved, the 2:4 sparse FP8 model would have a broader applicability. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: tch I've found that the current 2:4 sparse fp8 quantized model requires CUDA Compute Capability of >=9.0, but fp8 quantized model can run on L20, which has CUDA Compute Capability of 8.9. Is it possible to run the 2:4 s...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: [Feature]: Is it possible to run a 2:4 sparse fp8 quantized model on L20 GPUs? feature request ### 🚀 The feature, motivation and pitch I've found that the current 2:4 sparse fp8 quantized model requires CUDA Compute Cap...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Feature]: Is it possible to run a 2:4 sparse fp8 quantized model on L20 GPUs? feature request ### 🚀 The feature, motivation and pitch I've found that the current 2:4 sparse fp8 quantized model requires CUDA Compute Cap...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: it possible to run a 2:4 sparse fp8 quantized model on L20 GPUs? feature request ### 🚀 The feature, motivation and pitch I've found that the current 2:4 sparse fp8 quantized model requires CUDA Compute Capability of >=9...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
