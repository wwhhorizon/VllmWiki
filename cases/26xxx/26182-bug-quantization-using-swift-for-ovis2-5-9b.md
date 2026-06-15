# vllm-project/vllm#26182: [Bug]: Quantization using swift for Ovis2.5 9B

| 字段 | 值 |
| --- | --- |
| Issue | [#26182](https://github.com/vllm-project/vllm/issues/26182) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 14; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Quantization using swift for Ovis2.5 9B

### Issue 正文摘录

### Your current environment ValueError: The input size is not aligned with the quantized weight shape. This can be caused by too large tensor parallel size. Model name - Ovis2.5 9B Method - gptq ### 🐛 Describe the bug ValueError: The input size is not aligned with the quantized weight shape. This can be caused by too large tensor parallel size. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: [Bug]: Quantization using swift for Ovis2.5 9B bug;stale ### Your current environment ValueError: The input size is not aligned with the quantized weight shape. This can be caused by too large tensor parallel size. Mode...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ze. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: zed weight shape. This can be caused by too large tensor parallel size. Model name - Ovis2.5 9B Method - gptq ### 🐛 Describe the bug ValueError: The input size is not aligned with the quantized weight shape. This can be...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: Quantization using swift for Ovis2.5 9B bug;stale ### Your current environment ValueError: The input size is not aligned with the quantized weight shape. This can be caused by too large tensor parallel size. Mode...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
