# vllm-project/vllm#31206: [Bug]: AsyncLLM Qwen/Qwen3-Embedding got stuck in max_model_len >= 6100 (vllm==0.13.0)

| 字段 | 值 |
| --- | --- |
| Issue | [#31206](https://github.com/vllm-project/vllm/issues/31206) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
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

> [Bug]: AsyncLLM Qwen/Qwen3-Embedding got stuck in max_model_len >= 6100 (vllm==0.13.0)

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ### How I deployed the service: ```server.py``` ```python import time from contextlib import asynccontextmanager from starlette import status from starlette.requests import Request from vllm import PoolingParams from vllm.v1.engine.async_llm import AsyncLLM, PoolingParams from vllm import AsyncEngineArgs # from vllm.utils import FlexibleArgumentParser from fastapi import FastAPI, HTTPException from fastapi.responses import JSONResponse from pydantic import BaseModel, ConfigDict @asynccontextmanager async def lifespan(app: FastAPI): app.state.model = AsyncLLM.from_engine_args(AsyncEngineArgs( model="Qwen/Qwen3-Embedding-0.6B", tokenizer="Qwen/Qwen3-Embedding-0.6B", gpu_memory_utilization=0.3, runner="pooling", convert="embed", max_model_len=6100, )) yield app = FastAPI(lifespan=lifespan) class ConfitRequestBody(BaseModel): model_config = ConfigDict(extra='allow') text: str | None = None @app.post("/confit_service/encode") async def text_to_vector( request: Request, request_body: ConfitRequestBody, ): model: AsyncLLM = app.state.model async for output in model.encode(request_body.text, pooling_params=PoolingParams(task='embed'), re...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: ibe the bug ### How I deployed the service: ```server.py``` ```python import time from contextlib import asynccontextmanager from starlette import status from starlette.requests import Request from vllm import PoolingPa...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: AsyncLLM Qwen/Qwen3-Embedding got stuck in max_model_len >= 6100 (vllm==0.13.0) bug;stale ### Your current environment ### 🐛 Describe the bug ### How I deployed the service: ```server.py``` ```python import time...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: en/Qwen3-Embedding got stuck in max_model_len >= 6100 (vllm==0.13.0) bug;stale ### Your current environment ### 🐛 Describe the bug ### How I deployed the service: ```server.py``` ```python import time from contextlib im...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: .0` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
