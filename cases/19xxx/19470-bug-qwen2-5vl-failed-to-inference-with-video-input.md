# vllm-project/vllm#19470: [Bug]: qwen2.5vl failed to inference with video input

| 字段 | 值 |
| --- | --- |
| Issue | [#19470](https://github.com/vllm-project/vllm/issues/19470) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: qwen2.5vl failed to inference with video input

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Qwen2.5-VL-72B-Instruct failed to inference with video input under `vllm0.8.5.post1`. **Server code** ```bash "vllm serve /pretrained/Qwen/Qwen2.5-VL-72B-Instruct --host 0.0.0.0 --port 8000 --served-model-name Qwen2.5-VL-72B-Instruct --tensor-parallel-size 4 --max-num-seqs 1 --trust-remote-code --max-model-len=32768 --gpu-memory-utilization 0.95 ``` **Client code** ```python import base64 import requests from openai import OpenAI openai_api_key = "EMPTY" openai_api_base = "http://10.1.6.147:8000/v1" model = "Qwen2.5-VL-72B-Instruct" client = OpenAI( api_key=openai_api_key, base_url=openai_api_base, ) def encode_base64_content_from_url(content_url: str) -> str: """Encode a content retrieved from a remote url to base64 format.""" with requests.get( content_url, ) as response: response.raise_for_status() result = base64.b64encode(response.content).decode("utf-8") return result video_url = "http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/ForBiggerFun.mp4" video_base64 = encode_base64_content_from_url(video_url) chat_completion_from_base64 = client.chat.completions.create( messages=[ { "role": "user", "content": [ {"t...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: l-len=32768 --gpu-memory-utilization 0.95 ``` **Client code** ```python import base64 import requests from openai import OpenAI openai_api_key = "EMPTY" openai_api_base = "http://10.1.6.147:8000/v1" model = "Qwen2.5-VL-...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: qwen2.5vl failed to inference with video input bug ### Your current environment ### 🐛 Describe the bug Qwen2.5-VL-72B-Instruct failed to inference with video input under `vllm0.8.5.post1`. **Server code** ```bash...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: ling_params.py:347] temperature 1e-06 is less than 0.01, which may cause numerical errors nan or inf in tensors. We have maxed it out to 0.01. [2025-06-11 13:20:55] INFO 06-10 22:20:55 [logger.py:39] Received request ch...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ry-utilization 0.95 ``` **Client code** ```python import base64 import requests from openai import OpenAI openai_api_key = "EMPTY" openai_api_base = "http://10.1.6.147:8000/v1" model = "Qwen2.5-VL-72B-Instruct" client =...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
