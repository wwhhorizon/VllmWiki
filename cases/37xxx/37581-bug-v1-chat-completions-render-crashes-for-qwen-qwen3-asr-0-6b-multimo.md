# vllm-project/vllm#37581: [Bug]: /v1/chat/completions/render` crashes for Qwen/Qwen3-ASR-0.6B multimodal audio, and chat audio returns empty/junk

| 字段 | 值 |
| --- | --- |
| Issue | [#37581](https://github.com/vllm-project/vllm/issues/37581) |
| 状态 | open |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: /v1/chat/completions/render` crashes for Qwen/Qwen3-ASR-0.6B multimodal audio, and chat audio returns empty/junk

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug With `Qwen/Qwen3-ASR-0.6B`, `/v1/audio/transcriptions` works, but the multimodal chat path is broken: - `/v1/chat/completions/render` returns `500` - server traceback ends with: `TypeError: Object of type MultiModalKwargsItems is not JSON serializable` - `/v1/chat/completions` returns `200`, but content is empty or junk like: `languageassistantlanguage` ## Server args: ```bash vllm serve Qwen/Qwen3-ASR-0.6B \ --host 0.0.0.0 \ --port 8000 \ --served-model-name qwen3-asr-0.6b \ --dtype bfloat16 \ --enforce-eager \ --max-num-batched-tokens 12288 \ --limit-mm-per-prompt '{"audio":{"count":1,"length":12288}}' ``` ## What works ```bash curl http://127.0.0.1:8000/v1/audio/transcriptions \ -F model=qwen3-asr-0.6b \ -F language=en \ -F file=@test.wav ``` This returns a valid transcript. ## What fails ### 1. render endpoint crashes ```bash AUDIO_B64="$(base64 -w0 test.wav)" curl -s http://127.0.0.1:8000/v1/chat/completions/render \ -H 'Content-Type: application/json' \ -d @ \"}, { \"type\": \"input_audio\", \"input_audio\": { \"data\": \"${AUDIO_B64}\", \"format\": \"wav\" } } ] } ] }") ``` Server traceback ends with: ```text TypeError: Ob...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: /v1/chat/completions/render` crashes for Qwen/Qwen3-ASR-0.6B multimodal audio, and chat audio returns empty/junk bug ### Your current environment ### 🐛 Describe the bug With `Qwen/Qwen3-ASR-0.6B`, `/v1/audio/tran...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: ost 0.0.0.0 \ --port 8000 \ --served-model-name qwen3-asr-0.6b \ --dtype bfloat16 \ --enforce-eager \ --max-num-batched-tokens 12288 \ --limit-mm-per-prompt '{"audio":{"count":1,"length":12288}}' ``` ## What works ```ba...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ver ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ns` should either return a usable transcript-like response or reject the request clearly with `4xx` ## Actual - `render` crashes with `MultiModalKwargsItems is not JSON serializable` - `chat/completions` returns semanti...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: anscriptions \ -F model=qwen3-asr-0.6b \ -F language=en \ -F file=@test.wav ``` This returns a valid transcript. ## What fails ### 1. render endpoint crashes ```bash AUDIO_B64="$(base64 -w0 test.wav)" curl -s http://127...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
