# vllm-project/vllm#2683: OpenAIServingChat cannot be instantiated within a running event loop

| 字段 | 值 |
| --- | --- |
| Issue | [#2683](https://github.com/vllm-project/vllm/issues/2683) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> OpenAIServingChat cannot be instantiated within a running event loop

### Issue 正文摘录

I am working with the OpenAI-serving-engines from the current main branch (python 3.10). When I try to instantiate an `OpenAIServingChat` from a coroutine I get the error message `AttributeError: 'NoneType' object has no attribute 'chat_template'`. ## Code Example Here is some sample code to replicate the problem: ```python from vllm import AsyncEngineArgs from vllm.engine.async_llm_engine import AsyncLLMEngine from vllm.entrypoints.openai.serving_chat import OpenAIServingChat import asyncio async def main(): model = "microsoft/phi-2" engine_args = AsyncEngineArgs(model=model) engine = AsyncLLMEngine.from_engine_args(engine_args) serving_chat = OpenAIServingChat( engine, served_model=model, response_role="assistant", chat_template=None, ) if __name__ == "__main__": asyncio.run(main()) ``` If I turn the main-coroutine into a function (just removing the `async`) and just run it directly (without `asyncio`) everything works as expected. ## Problem Investigation From what I can tell the problem is as follows: In the `__init__` for `OpenAIServing` [link](https://github.com/vllm-project/vllm/blob/ab406446691f289ef51d1abd8d1ff66760eda36f/vllm/entrypoints/openai/serving_engine.py#L25) lin...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: e Here is some sample code to replicate the problem: ```python from vllm import AsyncEngineArgs from vllm.engine.async_llm_engine import AsyncLLMEngine from vllm.entrypoints.openai.serving_chat import OpenAIServingChat...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: eady a running event loop event_loop.create_task(self._post_init()) else: # When using single vLLM without engine_use_ray asyncio.run(self._post_init()) ``` ### Synchronous Case In the case of a synchronous main functio...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ing_chat import OpenAIServingChat import asyncio async def main(): model = "microsoft/phi-2" engine_args = AsyncEngineArgs(model=model) engine = AsyncLLMEngine.from_engine_args(engine_args) serving_chat = OpenAIServingC...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: _chat_template()` tries to access it. ## Possible solutions I am not an expert in asyncio-programming so the only solution I found so far is to make `_load_chat_template` in `OpenAIServingChat` async as well and replica...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
