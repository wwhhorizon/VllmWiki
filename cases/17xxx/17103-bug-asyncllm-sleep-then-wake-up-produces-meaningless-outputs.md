# vllm-project/vllm#17103: [Bug]: AsyncLLM sleep then wake_up produces meaningless outputs

| 字段 | 值 |
| --- | --- |
| Issue | [#17103](https://github.com/vllm-project/vllm/issues/17103) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: AsyncLLM sleep then wake_up produces meaningless outputs

### Issue 正文摘录

Hi @youkaichao , AsyncLLM engine seems not working properly in sleep/wake_up mode. Related to https://github.com/volcengine/verl/pull/1138 ### Your current environment package version info ``` open_verl [main] $ pip list | grep -E "torch|vllm|ray|transformers" ray 2.44.0 torch 2.6.0+cu124 torchaudio 2.6.0 torchdata 0.11.0 torchvision 0.21.0 transformers 4.47.1 vllm 0.8.3 ``` ### 🐛 Describe the bug ```python import asyncio import fastapi import ray import uvicorn from ray.util.placement_group import placement_group from starlette.requests import Request from starlette.responses import JSONResponse, StreamingResponse from vllm.engine.arg_utils import AsyncEngineArgs from vllm.entrypoints.openai.protocol import ChatCompletionRequest, ChatCompletionResponse, ErrorResponse from vllm.entrypoints.openai.serving_chat import OpenAIServingChat from vllm.entrypoints.openai.serving_models import BaseModelPath, OpenAIServingModels from vllm.v1.engine.async_llm import AsyncLLM @ray.remote(num_cpus=1) class AsyncLLMWorker: def __init__(self, tensor_parallel_size: int=2): model = "Qwen/Qwen2-7B-Instruct" sampling_params = {'n': 1, 'max_completion_tokens': 4096, 'temperature': 1.0, 'top_p': 1, 'to...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: thub.com/volcengine/verl/pull/1138 ### Your current environment package version info ``` open_verl [main] $ pip list | grep -E "torch|vllm|ray|transformers" ray 2.44.0 torch 2.6.0+cu124 torchaudio 2.6.0 torchd
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: rving_chat import OpenAIServingChat from vllm.entrypoints.openai.serving_models import BaseModelPath, OpenAIServingModels from vllm.v1.engine.async_llm import AsyncLLM @ray.remote(num_cpus=1) class AsyncLLMWorker: def _...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: rams, tensor_parallel_size=tensor_parallel_size, dtype="bfloat16", enforce_eager=False, gpu_memory_utilization=0.5, disable_custom_all_reduce=True, disable_mm_preprocessor_cache=True, skip_tokenizer_init=False
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: AsyncLLM sleep then wake_up produces meaningless outputs bug;stale Hi @youkaichao , AsyncLLM engine seems not working properly in sleep/wake_up mode. Related to https://github.com/volcengine/verl/pull/1138 ### Yo...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
