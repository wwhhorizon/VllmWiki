# vllm-project/vllm#16335: [Bug]: Run transcription task with mp4 file failed.

| 字段 | 值 |
| --- | --- |
| Issue | [#16335](https://github.com/vllm-project/vllm/issues/16335) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | kernel_eff |
| Operator 关键词 | cuda;operator;quantization;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Run transcription task with mp4 file failed.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug model：openai/whisper-large-v3-turbo ``` python -m vllm.entrypoints.openai.api_server --gpu-memory-utilization 0.9 --model models/whisper-large-v3-turbo --served-model-name models/whisper-large-v3-turbo --task transcription --port 28037 ``` 1. When use .mp4 file as input, failed as below: ![Image](https://github.com/user-attachments/assets/50fc5898-2c6a-4b07-80c6-343ca893aa13) ![Image](https://github.com/user-attachments/assets/7b180b6f-a078-46da-be49-8b6ff5131ea2) 2. When use .ogg file as input, work correct. 3. When I convert the same .mp4 file to .ogg, work correct. I just extract [examples/online_serving/openai_transcription_client.py](https://github.com/vllm-project/vllm/blob/main/examples/online_serving/openai_transcription_client.py) and modify as below: ``` ...... def sync_openai(audio_url): url = "1.mp4" with open(url, "rb") as f: transcription = client.audio.transcriptions.create( file=f, model="models/whisper-large-v3-turbo", language="ar", response_format="json", temperature=0.0) return transcription.text ...... ``` or how can I read mp4 correctly? ### Before submitting a new issue... - [x] Make sure you already search...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. performance ci_build;distributed_parallel;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding cuda;operator;quantization;triton b...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ly? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: iled. bug;stale ### Your current environment ### 🐛 Describe the bug model：openai/whisper-large-v3-turbo ``` python -m vllm.entrypoints.openai.api_server --gpu-memory-utilization 0.9 --model models/whisper-large-v3-turbo...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: Run transcription task with mp4 file failed. bug;stale ### Your current environment ### 🐛 Describe the bug model：openai/whisper-large-v3-turbo ``` python -m vllm.entrypoints.openai.api_server --gpu-memory-utiliza...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: tization;sampling_logits;speculative_decoding cuda;operator;quantization;triton build_error env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
