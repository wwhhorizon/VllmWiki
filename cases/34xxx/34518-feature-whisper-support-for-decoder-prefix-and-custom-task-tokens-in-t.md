# vllm-project/vllm#34518: [Feature]: [Whisper] Support for decoder prefix and custom task tokens in transcription API

| 字段 | 值 |
| --- | --- |
| Issue | [#34518](https://github.com/vllm-project/vllm/issues/34518) |
| 状态 | open |
| 标签 | feature request;unstale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: [Whisper] Support for decoder prefix and custom task tokens in transcription API

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Hi! We use vLLM to serve Whisper models for transcription and are very happy with it for our batch transcription use case. We'd now like to migrate our real-time dictation pipeline to vLLM as well, but we're blocked by two missing features in the `/v1/audio/transcriptions` API. I'd love to understand if these are feasible and get some guidance. # Feature 1: True decoder prefix (distinct from prompt) ## What I need In our dictation product, the user speaks continuously and we receive overlapping audio chunks. Each chunk contains both audio the user has already spoken (which we've already transcribed) and new audio. To avoid re-transcribing the old part, we seed the Whisper decoder with the previous transcription as a prefix, so the model is forced to continue from that point and only decodes the new content. Concretely, using HuggingFace transformers, we do this by building `decoder_input_ids` as: ``` [task tokens: ] + [tokenized prefix text] ``` and then passing that to `model.generate(decoder_input_ids=...)`. After generation, we strip the prefix tokens from the output to get only the newly decoded text. ## How it differs from prompt The ex...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Feature]: [Whisper] Support for decoder prefix and custom task tokens in transcription API feature request;unstale ### 🚀 The feature, motivation and pitch Hi! We use vLLM to serve Whisper models for transcription and a...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: e new content. Concretely, using HuggingFace transformers, we do this by building `decoder_input_ids` as: ``` [task tokens: ] + [tokenized prefix text] ``` and then passing that to `model.generate(decoder_input_ids=...)...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: er in vLLM's transcription API maps to Whisper's ` ` conditioning mechanism: ``` {prompt} ``` This places the text before ` ` and is designed to bias the model's style and terminology. It does not force the decoder to b...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ## 🚀 The feature, motivation and pitch Hi! We use vLLM to serve Whisper models for transcription and are very happy with it for our batch transcription use case. We'd now like to migrate our real-time dictation pipeline...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: prefix approach given how vLLM handles encoder-decoder generation (e.g. KV cache, speculative decoding, etc.)? For the custom task tokens — is there a clean extension point, or would this require deeper changes? If eith...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
