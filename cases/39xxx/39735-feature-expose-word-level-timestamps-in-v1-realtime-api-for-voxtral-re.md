# vllm-project/vllm#39735: [Feature]: Expose Word-Level Timestamps in `/v1/realtime` API for Voxtral Realtime

| 字段 | 值 |
| --- | --- |
| Issue | [#39735](https://github.com/vllm-project/vllm/issues/39735) |
| 状态 | open |
| 标签 | feature request |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Expose Word-Level Timestamps in `/v1/realtime` API for Voxtral Realtime

### Issue 正文摘录

## Summary The vLLM Realtime API (`/v1/realtime`) currently returns only text in `transcription.delta` and `transcription.done` events. However, the Voxtral Realtime model already has enough internal information to derive **per-word timestamps** via `[STREAMING_WORD]` token positions and the known `transcription_delay`. Exposing these timestamps in the WebSocket protocol would unlock critical downstream use cases without any model changes. ## Motivation ### Current behavior ```json {"type": "transcription.delta", "delta": "Hello world"} {"type": "transcription.done", "text": "Hello world."} ``` Clients receive text but have **no timing information**. Applications that need to know *when* a word was spoken must resort to coarse heuristics (e.g., wall-clock arrival time of deltas) or run a separate forced-alignment model. ### Why this matters | Use case | How timestamps help | |---|---| | **Speaker diarization** | When a speaker change is detected mid-sentence, precise word boundaries allow splitting the transcript at the exact audio position instead of an approximate byte offset. | | **Live subtitling** | Word-level sync enables karaoke-style highlighting where each word lights up...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: on.delta` and `transcription.done` events. However, the Voxtral Realtime model already has enough internal information to derive **per-word timestamps** via `[STREAMING_WORD]` token positions and the known `transcriptio...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: Word-Level Timestamps in `/v1/realtime` API for Voxtral Realtime feature request ## Summary The vLLM Realtime API (`/v1/realtime`) currently returns only text in `transcription.delta` and `transcription.done` events. Ho...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: eaker diarization** | When a speaker change is detected mid-sentence, precise word boundaries allow splitting the transcript at the exact audio position instead of an approximate byte offset. | | **Live subtitling** | W...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: 298) - vLLM Realtime API docs: [vLLM Realtime](https://docs.vllm.ai/en/latest/serving/openai_compatible_server/?h=realtime#realtime-api) - Related HF discussion: [#2 — transcription_delay param](https://huggingface.co/m...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
