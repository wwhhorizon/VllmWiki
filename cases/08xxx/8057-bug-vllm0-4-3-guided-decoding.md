# vllm-project/vllm#8057: [Bug]: vllm0.4.3 guided decoding 

| 字段 | 值 |
| --- | --- |
| Issue | [#8057](https://github.com/vllm-project/vllm/issues/8057) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: vllm0.4.3 guided decoding 

### Issue 正文摘录

### Your current environment ```text Traceback (most recent call last): File "/data/tangjiakai/anaconda3/lib/python3.11/site-packages/uvicorn/protocols/http/httptools_impl.py", line 419, in run_asgi result = await app( # type: ignore[func-returns-value] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/data/tangjiakai/anaconda3/lib/python3.11/site-packages/uvicorn/middleware/proxy_headers.py", line 84, in __call__ return await self.app(scope, receive, send) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/data/tangjiakai/anaconda3/lib/python3.11/site-packages/fastapi/applications.py", line 1054, in __call__ await super().__call__(scope, receive, send) File "/data/tangjiakai/anaconda3/lib/python3.11/site-packages/starlette/applications.py", line 123, in __call__ await self.middleware_stack(scope, receive, send) File "/data/tangjiakai/anaconda3/lib/python3.11/site-packages/starlette/middleware/errors.py", line 186, in __call__ raise exc File "/data/tangjiakai/anaconda3/lib/python3.11/site-packages/starlette/middleware/errors.py", line 164, in __call__ await self.app(scope, receive, _send) File "/data/tangjiakai/anaconda3/lib/python3.11/site-packages/starlette/middleware/base.py", lin...

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: tte/middleware/base.py", line 191, in __call__ response = await self.dispatch_func(request, call_next) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/data/tangjiakai/anaconda3/lib/python3.11/site-packages/vllm/entr...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: uided_decoding/outlines_logits_processors.py", line 77, in __init__ fsm = RegexFSM(regex_string, tokenizer) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/data/tangjiakai/anaconda3/lib/python3.11/site-packages/outlines/fsm/fs...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: core.Timeout: 0 ``` ### 🐛 Describe the bug When I use guided choice in version 0.4.3 of vllm using api server, I get an error. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issue...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: or( File "/data/tangjiakai/anaconda3/lib/python3.11/site-packages/vllm/model_executor/guided_decoding/__init__.py", line 17, in get_guided_decoding_logits_processor return await get_outlines_guided_decoding_logits_proce...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: File "/data/tangjiakai/anaconda3/lib/python3.11/site-packages/starlette/routing.py", line 758, in __call__ await self.middleware_stack(scope, receive, send) File "/data/tangjiakai/anaconda3/lib/python3.11/site-packages/...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
