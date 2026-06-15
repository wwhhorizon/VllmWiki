# vllm-project/vllm#11335: [Bug]: vllm crash when 20 concurrent test with long content (9k words) 

| 字段 | 值 |
| --- | --- |
| Issue | [#11335](https://github.com/vllm-project/vllm/issues/11335) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;speculative_decoding |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vllm crash when 20 concurrent test with long content (9k words) 

### Issue 正文摘录

### Your current environment ### Model Input Dumps INFO: 10.4.38.9:60586 - "POST /v1/chat/completions HTTP/1.1" 200 OK ERROR 12-19 16:32:36 client.py:250] RuntimeError('Engine loop has died') ERROR 12-19 16:32:36 client.py:250] Traceback (most recent call last): ERROR 12-19 16:32:36 client.py:250] File "/usr/local/lib/python3.10/dist-packages/vllm/engine/multiprocessing/client.py", line 150, in run_heartbeat_loop ERROR 12-19 16:32:36 client.py:250] await self._check_success( ERROR 12-19 16:32:36 client.py:250] File "/usr/local/lib/python3.10/dist-packages/vllm/engine/multiprocessing/client.py", line 314, in _check_success ERROR 12-19 16:32:36 client.py:250] raise response ERROR 12-19 16:32:36 client.py:250] RuntimeError: Engine loop has died ERROR: Exception in ASGI application Traceback (most recent call last): File "/usr/local/lib/python3.10/dist-packages/starlette/responses.py", line 259, in __call__ await wrap(partial(self.listen_for_disconnect, receive)) File "/usr/local/lib/python3.10/dist-packages/starlette/responses.py", line 255, in wrap await func() File "/usr/local/lib/python3.10/dist-packages/starlette/responses.py", line 232, in listen_for_disconnect message = await r...

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: ceive, sender) File "/usr/local/lib/python3.10/dist-packages/starlette/routing.py", line 715, in __call__ await self.middleware_stack(scope, receive, send) File "/usr/local/lib/python3.10/dist-packages/starlette/routing...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: eive await self.message_event.wait() File "/usr/lib/python3.10/asyncio/locks.py", line 214, in wait await fut asyncio.exceptions.CancelledError: Cancelled by cancel scope 7f6a131a6c80 During handling of the above except...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: g]: vllm crash when 20 concurrent test with long content (9k words) bug;stale ### Your current environment ### Model Input Dumps INFO: 10.4.38.9:60586 - "POST /v1/chat/completions HTTP/1.1" 200 OK ERROR 12-19 16:32:36 c...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ent ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: long content (9k words) bug;stale ### Your current environment ### Model Input Dumps INFO: 10.4.38.9:60586 - "POST /v1/chat/completions HTTP/1.1" 200 OK ERROR 12-19 16:32:36 client.py:250] RuntimeError('Engine loop has...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
