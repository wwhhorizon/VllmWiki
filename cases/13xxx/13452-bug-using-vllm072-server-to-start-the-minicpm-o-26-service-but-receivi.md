# vllm-project/vllm#13452: [Bug]: Using VLLM072 server to start the MiniCPM-O-26 service, but receiving video and audio output model inference errors.

| 字段 | 值 |
| --- | --- |
| Issue | [#13452](https://github.com/vllm-project/vllm/issues/13452) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Using VLLM072 server to start the MiniCPM-O-26 service, but receiving video and audio output model inference errors.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug video bug: ImportError: please install vllm[video] for video support INFO: 172.16.50.151:0 -"POST /v1/chat/completions HTTP/1.1" 500 Internal Server Error ERROR: Exception in ASGI application Traceback (most recent call last): File "/opt/conda/lib/python3.10/site-packages/uvicorn/protocols/http/httptools_impl.py", line 426, in run_asgi result= await app(# type: ignore[func-returns-value] File "/opt/conda/lib/python3.10/site-packages/uvicorn/middleware/proxy_headers.py", line 84, in _call_ return await self.app(scope，receive, send) File "/opt/conda/lib/python3.10/site-packages/fastapi/applications.py", line 1054, in __call_ await super().__call_(scope, receive,send) File "/opt/conda/lib/python3.10/site-packages/starlette/applications.py", line 112, in __call__ await self.middleware_stack(scope,receive, send) File "/opt/conda/lib/python3.10/site-packages/starlette/middleware/errors.py", line 187, in _call_ raise exc File "/opt/conda/lib/python3.10/site-packages/starlette/middleware/errors.py", line 165, in __call_ await self.app(scope,receive, _send) File "/opt/conda/lib/python3.10/site-packages/starlette/middleware/cors.py",line 8...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: tale ### Your current environment ### 🐛 Describe the bug video bug: ImportError: please install vllm[video] for video support INFO: 172.16.50.151:0 -"POST /v1/chat/completions HTTP/1.1" 500 Internal Server Error ERROR:...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: to start the MiniCPM-O-26 service, but receiving video and audio output model inference errors. bug;stale ### Your current environment ### 🐛 Describe the bug video bug: ImportError: please install vllm[video] for video...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ervice, but receiving video and audio output model inference errors. bug;stale ### Your current environment ### 🐛 Describe the bug video bug: ImportError: please install vllm[video] for video support INFO: 172.16.50.151...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: receive, sender) File "/opt/conda/lib/python3.10/site-packages/starlette/routing.py", line 715, in call_ await self.middleware_stack(scope，receive, send) File "/opt/conda/lib/python3.10/site-packages/starlette/routing ....
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: or ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whi...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
