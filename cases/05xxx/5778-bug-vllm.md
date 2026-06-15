# vllm-project/vllm#5778: [Bug]: vllm批量推理报错

| 字段 | 值 |
| --- | --- |
| Issue | [#5778](https://github.com/vllm-project/vllm/issues/5778) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: vllm批量推理报错

### Issue 正文摘录

### Your current environment vllm 0.4.3 ### 🐛 Describe the bug 多线程测试完vllm部署的模型服务报错如下 模型为qwen2-72b-int4-gptq RROR: Exception in ASGI application 0|startvllm72b | Traceback (most recent call last): 0|startvllm72b | File "/usr/local/lib/python3.10/dist-packages/sse_starlette/sse.py", line 281, in __call__ 0|startvllm72b | await wrap(partial(self.listen_for_disconnect, receive)) 0|startvllm72b | File "/usr/local/lib/python3.10/dist-packages/sse_starlette/sse.py", line 270, in wrap 0|startvllm72b | await func() 0|startvllm72b | File "/usr/local/lib/python3.10/dist-packages/sse_starlette/sse.py", line 221, in listen_for_disconnect 0|startvllm72b | message = await receive() 0|startvllm72b | File "/usr/local/lib/python3.10/dist-packages/uvicorn/protocols/http/httptools_impl.py", line 580, in receive 0|startvllm72b | await self.message_event.wait() 0|startvllm72b | File "/usr/lib/python3.10/asyncio/locks.py", line 214, in wait 0|startvllm72b | await fut 0|startvllm72b | asyncio.exceptions.CancelledError: Cancelled by cancel scope 7f81f02e3be0 0|startvllm72b | During handling of the above exception, another exception occurred: 0|startvllm72b | Traceback (most recent call last): 0|startvllm7...

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: tartvllm72b | File "/usr/local/lib/python3.10/dist-packages/starlette/routing.py", line 762, in __call__ 0|startvllm72b | await self.middleware_stack(scope, receive, send) 0|startvllm72b | File "/usr/local/lib/python3.1...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: vllm批量推理报错 bug;stale ### Your current environment vllm 0.4.3 ### 🐛 Describe the bug 多线程测试完vllm部署的模型服务报错如下 模型为qwen2-72b-int4-gptq RROR: Exception in ASGI application 0|startvllm72b | Traceback (most recent call la...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: f.message_event.wait() 0|startvllm72b | File "/usr/lib/python3.10/asyncio/locks.py", line 214, in wait 0|startvllm72b | await fut 0|startvllm72b | asyncio.exceptions.CancelledError: Cancelled by cancel scope 7f81f02e3be...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: vllm 0.4.3 ### 🐛 Describe the bug 多线程测试完vllm部署的模型服务报错如下 模型为qwen2-72b-int4-gptq RROR: Exception in ASGI application 0|startvllm72b | Traceback (most recent call last): 0|startvllm72b | File "/usr/local/lib/python3.10/dis...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: vironment vllm 0.4.3 ### 🐛 Describe the bug 多线程测试完vllm部署的模型服务报错如下 模型为qwen2-72b-int4-gptq RROR: Exception in ASGI application 0|startvllm72b | Traceback (most recent call last): 0|startvllm72b | File "/usr/local/lib/pyth...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
