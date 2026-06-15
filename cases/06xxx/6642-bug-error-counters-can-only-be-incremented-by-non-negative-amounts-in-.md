# vllm-project/vllm#6642: [Bug]: error `Counters can only be incremented by non-negative amounts.` in `metrics` module

| 字段 | 值 |
| --- | --- |
| Issue | [#6642](https://github.com/vllm-project/vllm/issues/6642) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: error `Counters can only be incremented by non-negative amounts.` in `metrics` module

### Issue 正文摘录

### Your current environment I got the error in vllm server when I use `results = await asyncio.gather(*tasks)` in client. ### 🐛 Describe the bug Here is the error log: ``` ERROR 07-22 09:54:47 async_llm_engine.py:52] Engine background task failed ERROR 07-22 09:54:47 async_llm_engine.py:52] Traceback (most recent call last): ERROR 07-22 09:54:47 async_llm_engine.py:52] File "/home/a100user/miniconda3/envs/glm/lib/python3.10/site-packages/vllm/engine/async_llm_engine.py", line 42, in _log_task_completion ERROR 07-22 09:54:47 async_llm_engine.py:52] return_value = task.result() ERROR 07-22 09:54:47 async_llm_engine.py:52] File "/home/a100user/miniconda3/envs/glm/lib/python3.10/site-packages/vllm/engine/async_llm_engine.py", line 532, in run_engine_loop ERROR 07-22 09:54:47 async_llm_engine.py:52] has_requests_in_progress = await asyncio.wait_for( ERROR 07-22 09:54:47 async_llm_engine.py:52] File "/home/a100user/miniconda3/envs/glm/lib/python3.10/asyncio/tasks.py", line 445, in wait_for ERROR 07-22 09:54:47 async_llm_engine.py:52] return fut.result() ERROR 07-22 09:54:47 async_llm_engine.py:52] File "/home/a100user/miniconda3/envs/glm/lib/python3.10/site-packages/vllm/engine/async_l...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: in run_engine_loop ERROR 07-22 09:54:47 async_llm_engine.py:52] has_requests_in_progress = await asyncio.wait_for( ERROR 07-22 09:54:47 async_llm_engine.py:52] File "/home/a100user/miniconda3/envs/glm/lib/python3.10/asy...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ironment I got the error in vllm server when I use `results = await asyncio.gather(*tasks)` in client. ### 🐛 Describe the bug Here is the error log: ``` ERROR 07-22 09:54:47 async_llm_engine.py:52] Engine background tas...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: t call last): ERROR 07-22 09:54:47 async_llm_engine.py:52] File "/home/a100user/miniconda3/envs/glm/lib/python3.10/site-packages/vllm/engine/async_llm_engine.py", line 42, in _log_task_completion ERROR 07-22 09:54:47 as...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
