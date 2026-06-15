# vllm-project/vllm#5697: [Usage]: TimeoutError() 

| 字段 | 值 |
| --- | --- |
| Issue | [#5697](https://github.com/vllm-project/vllm/issues/5697) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: TimeoutError() 

### Issue 正文摘录

### Your current environment [Bug]: INFO 06-19 11:23:59 metrics.py:341] Avg prompt throughput: 3526.1 tokens/s, Avg generation throughput: 115.2 tokens/s, Running: 8 reqs, Swapped: 0 reqs, Pending: 0 reqs, GPU KV cache usage: 0.9%, CPU KV cache usage: 0.0%. ERROR 06-19 11:25:01 async_llm_engine.py:535] Engine iteration timed out. This should never happen! ERROR 06-19 11:25:01 async_llm_engine.py:52] Engine background task failed ERROR 06-19 11:25:01 async_llm_engine.py:52] Traceback (most recent call last): ERROR 06-19 11:25:01 async_llm_engine.py:52] File "/root/anaconda3/envs/vllm/lib/python3.10/site-packages/vllm/engine/async_llm_engine.py", line 506, in engine_step ERROR 06-19 11:25:01 async_llm_engine.py:52] request_outputs = await self.engine.step_async() ERROR 06-19 11:25:01 async_llm_engine.py:52] File "/root/anaconda3/envs/vllm/lib/python3.10/site-packages/vllm/engine/async_llm_engine.py", line 235, in step_async ERROR 06-19 11:25:01 async_llm_engine.py:52] output = await self.model_executor.execute_model_async( ERROR 06-19 11:25:01 async_llm_engine.py:52] File "/root/anaconda3/envs/vllm/lib/python3.10/site-packages/vllm/executor/distributed_gpu_executor.py", line 166, in...

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: File "/root/anaconda3/envs/vllm/lib/python3.10/site-packages/starlette/routing.py", line 756, in __call__ await self.middleware_stack(scope, receive, send) File "/root/anaconda3/envs/vllm/lib/python3.10/site-packages/st...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: odel(execute_model_req) ERROR 06-19 11:25:01 async_llm_engine.py:52] asyncio.exceptions.CancelledError ERROR 06-19 11:25:01 async_llm_engine.py:52] ERROR 06-19 11:25:01 async_llm_engine.py:52] During handling of the abo...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: : 115.2 tokens/s, Running: 8 reqs, Swapped: 0 reqs, Pending: 0 reqs, GPU KV cache usage: 0.9%, CPU KV cache usage: 0.0%. ERROR 06-19 11:25:01 async_llm_engine.py:535] Engine iteration timed out. This should never happen...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ync ERROR 06-19 11:25:01 async_llm_engine.py:52] output = await self.model_executor.execute_model_async( ERROR 06-19 11:25:01 async_llm_engine.py:52] File "/root/anaconda3/envs/vllm/lib/python3.10/site-packages/vllm/exe...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: File "/root/anaconda3/envs/vllm/lib/python3.10/site-packages/starlette/routing.py", line 756, in __call__ await self.middleware_stack(scope, receive, send) File "/root/anaconda3/envs/vllm/lib/python3.10/site-packages/st...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
