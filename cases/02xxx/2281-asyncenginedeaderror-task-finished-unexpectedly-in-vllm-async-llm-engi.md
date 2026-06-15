# vllm-project/vllm#2281: AsyncEngineDeadError: Task Finished Unexpectedly in VLLM Async LLM Engine

| 字段 | 值 |
| --- | --- |
| Issue | [#2281](https://github.com/vllm-project/vllm/issues/2281) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | frontend_api;gemm_linear;model_support;sampling_logits |
| 子分类 | runtime_err |
| Operator 关键词 | cuda;gemm |
| 症状 | crash |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> AsyncEngineDeadError: Task Finished Unexpectedly in VLLM Async LLM Engine

### Issue 正文摘录

Environment: Date: 2023-12-27 Python Version: 3.11 Library: vllm (0.2.4) OS: (ubuntu22) Issue Description: During a POST request to /worker_generate, the server returned a 500 Internal Server Error. The traceback indicates an issue within the vllm library, specifically in the async_llm_engine.py file. Actual Behavior: The server returned a 500 Internal Server Error, and an exception was raised in the ASGI application. The error seems to originate from the AsyncLLMEngine within the vllm library. Error Log: 2023-12-27 11:25:36 | INFO | stdout | INFO: 127.0.0.1:34180 - "POST /worker_generate HTTP/1.1" 500 Internal Server Error 2023-12-27 11:25:36 | ERROR | stderr | ERROR: Exception in ASGI application 2023-12-27 11:25:36 | ERROR | stderr | Traceback (most recent call last): 2023-12-27 11:25:36 | ERROR | stderr | File "/root/miniconda3/envs/vllm/lib/python3.11/site-packages/vllm/engine/async_llm_engine.py", line 28, in _raise_exception_on_finish 2023-12-27 11:25:36 | ERROR | stderr | task.result() 2023-12-27 11:25:36 | ERROR | stderr | File "/root/miniconda3/envs/vllm/lib/python3.11/site-packages/vllm/engine/async_llm_engine.py", line 359, in run_engine_loop 2023-12-27 11:25:36 | ERRO...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: xpectedly in VLLM Async LLM Engine Environment: Date: 2023-12-27 Python Version: 3.11 Library: vllm (0.2.4) OS: (ubuntu22) Issue Description: During a POST request to /worker_generate, the server returned a 500 Internal...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ib/python3.11/site-packages/vllm/worker/worker.py", line 147, in execute_model 2023-12-27 11:25:36 | ERROR | stderr | output = self.model_runner.execute_model(seq_group_metadata_list, 2023-12-27 11:25:36 | ERROR | stder...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: File "/root/miniconda3/envs/vllm/lib/python3.11/site-packages/starlette/routing.py", line 718, in __call__ 2023-12-27 11:25:36 | ERROR | stderr | await route.handle(scope, receive, send) 2023-12-27 11:25:36 | ERROR | st...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: File "/root/miniconda3/envs/vllm/lib/python3.11/site-packages/starlette/routing.py", line 718, in __call__ 2023-12-27 11:25:36 | ERROR | stderr | await route.handle(scope, receive, send) 2023-12-27 11:25:36 | ERROR | st...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ^^^^^^^^^^^^^^^^^^^ 2023-12-27 11:25:36 | ERROR | stderr | RuntimeError: CUDA error: CUBLAS_STATUS_ALLOC_FAILED when calling `cublasCreate(handle)` 2023-12-27 11:25:36 | ERROR | stderr | 2023-12-27 11:25:36 | ERROR | st...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
