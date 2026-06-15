# vllm-project/vllm#9324: [Feature]: Quantization support for LLaVA OneVision 

| 字段 | 值 |
| --- | --- |
| Issue | [#9324](https://github.com/vllm-project/vllm/issues/9324) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Quantization support for LLaVA OneVision 

### Issue 正文摘录

### 🚀 The feature, motivation and pitch I'm working on applications that must run locally in resource-limited HW. Threrefore, quantization becomes essential. Such applications need from multimodal video-text processing. The candidate model in question is LLaVA OneVision. However, it does not support BitsAndBytes quantization yet. **Model** LLaVA-OneVision https://huggingface.co/llava-hf/llava-onevision-qwen2-7b-ov-hf **Challenges** AFAIK Siglip, the multimodal projector and Qwen2 need from quantization support. Perhaps it is also useful to enable quantization per module to quantize only the language part. ### Alternatives _No response_ ### Additional context Trying to load a pre-quantized LLaVA OneVision model into vLLM throws: ```python AttributeError: Model LlavaOnevisionForConditionalGeneration does not support BitsAndBytes quantization yet. ``` ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: Threrefore, quantization becomes essential. Such applications need from multimodal video-text processing. The candidate model in question is LLaVA OneVision. However, it does not support BitsAndBytes quantization yet. *...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: Quantization support for LLaVA OneVision feature request;stale ### 🚀 The feature, motivation and pitch I'm working on applications that must run locally in resource-limited HW. Threrefore, quantization become...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: [Feature]: Quantization support for LLaVA OneVision feature request;stale ### 🚀 The feature, motivation and pitch I'm working on applications that must run locally in resource-limited HW. Threrefore, quantization become...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
