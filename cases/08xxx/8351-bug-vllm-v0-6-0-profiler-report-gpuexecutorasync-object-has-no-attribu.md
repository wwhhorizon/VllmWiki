# vllm-project/vllm#8351: [Bug]: vllm v0.6.0 profiler report GPUExecutorAsync object has no attribute '_run_workers' on ROCm and NV H20

| 字段 | 值 |
| --- | --- |
| Issue | [#8351](https://github.com/vllm-project/vllm/issues/8351) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vllm v0.6.0 profiler report GPUExecutorAsync object has no attribute '_run_workers' on ROCm and NV H20

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug To profile LLM, I tried run command ` VLLM_TORCH_PROFILER_DIR=/vllm-workspace/vllm/traces/ python -m vllm.entrypoints.openai.api_server --model /path/to/NousResearch-Llama-3.1-8B` under vllm v0.6.0 root dir on both AMD GPU and NV GPU. Both of them reported below error: ``` INFO 09-11 02:31:38 api_server.py:333] Starting profiler... INFO: 127.0.0.1:52216 - "POST /start_profile HTTP/1.1" 500 Internal Server Error ERROR: Exception in ASGI application Traceback (most recent call last): File "/opt/conda/envs/py_3.9/lib/python3.9/site-packages/uvicorn/protocols/http/httptools_impl.py", line 401, in run_asgi result = await app( # type: ignore[func-returns-value] File "/opt/conda/envs/py_3.9/lib/python3.9/site-packages/uvicorn/middleware/proxy_headers.py", line 70, in __call__ return await self.app(scope, receive, send) File "/opt/conda/envs/py_3.9/lib/python3.9/site-packages/fastapi/applications.py", line 1054, in __call__ await super().__call__(scope, receive, send) File "/opt/conda/envs/py_3.9/lib/python3.9/site-packages/starlette/applications.py", line 123, in __call__ await self.middleware_stack(scope, receive, send) File "/opt/cond...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;crash;nan_inf...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ofiler report GPUExecutorAsync object has no attribute '_run_workers' on ROCm and NV H20 bug ### Your current environment ### 🐛 Describe the bug To profile LLM, I tried run command ` VLLM_TORCH_PROFILER_DIR=/vllm-worksp...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: er) File "/opt/conda/envs/py_3.9/lib/python3.9/site-packages/starlette/routing.py", line 754, in __call__ await self.middleware_stack(scope, receive, send) File "/opt/conda/envs/py_3.9/lib/python3.9/site-packages/starle...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: lm-workspace/vllm/traces/ python -m vllm.entrypoints.openai.api_server --model /path/to/NousResearch-Llama-3.1-8B` under vllm v0.6.0 root dir on both AMD GPU and NV GPU. Both of them reported below error: ``` INFO 09-11...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: routing.py", line 77, in app await wrap_app_handling_exceptions(app, request)(scope, receive, send) File "/opt/conda/envs/py_3.9/lib/python3.9/site-packages/starlette/_exception_handler.py", line 64, in wrapped_app rais...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
