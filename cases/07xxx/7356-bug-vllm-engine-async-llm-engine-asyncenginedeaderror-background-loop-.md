# vllm-project/vllm#7356: [Bug]: vllm.engine.async_llm_engine.AsyncEngineDeadError: Background loop has errored already.

| 字段 | 值 |
| --- | --- |
| Issue | [#7356](https://github.com/vllm-project/vllm/issues/7356) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support |
| 子分类 | env_compat |
| Operator 关键词 | cuda;triton |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vllm.engine.async_llm_engine.AsyncEngineDeadError: Background loop has errored already.

### Issue 正文摘录

### Your current environment # 🐛 Describe the bug My Bug ```script NFO: ::1:47724 - "POST /v1/chat/completions HTTP/1.1" 500 Internal Server Error ERROR: Exception in ASGI application Traceback (most recent call last): File "/cpfs01/shared/Llm_code/xiechengxing/workspace/anaconda3/envs/vllm_new/lib/python3.11/site-packages/vllm/engine/async_llm_engine.py", line 631, in run_engine_loop done, _ = await asyncio.wait( ^^^^^^^^^^^^^^^^^^^ File "/cpfs01/shared/Llm_code/xiechengxing/workspace/anaconda3/envs/vllm_new/lib/python3.11/asyncio/tasks.py", line 428, in wait return await _wait(fs, timeout, return_when, loop) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/cpfs01/shared/Llm_code/xiechengxing/workspace/anaconda3/envs/vllm_new/lib/python3.11/asyncio/tasks.py", line 535, in _wait await waiter asyncio.exceptions.CancelledError The above exception was the direct cause of the following exception: Traceback (most recent call last): File "/cpfs01/shared/Llm_code/xiechengxing/workspace/anaconda3/envs/vllm_new/lib/python3.11/site-packages/uvicorn/protocols/http/httptools_impl.py", line 399, in run_asgi result = await app( # type: ignore[func-returns-value] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^...

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: await waiter
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: done, _ = await asyncio.wait(
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: i_build;distributed_parallel;frontend_api;hardware_porting;model_support cuda;triton build_error;crash env_dependency Your current environment
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: development ci_build;distributed_parallel;frontend_api;hardware_porting;model_support cuda;triton build_error;crash env_dependency Your current environment
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: workspace/anaconda3/envs/vllm_new/lib/python3.11/site-packages/starlette/routing.py", line 756, in __call__ await self.middleware_stack(scope, receive, send) File "/cpfs01/shared/Llm_code/xiechengxing/workspace/anaconda...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
