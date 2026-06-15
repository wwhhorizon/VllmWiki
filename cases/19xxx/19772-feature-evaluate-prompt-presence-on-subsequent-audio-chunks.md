# vllm-project/vllm#19772: [Feature]: Evaluate prompt presence on subsequent audio chunks

| 字段 | 值 |
| --- | --- |
| Issue | [#19772](https://github.com/vllm-project/vllm/issues/19772) |
| 状态 | closed |
| 标签 | good first issue;feature request;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Evaluate prompt presence on subsequent audio chunks

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Starting with #19597 , vllm now supports chunking audios longer than 30s when serving Whisper. The logic is pretty simple right now, as the audio is chunked at semi-fixed intervals, looking for "silence" in a small window around the chunk limit. The request is then executed in a "concurrent mode", batching the audio chunks. https://github.com/vllm-project/vllm/blob/cda92307c145e7722cdc33e6d26e105eeb22b882/vllm/entrypoints/openai/serving_transcription.py#L215-L226 Hence there's no sequential dependency at the moment, in particular the transcription of chunk_i is not piped as prompt to chunk_i+1 (optimal strategy, as per the Whisper paper). In this regard, it would be nice to asses with longer audio samples whether feeding the original prompt to subsequent chunks after the first one is actually beneficial to the quality of the generated output. My understanding is that the prompt will condition the model on the text that appeared in the past 30s, and hence it may actually be harmful to the final quality of the transcription, given a long enough input. This task requires evaluating the precision/error rate on longer sequences similarly to what...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: s/openai/serving_transcription.py#L215-L226 Hence there's no sequential dependency at the moment, in particular the transcription of chunk_i is not piped as prompt to chunk_i+1 (optimal strategy, as per the Whisper pape...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: the audio is chunked at semi-fixed intervals, looking for "silence" in a small window around the chunk limit. The request is then executed in a "concurrent mode", batching the audio chunks. https://github.com/vllm-proje...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: uate prompt presence on subsequent audio chunks good first issue;feature request;stale ### 🚀 The feature, motivation and pitch Starting with #19597 , vllm now supports chunking audios longer than 30s when serving Whispe...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [Feature]: Evaluate prompt presence on subsequent audio chunks good first issue;feature request;stale ### 🚀 The feature, motivation and pitch Starting with #19597 , vllm now supports chunking audios longer than 30s when...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: nscription, given a long enough input. This task requires evaluating the precision/error rate on longer sequences similarly to what it was done here https://github.com/vllm-project/vllm/blob/main/tests/entrypoints/opena...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
