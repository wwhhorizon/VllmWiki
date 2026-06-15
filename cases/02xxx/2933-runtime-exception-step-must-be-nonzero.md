# vllm-project/vllm#2933: Runtime exception [step must be nonzero]

| 字段 | 值 |
| --- | --- |
| Issue | [#2933](https://github.com/vllm-project/vllm/issues/2933) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Runtime exception [step must be nonzero]

### Issue 正文摘录

Somehow `max_prompt_len` may be 0 in this code: https://github.com/vllm-project/vllm/blob/264017a2bf030f060ebad91eb9be9b4e0033edb9/vllm/worker/model_runner.py#L232 ``` | File "/usr/local/lib/python3.10/dist-packages/vllm/engine/async_llm_engine.py", line 29, in _raise_exception_on_finish [32/1990] | task.result() | File "/usr/local/lib/python3.10/dist-packages/vllm/engine/async_llm_engine.py", line 411, in run_engine_loop | has_requests_in_progress = await self.engine_step() | File "/usr/local/lib/python3.10/dist-packages/vllm/engine/async_llm_engine.py", line 390, in engine_step | request_outputs = await self.engine.step_async() | File "/usr/local/lib/python3.10/dist-packages/vllm/engine/async_llm_engine.py", line 189, in step_async | all_outputs = await self._run_workers_async( | File "/usr/local/lib/python3.10/dist-packages/vllm/engine/async_llm_engine.py", line 276, in _run_workers_async | all_outputs = await asyncio.gather(*coros) | File "/usr/lib/python3.10/concurrent/futures/thread.py", line 58, in run | result = self.fn(*self.args, **self.kwargs) | File "/usr/local/lib/python3.10/dist-packages/torch/utils/_contextlib.py", line 115, in decorate_context | return func(*args,...

## 候选优化模式

- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: | output = self.model_runner.execute_model(seq_group_metadata_list, | File "/usr/local/lib/python3.10/dist-packages/torch/utils/_contextlib.py", line 115, in decorate_context
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: Runtime exception [step must be nonzero] stale Somehow `max_prompt_len` may be 0 in this code: https://github.com/vllm-project/vllm/blob/264017a2bf030f060ebad91eb9be9b4e0033edb9/vllm/worker/model_runner.py#L232 ``` | Fi...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: rkers_async | all_outputs = await asyncio.gather(*coros) | File "/usr/lib/python3.10/concurrent/futures/thread.py", line 58, in run
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: m-project/vllm/blob/264017a2bf030f060ebad91eb9be9b4e0033edb9/vllm/worker/model_runner.py#L232 ``` | File "/usr/local/lib/python3.10/dist-packages/vllm/engine/async_llm_engine.py", line 29, in _raise_exception_on_finish...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
