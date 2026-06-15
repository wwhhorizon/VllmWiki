# vllm-project/vllm#29350: [Bug]: Audio transcription duplicated words between chunks

| 字段 | 值 |
| --- | --- |
| Issue | [#29350](https://github.com/vllm-project/vllm/issues/29350) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Audio transcription duplicated words between chunks

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When using whisper-large-v3, there are cases where a word pronounced at the end of a chunk is duplicated at the beginning of the next one on Audio Transcription endpoint. Output example: ``` [...] all these conversations are what have kept me me honest, kept me inspired, and kept me going. Every day, I learned from you [...] ``` Here `have kept me me honest` is typically a duplication. ### Steps to reproduce Audio sample used is a HuggingFace's Obama MP3 file sample of 03:24 duration, [you can download it here](https://huggingface.co/datasets/hf-internal-testing/dummy-audio-samples/blob/main/obama.mp3). Make a curl request with a prompt on audio transcription endpoint : ``` curl " /v1/audio/transcriptions" \ -H "Authorization: Bearer " \ -H 'Content-Type: multipart/form-data' \ -F "model= " \ -F 'stream=false' \ -F "file=@ " \ -F "prompt=I've seen our doctors and volunteers rebuild" \ -F 'temperature=0.6' \ -F 'language=en' ``` ### Expectations I expect my output not to contains exact consecutive duplications like "kept me me honest" ### Note I fixed this behaviour by increasing the audio overlap chunk second from 1s to 2s or mor...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: typically a duplication. ### Steps to reproduce Audio sample used is a HuggingFace's Obama MP3 file sample of 03:24 duration, [you can download it here](https://huggingface.co/datasets/hf-internal-testing/dummy-audio-sa...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: Audio transcription duplicated words between chunks bug;stale ### Your current environment ### 🐛 Describe the bug When using whisper-large-v3, there are cases where a word pronounced at the end of a chunk is dupl...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: Here `have kept me me honest` is typically a duplication. ### Steps to reproduce Audio sample used is a HuggingFace's Obama MP3 file sample of 03:24 duration, [you can download it here](https://huggingface.co/datasets/h...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: se' \ -F "file=@ " \ -F "prompt=I've seen our doctors and volunteers rebuild" \ -F 'temperature=0.6' \ -F 'language=en' ``` ### Expectations I expect my output not to contains exact consecutive duplications like "kept m...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: arg ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
