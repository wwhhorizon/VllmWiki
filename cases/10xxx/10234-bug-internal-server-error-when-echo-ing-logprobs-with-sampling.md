# vllm-project/vllm#10234: [Bug]: Internal Server Error when echo'ing logprobs with sampling

| 字段 | 值 |
| --- | --- |
| Issue | [#10234](https://github.com/vllm-project/vllm/issues/10234) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Internal Server Error when echo'ing logprobs with sampling

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Sending an request that asks for prompt logprobs while also specifying certain sampling parameters can result in an Internal Server Error. For example: ``` curl -v http://localhost:8000/v1/completions \ -H "Content-Type: application/json" \ -d '{ "model": "meta-llama/Llama-3.2-1B", "prompt": "correct horse battery staple", "echo": 1, "logprobs": 1, "temperature": 1, "top_k": 1 }' ``` Results in this stack trace: ``` INFO: ::1:47926 - "POST /v1/completions HTTP/1.1" 500 Internal Server Error ERROR: Exception in ASGI application Traceback (most recent call last): File "/opt/vllm/lib64/python3.12/site-packages/uvicorn/protocols/http/httptools_impl.py", line 401, in run_asgi result = await app( # type: ignore[func-returns-value] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/opt/vllm/lib64/python3.12/site-packages/uvicorn/middleware/proxy_headers.py", line 60, in __call__ return await self.app(scope, receive, send) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/opt/vllm/lib64/python3.12/site-packages/fastapi/applications.py", line 1054, in __call__ await super().__call__(scope, receive, send) F...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: echo'ing logprobs with sampling bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Sending an request that asks for prompt logprobs while also specifying certain sampling paramet...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: eive, sender) File "/opt/vllm/lib64/python3.12/site-packages/starlette/routing.py", line 715, in __call__ await self.middleware_stack(scope, receive, send) File "/opt/vllm/lib64/python3.12/site-packages/starlette/routin...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: the bug Sending an request that asks for prompt logprobs while also specifying certain sampling parameters can result in an Internal Server Error. For example: ``` curl -v http://localhost:8000/v1/completions \ -H "Cont...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 0. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whi...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: eive, sender) File "/opt/vllm/lib64/python3.12/site-packages/starlette/routing.py", line 715, in __call__ await self.middleware_stack(scope, receive, send) File "/opt/vllm/lib64/python3.12/site-packages/starlette/routin...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
