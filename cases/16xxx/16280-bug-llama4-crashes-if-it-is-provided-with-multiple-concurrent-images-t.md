# vllm-project/vllm#16280: [Bug]: LLama4 crashes if it is provided with multiple concurrent images to process

| 字段 | 值 |
| --- | --- |
| Issue | [#16280](https://github.com/vllm-project/vllm/issues/16280) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;frontend_api;hardware_porting;model_support;multimodal_vlm;sampling_logits;speculative_decoding |
| 子分类 | race_cond |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf;nondeterministic |
| 根因提示 | env_dependency;race_condition |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: LLama4 crashes if it is provided with multiple concurrent images to process

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug On V0 of vLLM, LLama 4 (meta-llama/Llama-4-Scout-17B-16E-Instruct) crashes if multiple images are provided for it to process concurrently. Example script (one needs to provide `image_folder` and `endpoint_url`): ```python import asyncio import aiohttp import base64 import os async def send_image(session, api_key, endpoint_url, image_path): # Encode image to base64 with open(image_path, "rb") as image_file: base64_image = base64.b64encode(image_file.read()).decode('utf-8') headers = { "Content-Type": "application/json", "x-api-key": api_key } payload = { "model": "meta-llama/Llama-4-Scout-17B-16E-Instruct", "messages": [ { "role": "user", "content": [ {"type": "text", "text": "What's in this image?"}, { "type": "image_url", "image_url": { "url": f"data:image/jpeg;base64,{base64_image}" } }, {"type": "text", "text": "Are you sure?"} ] } ], "max_tokens": 300 } async with session.post(endpoint_url, headers=headers, json=payload, ssl=False) as response: return await response.json() async def main(): api_key = "your-api-key" endpoint_url = "http://api.example.com/v1/chat/completions" # Get 10 images image_folder = "path/to/images" imag...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ript (one needs to provide `image_folder` and `endpoint_url`): ```python import asyncio import aiohttp import base64 import os async def send_image(session, api_key, endpoint_url, image_path): # Encode image to base64 w...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: LLama4 crashes if it is provided with multiple concurrent images to process bug ### Your current environment ### 🐛 Describe the bug On V0 of vLLM, LLama 4 (meta-llama/Llama-4-Scout-17B-16E-Instruct) crashes if mu...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 3: n 1440 = 1440 multimodal tokens to 720 placeholders ``` The issue seems non-deterministic, depends on how fast the images get processed concurrently. ### Before submitting a new issue... - [x] Make sure you already sear...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: s image_file: base64_image = base64.b64encode(image_file.read()).decode('utf-8') headers = { "Content-Type": "application/json", "x-api-key": api_key } payload = { "model": "meta-llama/Llama-4-Scout-17B-16E-Instruct", "...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ly. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
