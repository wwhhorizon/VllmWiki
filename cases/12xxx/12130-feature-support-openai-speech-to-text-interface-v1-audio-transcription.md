# vllm-project/vllm#12130: [Feature]: Support OpenAI speech-to-text interface `v1/audio/[transcriptions,translations]`

| 字段 | 值 |
| --- | --- |
| Issue | [#12130](https://github.com/vllm-project/vllm/issues/12130) |
| 状态 | closed |
| 标签 | help wanted;feature request |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Support OpenAI speech-to-text interface `v1/audio/[transcriptions,translations]`

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Now that we have support for Whisper (https://github.com/vllm-project/vllm/pull/11280), we should consider implementing OpenAI's explicit speech-to-text API. Documentation is here https://platform.openai.com/docs/guides/speech-to-text ### Example of `v1/audio/transcriptions` ```python from openai import OpenAI client = OpenAI() audio_file= open("/path/to/file/audio.mp3", "rb") transcription = client.audio.transcriptions.create( model="whisper-1", file=audio_file ) print(transcription.text) ``` ### Example of `v1/audio/translations` ```python from openai import OpenAI client = OpenAI() audio_file = open("/path/to/file/german.mp3", "rb") transcription = client.audio.translations.create( model="whisper-1", file=audio_file, ) print(transcription.text) ``` ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: -project/vllm/pull/11280), we should consider implementing OpenAI's explicit speech-to-text API. Documentation is here https://platform.openai.com/docs/guides/speech-to-text ### Example of `v1/audio/transcriptions` ```p...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: udio.mp3", "rb") transcription = client.audio.transcriptions.create( model="whisper-1", file=audio_file ) print(transcription.text) ``` ### Example of `v1/audio/translations` ```python from openai import OpenAI client =...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: t interface `v1/audio/[transcriptions,translations]` help wanted;feature request ### 🚀 The feature, motivation and pitch Now that we have support for Whisper (https://github.com/vllm-project/vllm/pull/11280), we should...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
