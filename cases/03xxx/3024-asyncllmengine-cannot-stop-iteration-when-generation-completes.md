# vllm-project/vllm#3024: AsyncLLMEngine cannot stop iteration when generation completes

| 字段 | 值 |
| --- | --- |
| Issue | [#3024](https://github.com/vllm-project/vllm/issues/3024) |
| 状态 | closed |
| 标签 |  |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> AsyncLLMEngine cannot stop iteration when generation completes

### Issue 正文摘录

@WoosukKwon @simon-mo ### Environment - torch 2.1.2 - vllm 0.3.2 ### Reproduce ```python import asyncio from vllm import AsyncEngineArgs, AsyncLLMEngine, SamplingParams engine = AsyncLLMEngine.from_engine_args(AsyncEngineArgs("01-ai/Yi-6B-Chat")) param = SamplingParams(max_tokens=50, stop_token_ids=[7]) generator = engine.generate(" user\nhi \n assistant\n", param, "req_test") async def test(): answer = None async for result in generator: print(result.finished, "-", result.outputs[0].text) answer = result.outputs[0].text print("Answer:", answer) asyncio.get_event_loop().run_until_complete(test()) ``` ### Outputs ``` False - Hello False - Hello! False - Hello! How False - Hello! How can False - Hello! How can I False - Hello! How can I assist False - Hello! How can I assist you False - Hello! How can I assist you today False - Hello! How can I assist you today? INFO 02-25 01:20:26 async_llm_engine.py:110] Finished request req_test. True - Hello! How can I assist Answer: Hello! How can I assist ``` ### Expected behaviour The `answer` should be "Hello! How can I assist you today?" instead of "Hello! How can I assist".

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ### Environment - torch 2.1.2 - vllm 0.3.2 ### Reproduce ```python import asyncio from vllm import AsyncEngineArgs, AsyncLLMEngine, SamplingParams engine = AsyncLLMEngine.from_engine_args(AsyncEngineArgs("01-ai/Yi-6B-Ch...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: @WoosukKwon @simon-mo ### Environment - torch 2.1.2 - vllm 0.3.2 ### Reproduce ```python import asyncio from vllm import AsyncEngineArgs, AsyncLLMEngine, SamplingParams engine = AsyncLLMEngine.from_engine_args(AsyncEngi...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: ncio.get_event_loop().run_until_complete(test()) ``` ### Outputs ``` False - Hello False - Hello! False - Hello! How False - Hello! How can False - Hello! How can I False - Hello! How can I assist False - Hello! How can...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: assist you today? INFO 02-25 01:20:26 async_llm_engine.py:110] Finished request req_test. True - Hello! How can I assist Answer: Hello! How can I assist ``` ### Expected behaviour The `answer` should be "Hello! How can...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: [7]) generator = engine.generate(" user\nhi \n assistant\n", param, "req_test") async def test(): answer = None async for result in generator: print(result.finished, "-", result.outputs[0].text) answer = result.outputs[...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
