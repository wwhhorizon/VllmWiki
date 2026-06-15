# vllm-project/vllm#31254: [Feature]: Add kimi_k2 supported eagle3

| 字段 | 值 |
| --- | --- |
| Issue | [#31254](https://github.com/vllm-project/vllm/issues/31254) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Add kimi_k2 supported eagle3

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Current kimi_k2 is not support use eagle3 speculative decoding, because in code only support `eagle3_target_supported = ["llama", "qwen", "minicpm", "gpt_oss"]` this model. Current in huggingface have a eagle3 model https://huggingface.co/AQ-MedAI/Kimi-K2-Instruct-eagle3, so need to support. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: tive decoding, because in code only support `eagle3_target_supported = ["llama", "qwen", "minicpm", "gpt_oss"]` this model. Current in huggingface have a eagle3 model https://huggingface.co/AQ-MedAI/Kimi-K2-Instruct-eag...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: Add kimi_k2 supported eagle3 feature request ### 🚀 The feature, motivation and pitch Current kimi_k2 is not support use eagle3 speculative decoding, because in code only support `eagle3_target_supported = ["l...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
