# vllm-project/vllm#35908: [RFC]: Model-specific realtime streaming abstraction

| 字段 | 值 |
| --- | --- |
| Issue | [#35908](https://github.com/vllm-project/vllm/issues/35908) |
| 状态 | open |
| 标签 | stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Model-specific realtime streaming abstraction

### Issue 正文摘录

### Motivation. The `SupportsRealtime` protocol defines a minimal contract for realtime audio streaming: ```python @classmethod async def buffer_realtime_audio( cls, audio_stream: AsyncGenerator[np.ndarray, None], input_stream: asyncio.Queue[list[int]], model_config: ModelConfig, ) -> AsyncGenerator[PromptType, None]: ... ``` This works for Voxtral (fixed-size frames, token feedback via background task). But implementing Qwen3-ASR's SDK-style streaming — which needs a growing audio buffer, prefix rollback, unfixed chunk heuristics, and holdback logic — required changes in: - **`qwen3_asr_realtime.py`** — model layer (expected) - **`connection.py`** — imports Qwen-specific constants (`_DEFAULT_ROLLBACK_TOKENS`), implements Qwen-specific `_holdback_rollback` logic - **`serving.py`** — passes `prefix_texts` and `**kwargs` to `buffer_realtime_audio` that Voxtral doesn't accept (would break at runtime) - **`protocol.py`** — adds `RealtimeSessionConfig` with Qwen-specific fields (`rollback_tokens`, `unfixed_chunks`, `max_prefix_tokens`) - **`async_llm.py`** — changes `finished=True` handling for streaming input (engine-level change for a model-specific need) See #35894 for the full diff...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [RFC]: Model-specific realtime streaming abstraction stale ### Motivation. The `SupportsRealtime` protocol defines a minimal contract for realtime audio streaming: ```python @classmethod async def buffer_realtime_audio(...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [RFC]: Model-specific realtime streaming abstraction stale ### Motivation. The `SupportsRealtime` protocol defines a minimal contract for realtime audio streaming: ```python @classmethod async def buffer_realtime_audio(...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: defines a minimal contract for realtime audio streaming: ```python @classmethod async def buffer_realtime_audio( cls, audio_stream: AsyncGenerator[np.ndarray, None], input_stream: asyncio.Queue[list[int]], model_config:...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [RFC]: Model-specific realtime streaming abstraction stale ### Motivation. The `SupportsRealtime` protocol defines a minimal contract for realtime audio streaming: ```python @classmethod async def buffer_realtime_audio(...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: ng audio buffer each request (bandwidth cost) - **Con**: HTTP round-trip latency per segment adds up #### Option B: Richer `SupportsRealtime` protocol (push model-specific logic down) Extend the protocol so models can d...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
