# vllm-project/vllm#21030: [Feature]: The inference accelation for quantized qwen2.5vl

| 字段 | 值 |
| --- | --- |
| Issue | [#21030](https://github.com/vllm-project/vllm/issues/21030) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: The inference accelation for quantized qwen2.5vl

### Issue 正文摘录

### 🚀 The feature, motivation and pitch I launched a vLLM server to test the inference speed of quantized Qwen2.5-VL models (GPTQ and AWQ). Surprisingly, the quantized models performed slower than the original model. I noticed the dtype of vllm cannot be int4 or int8. Below is my server configuration: `vllm serve Qwen/Qwen2.5-VL-3B-Instruct-AWQ --port 8000 --host 0.0.0.0 --dtype half --limit-mm-per-prompt image=5,video=5 --tensor-parallel-size 1 --max-model-len 3200 -q awq` Could the dtype setting impact inference speed? Are there other configurations I should consider optimizing? ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Feature]: The inference accelation for quantized qwen2.5vl feature request;stale ### 🚀 The feature, motivation and pitch I launched a vLLM server to test the inference speed of quantized Qwen2.5-VL models (GPTQ and AWQ...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Feature]: The inference accelation for quantized qwen2.5vl feature request;stale ### 🚀 The feature, motivation and pitch I launched a vLLM server to test the inference speed of quantized Qwen2.5-VL models (GPTQ and AWQ...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: The inference accelation for quantized qwen2.5vl feature request;stale ### 🚀 The feature, motivation and pitch I launched a vLLM server to test the inference speed of quantized Qwen2.5-VL models (GPTQ and AWQ...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ale ### 🚀 The feature, motivation and pitch I launched a vLLM server to test the inference speed of quantized Qwen2.5-VL models (GPTQ and AWQ). Surprisingly, the quantized models performed slower than the original model...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
