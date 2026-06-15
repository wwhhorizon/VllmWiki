# vllm-project/vllm#24302: [Feature]: Implement SRT generation for audio transcription  in vLLM

| 字段 | 值 |
| --- | --- |
| Issue | [#24302](https://github.com/vllm-project/vllm/issues/24302) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Implement SRT generation for audio transcription  in vLLM

### Issue 正文摘录

### 🚀 The feature, motivation and pitch As an AI engineer, I aim to leverage vLLM to host speech-to-text models and produce audio transcriptions with timestamps(audio "segments" ). My goal is to use a Whisper model hosted on vLLM, following the [OpenAI specification for transcription](https://platform.openai.com/docs/api-reference/audio/createTranscription). I would like the output to be in the "srt" format, with word-level granularity for the timestamps. The following OpenAI client call is executed against a Whisper model hosted via vLLM: ```python transcript = client.audio.transcriptions.create( file=audio_file, model=model_name, response_format="srt", timestamp_granularities=["word"] ) ``` Expected Behavior: vLLM returns a valid SRT output according to the [OpenAI specification.](https://platform.openai.com/docs/api-reference/audio/createTranscription) Current Output: vLLM returns the following message: ```shell BadRequestError: Error code: 400 - {'object': 'error', 'message': 'Currently only support response_format `text` or `json`', 'type': 'BadRequestError', 'param': None, 'code': 400} ``` ### Alternatives _No response_ ### Additional context more detail about srt can be fou...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: pitch As an AI engineer, I aim to leverage vLLM to host speech-to-text models and produce audio transcriptions with timestamps(audio "segments" ). My goal is to use a Whisper model hosted on vLLM, following the [OpenAI...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ture]: Implement SRT generation for audio transcription in vLLM feature request;stale ### 🚀 The feature, motivation and pitch As an AI engineer, I aim to leverage vLLM to host speech-to-text models and produce audio tra...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: goal is to use a Whisper model hosted on vLLM, following the [OpenAI specification for transcription](https://platform.openai.com/docs/api-reference/audio/createTranscription). I would like the output to be in the "srt"...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: /98 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
