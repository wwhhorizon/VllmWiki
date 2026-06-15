# vllm-project/vllm#9833: [Usage]: How to use GLM4v multi_modal_data to make Multi-turn dialogue 

| 字段 | 值 |
| --- | --- |
| Issue | [#9833](https://github.com/vllm-project/vllm/issues/9833) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | frontend_api;model_support;multimodal_vlm;sampling_logits |
| 子分类 | latency_reg |
| Operator 关键词 | cuda;sampling |
| 症状 | crash;oom;slowdown |
| 根因提示 | dtype |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: How to use GLM4v multi_modal_data to make Multi-turn dialogue 

### Issue 正文摘录

### Your current environment vllm = 0.6.3post1 ### How would you like to use vllm According to the demo in GLM4 repository, the specification for multimodal input in vLLM is as follows: ``` { "prompt": "input_text", "multi_modal_data": { "image": image } } ``` I want to know how to make a multi-turn dialogue such as: ``` import time import asyncio from PIL import Image from typing import List, Dict from vllm import SamplingParams, AsyncEngineArgs, AsyncLLMEngine MODEL_PATH = 'path' def load_model_and_tokenizer(model_dir: str): engine_args = AsyncEngineArgs( model=model_dir, tensor_parallel_size=2, dtype="bfloat16", trust_remote_code=True, gpu_memory_utilization=0.4, enforce_eager=True, worker_use_ray=True, disable_log_requests=True # 如果遇见 OOM 现象，建议开启下述参数 # enable_chunked_prefill=True, # max_num_batched_tokens=8192 ) engine = AsyncLLMEngine.from_engine_args(engine_args) return engine async def chat(): engine = load_model_and_tokenizer(MODEL_PATH) params_dict = { "n": 1, "best_of": 1, "presence_penalty": 1.0, "frequency_penalty": 0.0, "temperature": 0.7, "top_p": 0.8, "top_k": -1, # "use_beam_search": False, # "length_penalty": 1, # "early_stopping": False, "ignore_eos": False, "max...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: neArgs( model=model_dir, tensor_parallel_size=2, dtype="bfloat16", trust_remote_code=True, gpu_memory_utilization=0.4, enforce_eager=True, worker_use_ray=True, disable_log_requests=True # 如果遇见 OOM 现象，建议开启下述参数 # en
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: se vllm According to the demo in GLM4 repository, the specification for multimodal input in vLLM is as follows: ``` { "prompt": "input_text", "multi_modal_data": { "image": image } } ``` I want to know how to make a mul...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: enforce_eager=True, worker_use_ray=True, disable_log_requests=True # 如果遇见 OOM 现象，建议开启下述参数 # enable_chunked_prefill=True, # max_num_batched_tokens=8192 ) engine = AsyncLLMEngine.from_engine_args(engine_args) return engin...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: d you like to use vllm According to the demo in GLM4 repository, the specification for multimodal input in vLLM is as follows: ``` { "prompt": "input_text", "multi_modal_data": { "image": image } } ``` I want to know ho...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ": 0.7, "top_p": 0.8, "top_k": -1, # "use_beam_search": False, # "length_penalty": 1, # "early_stopping": False, "ignore_eos": False, "max_tokens": 8192, "logprobs": None, "prompt_logprobs": None, "skip_special_to

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
