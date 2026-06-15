# vllm-project/vllm#9949: [Usage]: Inference delay

| 字段 | 值 |
| --- | --- |
| Issue | [#9949](https://github.com/vllm-project/vllm/issues/9949) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | frontend_api;model_support;quantization;sampling_logits |
| 子分类 | latency_reg |
| Operator 关键词 | cuda;quantization |
| 症状 |  |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: Inference delay

### Issue 正文摘录

### Inference Delay I'm deploying a large language model (LLM) using FastAPI and vLLM, but I'm facing significant delays during the initial inference (up to 5 minutes). I have tried loading the model at startup using the lifespan context manager, but the performance issue persists. Are there effective strategies to reduce this initial response time? ``` from vllm import LLM, SamplingParams from fastapi import FastAPI from pydantic import BaseModel import uvicorn from typing import List import os import torch app = FastAPI() device = "cuda" if torch.cuda.is_available() else "cpu" model_name = "" #Finetuned llama 3.1 70b llm = LLM(model=model_name, dtype=torch.bfloat16, gpu_memory_utilization=0.8, max_model_len = 4096, trust_remote_code=True, quantization="bitsandbytes", load_format="bitsandbytes") SYSTEM_MESSAGE = """ Act as an ... """ class RequestData(BaseModel): prompts: List[str] max_tokens: int = 2048 temperature: float = 0.7 @app.post("/predict") async def generate_text(data: RequestData): formatted_prompts = [ f" {SYSTEM_MESSAGE}\n : {prompt}\n :" for prompt in data.prompts ] sampling_params = SamplingParams( max_tokens=data.max_tokens, temperature=data.temperature, ) result...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: pu" model_name = "" #Finetuned llama 3.1 70b llm = LLM(model=model_name, dtype=torch.bfloat16, gpu_memory_utilization=0.8, max_model_len = 4096, trust_remote_code=True, quantization="bitsandbytes", load_format="bitsandb...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: deploying a large language model (LLM) using FastAPI and vLLM, but I'm facing significant delays during the initial inference (up to 5 minutes). I have tried loading the model at startup using the lifespan context manag...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ce delay usage;stale ### Inference Delay I'm deploying a large language model (LLM) using FastAPI and vLLM, but I'm facing significant delays during the initial inference (up to 5 minutes). I have tried loading the mode...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Usage]: Inference delay usage;stale ### Inference Delay I'm deploying a large language model (LLM) using FastAPI and vLLM, but I'm facing significant delays during the initial inference (up to 5 minutes). I have tried...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: rom typing import List import os import torch app = FastAPI() device = "cuda" if torch.cuda.is_available() else "cpu" model_name = "" #Finetuned llama 3.1 70b llm = LLM(model=model_name, dtype=torch.bfloat16, gpu_memory...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
