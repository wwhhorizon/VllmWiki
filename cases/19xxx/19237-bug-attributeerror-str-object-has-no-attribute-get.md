# vllm-project/vllm#19237: [Bug]: AttributeError: 'str' object has no attribute 'get'

| 字段 | 值 |
| --- | --- |
| Issue | [#19237](https://github.com/vllm-project/vllm/issues/19237) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: AttributeError: 'str' object has no attribute 'get'

### Issue 正文摘录

### Your current environment vllm 0.9.0.1 ### 🐛 Describe the bug `AttributeError: 'str' object has no attribute 'get'` is thrown if `tool_choince` is not defined correctly: ``` "tool_choice":{ "function":"do-something", "type":"function" } ``` Instead of the correct: ``` "tool_choice":{ "function": {"name": "do-something"}, "type":"function" } ``` Log: ``` ERROR: Exception in ASGI application Traceback (most recent call last): File "/usr/local/lib/python3.12/dist-packages/uvicorn/protocols/http/httptools_impl.py", line 409, in run_asgi result = await app( # type: ignore[func-returns-value] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/usr/local/lib/python3.12/dist-packages/uvicorn/middleware/proxy_headers.py", line 60, in __call__ return await self.app(scope, receive, send) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/usr/local/lib/python3.12/dist-packages/fastapi/applications.py", line 1054, in __call__ await super().__call__(scope, receive, send) File "/usr/local/lib/python3.12/dist-packages/starlette/applications.py", line 112, in __call__ await self.middleware_stack(scope, receive, send) File "/usr/local/lib/python3.12/dist-packages/starlette/middleware/errors.py", line...

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: File "/usr/local/lib/python3.12/dist-packages/starlette/routing.py", line 714, in __call__
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: solved_result = await solve_dependencies(
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: v_, errors_ = _validate_value_with_model_field(
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: File "/usr/local/lib/python3.12/dist-packages/starlette/routing.py", line 714, in __call__

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
