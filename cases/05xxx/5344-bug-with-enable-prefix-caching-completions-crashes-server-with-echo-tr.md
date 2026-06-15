# vllm-project/vllm#5344: [Bug]: with `--enable-prefix-caching` , `/completions` crashes server with `echo=True` above certain prompt length

| 字段 | 值 |
| --- | --- |
| Issue | [#5344](https://github.com/vllm-project/vllm/issues/5344) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 18; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: with `--enable-prefix-caching` , `/completions` crashes server with `echo=True` above certain prompt length

### Issue 正文摘录

### Your current environment ```text vLLM 0.4.3 RTX 4090 24GB (reproduces also on A100) ``` ### 🐛 Describe the bug Hi, When server started with: ``` python -m vllm.entrypoints.openai.api_server --model TinyLlama/TinyLlama-1.1B-Chat-v1.0 --enable-prefix-caching ``` running this client code: ```python import openai client = openai.OpenAI( base_url="http://localhost:8000/v1", api_key="foo" ) prompt = [1] * 256 out = client.completions.create( model="TinyLlama/TinyLlama-1.1B-Chat-v1.0", prompt=prompt, max_tokens=1, logprobs=5, echo=True ) print(out) ``` Triggers this assert: ```python INFO: 127.0.0.1:39724 - "POST /v1/completions HTTP/1.1" 500 Internal Server Error ERROR: Exception in ASGI application Traceback (most recent call last): File "/home/user/code/play-vllm/.venv/lib/python3.10/site-packages/uvicorn/protocols/http/httptools_impl.py", line 411, in run_asgi result = await app( # type: ignore[func-returns-value] File "/home/user/code/play-vllm/.venv/lib/python3.10/site-packages/uvicorn/middleware/proxy_headers.py", line 69, in __call__ return await self.app(scope, receive, send) File "/home/user/code/play-vllm/.venv/lib/python3.10/site-packages/fastapi/applications.py", line 10...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: at-v1.0 --enable-prefix-caching ``` running this client code: ```python import openai client = openai.OpenAI( base_url="http://localhost:8000/v1", api_key="foo" ) prompt = [1] * 256 out = client.completions.create( mode...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: rompt length bug;stale ### Your current environment ```text vLLM 0.4.3 RTX 4090 24GB (reproduces also on A100) ``` ### 🐛 Describe the bug Hi, When server started with: ``` python -m vllm.entrypoints.openai.api_server --...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: server started with: ``` python -m vllm.entrypoints.openai.api_server --model TinyLlama/TinyLlama-1.1B-Chat-v1.0 --enable-prefix-caching ``` running this client code: ```python import openai client = openai.OpenAI( base...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: letions` crashes server with `echo=True` above certain prompt length bug;stale ### Your current environment ```text vLLM 0.4.3 RTX 4090 24GB (reproduces also on A100) ``` ### 🐛 Describe the bug Hi, When server started w...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: "/home/user/code/play-vllm/.venv/lib/python3.10/site-packages/starlette/routing.py", line 756, in __call__ await self.middleware_stack(scope, receive, send) File "/home/user/code/play-vllm/.venv/lib/python3.10/site-pack...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
