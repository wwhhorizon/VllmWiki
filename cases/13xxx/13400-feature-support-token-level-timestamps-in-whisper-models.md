# vllm-project/vllm#13400: [Feature]: Support token-level timestamps in whisper models

| 字段 | 值 |
| --- | --- |
| Issue | [#13400](https://github.com/vllm-project/vllm/issues/13400) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Support token-level timestamps in whisper models

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Dynamic time warping applied on encoder-decoder cross-attention matrices of whisper models can be used to find a word-level alignment between audio and transcriptions. [openai/whisper provides an implementation this in `find_alignment`](https://github.com/openai/whisper/blob/517a43ecd132a2089d85f4ebc044728a71d49f6e/whisper/timing.py#L163) that returns timestamps (start and end) for each word in the transcription (here `text_tokens`). This has various usecases for us and it would be great to have this capability exposed via vLLM. ### Alternatives * one alternative here is to use the reference impl `find_alignment` from python directly, calling it once for each sample in a batch of audio samples (or maybe implement a variant `find_alignment` capable of handling batch inputs) * [whisper.cpp](https://github.com/ggerganov/whisper.cpp) and the code implemented in [this PR](https://github.com/ggerganov/whisper.cpp/pull/1485) is also an option Both options are feasible but: * require the client/user to run custom python or native code * both alternatives are neither efficient nor fast for a large number of (possibly concurrent) audio inputs/requests...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Feature]: Support token-level timestamps in whisper models feature request;stale ### 🚀 The feature, motivation and pitch Dynamic time warping applied on encoder-decoder cross-attention matrices of whisper models can be...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: d be easy, whereas decoder batching is probably more complicated (due to flash attention and bookkeeping of the cross-attention matrices) * `text_tokens` could be a transcription of the whisper model itself but doesn't...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: to run custom python or native code * both alternatives are neither efficient nor fast for a large number of (possibly concurrent) audio inputs/requests ### Additional context [This is the PR for initial whisper support...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: `). This has various usecases for us and it would be great to have this capability exposed via vLLM. ### Alternatives * one alternative here is to use the reference impl `find_alignment` from python directly, calling it...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Feature]: Support token-level timestamps in whisper models feature request;stale ### 🚀 The feature, motivation and pitch Dynamic time warping applied on encoder-decoder cross-attention matrices of whisper models can be...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
