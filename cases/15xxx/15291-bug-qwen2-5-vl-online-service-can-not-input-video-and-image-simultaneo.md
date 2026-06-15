# vllm-project/vllm#15291: [Bug]: Qwen2.5 VL online service can not input video and image simultaneously.

| 字段 | 值 |
| --- | --- |
| Issue | [#15291](https://github.com/vllm-project/vllm/issues/15291) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Qwen2.5 VL online service can not input video and image simultaneously.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug With server run as: ```shell vllm serve ckpt/Qwen2.5-VL-72B-Instruct \ --allowed-local-media-path / \ --tensor-parallel-size 4 \ --port 8000 \ ``` and request to input video and image simultaneously: ```python import json from openai import OpenAI # Set OpenAI's API key and API base to use vLLM's API server. openai_api_key = "EMPTY" openai_api_base = "http://localhost:8000/v1" client = OpenAI( api_key=openai_api_key, base_url=openai_api_base, ) ### visual input preparation import os import base64 def encode_image_b64(image_path): with open(image_path, "rb") as image_file: img = base64.b64encode(image_file.read()).decode("utf-8") return img def get_image_url_b64(img_b64: str): return f"data:image/png;base64,{img_b64}" def get_video_url_b64(img_b64_list: list[str]): return f"data:video/png;base64,{','.join(img_b64_list)}" images_fnames = sorted([ fn for fn in os.listdir("/path/to/images") if fn.endswith(".png") ]) images_b64 = [ encode_image_b64("/path/to/images/" + fn) for fn in historical_images_fnames ] image_url = get_image_url_b64(images_b64[-1]) video_url = get_video_url_b64(images_b64) messages = [ { "role": "system", "conte...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: 0 \ ``` and request to input video and image simultaneously: ```python import json from openai import OpenAI # Set OpenAI's API key and API base to use vLLM's API server. openai_api_key = "EMPTY" openai_api_base = "http...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: media-path / \ --tensor-parallel-size 4 \ --port 8000 \ ``` and request to input video and image simultaneously: ```python import json from openai import OpenAI # Set OpenAI's API key and API base to use vLLM's API serv...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: it. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Qwen2.5 VL online service can not input video and image simultaneously. bug ### Your current environment ### 🐛 Describe the bug With server run as: ```shell vllm serve ckpt/Qwen2.5-VL-72B-Instruct \ --allowed-l
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: rontend_api;hardware_porting;model_support;sampling_logits cuda;operator;triton build_error;crash env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
