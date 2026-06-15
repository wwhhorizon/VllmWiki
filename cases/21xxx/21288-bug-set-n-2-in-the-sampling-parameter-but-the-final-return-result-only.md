# vllm-project/vllm#21288: [Bug]: set n=2 in the sampling parameter, but the final return result only contains one sequence

| 字段 | 值 |
| --- | --- |
| Issue | [#21288](https://github.com/vllm-project/vllm/issues/21288) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: set n=2 in the sampling parameter, but the final return result only contains one sequence

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug here is my code. I set n=2 in the sampling parameter, but the final return result only contains one sequence. I found that there are two sequences being generated in the earlier output, but only one sequence is included in the subsequent output. ```python import asyncio from vllm.engine.arg_utils import AsyncEngineArgs from vllm.engine.async_llm_engine import AsyncLLMEngine from vllm.sampling_params import SamplingParams async def main(): engine_args = AsyncEngineArgs( model="Qwen/Qwen2.5-0.5B", dtype="auto", max_model_len=2048, enforce_eager=True, ) engine_client = AsyncLLMEngine.from_engine_args(engine_args) sampling_params = SamplingParams( max_tokens=128, n=2, ) prompt = "stop output." final_output = None async for output in engine_client.generate( prompt=prompt, sampling_params=sampling_params, request_id="abcdef", ): if final_output: print(final_output.outputs) print(len(final_output.outputs)) else: print("none") final_output = output if final_output: print(final_output.outputs) if __name__ == "__main__": asyncio.run(main()) ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, a...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: , but only one sequence is included in the subsequent output. ```python import asyncio from vllm.engine.arg_utils import AsyncEngineArgs from vllm.engine.async_llm_engine import AsyncLLMEngine from vllm.sampling_params...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: plingParams async def main(): engine_args = AsyncEngineArgs( model="Qwen/Qwen2.5-0.5B", dtype="auto", max_model_len=2048, enforce_eager=True, ) engine_client = AsyncLLMEngine.from_engine_args(engine_args) sampling_param...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: prompt=prompt, sampling_params=sampling_params, request_id="abcdef", ): if final_output: print(final_output.outputs) print(len(final_output.outputs)) else: print("none") final_output = output if final
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error dtype;env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
