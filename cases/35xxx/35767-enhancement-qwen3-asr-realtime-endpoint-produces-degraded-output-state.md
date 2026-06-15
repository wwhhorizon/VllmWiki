# vllm-project/vllm#35767: [Enhancement]: Qwen3-ASR realtime endpoint produces degraded output — stateless segments, no cross-segment context, raw format leaks

| 字段 | 值 |
| --- | --- |
| Issue | [#35767](https://github.com/vllm-project/vllm/issues/35767) |
| 状态 | open |
| 标签 |  |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Enhancement]: Qwen3-ASR realtime endpoint produces degraded output — stateless segments, no cross-segment context, raw format leaks

### Issue 正文摘录

## Enhancement Report The Qwen3-ASR realtime WebSocket endpoint (`/v1/realtime`) produces significantly degraded transcription compared to the REST batch endpoint (`/v1/audio/transcriptions`). The root cause is that each 5-second audio segment is transcribed in complete isolation — no cross-segment context, no output post-processing, and no use of the `input_stream` mechanism that vLLM's realtime infrastructure already provides. ## Problems ### 1. `input_stream` is accepted but never used `Qwen3ASRRealtimeGeneration.buffer_realtime_audio` accepts an `input_stream` parameter but never reads from it: ```python # vllm/model_executor/models/qwen3_asr_realtime.py, lines 188-220 async def buffer_realtime_audio( cls, audio_stream: AsyncGenerator[np.ndarray, None], input_stream: asyncio.Queue[list[int]], # AsyncGenerator[PromptType, None]: ... async for audio_chunk in audio_stream: buffer.write_audio(audio_chunk) while (segment := buffer.read_audio()) is not None: yield TokensPrompt( prompt_token_ids=prompt_token_ids, # same prompt every time multi_modal_data={"audio": segment}, ) ``` Compare with Voxtral's implementation which actively feeds output tokens back for cross-segment context:...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Enhancement]: Qwen3-ASR realtime endpoint produces degraded output — stateless segments, no cross-segment context, raw format leaks ## Enhancement Report The Qwen3-ASR realtime WebSocket endpoint (`/v1/realtime`) produ...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: text, no output post-processing, and no use of the `input_stream` mechanism that vLLM's realtime infrastructure already provides. ## Problems ### 1. `input_stream` is accepted but never used `Qwen3ASRRealtimeGeneration....
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: udio_stream: AsyncGenerator[np.ndarray, None], input_stream: asyncio.Queue[list[int]], # AsyncGenerator[PromptType, None]: ... async for audio_chunk in audio_stream: buffer.write_audio(audio_chunk) while (segment := buf...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: audio_stream: AsyncGenerator[np.ndarray, None], input_stream: asyncio.Queue[list[int]], # AsyncGenerator[PromptType, None]: ... async for audio_chunk in audio_stream: buffer.write_audio(audio_chunk) while (segment := bu...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ment boundaries gets transcribed twice. Real output from a single-stream test: ``` language English We have been a misunderstood and badly mocked orc for a long time. Like when we started. language English We have been...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
