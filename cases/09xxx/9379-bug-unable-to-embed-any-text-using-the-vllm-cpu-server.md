# vllm-project/vllm#9379: [Bug]: Unable to embed any text using the vLLM CPU server

| 字段 | 值 |
| --- | --- |
| Issue | [#9379](https://github.com/vllm-project/vllm/issues/9379) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;frontend_api;hardware_porting;model_support;sampling_logits |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;import_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Unable to embed any text using the vLLM CPU server

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug The OpenAI Embeddings endpoint (/v1/embeddings) served by the vLLM server (CPU) throws the following exception: ``` ERROR: Exception in ASGI application Traceback (most recent call last): File "/home/ubuntu/avi/venv/lib/python3.10/site-packages/uvicorn/protocols/http/httptools_impl.py", line 401, in run_asgi result = await app( # type: ignore[func-returns-value] File "/home/ubuntu/avi/venv/lib/python3.10/site-packages/uvicorn/middleware/proxy_headers.py", line 60, in __call__ return await self.app(scope, receive, send) File "/home/ubuntu/avi/venv/lib/python3.10/site-packages/fastapi/applications.py", line 1054, in __call__ await super().__call__(scope, receive, send) File "/home/ubuntu/avi/venv/lib/python3.10/site-packages/starlette/applications.py", line 113, in __call__ await self.middleware_stack(scope, receive, send) File "/home/ubuntu/avi/venv/lib/python3.10/site-packages/starlette/middleware/errors.py", line 187, in __call__ raise exc File "/home/ubuntu/avi/venv/lib/python3.10/site-packages/starlette/middleware/errors.py", line 165, in __call__ await self.app(scope, receive, _send) File "...

## 现有链接修复摘要

#10193 [Hardware][CPU] Add embedding models support for CPU backend

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: ternal Server Error ``` upon running the below script, ``` from openai import OpenAI # Modify OpenAI's API key and API base to use vLLM's API server. openai_api_key = "EMPTY" openai_api_base = "http://localhost:8000/v1"...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: er) File "/home/ubuntu/avi/venv/lib/python3.10/site-packages/starlette/routing.py", line 715, in __call__ await self.middleware_stack(scope, receive, send) File "/home/ubuntu/avi/venv/lib/python3.10/site-packages/starle...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: entrypoints.openai.api_server --model intfloat/e5-mistral-7b-instruct --dtype float32 --download-dir ../models/ --port 8000 ``` Same issue happens with the vlLM cpu installation using Dockerfile. ### Before submitting a...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: le. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: 15523975-0: prompt: 'Hello my name is', params: PoolingParams(additional_metadata=None), prompt_token_ids: [1, 22557, 586, 1141, 349, 2], lora_request: None, prompt_adapter_request: None. INFO 10-15 15:51:22 logger.py:3...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#10193](https://github.com/vllm-project/vllm/pull/10193) | closes_keyword | 0.95 | [Hardware][CPU] Add embedding models support for CPU backend | FIX #9379 - Implement CPU embedding model runner - Add encoder-only attention support to SDPA backend |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
