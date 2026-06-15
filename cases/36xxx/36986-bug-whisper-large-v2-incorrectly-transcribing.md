# vllm-project/vllm#36986: [Bug]: whisper large v2 incorrectly transcribing

| 字段 | 值 |
| --- | --- |
| Issue | [#36986](https://github.com/vllm-project/vllm/issues/36986) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: whisper large v2 incorrectly transcribing

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug We are on `vllm==0.14.1` and are observing that Whisper Large V2 is not transcribing our audio requests. ```python3 import asyncio import json import httpx from openai import OpenAI audio_file = "Chorus.wav" api_base = "http://localhost:8001/v1" client = OpenAI( base_url=api_base, ) def sync_openai(): with open(audio_file, "rb") as f: transcription = client.audio.transcriptions.create( file=f, model="openai/whisper-large-v2", language="en", response_format="json", temperature=0.0, ) print("transcription result:", transcription.text) sync_openai() async def stream_openai_response(): data = { "language": "en", "stream": True, "model": "vllm:openai/whisper-large-v2", } url = api_base + "/audio/transcriptions" print("transcription result:", end=" ") async with httpx.AsyncClient() as http: with open(audio_file, "rb") as f: async with http.stream( "POST", url, files={"file": f}, data=data ) as response: async for line in response.aiter_lines(): if line: if line.startswith("data: "): line = line[len("data: ") :] if line.strip() == "[DONE]": break chunk = json.loads(line) content = chunk["choices"][0].get("delta", {}).get("content") prin...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: hat Whisper Large V2 is not transcribing our audio requests. ```python3 import asyncio import json import httpx from openai import OpenAI audio_file = "Chorus.wav" api_base = "http://localhost:8001/v1" client = OpenAI(...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: ta ) as response: async for line in response.aiter_lines(): if line: if line.startswith("data: "): line = line[len("data: ") :] if line.strip() == "[DONE]":
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: av) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: on = client.audio.transcriptions.create( file=f, model="openai/whisper-large-v2", language="en", response_format="json", temperature=0.0, ) print("transcription result:", transcription.text) sync_openai() async def
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: 1` and are observing that Whisper Large V2 is not transcribing our audio requests. ```python3 import asyncio import json import httpx from openai import OpenAI audio_file = "Chorus.wav" api_base = "http://localhost:8001...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
