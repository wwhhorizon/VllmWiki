# vllm-project/vllm#28380: [Feature]: WhisperX support

| 字段 | 值 |
| --- | --- |
| Issue | [#28380](https://github.com/vllm-project/vllm/issues/28380) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: WhisperX support

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Possibility of supporting WhisperX, built on top of Whisper. https://github.com/m-bain/whisperX ### Alternatives _No response_ ### Additional context Mainly for features built on top such as VAD, Timestamps, Speaker Diarization. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: WhisperX support feature request;stale ### 🚀 The feature, motivation and pitch Possibility of supporting WhisperX, built on top of Whisper. https://github.com/m-bain/whisperX ### Alternatives _No response_ ##...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: n. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whi...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
