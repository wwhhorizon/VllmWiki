# vllm-project/vllm#28123: [Bug]: base64 images not working in OpenAI server API

| 字段 | 值 |
| --- | --- |
| Issue | [#28123](https://github.com/vllm-project/vllm/issues/28123) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: base64 images not working in OpenAI server API

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When running the OpenAI compatible server using docker and with `Qwen/Qwen3-VL-30B-A3B-Instruct-FP8` as model, I can pass images through URLs but not with base64. Deployment `docker-compose.yaml`: ```yaml services: vllm: image: vllm/vllm-openai:latest ports: - "8000:8000" volumes: - ~/.cache/huggingface:/root/.cache/huggingface runtime: nvidia restart: unless-stopped ipc: host command: ["--model", "Qwen/Qwen3-VL-30B-A3B-Instruct-FP8", "--enable-auto-tool-choice", "--tool-call-parser", "hermes"] ``` Code used for sending images via URL: ```python from openai import OpenAI openai_api_base = "http://localhost:8000/v1" client = OpenAI( api_key="example", base_url=openai_api_base, ) image_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg" chat_response = client.chat.completions.create( model="Qwen/Qwen3-VL-30B-A3B-Instruct-FP8", messages=[ { "role": "user", "content": [ { "type": "text", "text": "Whats in this image?", }, { "type": "image_url", "image_url": {"url": image_url}, }, ], } ], ) print("Chat completion output:"...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: he bug When running the OpenAI compatible server using docker and with `Qwen/Qwen3-VL-30B-A3B-Instruct-FP8` as model, I can pass images through URLs but not with base64. Deployment `docker-compose.yaml`: ```yaml service...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: ### 🐛 Describe the bug When running the OpenAI compatible server using docker and with `Qwen/Qwen3-VL-30B-A3B-Instruct-FP8` as model, I can pass images through URLs but not with base64. Deployment `docker-compose.yaml`:...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: compatible server using docker and with `Qwen/Qwen3-VL-30B-A3B-Instruct-FP8` as model, I can pass images through URLs but not with base64. Deployment `docker-compose.yaml`: ```yaml services: vllm: image: vllm/vllm-opena...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: url it fails: ```python from openai import OpenAI import base64 import requests openai_api_base = "http://localhost:8000/v1" client = OpenAI( api_key="example", base_url=openai_api_base, ) image_url = "https://upload.wi...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: erature, tool_choice, tools, top_logprobs, top_p, user, verbosity, web_search_options, extra_headers, extra_query, extra_body, timeout) 1110 @required_args(["messages", "model"], ["messages", "model", "stream"]) 1111 de...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
