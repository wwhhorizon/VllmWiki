# vllm-project/vllm#1965: qwen72b bug：UnboundLocalError: local variable 'completion_tokens' referenced before assignment

| 字段 | 值 |
| --- | --- |
| Issue | [#1965](https://github.com/vllm-project/vllm/issues/1965) |
| 状态 | closed |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> qwen72b bug：UnboundLocalError: local variable 'completion_tokens' referenced before assignment

### Issue 正文摘录

WARNING 12-07 23:54:18 scheduler.py:161] Input prompt (6095 tokens) is too long and exceeds the capacity of block_manager INFO 12-07 23:54:18 async_llm_engine.py:111] Finished request cmpl-04b5ec1223bb4cbfa095ad34f921b62a. ERROR: Exception in ASGI application Traceback (most recent call last): File "/root/miniconda3/envs/chatglm_etuning/lib/python3.10/site-packages/uvicorn/protocols/http/httptools_impl.py", line 426, in run_asgi result = await app( # type: ignore[func-returns-value] File "/root/miniconda3/envs/chatglm_etuning/lib/python3.10/site-packages/uvicorn/middleware/proxy_headers.py", line 84, in __call__ return await self.app(scope, receive, send) File "/root/miniconda3/envs/chatglm_etuning/lib/python3.10/site-packages/fastapi/applications.py", line 276, in __call__ await super().__call__(scope, receive, send) File "/root/miniconda3/envs/chatglm_etuning/lib/python3.10/site-packages/starlette/applications.py", line 122, in __call__ await self.middleware_stack(scope, receive, send) File "/root/miniconda3/envs/chatglm_etuning/lib/python3.10/site-packages/starlette/middleware/errors.py", line 184, in __call__ raise exc File "/root/miniconda3/envs/chatglm_etuning/lib/python3.10...

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: t/miniconda3/envs/chatglm_etuning/lib/python3.10/site-packages/starlette/routing.py", line 718, in __call__ await route.handle(scope, receive, send) File "/root/miniconda3/envs/chatglm_etuning/lib/python3.10/site-packag...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: 'completion_tokens' referenced before assignment WARNING 12-07 23:54:18 scheduler.py:161] Input prompt (6095 tokens) is too long and exceeds the capacity of block_manager INFO 12-07 23:54:18 async_llm_engine.py:111] Fin...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: duler.py:161] Input prompt (6095 tokens) is too long and exceeds the capacity of block_manager INFO 12-07 23:54:18 async_llm_engine.py:111] Finished request cmpl-04b5ec1223bb4cbfa095ad34f921b62a. ERROR: Exception in ASG...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: :161] Input prompt (6095 tokens) is too long and exceeds the capacity of block_manager INFO 12-07 23:54:18 async_llm_engine.py:111] Finished request cmpl-04b5ec1223bb4cbfa095ad34f921b62a. ERROR: Exception in ASGI applic...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: qwen72b bug：UnboundLocalError: local variable 'completion_tokens' referenced before assignment WARNING 12-07 23:54:18 scheduler.py:161] Input prompt (6095 tokens) is too long and exceeds the capacity of block_manager INF

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
