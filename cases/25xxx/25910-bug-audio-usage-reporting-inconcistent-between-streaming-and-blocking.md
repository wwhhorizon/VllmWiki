# vllm-project/vllm#25910: [Bug]: Audio usage reporting inconcistent between streaming and blocking

| 字段 | 值 |
| --- | --- |
| Issue | [#25910](https://github.com/vllm-project/vllm/issues/25910) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Audio usage reporting inconcistent between streaming and blocking

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug The usage struct returned for transcription requests (for models like Whisper) is different depending on whether streaming is on or off. If `stream=False`, then the audio duration usage struct `TranscriptionUsageAudio` added by #23576 is returned. OpenAI returns this for models billed by audio duration. Relevant protocol line: https://github.com/vllm-project/vllm/blob/2e4fe48c370e833350eae092eddd1490b65ff529/vllm/entrypoints/openai/protocol.py#L2488 If `stream=True`, the token-based `UsageInfo` is returned. Relevant protocol line: https://github.com/vllm-project/vllm/blob/2e4fe48c370e833350eae092eddd1490b65ff529/vllm/entrypoints/openai/protocol.py#L1931 These should be harmonized. It makes sense that both should return the duration variant. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: [Bug]: Audio usage reporting inconcistent between streaming and blocking bug;stale ### Your current environment ### 🐛 Describe the bug The usage struct returned for transcription requests (for models like Whisper) is di...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ]: Audio usage reporting inconcistent between streaming and blocking bug;stale ### Your current environment ### 🐛 Describe the bug The usage struct returned for transcription requests (for models like Whisper) is differ...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: [Bug]: Audio usage reporting inconcistent between streaming and blocking bug;stale ### Your current environment ### 🐛 Describe the bug The usage struct returned for transcription requests (for models like Whisper) is di...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: nt. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: cribe the bug The usage struct returned for transcription requests (for models like Whisper) is different depending on whether streaming is on or off. If `stream=False`, then the audio duration usage struct `Transcripti...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
