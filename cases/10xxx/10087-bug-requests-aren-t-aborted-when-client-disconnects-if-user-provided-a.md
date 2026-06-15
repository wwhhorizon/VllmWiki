# vllm-project/vllm#10087: [Bug]: Requests aren't aborted when client disconnects if user provided a middleware

| 字段 | 值 |
| --- | --- |
| Issue | [#10087](https://github.com/vllm-project/vllm/issues/10087) |
| 状态 | closed |
| 标签 |  |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Requests aren't aborted when client disconnects if user provided a middleware

### Issue 正文摘录

In https://github.com/vllm-project/vllm/pull/7111/, @njhill did a great job to make sure requests are aborted if they are cancelled by the client. This works great and can really ease the load on the model engine in cases of timeouts / other client disconnects. Unfortunately, this mechanism doesn't work if a `BaseHTTPMiddleware` is added to the server, which is the case when a use provides a function to add as middleware (via the `--middleware` cmd arg of `vllm serve`). In this case, some weird starlette behavior causes `request.is_disconnected()` to return `False`, even if the client disconnects. This is discussed in https://github.com/encode/starlette/discussions/2094. One of the suggested solutions in that discussion (for example, in https://github.com/encode/starlette/discussions/2094#discussioncomment-9084737 and https://github.com/encode/starlette/discussions/2094#discussioncomment-7576379) is to change the mechanism used to check if the request was actually disconnected. Copied verbatim from that discussion, use this helper instead of `request.is_disconnected()`: > ``` python > async def my_is_disconnected(request: Request) -> bool: > assert hasattr(request, '_is_disconnect...

## 候选优化模式

- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: weird starlette behavior causes `request.is_disconnected()` to return `False`, even if the client disconnects. This is discussed in https://github.com/encode/starlette/discussions/2094. One of the suggested solutions in...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: I spec seems to imply it should be a blocking callable, as it doesn't specify > # what should be returned in case of no new messages. In this situation you can return an > # empty dict, but given that it's against the s...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ases of timeouts / other client disconnects. Unfortunately, this mechanism doesn't work if a `BaseHTTPMiddleware` is added to the server, which is the case when a use provides a function to add as middleware (via the `-...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: lled by the client. This works great and can really ease the load on the model engine in cases of timeouts / other client disconnects. Unfortunately, this mechanism doesn't work if a `BaseHTTPMiddleware` is added to the...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: Requests aren't aborted when client disconnects if user provided a middleware In https://github.com/vllm-project/vllm/pull/7111/, @njhill did a great job to make sure requests are aborted if they are cancelled by...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
