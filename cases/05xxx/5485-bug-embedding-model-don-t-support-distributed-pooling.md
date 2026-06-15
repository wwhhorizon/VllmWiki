# vllm-project/vllm#5485: [Bug]: Embedding model don't support distributed pooling

| 字段 | 值 |
| --- | --- |
| Issue | [#5485](https://github.com/vllm-project/vllm/issues/5485) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Embedding model don't support distributed pooling

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### 🐛 Describe the bug I met this bug when I was trying to deploy OpenAI compatible server with an embedding model on a 4x V100 machine, while it is good when I set the tensor-parallel-size as 1. The command to start server is as follow: ``` python -m vllm.entrypoints.openai.api_server --model intfloat/e5-mistral-7b-instruct --dtype auto --api-key token-abc123 --port 7866 --dtype=half --tensor-parallel-size 4 ``` when I send a embedding request like ``` curl http://localhost:7866/v1/embeddings \ -H "Content-Type: application/json" \ -H "Authorization: Bearer token-abc123" \ -d '{ "input": "Your text string goes here", "model": "intfloat/e5-mistral-7b-instruct" }' ``` I got the following error message: ``` ERROR 06-13 11:46:17 async_llm_engine.py:44] Engine background task failed ERROR 06-13 11:46:17 async_llm_engine.py:44] Traceback (most recent call last): ERROR 06-13 11:46:17 async_llm_engine.py:44] File "/data/workspace/vllm/vllm/engine/async_llm_engine.py", line 39, in _raise_exception_on_finish ERROR 06-13 11:46:17 async_llm_engine.py:44] task.result() ERROR 06-13 11:46:17 async_llm_engine.py:44] F...

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: t() File "/data/miniconda/envs/vllm/lib/python3.9/site-packages/anyio/_backends/_asyncio.py", line 678, in __aexit__ raise BaseExceptionGroup( exceptiongroup.ExceptionGroup: unhandled errors in a TaskGroup (1 sub-except...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: Embedding model don't support distributed pooling bug;stale ### Your current environment ```text The output of `python collect_env.py` ``` ### 🐛 Describe the bug I met this bug when I was trying to deploy OpenAI...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Embedding model don't support distributed pooling bug;stale ### Your current environment ```text The output of `python collect_env.py` ``` ### 🐛 Describe the bug I met this bug when I was trying to deploy OpenAI...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: 1:46:17 async_llm_engine.py:44] has_requests_in_progress = await asyncio.wait_for( ERROR 06-13 11:46:17 async_llm_engine.py:44] File "/data/miniconda/envs/vllm/lib/python3.9/asyncio/tasks.py", line 479, in wait_for ERRO...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: .entrypoints.openai.api_server --model intfloat/e5-mistral-7b-instruct --dtype auto --api-key token-abc123 --port 7866 --dtype=half --tensor-parallel-size 4 ``` when I send a embedding request like ``` curl http://local...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
