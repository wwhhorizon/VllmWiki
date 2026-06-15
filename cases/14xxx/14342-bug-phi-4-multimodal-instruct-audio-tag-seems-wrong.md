# vllm-project/vllm#14342: [Bug]: Phi-4-multimodal-instruct audio tag seems wrong

| 字段 | 值 |
| --- | --- |
| Issue | [#14342](https://github.com/vllm-project/vllm/issues/14342) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm;sampling_logits;speculative_decoding |
| 子分类 | env_compat |
| Operator 关键词 | cuda;gemm;operator;sampling;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Phi-4-multimodal-instruct audio tag seems wrong

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug the audio tag in vLLM for phi4-mm is while in sample code of phi4-mm is sample request file is like: ```python import base64 import requests import json VLLM_API_URL = "http://localhost:6666/v1/chat/completions" MODEL_NAME = "phi-4-multimodal" VLLM_API_KEY = "EMPTY" def process_audio_with_base64(audio_path): with open(audio_path, "rb") as f: audio_data = base64.b64encode(f.read()).decode("utf-8") payload = { "model": MODEL_NAME, "messages": [ { "role": "user", "content": [ {"type": "audio_url", "audio_url": {"url": f"data:audio/wav;base64,{audio_data}"}}, {"type": "text", "text": "将音频转录为文本，然后翻译成日文。使用 作为原始转录和翻译之间的分隔符。"}, ] } ], "temperature": 0.3, "max_tokens": 1000 } response = requests.post( VLLM_API_URL, headers={ "Content-Type": "application/json", "Authorization": f"Bearer {VLLM_API_KEY}" }, data=json.dumps(payload) ) if response.status_code == 200: result = response.json()["choices"][0]["message"]["content"] print(f">>> \n{result}") return result else: print(f"API failed {code: {response.status_code})") print(f"ERROR: {response.text}") raise Exception(f"API failed: {response.text}") process_audio_with_base64("sample.wav") ``...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: le in sample code of phi4-mm is sample request file is like: ```python import base64 import requests import json VLLM_API_URL = "http://localhost:6666/v1/chat/completions" MODEL_NAME = "phi-4-multimodal" VLLM_API_KEY =...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: Phi-4-multimodal-instruct audio tag seems wrong bug ### Your current environment ### 🐛 Describe the bug the audio tag in vLLM for phi4-mm is while in sample code of phi4-mm is sample request file is like: ```pyth...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: tag in vLLM for phi4-mm is while in sample code of phi4-mm is sample request file is like: ```python import base64 import requests import json VLLM_API_URL = "http://localhost:6666/v1/chat/completions" MODEL_NAME = "phi...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: tag ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: dal_vlm;sampling_logits;speculative_decoding cuda;gemm;operator;sampling;triton build_error env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
