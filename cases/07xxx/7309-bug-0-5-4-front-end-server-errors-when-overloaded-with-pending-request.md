# vllm-project/vllm#7309: [Bug][0.5.4] Front-end server errors when overloaded with pending requests

| 字段 | 值 |
| --- | --- |
| Issue | [#7309](https://github.com/vllm-project/vllm/issues/7309) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf;slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug][0.5.4] Front-end server errors when overloaded with pending requests

### Issue 正文摘录

### Your current environment The output of `python collect_env.py`: ### 🐛 Describe the bug It seems the front-end server can easily get overloaded when there are many pending requests (>1000 seems to roughly be the threshold). Individual requests over the threshold being failing with: ``` ERROR: Exception in ASGI application Traceback (most recent call last): File "/home/mgoin/venvs/vllm-rel/lib/python3.10/site-packages/starlette/responses.py", line 265, in __call__ await wrap(partial(self.listen_for_disconnect, receive)) File "/home/mgoin/venvs/vllm-rel/lib/python3.10/site-packages/starlette/responses.py", line 261, in wrap await func() File "/home/mgoin/venvs/vllm-rel/lib/python3.10/site-packages/starlette/responses.py", line 238, in listen_for_disconnect message = await receive() File "/home/mgoin/venvs/vllm-rel/lib/python3.10/site-packages/uvicorn/protocols/http/httptools_impl.py", line 553, in receive await self.message_event.wait() File "/usr/lib/python3.10/asyncio/locks.py", line 214, in wait await fut asyncio.exceptions.CancelledError: Cancelled by cancel scope 7f6028dc8ee0 During handling of the above exception, another exception occurred: Traceback (most recent call last...

## 现有链接修复摘要

#7394 [Bugfix][Frontend] Fix Issues Under High Load With `zeromq` Frontend | #41606 Bump the minor-update group across 1 directory with 140 updates | #41766 Bump the minor-update group across 1 directory with 141 updates | #41859 Bump the minor-update group across 1 directory with 141 updates

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: File "/home/mgoin/venvs/vllm-rel/lib/python3.10/site-packages/starlette/routing.py", line 756, in __call__ await self.middleware_stack(scope, receive, send) File "/home/mgoin/venvs/vllm-rel/lib/python3.10/site-packages/...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: eive await self.message_event.wait() File "/usr/lib/python3.10/asyncio/locks.py", line 214, in wait await fut asyncio.exceptions.CancelledError: Cancelled by cancel scope 7f6028dc8ee0 During handling of the above except...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug][0.5.4] Front-end server errors when overloaded with pending requests bug;stale ### Your current environment The output of `python collect_env.py`: ### 🐛 Describe the bug It seems the front-end server can easily ge...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ach request. ## Steps to replicate Server command: ``` vllm serve meta-llama/Meta-Llama-3.1-8B-Instruct --disable-log-requests ``` Benchmark command (needs more than 1000 pending prompts to trigger): ``` python benchmar...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: serve meta-llama/Meta-Llama-3.1-8B-Instruct --disable-log-requests ``` Benchmark command (needs more than 1000 pending prompts to trigger): ``` python benchmarks/benchmark_serving.py --model meta-llama/Meta-Llama-3.1-8B...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#7394](https://github.com/vllm-project/vllm/pull/7394) | closes_keyword | 0.95 | [Bugfix][Frontend] Fix Issues Under High Load With `zeromq` Frontend | FIX - #7309 - #7290 ### UPDATE 8/20 POST OFFLINE DISCUSSION Per discussion offline with @njhill @simon-mo and @youkaichao After much further investigation, we ran int |
| [#41606](https://github.com/vllm-project/vllm/pull/41606) | closes_keyword | 0.95 | Bump the minor-update group across 1 directory with 140 updates | Fix malformed value parsing for Content-Type (<a href="https://redirect.github.com/psf/requests/issues/7309">#7309</a>)</li> <li><a href="https://github.com/psf/requests/commit/bc7 |
| [#41766](https://github.com/vllm-project/vllm/pull/41766) | closes_keyword | 0.95 | Bump the minor-update group across 1 directory with 141 updates | Fix malformed value parsing for Content-Type (<a href="https://redirect.github.com/psf/requests/issues/7309">#7309</a>)</li> <li><a href="https://github.com/psf/requests/commit/bc7 |
| [#41859](https://github.com/vllm-project/vllm/pull/41859) | closes_keyword | 0.95 | Bump the minor-update group across 1 directory with 141 updates | Fix malformed value parsing for Content-Type (<a href="https://redirect.github.com/psf/requests/issues/7309">#7309</a>)</li> <li><a href="https://github.com/psf/requests/commit/bc7 |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
