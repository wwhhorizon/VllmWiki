# vllm-project/vllm#35310: [Feature]: Qwen-ASR Forced Aligner

| 字段 | 值 |
| --- | --- |
| Issue | [#35310](https://github.com/vllm-project/vllm/issues/35310) |
| 状态 | closed |
| 标签 | good first issue;feature request |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Qwen-ASR Forced Aligner

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Will vLLM support Qwen3-ASR [Forced-Aligner](https://huggingface.co/Qwen/Qwen3-ForcedAligner-0.6B), allowing to timestamp audio transcription segments? ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Feature]: Qwen-ASR Forced Aligner good first issue;feature request ### 🚀 The feature, motivation and pitch Will vLLM support Qwen3-ASR [Forced-Aligner](https://huggingface.co/Qwen/Qwen3-ForcedAligner-0.6B), allowing to...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature]: Qwen-ASR Forced Aligner good first issue;feature request ### 🚀 The feature, motivation and pitch Will vLLM support Qwen3-ASR [Forced-Aligner](https://huggingface.co/Qwen/Qwen3-ForcedAligner-0.6B), allowing to...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
