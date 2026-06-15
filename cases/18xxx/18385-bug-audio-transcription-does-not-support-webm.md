# vllm-project/vllm#18385: [Bug]: Audio transcription does not support webm

| 字段 | 值 |
| --- | --- |
| Issue | [#18385](https://github.com/vllm-project/vllm/issues/18385) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 14; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Audio transcription does not support webm

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ```python from openai import OpenAI client = OpenAI( api_key="sk-sxxxxx", base_url="http:// /v1" ) audio_file_path = "common_voice_yue_31209989.webm" # mp3 works, webm fails try: with open(audio_file_path, "rb") as audio_file: # Transcribe the audio file transcription = client.audio.transcriptions.create( file=audio_file, model="openai/whisper-large-v3" ) # Print the transcription text print("Transcription:", transcription.text) except Exception as e: print(f"An error occurred: {str(e)}") ``` Only the following line indicates the failure, no debug message appears.... > **INFO: 172.19.0.2:42158 - "POST /v1/audio/transcriptions HTTP/1.1" 500 Internal Server Error** ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ur current environment ### 🐛 Describe the bug ```python from openai import OpenAI client = OpenAI( api_key="sk-sxxxxx", base_url="http:// /v1" ) audio_file_path = "common_voice_yue_31209989.webm" # mp3 works, webm fails...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: r** ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: Audio transcription does not support webm bug;stale ### Your current environment ### 🐛 Describe the bug ```python from openai import OpenAI client = OpenAI( api_key="sk-sxxxxx", base_url="http:// /v1" ) audio_fil...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency Your current environment
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: nt.audio.transcriptions.create( file=audio_file, model="openai/whisper-large-v3" ) # Print the transcription text print("Transcription:", transcription.text) except Exception as e: print(f"An error occurred: {str(e)}")...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
