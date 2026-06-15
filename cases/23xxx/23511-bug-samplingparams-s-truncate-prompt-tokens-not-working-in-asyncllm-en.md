# vllm-project/vllm#23511: [Bug]: SamplingParams's truncate_prompt_tokens not working in AsyncLLM Engine

| 字段 | 值 |
| --- | --- |
| Issue | [#23511](https://github.com/vllm-project/vllm/issues/23511) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: SamplingParams's truncate_prompt_tokens not working in AsyncLLM Engine

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I've looked at the source code, and asyncllm indeed doesn't have a truncation implementation. The truncation works while using LLM engine. ``` from vllm import SamplingParams from vllm.engine.arg_utils import AsyncEngineArgs from vllm.v1.engine.async_llm import AsyncLLM import asyncio # Initialize AsyncLLM engine with your configuration engine_args = AsyncEngineArgs( model="meta-llama/Llama-3.1-8B-Instruct", max_model_len=20, data_parallel_size=4, # Note: AsyncLLM uses tensor_parallel_size instead of data_parallel_size enforce_eager=True ) # Create the AsyncLLM instance engine = AsyncLLM.from_engine_args(engine_args) # Set sampling parameters sampling_params = SamplingParams( temperature=0.3, top_p=0.9, max_tokens=10, truncate_prompt_tokens=10, ) # Define async generation logic inline async def generate(): result_text = "" async for output in engine.generate( request_id="request-1", prompt="Hello, how are you? Hello, how are you? Hello, how are you? Hello, how are you? Hello, how are you? Hello, how are you? Hello, how are you? Hello, how are you? Hello, how are you? Hello, how are you? ", sampling_params=sampling_params ): # Col...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: plementation. The truncation works while using LLM engine. ``` from vllm import SamplingParams from vllm.engine.arg_utils import AsyncEngineArgs from vllm.v1.engine.async_llm import AsyncLLM import asyncio # Initialize...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: han the maximum model length of 20. Make sure that `max_model_len` is no smaller than the number of text tokens. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked t...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: m import AsyncLLM import asyncio # Initialize AsyncLLM engine with your configuration engine_args = AsyncEngineArgs( model="meta-llama/Llama-3.1-8B-Instruct", max_model_len=20, data_parallel_size=4, # Note: AsyncLLM use...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: ): result_text = "" async for output in engine.generate( request_id="request-1", prompt="Hello, how are you? Hello, how are you? Hello, how are you? Hello, how are you? Hello, how are you? Hello, how are you? Hello, how...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
