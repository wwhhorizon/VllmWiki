# vllm-project/vllm#2705: stream infer error!

| 字段 | 值 |
| --- | --- |
| Issue | [#2705](https://github.com/vllm-project/vllm/issues/2705) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | frontend_api;model_support |
| 子分类 | debug |
| Operator 关键词 | cuda |
| 症状 | crash |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> stream infer error!

### Issue 正文摘录

I want to use AsyncLLMEngine for stream reasoning, and then I use the tornado method to serve. When I created the coroutine, I encountered the following error. ``` [2024-02-01 15:34:28 base_events.py:1707 ERROR] Exception in callback _raise_exception_on_finish(request_tracker= )( ) at /home/admin/vllm/vllm/engine/async_llm_engine.py:22 handle: )( ) at /home/admin/vllm/vllm/engine/async_llm_engine.py:22> Traceback (most recent call last): File "/home/admin/vllm/vllm/engine/async_llm_engine.py", line 28, in _raise_exception_on_finish task.result() File "/usr/local/lib/python3.8/asyncio/futures.py", line 178, in result raise self._exception File "/usr/local/lib/python3.8/asyncio/tasks.py", line 282, in __step result = coro.throw(exc) File "/home/admin/vllm/vllm/engine/async_llm_engine.py", line 363, in run_engine_loop has_requests_in_progress = await self.engine_step() File "/home/admin/vllm/vllm/engine/async_llm_engine.py", line 342, in engine_step request_outputs = await self.engine.step_async() File "/home/admin/vllm/vllm/engine/async_llm_engine.py", line 190, in step_async all_outputs = await self._run_workers_async( File "/home/admin/vllm/vllm/engine/async_llm_engine.py", line 2...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: on_finish task.result() File "/usr/local/lib/python3.8/asyncio/futures.py", line 178, in result raise self._exception File "/usr/local/lib/python3.8/asyncio/tasks.py", line 282, in __step result = coro.throw(exc) File "...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ensor(padded_x, File "/usr/local/lib/python3.8/site-packages/torch/cuda/__init__.py", line 235, in _lazy_init raise RuntimeError( RuntimeError: Cannot re-initialize CUDA in forked subprocess. To use CUDA with multiproce...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: execute_model output = self.model_runner.execute_model(seq_group_metadata_list, File "/usr/local/lib/python3.8/site-packages/torch/utils/_contextlib.py", line 115, in decorate_context return func(*args, **kwargs) File "...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: File "/home/admin/vllm/vllm/worker/worker.py", line 189, in execute_model output = self.model_runner.execute_model(seq_group_metadata_list, File "/usr/local/lib/python3.8/site-packages/torch/utils/_contextlib.py", line...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: e_events.py:1707 ERROR] Exception in callback _raise_exception_on_finish(request_tracker= )( ) at /home/admin/vllm/vllm/engine/async_llm_engine.py:22 handle: )( ) at /home/admin/vllm/vllm/engine/async_llm_engine.py:22>...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
