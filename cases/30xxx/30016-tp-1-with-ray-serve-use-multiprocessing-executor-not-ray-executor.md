# vllm-project/vllm#30016: TP > 1 with Ray Serve: Use Multiprocessing Executor (Not Ray Executor)

| 字段 | 值 |
| --- | --- |
| Issue | [#30016](https://github.com/vllm-project/vllm/issues/30016) |
| 状态 | open |
| 标签 | ray |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | distributed_parallel;frontend_api;model_support;sampling_logits;scheduler_memory |
| 子分类 | env_compat |
| Operator 关键词 | cuda |
| 症状 |  |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> TP > 1 with Ray Serve: Use Multiprocessing Executor (Not Ray Executor)

### Issue 正文摘录

# TP > 1 with Ray Serve: Use Multiprocessing Executor (Not Ray Executor) ## Summary When deploying vLLM with `tensor_parallel_size > 1` on Ray Serve, use the **multiprocessing executor** (`distributed_executor_backend="mp"`) instead of the Ray executor. This avoids placement group context issues with vLLM v1's subprocess architecture. ## Problem Description Attempting to use `tensor_parallel_size > 1` with Ray Serve and the Ray executor (`distributed_executor_backend="ray"`) results in worker initialization failures: ```python # This FAILS with TP > 1 on Ray Serve: @serve.deployment(ray_actor_options={"num_gpus": 2}) class VLLMDeployment: def __init__(self): engine_args = AsyncEngineArgs( model="Qwen/Qwen2-7B-Instruct", tensor_parallel_size=2, distributed_executor_backend="ray", # ❌ Fails ) self.engine = AsyncLLMEngine.from_engine_args(engine_args) ``` **Error symptoms:** - Workers cannot find or access Ray's placement group - "Placement group not found" or similar initialization errors - Timeout waiting for workers to initialize ## Root Cause vLLM v1 architecture: 1. Ray Serve creates an actor with a placement group 2. vLLM spawns `EngineCore` as a **subprocess** 3. The subproces...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: or. This avoids placement group context issues with vLLM v1's subprocess architecture. ## Problem Description Attempting to use `tensor_parallel_size > 1` with Ray Serve and the Ray executor (`distributed_executor_backe...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: location. ## Complete Working Example ```python #!/usr/bin/env python3 import ray from ray import serve from vllm.engine.async_llm_engine import AsyncLLMEngine from vllm import AsyncEngineArgs, SamplingParams from fasta...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: def __init__(self): engine_args = AsyncEngineArgs( model="Qwen/Qwen2-7B-Instruct", tensor_parallel_size=2, distributed_executor_backend="ray", # ❌ Fails ) self.engine = AsyncLLMEngine.from_engine_args(engine_args) ``` *...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: - "Placement group not found" or similar initialization errors - Timeout waiting for workers to initialize ## Root Cause vLLM v1 architecture: 1. Ray Serve creates an actor with a placement group 2. vLLM spawns `EngineC...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: n Ray Serve, use the **multiprocessing executor** (`distributed_executor_backend="mp"`) instead of the Ray executor. This avoids placement group context issues with vLLM v1's subprocess architecture. ## Problem Descript...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
