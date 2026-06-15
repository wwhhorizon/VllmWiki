# vllm-project/vllm#42794: with_cancellation can return None, causing FastAPI to send HTTP 200 with JSON null after http.disconnect

| 字段 | 值 |
| --- | --- |
| Issue | [#42794](https://github.com/vllm-project/vllm/issues/42794) |
| 状态 | open |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> with_cancellation can return None, causing FastAPI to send HTTP 200 with JSON null after http.disconnect

### Issue 正文摘录

## Summary The `with_cancellation` decorator in `vllm.entrypoints.utils` can return `None` when its `listen_for_disconnect()` task completes before the wrapped handler task. For FastAPI routes without an explicit response model or return annotation, FastAPI serializes that `None` return value as: ```http HTTP/1.1 200 OK content-type: application/json content-length: 4 null ``` This is observable as intermittent empty/null successful responses, especially with large request bodies, keep-alive connections, concurrent requests, or request paths that take enough time for a spurious or premature `http.disconnect` event to win the race. I hit this in practice through `/v1/audio/transcriptions` with long audio uploads. The server accepted and logged the complete multipart upload, did not schedule any engine request, and returned `200` with body `null`. The client saw this as `aiohttp.ClientOSError: [Errno 32] Broken pipe`. ## Current Code Path Current `vllm/entrypoints/utils.py` still has: ```python done, pending = await asyncio.wait( [handler_task, cancellation_task], return_when=asyncio.FIRST_COMPLETED ) for task in pending: task.cancel() if handler_task in done: return handler_task.re...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: tes before the wrapped handler task. For FastAPI routes without an explicit response model or return annotation, FastAPI serializes that `None` return value as: ```http HTTP/1.1 200 OK content-type: application/json con...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: "query_string": b"", "headers": [ (b"host", b"testserver"), (b"content-type", b"application/json"), (b"content-length", str(len(body)).encode()), ], "client": ("127.0.0.1", 12345), "server": ("testserver", 80),
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: StreamingResponse`, or an error response. ## Minimal Reproduction This reproducer does not require a model, GPU, uvicorn, a real TCP client, or any ASR/audio code. It directly invokes a tiny FastAPI ASGI app using the r...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: e as intermittent empty/null successful responses, especially with large request bodies, keep-alive connections, concurrent requests, or request paths that take enough time for a spurious or premature `http.disconnect`...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: me `HTTP 200 null` cancellation failure. ## Proposed Fix Direction The smallest fix appears to be the same core change proposed in #32945: ```diff if handler_task in done: return handler_task.result() -return None +rais...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
