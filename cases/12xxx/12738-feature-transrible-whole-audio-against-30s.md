# vllm-project/vllm#12738: [Feature]: Transrible whole audio against 30s

| 字段 | 值 |
| --- | --- |
| Issue | [#12738](https://github.com/vllm-project/vllm/issues/12738) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Transrible whole audio against 30s

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Hello, I have tested whisper with VLLM but i have seen that we transcribe only first part of audio (arround 20 or 30 s). is it normal as original whisper treat only 30s of audio ? Best regards ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature]: Transrible whole audio against 30s feature request ### 🚀 The feature, motivation and pitch Hello, I have tested whisper with VLLM but i have seen that we transcribe only first part of audio (arround 20 or 30...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: feature request ### 🚀 The feature, motivation and pitch Hello, I have tested whisper with VLLM but i have seen that we transcribe only first part of audio (arround 20 or 30 s). is it normal as original whisper treat onl...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
