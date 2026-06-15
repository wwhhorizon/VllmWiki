# vllm-project/vllm#13675: [Bug]: "ImportError: Please install vllm[audio] for audio support" while running whisper with '--task=transcription'

| 字段 | 值 |
| --- | --- |
| Issue | [#13675](https://github.com/vllm-project/vllm/issues/13675) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: "ImportError: Please install vllm[audio] for audio support" while running whisper with '--task=transcription'

### Issue 正文摘录

### Your current environment I'm using the latest docker image vllm/vllm-openai:latest ### 🐛 Describe the bug I set up the vllm using docker, my docker-compose file: ```` services: vllm-openai-whisper: image: 'vllm/vllm-openai:latest' volumes: - '/xxxx/.cache/huggingface:/root/.cache/huggingface' command: - "--host=0.0.0.0" - "--port=8000" - "--api-key=xxxx" - "--model=openai/whisper-large-v3-turbo" - "--task=transcription" ```` I'm able to set up the container without any issue, but when I'm trying to send requests to '/v1/audio/transcriptions', I got the following import error: ImportError: Please install vllm[audio] for audio support ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [Bug]: "ImportError: Please install vllm[audio] for audio support" while running whisper with '--task=transcription' bug ### Your current environment I'm using the latest docker image vllm/vllm-openai:latest ### 🐛 Descr...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: image: 'vllm/vllm-openai:latest' volumes: - '/xxxx/.cache/huggingface:/root/.cache/huggingface' command: - "--host=0.0.0.0" - "--port=8000" - "--api-key=xxxx" - "--model=openai/whisper-large-v3-turbo" - "--task=transcri...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ort ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: e to set up the container without any issue, but when I'm trying to send requests to '/v1/audio/transcriptions', I got the following import error: ImportError: Please install vllm[audio] for audio support ### Before sub...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: '--task=transcription' bug ### Your current environment I'm using the latest docker image vllm/vllm-openai:latest ### 🐛 Describe the bug I set up the vllm using docker, my docker-compose file: ```` services: vllm-openai...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
