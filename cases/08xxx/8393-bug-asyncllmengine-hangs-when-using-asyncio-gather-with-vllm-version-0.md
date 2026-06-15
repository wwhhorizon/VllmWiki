# vllm-project/vllm#8393: [Bug]: AsyncLLMEngine hangs when using `asyncio.gather` with vllm version 0.5.5

| 字段 | 值 |
| --- | --- |
| Issue | [#8393](https://github.com/vllm-project/vllm/issues/8393) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 |  |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: AsyncLLMEngine hangs when using `asyncio.gather` with vllm version 0.5.5

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I'm simply change a little bit of the api_server.py to serve with multiple prompts and using `asyncio.gather` to wait all responses to be ready. the log shows that all requests can successfully finishes, but the response can't be returned from the `asyncio.gather`, it just hangs forever until timeout. ```python """ NOTE: This API server is used only for demonstrating usage of AsyncEngine and simple performance benchmarks. It is not intended for production use. For production use, we recommend using our OpenAI compatible server. We are also not going to accept PRs modifying this file, please change `vllm/entrypoints/openai/api_server.py` instead. """ import asyncio import json import ssl from argparse import Namespace from typing import Any, AsyncGenerator, Optional from fastapi import FastAPI, Request from fastapi.responses import JSONResponse, Response, StreamingResponse from vllm.engine.arg_utils import AsyncEngineArgs from vllm.engine.async_llm_engine import AsyncLLMEngine from vllm.entrypoints.launcher import serve_http from vllm.logger import init_logger from vllm.sampling_params import Sa...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: [Bug]: AsyncLLMEngine hangs when using `asyncio.gather` with vllm version 0.5.5 bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I'm simply change a little bit of the api_serve...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: gather` with vllm version 0.5.5 bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I'm simply change a little bit of the api_server.py to serve with multiple prompts and using `a...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: yncio.gather` to wait all responses to be ready. the log shows that all requests can successfully finishes, but the response can't be returned from the `asyncio.gather`, it just hangs forever until timeout. ```python ""...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: lt=None, help="FastAPI root_path when app is behind a path based routing proxy") parser.add_argument("--log-level", type=str, default="debug") parser = AsyncEngineArgs.add_cli_args(parser) args = parser.parse_args() asy...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: b7cd7e79/ --disable-log-stats --enforce-eager --tensor-parallel-size=8 --dtype=float16 ``` the trace log file is too large, I picked the repeated part when the server hangs here: [vllm_trace.log](https://github.com/user...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
