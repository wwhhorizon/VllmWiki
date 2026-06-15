# vllm-project/vllm#37129: [Feature]: MiniCPM-o audio output (TTS) support

| 字段 | 值 |
| --- | --- |
| Issue | [#37129](https://github.com/vllm-project/vllm/issues/37129) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: MiniCPM-o audio output (TTS) support

### Issue 正文摘录

## Motivation MiniCPM-o 4.5 is an end-to-end omni model with a built-in TTS module (Token2wav vocoder). vLLM currently supports MiniCPM-o 4.5 for vision and audio input, but audio output is explicitly skipped: ```python # vllm/model_executor/models/minicpmo.py loader = AutoWeightsLoader(self, skip_prefixes=["tts"]) ``` There is also an open usage issue: #24665 ("how to get tts wav via vllm online server") where the answer was "Audio output is not supported yet." ## Proposal Add audio output support for MiniCPM-o in vLLM, following the existing contributing patterns (similar to how `SupportsTranscription` was introduced for STT models). ### What needs to be done 1. **Interface design** — Define a `SupportsAudioOutput` (or similar) interface analogous to `SupportsTranscription`, for models that generate audio tokens alongside text 2. **Model implementation** — Load TTS weights in `minicpmo.py` (remove `skip_prefixes=["tts"]`), implement audio decoding via Token2wav vocoder 3. **API layer** — Expose audio output via the OpenAI-compatible `/v1/chat/completions` endpoint (as base64-encoded audio, similar to OpenAI's `audio` response format) and/or the existing Realtime API WebSocket (P...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: output (TTS) support ## Motivation MiniCPM-o 4.5 is an end-to-end omni model with a built-in TTS module (Token2wav vocoder). vLLM currently supports MiniCPM-o 4.5 for vision and audio input, but audio output is explicit...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ports MiniCPM-o 4.5 for vision and audio input, but audio output is explicitly skipped: ```python # vllm/model_executor/models/minicpmo.py loader = AutoWeightsLoader(self, skip_prefixes=["tts"]) ``` There is also an ope...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: onse format) and/or the existing Realtime API WebSocket (PR #33187) 4. **Tests + docs** — Unit tests and contributing guide update ### Why this matters - MiniCPM-o 4.5 (Qwen3-8B backbone, 9B total) approaches Gemini 2.5...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ) - PR #33187 — Realtime API (WebSocket, STT only) - Issue #24665 — User request for TTS wav output - Issue #25066 — Streaming multi-modal I/O (broader tracking) ## Questions for maintainers 1. Is a new `SupportsAudioOu...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
