# vllm-project/vllm#32588: [Bug]: Wrong timestamps if audio > 30s

| 字段 | 值 |
| --- | --- |
| Issue | [#32588](https://github.com/vllm-project/vllm/issues/32588) |
| 状态 | open |
| 标签 | bug;help wanted;good first issue |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Wrong timestamps if audio > 30s

### Issue 正文摘录

### Your current environment NA ### 🐛 Describe the bug **Segment level timestamps are incrementally offset by ~0.5s per segment.** When transcribing long audio with vLLM Whisper, segment-level timestamps are increasingly inaccurate. Chunking uses by default a 1s window to find low-energy (quiet) regions for splitting, so the next chunk may start up to 1s earlier than the nominal chunk length. This offset is not compensated for when generating segment timestamps, resulting in an average delay of ~0.5s per segment, which accumulates (e.g., 5s after 10 segments). Clients can workaround by subtracting 0.5s per segment, but that's obviously not accurate. Also, the [related documentation](https://github.com/vllm-project/vllm/blob/e83b7e379c11bf136c1b96bc6a67b6d2207cfde4/docs/contributing/model/transcription.md#audio-preprocessing-and-chunking) is not correct: there are no overlapping chunks, but just a window for searching the best split point. Maybe this confusion is the cause of the issue. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.a...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: is not correct: there are no overlapping chunks, but just a window for searching the best split point. Maybe this confusion is the cause of the issue. ### Before submitting a new issue... - [x] Make sure you already sea...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ect/vllm/blob/e83b7e379c11bf136c1b96bc6a67b6d2207cfde4/docs/contributing/model/transcription.md#audio-preprocessing-and-chunking) is not correct: there are no overlapping chunks, but just a window for searching the best...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
