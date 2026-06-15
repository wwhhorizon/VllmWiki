# vllm-project/vllm#9263: [Bug]: AsyncLLMEngine stuck on a single too long request

| 字段 | 值 |
| --- | --- |
| Issue | [#9263](https://github.com/vllm-project/vllm/issues/9263) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: AsyncLLMEngine stuck on a single too long request

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug When there's a request that's too long (will be ignored by the scheduler), it will get stuck at returning. It's only unstuck if another request is made to the engine. This seems to be related to async output processing since with `disable_async_output_proc=True` - it will pass. See below script for the example ```python # Please refer to entrypoints/api_server.py for # the complete example. import asyncio from vllm import AsyncLLMEngine, SamplingParams from vllm.engine.arg_utils import AsyncEngineArgs async def run(): # initialize the engine and the example input engine_args = AsyncEngineArgs( model="meta-llama/Meta-Llama-3-8B-Instruct", disable_async_output_proc=False, # This will pass if it's true ) engine = AsyncLLMEngine.from_engine_args(engine_args) example_input = { "prompt": "Test prompt " + "test" * 200000, # A long request "stream": False, "temperature": 0.0, "request_id": 0, } # start the generation results_generator = engine.generate( example_input["prompt"], SamplingParams(temperature=example_input["temperature"]), example_input["request_id"]) # get the results async for request_out...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: # Please refer to entrypoints/api_server.py for # the complete example. import asyncio from vllm import AsyncLLMEngine, SamplingParams from vllm.engine.arg_utils import AsyncEngineArgs async def run(): # initialize the...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Bug]: AsyncLLMEngine stuck on a single too long request bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug When there's a request that's too long (will be ignored by the s...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: k. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whi...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: a single too long request bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug When there's a request that's too long (will be ignored by the scheduler), it will get stuck at...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ling_logits;scheduler_memory;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
