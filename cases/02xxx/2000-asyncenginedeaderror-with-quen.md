# vllm-project/vllm#2000: AsyncEngineDeadError with QUEN 

| 字段 | 值 |
| --- | --- |
| Issue | [#2000](https://github.com/vllm-project/vllm/issues/2000) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> AsyncEngineDeadError with QUEN 

### Issue 正文摘录

Hello, I am trying to test Qwen/Qwen-7B-Chat with openai.api_server and this error shows up: ''' vllm.engine.async_llm_engine.AsyncEngineDeadError: Task finished unexpectedly. This should never happen! Please open an issue on Github. See stack trace above for the actual cause ''' The Traceback: Traceback (most recent call last): File "/opt/conda/envs/myenv/lib/python3.10/site-packages/uvicorn/protocols/http/httptools_impl.py", line 426, in run_asgi result = await app( # type: ignore[func-returns-value] File "/opt/conda/envs/myenv/lib/python3.10/site-packages/uvicorn/middleware/proxy_headers.py", line 84, in __call__ return await self.app(scope, receive, send) File "/opt/conda/envs/myenv/lib/python3.10/site-packages/fastapi/applications.py", line 1106, in __call__ await super().__call__(scope, receive, send) File "/opt/conda/envs/myenv/lib/python3.10/site-packages/starlette/applications.py", line 122, in __call__ await self.middleware_stack(scope, receive, send) File "/opt/conda/envs/myenv/lib/python3.10/site-packages/starlette/middleware/errors.py", line 184, in __call__ raise exc File "/opt/conda/envs/myenv/lib/python3.10/site-packages/starlette/middleware/errors.py", line 162, i...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: AsyncEngineDeadError with QUEN stale Hello, I am trying to test Qwen/Qwen-7B-Chat with openai.api_server and this error shows up: ''' vllm.engine.async_llm_engine.AsyncEngineDeadError: Task finished unexpectedly. This s...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: nd) File "/opt/conda/envs/myenv/lib/python3.10/site-packages/starlette/routing.py", line 718, in __call__ await route.handle(scope, receive, send) File "/opt/conda/envs/myenv/lib/python3.10/site-packages/starlette/routi...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: AsyncEngineDeadError with QUEN stale Hello, I am trying to test Qwen/Qwen-7B-Chat with openai.api_server and this error shows up: ''' vllm.engine.async_llm_engine.AsyncEngineDeadError: Task finished unexpectedly. This s...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: nd) File "/opt/conda/envs/myenv/lib/python3.10/site-packages/starlette/routing.py", line 718, in __call__ await route.handle(scope, receive, send) File "/opt/conda/envs/myenv/lib/python3.10/site-packages/starlette/routi...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: AsyncEngineDeadError with QUEN stale Hello, I am trying to test Qwen/Qwen-7B-Chat with openai.api_server and this error shows up: ''' vllm.engine.async_llm_engine.AsyncEngineDeadError: Task finished unexpectedly. This s...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
