# vllm-project/vllm#26808: [Bug]: [OpenAI server][Transcriptions] M4A uploads fail while MP3 succeeds (Whisper)

| 字段 | 值 |
| --- | --- |
| Issue | [#26808](https://github.com/vllm-project/vllm/issues/26808) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: [OpenAI server][Transcriptions] M4A uploads fail while MP3 succeeds (Whisper)

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ### Environment - vLLM OpenAI-compatible API: `/v1/audio/transcriptions` - Model: `openai/whisper-large-v3` - Docs state M4A is supported ### Description Sending the same audio as MP3 works, but sending it as M4A fails. The MP3 request returns 200 and text; the M4A request return 500 Internal Server Error. ### Expected M4A should be accepted and transcribed, as documented. ### Actual - MP3: 200 OK with transcription - M4A: no 200 OK observed ### Reproduction steps 1) Start the vllm-server with a Whisper model (e.g., `openai/whisper-large-v3`). 2) MP3 (works): ```bash curl -X POST 'http://127.0.0.1:8000/v1/audio/transcriptions' \ -H 'accept: application/json' \ -H 'Content-Type: multipart/form-data' \ -F 'stream=false' \ -F 'timestamp_granularities[]=word' \ -F 'prompt=string' \ -F 'model=openai/whisper-large-v3' \ -F 'temperature=0' \ -F 'response_format=json' \ -F 'language=en' \ -F 'file=@/path/to/sample.mp3' ``` 3) M4A (fails): ```bash curl -X POST 'http://127.0.0.1:8000/v1/audio/transcriptions' \ -H 'accept: application/json' \ -H 'Content-Type: multipart/form-data' \ -F 'stream=false' \ -F 'timestamp_granularities[]=word' \...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: # Environment - vLLM OpenAI-compatible API: `/v1/audio/transcriptions` - Model: `openai/whisper-large-v3` - Docs state M4A is supported ### Description Sending the same audio as MP3 works, but sending it as M4A fails. T...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: erver][Transcriptions] M4A uploads fail while MP3 succeeds (Whisper) bug;stale ### Your current environment ### 🐛 Describe the bug ### Environment - vLLM OpenAI-compatible API: `/v1/audio/transcriptions` - Model: `opena...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: cation/json' \ -H 'Content-Type: multipart/form-data' \ -F 'stream=false' \ -F 'timestamp_granularities[]=word' \ -F 'prompt=string' \ -F 'model=openai/whisper-large-v3' \ -F 'temperature=0' \ -F 'response_format=json'...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
