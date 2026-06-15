# vllm-project/vllm#4627: [Bug]: Add logger and redirect logs to a file

| 字段 | 值 |
| --- | --- |
| Issue | [#4627](https://github.com/vllm-project/vllm/issues/4627) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Add logger and redirect logs to a file

### Issue 正文摘录

### Your current environment * `VLLM 0.3.0` * `ray 2.9.2` ### 🐛 Describe the bug If I used serve ray to run the chat completion entrypoint with VLLM. I can't use my logger to redirect logs into a file. even if I used it without redirection to a file it didn't output anything! > **NOTE** **Plus if I have multiple replicas how it handle writing to the logger file from many workers?** ``` from ray import serve from fastapi import FastAPI, Request from fastapi.responses import StreamingResponse from fastapi.responses import JSONResponse, StreamingResponse from vllm import AsyncEngineArgs, AsyncLLMEngine from protocol import ChatCompletionRequest, ErrorResponse from serving_chat import OpenAIServingChat ## logger import logging logger = logging.getLogger(__name__) logger.setLevel(logging.INFO) handler = logging.StreamHandler() logger.addHandler(handler) save_logs_path = Path("logs") file_handler = logging.FileHandler(str("logs" / "run.log")) logger.addHandler(file_handler) app = FastAPI() @serve.deployment( ray_actor_options={"num_gpus": 1}, ) @serve.ingress(app) class OpenLLMDeployment: def __init__(self) -> None: ENGINE_ARGS = AsyncEngineArgs( gpu_memory_utilization= 0.95, model="pat...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: it handle writing to the logger file from many workers?** ``` from ray import serve from fastapi import FastAPI, Request from fastapi.responses import StreamingResponse from fastapi.responses import JSONResponse, Stream...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: media_type="text/event-stream") else: return JSONResponse(content=generator.model_dump()) service = OpenLLMDeployment.bind() ```
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: = AsyncEngineArgs( gpu_memory_utilization= 0.95, model="path/to/model", max_model_len=4096, ) self.engine = AsyncLLMEngine.from_engine_args(ENGINE_ARGS) logger.info("Initilize LLM") @app.post("/v1/chat/completions")
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: many workers?** ``` from ray import serve from fastapi import FastAPI, Request from fastapi.responses import StreamingResponse from fastapi.responses import JSONResponse, StreamingResponse from vllm import AsyncEngineAr...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
