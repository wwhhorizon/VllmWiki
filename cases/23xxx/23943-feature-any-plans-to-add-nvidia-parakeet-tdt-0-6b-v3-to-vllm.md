# vllm-project/vllm#23943: [Feature]: Any plans to add nvidia/parakeet-tdt-0.6b-v3 to vllm?

| 字段 | 值 |
| --- | --- |
| Issue | [#23943](https://github.com/vllm-project/vllm/issues/23943) |
| 状态 | open |
| 标签 | new-model;multi-modality |
| 评论 | 24; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Any plans to add nvidia/parakeet-tdt-0.6b-v3 to vllm?

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Hello, Based on this and my tests this model is faster than whispher large v3 distill 3.5 and more accurate according to this https://huggingface.co/spaces/hf-audio/open_asr_leaderboard are there any plans to implement it ? ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Feature]: Any plans to add nvidia/parakeet-tdt-0.6b-v3 to vllm? new-model;multi-modality ### 🚀 The feature, motivation and pitch Hello, Based on this and my tests this model is faster than whispher large v3 distill 3.5...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ty ### 🚀 The feature, motivation and pitch Hello, Based on this and my tests this model is faster than whispher large v3 distill 3.5 and more accurate according to this https://huggingface.co/spaces/hf-audio/open_asr_le...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
