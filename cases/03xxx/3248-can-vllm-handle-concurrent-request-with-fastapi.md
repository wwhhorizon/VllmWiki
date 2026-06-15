# vllm-project/vllm#3248: Can vLLM handle concurrent request with FastAPI?

| 字段 | 值 |
| --- | --- |
| Issue | [#3248](https://github.com/vllm-project/vllm/issues/3248) |
| 状态 | closed |
| 标签 |  |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | frontend_api;model_support;quantization;sampling_logits |
| 子分类 | env_compat |
| Operator 关键词 | quantization;sampling |
| 症状 | crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> Can vLLM handle concurrent request with FastAPI?

### Issue 正文摘录

OS: ubuntu 20.04 (Google Colab) GPU : Nvidia T4 15GB, A100 40GB (Google Colab) ```python import nest_asyncio from pyngrok import ngrok, conf import uvicorn from typing import Union from fastapi import FastAPI from langchain_community.llms import VLLM from vllm import LLM, SamplingParams # Create an VLLM. llm_v = LLM(model="OrionStarAI/Orion-14B-Chat-Int4", trust_remote_code=True, quantization="AWQ", dtype="half", gpu_memory_utilization=0.8) @app.get("/chat/a") def chat(): prompt = generate_prompt('넌 김치만두가 좋아 고기 만두가 좋아?') sampling_params = SamplingParams(temperature=0.4, top_p=0.5, max_tokens=256) result = llm_v.generate(prompt, sampling_params) print(result[0].outputs[0].text) return {"Hello": result[0].outputs[0].text} ngrok_tunnel = ngrok.connect(8000) print('Public URL:', ngrok_tunnel.public_url) nest_asyncio.apply() uvicorn.run(app, port=8000) ``` The OrionStarAI/Orion-14B-Chat-Int4 quantization model is being tested in a FastAPI environment with vLLM. When testing requests, there is no problem processing them one by one, but if another request is received before the answer is generated, the following error occurs. ``` ERROR: Exception in ASGI application Traceback (most recen...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: (Google Colab) GPU : Nvidia T4 15GB, A100 40GB (Google Colab) ```python import nest_asyncio from pyngrok import ngrok, conf import uvicorn from typing import Union from fastapi import FastAPI from langchain_community.ll...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: gParams # Create an VLLM. llm_v = LLM(model="OrionStarAI/Orion-14B-Chat-Int4", trust_remote_code=True, quantization="AWQ", dtype="half", gpu_memory_utilization=0.8) @app.get("/chat/a") def chat(): prompt = generate_prom...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: ceive, sender) File "/usr/local/lib/python3.10/dist-packages/starlette/routing.py", line 758, in __call__ await self.middleware_stack(scope, receive, send) File "/usr/local/lib/python3.10/dist-packages/starlette/routing...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: Can vLLM handle concurrent request with FastAPI? OS: ubuntu 20.04 (Google Colab) GPU : Nvidia T4 15GB, A100 40GB (Google Colab) ```python import nest_asyncio from pyngrok import ngrok, conf import uvicorn from typing im...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: uest with FastAPI? OS: ubuntu 20.04 (Google Colab) GPU : Nvidia T4 15GB, A100 40GB (Google Colab) ```python import nest_asyncio from pyngrok import ngrok, conf import uvicorn from typing import Union from fastapi import...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
