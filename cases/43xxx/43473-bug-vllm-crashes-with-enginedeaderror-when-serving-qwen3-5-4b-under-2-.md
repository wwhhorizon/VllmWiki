# vllm-project/vllm#43473: [Bug]: vLLM crashes with `EngineDeadError` when serving Qwen3.5-4B under 2-way concurrent image requests

| 字段 | 值 |
| --- | --- |
| Issue | [#43473](https://github.com/vllm-project/vllm/issues/43473) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;operator;sampling |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vLLM crashes with `EngineDeadError` when serving Qwen3.5-4B under 2-way concurrent image requests

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ## Describe the bug When I serve `Qwen3.5-4B` with vLLM and send multiple concurrent image analysis requests, the engine crashes during attention metadata construction. The failure happens while handling concurrent requests through the OpenAI-compatible `/v1/chat/completions` endpoint. In my case, the crash appears when using 2-way concurrency on the client side, with the server configured with `--max-num-seqs 2`. It works fine when requests are processed sequentially, but crashes when there are two concurrent requests. Minimal reproduction client: ```python import asyncio import base64 import mimetypes import sys from pathlib import Path import aiohttp URL = "http://127.0.0.1:8088/v1/chat/completions" MODEL = "Qwen3.5-4B" def image_to_data_url(path: Path) -> str: mime_type = mimetypes.guess_type(path)[0] or "image/png" encoded = base64.b64encode(path.read_bytes()).decode("ascii") return f"data:{mime_type};base64,{encoded}" def build_payload(image_path: Path) -> dict: return { "model": MODEL, "messages": [ { "role": "system", "content": [ { "type": "text", "text": ( 'Extract the image info into this JSON schema. ' 'Return valid J...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: re are two concurrent requests. Minimal reproduction client: ```python import asyncio import base64 import mimetypes import sys from pathlib import Path import aiohttp URL = "http://127.0.0.1:8088/v1/chat/completions" M...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: h `EngineDeadError` when serving Qwen3.5-4B under 2-way concurrent image requests bug ### Your current environment ### 🐛 Describe the bug ## Describe the bug When I serve `Qwen3.5-4B` with vLLM and send multiple concurr...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: vLLM crashes with `EngineDeadError` when serving Qwen3.5-4B under 2-way concurrent image requests bug ### Your current environment ### 🐛 Describe the bug ## Describe the bug When I serve `Qwen3.5-4B` with vLLM an...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: concurrent image analysis requests, the engine crashes during attention metadata construction. The failure happens while handling concurrent requests through the OpenAI-compatible `/v1/chat/completions` endpoint. In my...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: build( File "/usr/local/lib/python3.12/dist-packages/vllm/v1/attention/backends/flashinfer.py", line 1213, in build decode_wrapper = self._get_decode_wrapper( File "/usr/local/lib/python3.12/dist-packages/vllm/v1/attent...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
