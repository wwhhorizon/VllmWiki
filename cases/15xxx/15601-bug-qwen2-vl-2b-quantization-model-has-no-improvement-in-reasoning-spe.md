# vllm-project/vllm#15601: [Bug]: Qwen2-VL-2B quantization model has no improvement in reasoning speed compared to the original model

| 字段 | 值 |
| --- | --- |
| Issue | [#15601](https://github.com/vllm-project/vllm/issues/15601) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 12; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Qwen2-VL-2B quantization model has no improvement in reasoning speed compared to the original model

### Issue 正文摘录

### Your current environment I performed GPTQ-int8 quantization using the fine-tuned Qwen2-VL-2B model, and there was no improvement in model inference speed after quantization ### 🐛 Describe the bug I performed GPTQ-int8 quantization using the fine-tuned Qwen2-VL-2B model, and there was no improvement in model inference speed after quantization ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Qwen2-VL-2B quantization model has no improvement in reasoning speed compared to the original model bug;stale ### Your current environment I performed GPTQ-int8 quantization using the fine-tuned Qwen2-VL-2B model...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: [Bug]: Qwen2-VL-2B quantization model has no improvement in reasoning speed compared to the original model bug;stale ### Your current environment I performed GPTQ-int8 quantization using the fine-tuned Qwen2-VL-2B model...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ion ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: has no improvement in reasoning speed compared to the original model bug;stale ### Your current environment I performed GPTQ-int8 quantization using the fine-tuned Qwen2-VL-2B model, and there was no improvement in mode...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
