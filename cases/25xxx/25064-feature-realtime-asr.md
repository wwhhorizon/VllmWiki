# vllm-project/vllm#25064: [Feature]: Realtime ASR

| 字段 | 值 |
| --- | --- |
| Issue | [#25064](https://github.com/vllm-project/vllm/issues/25064) |
| 状态 | closed |
| 标签 | feature request;multi-modality |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Realtime ASR

### Issue 正文摘录

### 🚀 The feature, motivation and pitch I need super short latency on a transcription service, so having realtime ASR implemented in vLLM would be awesome. See i.e. https://platform.openai.com/docs/guides/speech-to-text?lang=curl#streaming-the-transcription-of-an-ongoing-audio-recording https://github.com/QuentinFuxa/WhisperLiveKit ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: lti-modality ### 🚀 The feature, motivation and pitch I need super short latency on a transcription service, so having realtime ASR implemented in vLLM would be awesome. See i.e. https://platform.openai.com/docs/guides/s...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature]: Realtime ASR feature request;multi-modality ### 🚀 The feature, motivation and pitch I need super short latency on a transcription service, so having realtime ASR implemented in vLLM would be awesome. See i.e....

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
