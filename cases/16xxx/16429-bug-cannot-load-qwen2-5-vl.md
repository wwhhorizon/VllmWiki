# vllm-project/vllm#16429: [Bug]: Cannot load  Qwen2.5-VL

| 字段 | 值 |
| --- | --- |
| Issue | [#16429](https://github.com/vllm-project/vllm/issues/16429) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 28; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Cannot load  Qwen2.5-VL

### Issue 正文摘录

We had loaded Qwen2.5-VL successfully nearly 20 days ago. We cannot load Qwen2.5-VL model, after restarting the environment. We suspect that V1 update broke something. ### 🐛 Describe the bug ```python import logging import os from typing import Dict, Optional from fastapi import FastAPI from starlette.requests import Request from starlette.responses import StreamingResponse, JSONResponse from vllm.engine.arg_utils import AsyncEngineArgs from vllm.engine.async_llm_engine import AsyncLLMEngine from vllm.entrypoints.chat_utils import load_chat_template from vllm.entrypoints.openai.cli_args import make_arg_parser from vllm.entrypoints.openai.protocol import ( ChatCompletionRequest, ChatCompletionResponse, ErrorResponse, ) from vllm.entrypoints.openai.serving_chat import OpenAIServingChat from vllm.entrypoints.openai.serving_models import (BaseModelPath, OpenAIServingModels) from vllm.utils import FlexibleArgumentParser logger = logging.getLogger("ray.serve") app = FastAPI() os.environ["HF_HUB_ENABLE_HF_TRANSFER"] = "1" os.environ["VLLM_USE_V1"] = "0" class VLLMDeployment: def __init__( self, engine_args: AsyncEngineArgs, response_role: str, chat_template: Optional[str] = None, ): logg...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 7: [Bug]: Cannot load Qwen2.5-VL bug;stale We had loaded Qwen2.5-VL successfully nearly 20 days ago. We cannot load Qwen2.5-VL model, after restarting the environment. We suspect that V1 update broke something. ### 🐛 Descr...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: ct that V1 update broke something. ### 🐛 Describe the bug ```python import logging import os from typing import Dict, Optional from fastapi import FastAPI from starlette.requests import Request from starlette.responses...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: [Bug]: Cannot load Qwen2.5-VL bug;stale We had loaded Qwen2.5-VL successfully nearly 20 days ago. We cannot load Qwen2.5-VL model, after restarting the environment. We suspect that V1 update broke something. ### 🐛 Descr...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: ce_eager = True engine_args.tensor_parallel_size = 4 engine_args.dtype="bfloat16" engine_args.model="Qwen/Qwen2.5-VL-72B-Instruct" return VLLMDeployment( engine_args, parsed_args.response_role, parsed_args.chat_template...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: s = OpenAIServingModels(self.engine_args.served_model_name) else: served_model_names = [self.engine_args.model] base_model_paths = [ BaseModelPath(name=name, model_path=self.engine_args.model) for name in served_model_na

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
