# vllm-project/vllm#8236: [Feature]: Add multi-image input support for LLaVA offline inference (similar to #7230)

| 字段 | 值 |
| --- | --- |
| Issue | [#8236](https://github.com/vllm-project/vllm/issues/8236) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Add multi-image input support for LLaVA offline inference (similar to #7230)

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Recently, I released a model https://huggingface.co/aws-prototyping/long-llava-qwen2-7b using the `llava` model architecture and could support multiple images (or video) as input, so it is reasonable to enable multiple images as a input for llava in vllm also. Thank you! ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: request ### 🚀 The feature, motivation and pitch Recently, I released a model https://huggingface.co/aws-prototyping/long-llava-qwen2-7b using the `llava` model architecture and could support multiple images (or video) a...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ggingface.co/aws-prototyping/long-llava-qwen2-7b using the `llava` model architecture and could support multiple images (or video) as input, so it is reasonable to enable multiple images as a input for llava in vllm als...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: age input support for LLaVA offline inference (similar to #7230) feature request ### 🚀 The feature, motivation and pitch Recently, I released a model https://huggingface.co/aws-prototyping/long-llava-qwen2-7b using the...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
