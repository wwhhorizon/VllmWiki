# vllm-project/vllm#5815: [Bug]: flashinfer backend bug

| 字段 | 值 |
| --- | --- |
| Issue | [#5815](https://github.com/vllm-project/vllm/issues/5815) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: flashinfer backend bug

### Issue 正文摘录

### Your current environment ```text I set vllm to flashinfer, but i get the error below: INFO: 127.0.0.1:38616 - "POST /v1/completions HTTP/1.1" 200 OK ERROR: Exception in ASGI application Traceback (most recent call last): File "/mnt/harddisk/miniconda3/envs/flashinfer/lib/python3.9/site-packages/starlette/responses.py", line 265, in __call__ await wrap(partial(self.listen_for_disconnect, receive)) File "/mnt/harddisk/miniconda3/envs/flashinfer/lib/python3.9/site-packages/starlette/responses.py", line 261, in wrap await func() File "/mnt/harddisk/miniconda3/envs/flashinfer/lib/python3.9/site-packages/starlette/responses.py", line 238, in listen_for_disconnect message = await receive() File "/mnt/harddisk/miniconda3/envs/flashinfer/lib/python3.9/site-packages/uvicorn/protocols/http/httptools_impl.py", line 553, in receive await self.message_event.wait() File "/mnt/harddisk/miniconda3/envs/flashinfer/lib/python3.9/asyncio/locks.py", line 226, in wait await fut asyncio.exceptions.CancelledError: Cancelled by cancel scope 7f47bc642f40 During handling of the above exception, another exception occurred: Traceback (most recent call last): File "/mnt/harddisk/miniconda3/envs/flashinfer/...

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: [Bug]: flashinfer backend bug bug ### Your current environment ```text I set vllm to flashinfer, but i get the error below: INFO: 127.0.0.1:38616 - "POST /v1/completions HTTP/1.1" 200 OK ERROR: Exception in ASGI applic
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: run the vllm server as: `python -m vllm.entrypoints.openai.api_server --model LLM-Research/Meta-Llama-3-70B-Instruct --tensor-parallel-size 4 --trust-remote-code --max-model-len 8192 --port 30000 --swap-space 16 --disab...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ait() File "/mnt/harddisk/miniconda3/envs/flashinfer/lib/python3.9/asyncio/locks.py", line 226, in wait await fut asyncio.exceptions.CancelledError: Cancelled by cancel scope 7f47bc642f40 During handling of the above ex...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: server as: `python -m vllm.entrypoints.openai.api_server --model LLM-Research/Meta-Llama-3-70B-Instruct --tensor-parallel-size 4 --trust-remote-code --max-model-len 8192 --port 30000 --swap-space 16 --disable-log-reques...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: arddisk/miniconda3/envs/flashinfer/lib/python3.9/site-packages/starlette/routing.py", line 756, in __call__ await self.middleware_stack(scope, receive, send) File "/mnt/harddisk/miniconda3/envs/flashinfer/lib/python3.9/...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
