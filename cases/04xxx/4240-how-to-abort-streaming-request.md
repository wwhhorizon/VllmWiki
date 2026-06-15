# vllm-project/vllm#4240: How to abort streaming request?

| 字段 | 值 |
| --- | --- |
| Issue | [#4240](https://github.com/vllm-project/vllm/issues/4240) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> How to abort streaming request?

### Issue 正文摘录

### Your current environment vllm 0.3.0 ray 2.9.2 ### 🐛 Describe the bug If I have a streaming request, and I need to stop the request from continue generating tokens, how? if I have the following endpoint? Or how to abort a streaming request in VLLM as general? `In ray_serv.py` ``` from ray import serve from fastapi import FastAPI, Request from fastapi.responses import StreamingResponse from fastapi.responses import JSONResponse, StreamingResponse from vllm import AsyncEngineArgs, AsyncLLMEngine from protocol import ChatCompletionRequest, ErrorResponse from serving_chat import OpenAIServingChat app = FastAPI() @serve.deployment( ray_actor_options={"num_gpus": 1}, ) @serve.ingress(app) class OpenLLMDeployment: def __init__(self) -> None: ENGINE_ARGS = AsyncEngineArgs( gpu_memory_utilization= 0.95, model="path/to/model", max_model_len=4096, ) self.engine = AsyncLLMEngine.from_engine_args(ENGINE_ARGS) @app.post("/v1/chat/completions") async def create_chat_completion(request: ChatCompletionRequest, raw_request: Request): generator = await OpenAIServingChat.create_chat_completion( request, raw_request) if isinstance(generator, ErrorResponse): return JSONResponse(content=generator.mod...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: a streaming request in VLLM as general? `In ray_serv.py` ``` from ray import serve from fastapi import FastAPI, Request from fastapi.responses import StreamingResponse from fastapi.responses import JSONResponse, Streami...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: media_type="text/event-stream") else: return JSONResponse(content=generator.model_dump()) service = OpenLLMDeployment.bind() ``` I run it as following: `serve run ray_serv:service --port 5000 --host 0.0.0.0`
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: = AsyncEngineArgs( gpu_memory_utilization= 0.95, model="path/to/model", max_model_len=4096, ) self.engine = AsyncLLMEngine.from_engine_args(ENGINE_ARGS) @app.post("/v1/chat/completions") async def create_chat_completion(
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: How to abort streaming request? bug ### Your current environment vllm 0.3.0 ray 2.9.2 ### 🐛 Describe the bug If I have a streaming request, and I need to stop the request from continue generating tokens, how? if I have...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
