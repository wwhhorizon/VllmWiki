# vllm-project/vllm#16348: [Bug]: Missing metrics  in V1

| 字段 | 值 |
| --- | --- |
| Issue | [#16348](https://github.com/vllm-project/vllm/issues/16348) |
| 状态 | closed |
| 标签 | bug;stale;v1 |
| 评论 | 17; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | activation_norm;attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf;slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Missing metrics  in V1

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug This is my sample `script.py` ```python from vllm import SamplingParams, AsyncEngineArgs, AsyncLLMEngine import uuid import asyncio import time async def main(): """ Simulates sending 100 concurrent requests to a vLLM inference engine. :returns: None """ # Configure sampling parameters sampling_params = SamplingParams( max_tokens=100, ) # Configure engine engine_args = AsyncEngineArgs( model="facebook/opt-125m", enforce_eager=True, gpu_memory_utilization=0.90, disable_log_requests=True, disable_log_stats=False ) # Initialize engine engine = AsyncLLMEngine.from_engine_args(engine_args) # Define request processing coroutine async def process_request(request_id): """ Process a single request using the vLLM engine. :param request_id: Unique identifier for the request :returns: Generated text output """ prompt = f"Hello, how are you? This is request {request_id}" # Send request to the engine result_generator = engine.generate( prompt=prompt, sampling_params=sampling_params, request_id=str(request_id), ) # Process the streaming results final_output = None async for request_output in result_generator: final_output = request_output retur...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: # 🐛 Describe the bug This is my sample `script.py` ```python from vllm import SamplingParams, AsyncEngineArgs, AsyncLLMEngine import uuid import asyncio import time async def main(): """ Simulates sending 100 concurrent...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: Missing metrics in V1 bug;stale;v1 ### Your current environment ### 🐛 Describe the bug This is my sample `script.py` ```python from vllm import SamplingParams, AsyncEngineArgs, AsyncLLMEngine import uuid import a...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: ``` When I run `VLLM_USE_V1=0 python script.py` I do see the aggregate throughput metrics being regularly shown to me: ```bash ... INFO 04-09 14:25:03 [worker.py:267] model weights take 0.24GiB; non_torch_memory takes 0...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: d for KV Cache is 19.00GiB. INFO 04-09 14:25:03 [executor_base.py:112] # cuda blocks: 34595, # CPU blocks: 7281 INFO 04-09 14:25:03 [executor_base.py:117] Maximum concurrency for 2048 tokens per request: 270.27x INFO 04...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: ion=0.90, disable_log_requests=True, disable_log_stats=False ) # Initialize engine engine = AsyncLLMEngine.from_engine_args(engine_args) # Define request processing coroutine async def process_request(request_id): """ P...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
