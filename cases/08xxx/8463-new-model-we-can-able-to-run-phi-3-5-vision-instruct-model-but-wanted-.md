# vllm-project/vllm#8463: [New Model]: We can able to run phi-3.5 vision instruct model but wanted to run in int4 quantization 

| 字段 | 值 |
| --- | --- |
| Issue | [#8463](https://github.com/vllm-project/vllm/issues/8463) |
| 状态 | closed |
| 标签 | new-model;stale |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [New Model]: We can able to run phi-3.5 vision instruct model but wanted to run in int4 quantization 

### Issue 正文摘录

### The model to consider. ```python from typing import List from fastapi import FastAPI, HTTPException from pydantic import BaseModel from PIL import Image from vllm import LLM, SamplingParams import os import uvicorn import time app = FastAPI() class InferenceRequest(BaseModel): model: str question: str image_paths: List[str] # Initialize models once during application startup models = {} def load_image_from_path(image_path: str) -> Image.Image: """Load a PIL image from a local file path.""" if not os.path.isfile(image_path): raise ValueError(f"File {image_path} does not exist.") return Image.open(image_path).convert("RGB") def load_phi3v(): """Load Phi3V model and return instance.""" return LLM( model="microsoft/Phi-3.5-vision-instruct", trust_remote_code=True, max_model_len=4096, limit_mm_per_prompt={"image": 1}, ) def initialize_models(): """Initialize all models required for inference.""" global models models["phi3_v"] = load_phi3v() def load_phi3v_prompt(question, image_paths: List[str]): placeholders = "\n".join(f" " for i, _ in enumerate(image_paths, start=1)) prompt = f" \n{placeholders}\n{question} \n \n" stop_token_ids = None return prompt, stop_token_ids def run_gener...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: ]: We can able to run phi-3.5 vision instruct model but wanted to run in int4 quantization new-model;stale ### The model to consider. ```python from typing import List from fastapi import FastAPI, HTTPException from pyd...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [New Model]: We can able to run phi-3.5 vision instruct model but wanted to run in int4 quantization new-model;stale ### The model to consider. ```python from typing import List from fastapi import FastAPI, HTTPExceptio...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: vision instruct model but wanted to run in int4 quantization new-model;stale ### The model to consider. ```python from typing import List from fastapi import FastAPI, HTTPException from pydantic import BaseModel from PI...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ation new-model;stale ### The model to consider. ```python from typing import List from fastapi import FastAPI, HTTPException from pydantic import BaseModel from PIL import Image from vllm import LLM, SamplingParams imp...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: del ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
