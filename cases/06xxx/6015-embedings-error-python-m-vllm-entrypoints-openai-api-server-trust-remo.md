# vllm-project/vllm#6015: embedings  error                    python -m vllm.entrypoints.openai.api_server --trust-remote-code --model gte_Qwen2-7B-instruct --seed 48 --max-model-len 1000 --tensor-parallel-size 2 --gpu-memory-utilization 1 --dtype float16 

| 字段 | 值 |
| --- | --- |
| Issue | [#6015](https://github.com/vllm-project/vllm/issues/6015) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> embedings  error                    python -m vllm.entrypoints.openai.api_server --trust-remote-code --model gte_Qwen2-7B-instruct --seed 48 --max-model-len 1000 --tensor-parallel-size 2 --gpu-memory-utilization 1 --dtype float16 

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### 🐛 Describe the bug ERROR 07-01 08:12:10 async_llm_engine.py:52] Engine background task failed ERROR 07-01 08:12:10 async_llm_engine.py:52] Traceback (most recent call last): ERROR 07-01 08:12:10 async_llm_engine.py:52] File "/opt/conda/lib/python3.10/site-packages/vllm/engine/async_llm_engine.py", line 42, in _log_task_completion ERROR 07-01 08:12:10 async_llm_engine.py:52] return_value = task.result() ERROR 07-01 08:12:10 async_llm_engine.py:52] File "/opt/conda/lib/python3.10/site-packages/vllm/engine/async_llm_engine.py", line 532, in run_engine_loop ERROR 07-01 08:12:10 async_llm_engine.py:52] has_requests_in_progress = await asyncio.wait_for( ERROR 07-01 08:12:10 async_llm_engine.py:52] File "/opt/conda/lib/python3.10/asyncio/tasks.py", line 445, in wait_for ERROR 07-01 08:12:10 async_llm_engine.py:52] return fut.result() ERROR 07-01 08:12:10 async_llm_engine.py:52] File "/opt/conda/lib/python3.10/site-packages/vllm/engine/async_llm_engine.py", line 506, in engine_step ERROR 07-01 08:12:10 async_llm_engine.py:52] request_outputs = await self.engine.step_async() ERROR 07-01 08:12:10 async_llm_en...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: max-model-len 1000 --tensor-parallel-size 2 --gpu-memory-utilization 1 --dtype float16 bug;stale ### Your current environment ```text The output of `python collect_env.py` ``` ### 🐛 Describe the bug ERROR 07-01 08:12:10...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: python -m vllm.entrypoints.openai.api_server --trust-remote-code --model gte_Qwen2-7B-instruct --seed 48 --max-model-len 1000 --tensor-parallel-size 2 --gpu-memory-utilization 1 --dtype float16 bug;stale ### Your curren...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: --tensor-parallel-size 2 --gpu-memory-utilization 1 --dtype float16 bug;stale ### Your current environment ```text The output of `python collect_env.py` ``` ### 🐛 Describe the bug ERROR 07-01 08:12:10 async_llm_engine.p...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ceive, sender) File "/opt/conda/lib/python3.10/site-packages/starlette/routing.py", line 756, in __call__ await self.middleware_stack(scope, receive, send) File "/opt/conda/lib/python3.10/site-packages/starlette/routing...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: 8:12:10 async_llm_engine.py:52] has_requests_in_progress = await asyncio.wait_for( ERROR 07-01 08:12:10 async_llm_engine.py:52] File "/opt/conda/lib/python3.10/asyncio/tasks.py", line 445, in wait_for ERROR 07-01 08:12:...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
