# vllm-project/vllm#8945: [Question]: Apply LoRA adapter on quantized model

| 字段 | 值 |
| --- | --- |
| Issue | [#8945](https://github.com/vllm-project/vllm/issues/8945) |
| 状态 | closed |
| 标签 |  |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Question]: Apply LoRA adapter on quantized model

### Issue 正文摘录

### Anything you want to discuss about vllm. I've fine-tuned Qwen2.5-14B-Instruct using QLora(bitsandbytes 4bit) and also a full fine-tune. However when I tried to use it with a quantized model (Qwen2.5-14B-Instruct-gptq-int4) , vllm crashed. Is this a technical constraint or I'm missing something? Thank you for your response. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: [Question]: Apply LoRA adapter on quantized model ### Anything you want to discuss about vllm. I've fine-tuned Qwen2.5-14B-Instruct using QLora(bitsandbytes 4bit) and also a full fine-tune. However when I tried to use i...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Question]: Apply LoRA adapter on quantized model ### Anything you want to discuss about vllm. I've fine-tuned Qwen2.5-14B-Instruct using QLora(bitsandbytes 4bit) and also a full fine-tune. However when I tried to use i...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
