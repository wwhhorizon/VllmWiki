# vllm-project/vllm#15987: [Bug]: EADDRINUSE (-98) error when setting up NCCL communicator

| 字段 | 值 |
| --- | --- |
| Issue | [#15987](https://github.com/vllm-project/vllm/issues/15987) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: EADDRINUSE (-98) error when setting up NCCL communicator

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When launcing a node-local inference server using trl's `vllm_serve`, I often get EADDRINUSE errors coming from the NCCL communicator setup ``` ERROR: Exception in ASGI application Traceback (most recent call last): File "/lustre/orion/stf006/world-shared/glaser/miniconda3/envs/grpo/lib/python3.12/site-packages/uvicorn-0.34.0-py3.12.egg/uvicorn/protocols/http/httptools_impl.py", line 409, in run _asgi result = await app( # type: ignore[func-returns-value] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/lustre/orion/stf006/world-shared/glaser/miniconda3/envs/grpo/lib/python3.12/site-packages/uvicorn-0.34.0-py3.12.egg/uvicorn/middleware/proxy_headers.py", line 60, in __call__ return await self.app(scope, receive, send) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/lustre/orion/stf006/world-shared/glaser/miniconda3/envs/grpo/lib/python3.12/site-packages/fastapi-0.115.8-py3.12.egg/fastapi/applications.py", line 1054, in __call__ await super().__call__(scope, receive, send) File "/lustre/orion/stf006/world-shared/glaser/miniconda3/envs/grpo/lib/python3.12/site-packages/starlette/applications.py", line 112, in __call__ await self.m...

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: hared/glaser/miniconda3/envs/grpo/lib/python3.12/site-packages/starlette/routing.py", line 715, in __call__ await self.middleware_stack(scope, receive, send) File "/lustre/orion/stf006/world-shared/glaser/miniconda3/env...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: or bug ### Your current environment ### 🐛 Describe the bug When launcing a node-local inference server using trl's `vllm_serve`, I often get EADDRINUSE errors coming from the NCCL communicator setup ``` ERROR: Exception...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: 273 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: routing.py", line 76, in app await wrap_app_handling_exceptions(app, request)(scope, receive, send) File "/lustre/orion/stf006/world-shared/glaser/miniconda3/envs/grpo/lib/python3.12/site-packages/starlette/_exception_h...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: vllm/engine/llm_engine.py", line 2132, in collective_rpc return self.model_executor.collective_rpc(method, timeout, args, ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/lustre/orion/stf006/world-shared...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
