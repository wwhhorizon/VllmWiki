# vllm-project/vllm#35276: [Bug]: OpenAI transcribe prompt parameter with whisper return hallucinated transcription

| 字段 | 值 |
| --- | --- |
| Issue | [#35276](https://github.com/vllm-project/vllm/issues/35276) |
| 状态 | open |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: OpenAI transcribe prompt parameter with whisper return hallucinated transcription

### Issue 正文摘录

### Your current environment vllm 0.13.0 ### 🐛 Describe the bug When i prompt a short list (~10 elements) of Cities to Whisper to improve his spelling, i get a transcription full of hallucination (Repetitive word or syllable). I followed the [guideline of prompting](https://developers.openai.com/cookbook/examples/whisper_prompting_guide) but still got no good result. I tried multiple kind of prompting (with and without , etc). [Transcription without prompt.txt](https://github.com/user-attachments/files/25541341/Transcription.without.prompt.txt) [Transcription with prompt.txt](https://github.com/user-attachments/files/25541342/Transcription.with.prompt.txt) (I took a public french speech for good audio quality) ```Python import openai client = openai.AsyncOpenAI( base_url= , api_key= , ) with open(audio_file_path, "rb") as f: response = await client.audio.transcriptions.create( model="openai/whisper-large-v3-turbo", file=f, language="fr", temperature=0.0, timeout=None, prompt="Kiev, Beyrouth, Jérusalem, Tel-Aviv, Bamako, Ouagadougou, Port-au-Prince, Port-Vila, Caraca", ) print(response.text) ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [Bug]: OpenAI transcribe prompt parameter with whisper return hallucinated transcription bug;stale ### Your current environment vllm 0.13.0 ### 🐛 Describe the bug When i prompt a short list (~10 elements) of Cities to W...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: se = await client.audio.transcriptions.create( model="openai/whisper-large-v3-turbo", file=f, language="fr", temperature=0.0, timeout=None,
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ribe prompt parameter with whisper return hallucinated transcription bug;stale ### Your current environment vllm 0.13.0 ### 🐛 Describe the bug When i prompt a short list (~10 elements) of Cities to Whisper to improve hi...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
