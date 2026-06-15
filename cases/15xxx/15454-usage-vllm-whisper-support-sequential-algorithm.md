# vllm-project/vllm#15454: [Usage]: vLLM Whisper support Sequential algorithm?

| 字段 | 值 |
| --- | --- |
| Issue | [#15454](https://github.com/vllm-project/vllm/issues/15454) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: vLLM Whisper support Sequential algorithm?

### Issue 正文摘录

Hello. Thanks for Great Work! We are using whisper utilizing vLLM as shown in the code below. ``` files = {"file": ("audio.mp3", open("audio.mp3", "rb"), "audio/mpeg")} data = {"model": "local-whisper-large-v3-turbo"} response = requests.post("http://localhost:8000/v1/audio/transcriptions", files=files, data=data) text = response.json()["text"] ``` But if the audio is longer than 30 seconds, I'm chunking it into 30 seconds. Does vLLM support the Sequential algorithm processing long audio like the whisper API? Thanks. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ks. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: {"file": ("audio.mp3", open("audio.mp3", "rb"), "audio/mpeg")} data = {"model": "local-whisper-large-v3-turbo"} response = requests.post("http://localhost:8000/v1/audio/transcriptions", files=files, data=data) text = re...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: udio/mpeg")} data = {"model": "local-whisper-large-v3-turbo"} response = requests.post("http://localhost:8000/v1/audio/transcriptions", files=files, data=data) text = response.json()["text"] ``` But if the audio is long...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
