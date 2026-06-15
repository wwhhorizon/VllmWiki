# vllm-project/vllm#5533: [Usage]: how to use enable-chunked-prefill?

| 字段 | 值 |
| --- | --- |
| Issue | [#5533](https://github.com/vllm-project/vllm/issues/5533) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 16; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: how to use enable-chunked-prefill?

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm I want to know more about `--enable-chunked-prefill`. and the constriant between args `max-num-seqs`, `max-num-batched-tokens` and `max-model-len`. can I use `--enable-chunked-prefill` and `--enable-prefix-caching` at the same time? I tried to use chunked-prefill based on vllm-0.4.0, but got following error. ``` ERROR: Exception in ASGI application Traceback (most recent call last): File "/usr/local/lib/python3.10/dist-packages/starlette/responses.py", line 264, in __call__ await wrap(partial(self.listen_for_disconnect, receive)) File "/usr/local/lib/python3.10/dist-packages/starlette/responses.py", line 260, in wrap await func() File "/usr/local/lib/python3.10/dist-packages/starlette/responses.py", line 237, in listen_for_disconnect message = await receive() File "/usr/local/lib/python3.10/dist-packages/uvicorn/protocols/http/httptools_impl.py", line 568, in receive await self.message_event.wait() File "/usr/lib/python3.10/asyncio/locks.py", line 214, in wait await fut asyncio.exceptions.CancelledError: Cancelled by cancel scope 7fbb404e2b30 During handling of the abo...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Usage]: how to use enable-chunked-prefill? usage;stale ### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm I want to know more about `--enable-chunked-prefi...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: ive, sender) File "/usr/local/lib/python3.10/dist-packages/starlette/routing.py", line 758, in __call__ await self.middleware_stack(scope, receive, send) File "/usr/local/lib/python3.10/dist-packages/starlette/routing.p...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: await self.message_event.wait() File "/usr/lib/python3.10/asyncio/locks.py", line 214, in wait await fut asyncio.exceptions.CancelledError: Cancelled by cancel scope 7fbb404e2b30 During handling of the above exception,...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: onstriant between args `max-num-seqs`, `max-num-batched-tokens` and `max-model-len`. can I use `--enable-chunked-prefill` and `--enable-prefix-caching` at the same time? I tried to use chunked-prefill based on vllm-0.4....
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: ive, sender) File "/usr/local/lib/python3.10/dist-packages/starlette/routing.py", line 758, in __call__ await self.middleware_stack(scope, receive, send) File "/usr/local/lib/python3.10/dist-packages/starlette/routing.p...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
