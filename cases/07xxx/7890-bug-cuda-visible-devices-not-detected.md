# vllm-project/vllm#7890: [Bug]: CUDA_VISIBLE_DEVICES not detected

| 字段 | 值 |
| --- | --- |
| Issue | [#7890](https://github.com/vllm-project/vllm/issues/7890) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;quantization;triton |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: CUDA_VISIBLE_DEVICES not detected

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Hi, I am trying to execute the following `llm.py` from https://docs.ray.io/en/latest/serve/tutorials/vllm-example.html ```py from typing import Dict, Optional, List import logging from fastapi import FastAPI from starlette.requests import Request from starlette.responses import StreamingResponse, JSONResponse from ray import serve from vllm.engine.arg_utils import AsyncEngineArgs from vllm.engine.async_llm_engine import AsyncLLMEngine from vllm.entrypoints.openai.cli_args import make_arg_parser from vllm.entrypoints.openai.protocol import ( ChatCompletionRequest, ChatCompletionResponse, ErrorResponse, ) from vllm.entrypoints.openai.serving_chat import OpenAIServingChat from vllm.entrypoints.openai.serving_engine import LoRAModulePath from vllm.utils import FlexibleArgumentParser logger = logging.getLogger("ray.serve") app = FastAPI() @serve.deployment( autoscaling_config={ "min_replicas": 1, "max_replicas": 10, "target_ongoing_requests": 5, }, max_ongoing_requests=10, ) @serve.ingress(app) class VLLMDeployment: def __init__( self, engine_args: AsyncEngineArgs, response_role: str, lora_modules: Optional[List[LoRAModulePath]] = Non...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: Logger("ray.serve") app = FastAPI() @serve.deployment( autoscaling_config={ "min_replicas": 1, "max_replicas": 10, "target_ongoing_requests": 5, }, max_ongoing_requests=10, ) @serve.ingress(app) class VLLMDeployment: de...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: ptional, List import logging from fastapi import FastAPI from starlette.requests import Request from starlette.responses import StreamingResponse, JSONResponse from ray import serve from vllm.engine.arg_utils import Asy...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: cs.ray.io/en/latest/serve/tutorials/vllm-example.html ```py from typing import Dict, Optional, List import logging from fastapi import FastAPI from starlette.requests import Request from starlette.responses import Strea...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [Bug]: CUDA_VISIBLE_DEVICES not detected bug ### Your current environment ### 🐛 Describe the bug Hi, I am trying to execute the following `llm.py` from https://docs.ray.io/en/latest/serve/tutorials/vllm-example.html ```p
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 4: served_model_names = self.engine_args.served_model_name else: served_model_names = [self.engine_args.model] self.openai_serving_chat = OpenAIServingChat( self.engine, model_config, served_model_names,

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
