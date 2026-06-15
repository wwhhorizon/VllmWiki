# vllm-project/vllm#25714: How to pass `thinking_budget` for Qwen-3 Thinking models in offline AsyncLLMEngine?

| 字段 | 值 |
| --- | --- |
| Issue | [#25714](https://github.com/vllm-project/vllm/issues/25714) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> How to pass `thinking_budget` for Qwen-3 Thinking models in offline AsyncLLMEngine?

### Issue 正文摘录

### Your current environment Hi vLLM team 👋 I’m trying to run **Qwen3-30B-A3B-Thinking-2507** with offline inference using `AsyncLLMEngine`. My code looks like this: ```python import asyncio import time import torch from vllm import AsyncLLMEngine, AsyncEngineArgs, SamplingParams from transformers import AutoTokenizer from huggingface_hub import login # Login to Hugging Face Hub login("REMOVED") MODEL_NAME = "Qwen/Qwen3-30B-A3B-Thinking-2507" prompt = "who is kim dahyun" # Detect GPUs num_device = torch.cuda.device_count() print(f"Detected {num_device} CUDA device(s).") # Initialize engine engine_args = AsyncEngineArgs( model=MODEL_NAME, tokenizer=MODEL_NAME, max_model_len=8192, tensor_parallel_size=num_device, dtype="bfloat16", enforce_eager=True, enable_chunked_prefill=True, gpu_memory_utilization=0.95, reasoning_parser="qwen3" ) engine = AsyncLLMEngine.from_engine_args(engine_args) # Sampling params sampling_params = SamplingParams( max_tokens=2048, temperature=0.6, top_p=0.95, top_k=20, min_p=0.0, extra_body={"thinking_budget": 50} ) # Tokenizer + format messages messages = [ {"role": "system", "content": "You are a helpful assistant."}, {"role": "user", "content": prompt} ] t...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: How to pass `thinking_budget` for Qwen-3 Thinking models in offline AsyncLLMEngine? usage;stale ### Your current environment Hi vLLM team 👋 I’m trying to run **Qwen3-30B-A3B-Thinking-2507** with offline inference using...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: L_NAME, max_model_len=8192, tensor_parallel_size=num_device, dtype="bfloat16", enforce_eager=True, enable_chunked_prefill=True, gpu_memory_utilization=0.95, reasoning_parser="qwen3" ) engine = AsyncLLMEngine.from_engine...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ing-2507" prompt = "who is kim dahyun" # Detect GPUs num_device = torch.cuda.device_count() print(f"Detected {num_device} CUDA device(s).") # Initialize engine engine_args = AsyncEngineArgs( model=MODEL_NAME, tokenizer=...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: king_budget` for Qwen-3 Thinking models in offline AsyncLLMEngine? usage;stale ### Your current environment Hi vLLM team 👋 I’m trying to run **Qwen3-30B-A3B-Thinking-2507** with offline inference using `AsyncLLMEngine`....
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: e inference using `AsyncLLMEngine`. My code looks like this: ```python import asyncio import time import torch from vllm import AsyncLLMEngine, AsyncEngineArgs, SamplingParams from transformers import AutoTokenizer from...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
