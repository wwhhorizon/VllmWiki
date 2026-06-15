# vllm-project/vllm#33361: [Bug]: Different embeddings produced by LLM and AsyncLLM

| 字段 | 值 |
| --- | --- |
| Issue | [#33361](https://github.com/vllm-project/vllm/issues/33361) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Different embeddings produced by LLM and AsyncLLM

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Different embeddings produced by LLM and AsyncLLM I tried multiple versions of vllm (0.11.0, 0.12.0, 0.14.1 and the latest) and multiple embedding models (e.g. `Qwen/Qwen3-Embedding-0.6B` or `intfloat/e5-mistral-7b-instruct`) but I'm getting different embeddings. ```python import uuid import asyncio from vllm.v1.engine.async_llm import AsyncLLM, PoolingParams from vllm import AsyncEngineArgs, LLM async def main(): engine_args = AsyncEngineArgs( model="Qwen/Qwen3-Embedding-0.6B", runner="pooling", ) model = AsyncLLM.from_engine_args(engine_args) async for request_output in model.encode( prompt="Hello world!", pooling_params=PoolingParams(task="embed"), request_id=str(uuid.uuid4()), ): print(request_output.outputs.data.tolist()[:100]) asyncio.run(main()) # >>> [0.60546875, 0.458984375, -0.98046875, -6.25, 0.2890625, -1.21875, -2.03125, -1.0390625, -10.75, -1.984375, -1.6484375, -1.828125, 2.671875, -0.921875, -4.3125, 8.6875, -1.2421875, 9.6875, 10.625, -5.71875, -0.77734375, 3.78125, -3.296875, 10.375, -3.828125, -4.5, -4.875, 10.6875, 1.8671875, -0.703125, -0.69140625, 4.5625, -1.875, -2.375, -4.5, -1.359375, 4.34375, 0.484375, -...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: bug Different embeddings produced by LLM and AsyncLLM I tried multiple versions of vllm (0.11.0, 0.12.0, 0.14.1 and the latest) and multiple embedding models (e.g. `Qwen/Qwen3-Embedding-0.6B` or `intfloat/e5-mistral-7b-...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: Different embeddings produced by LLM and AsyncLLM bug;stale ### Your current environment ### 🐛 Describe the bug Different embeddings produced by LLM and AsyncLLM I tried multiple versions of vllm (0.11.0, 0.12.0,...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ng? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: s of vllm (0.11.0, 0.12.0, 0.14.1 and the latest) and multiple embedding models (e.g. `Qwen/Qwen3-Embedding-0.6B` or `intfloat/e5-mistral-7b-instruct`) but I'm getting different embeddings. ```python import uuid import...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
