# vllm-project/vllm#14127: [Usage]:   "POST /v1/audio/transcriptions HTTP/1.1" 404 Not Found

| 字段 | 值 |
| --- | --- |
| Issue | [#14127](https://github.com/vllm-project/vllm/issues/14127) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]:   "POST /v1/audio/transcriptions HTTP/1.1" 404 Not Found

### Issue 正文摘录

### Your current environment ```text my env: fastapi 0.115.7 prometheus-fastapi-instrumentator 7.0.2 vllm 0.7.3.dev3+gc786e75.cu124 openai 1.60.0 openai-whisper 20240930 I am using: def call_whisper(audio_path): # Modify OpenAI's API key and API base to use vLLM's API server. openai_api_key = "EMPTY" # openai_api_base = "http://localhost:8000/v1" # openai_api_base = "http://localhost:8261/v1" # openai_api_base = "http://0.0.0.0:8261/" openai_api_base = "http://0.0.0.0:8261/v1" client = OpenAI( api_key=openai_api_key, base_url=openai_api_base, ) with open(audio_path, "rb") as audio_file: transcription = client.audio.transcriptions.create( file=audio_file, model="whisper-large-v3-turbo", language="en", response_format="text", temperature=0.0) print("transcription result:", transcription) audio_path = "../datasets/sample-3s.wav" print(call_whisper(audio_path)) vllm.sh: vllm serve whisper-large-v3-turbo --port 8261 --host 0.0.0.0 --dtype float16 --gpu_memory_utilization 0.99 vllm succuss: INFO 03-03 17:12:11 launcher.py:21] Available routes are: INFO 03-03 17:12:11 launcher.py:29] Route: /openapi.json, Methods: GET, HEAD INFO 03-03 17:12:11 launcher.py:29] Route: /docs, Methods: GET,...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: te: /v1/models, Methods: GET INFO 03-03 17:12:11 launcher.py:29] Route: /version, Methods: GET INFO 03-03 17:12:11 launcher.py:29] Route: /v1/chat/completions, Methods: POST INFO 03-03 17:12:11 launcher.py:29] Route: /v...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: lm.sh: vllm serve whisper-large-v3-turbo --port 8261 --host 0.0.0.0 --dtype float16 --gpu_memory_utilization 0.99 vllm succuss: INFO 03-03 17:12:11 launcher.py:21] Available routes are: INFO 03-03 17:12:11 launcher.py:2...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: nt.audio.transcriptions.create( file=audio_file, model="whisper-large-v3-turbo", language="en", response_format="text", temperature=0.0) print("transcription result:", transcription) audio_path = "../datasets/sample-3s....
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: lm. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ations, Methods: POST INFO: Started server process [10525] INFO: Waiting for application startup. INFO: Application startup complete. INFO: Uvicorn running on http://0.0.0.0:8261 (Press CTRL+C to quit) INFO: 127.0.0.1:5...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
