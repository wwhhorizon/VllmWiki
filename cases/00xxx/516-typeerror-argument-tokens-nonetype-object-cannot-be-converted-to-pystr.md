# vllm-project/vllm#516: TypeError: argument 'tokens': 'NoneType' object cannot be converted to 'PyString'

| 字段 | 值 |
| --- | --- |
| Issue | [#516](https://github.com/vllm-project/vllm/issues/516) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> TypeError: argument 'tokens': 'NoneType' object cannot be converted to 'PyString'

### Issue 正文摘录

When using vLLM with MPT-30b-chat, run on single A100 80GB: ``` export MODEL=mosaicml/mpt-30b-chat export HF_PORT=3000 export NCCL_IGNORE_DISABLED_P2P=1 python -m vllm.entrypoints.openai.api_server --port=$HF_PORT --host=0.0.0.0 --model $MODEL --seed=1234 &>> logs.$MODEL_NAME.vllm_inference_server.txt & ``` eventually hit below, after which all requests are not completed and are instead aborted: ``` ERROR: Exception in ASGI application Traceback (most recent call last): File "/home/ubuntu/miniconda3/envs/h2ollm/lib/python3.10/site-packages/uvicorn/protocols/http/httptools_impl.py", line 436, in run_asgi result = await app( # type: ignore[func-returns-value] File "/home/ubuntu/miniconda3/envs/h2ollm/lib/python3.10/site-packages/uvicorn/middleware/proxy_headers.py", line 78, in __call__ return await self.app(scope, receive, send) File "/home/ubuntu/miniconda3/envs/h2ollm/lib/python3.10/site-packages/fastapi/applications.py", line 276, in __call__ await super().__call__(scope, receive, send) File "/home/ubuntu/miniconda3/envs/h2ollm/lib/python3.10/site-packages/starlette/applications.py", line 122, in __call__ await self.middleware_stack(scope, receive, send) File "/home/ubuntu/minic...

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: ome/ubuntu/miniconda3/envs/h2ollm/lib/python3.10/site-packages/starlette/routing.py", line 718, in __call__ await route.handle(scope, receive, send) File "/home/ubuntu/miniconda3/envs/h2ollm/lib/python3.10/site-packages...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: g When using vLLM with MPT-30b-chat, run on single A100 80GB: ``` export MODEL=mosaicml/mpt-30b-chat export HF_PORT=3000 export NCCL_IGNORE_DISABLED_P2P=1 python -m vllm.entrypoints.openai.api_server --port=$HF_PORT --h...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: E.vllm_inference_server.txt & ``` eventually hit below, after which all requests are not completed and are instead aborted: ``` ERROR: Exception in ASGI application Traceback (most recent call last): File "/home/ubuntu/...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: miniconda3/envs/h2ollm/lib/python3.10/site-packages/anyio/_backends/_asyncio.py", line 662, in __aexit__ raise exceptions[0] File "/home/ubuntu/miniconda3/envs/h2ollm/lib/python3.10/site-packages/starlette/responses.py"...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: erted to 'PyString' bug When using vLLM with MPT-30b-chat, run on single A100 80GB: ``` export MODEL=mosaicml/mpt-30b-chat export HF_PORT=3000 export NCCL_IGNORE_DISABLED_P2P=1 python -m vllm.entrypoints.openai.api_serv...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
