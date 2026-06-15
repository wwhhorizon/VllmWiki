# vllm-project/vllm#3310: AsyncEngineDeadError when LoRA loading fails

| 字段 | 值 |
| --- | --- |
| Issue | [#3310](https://github.com/vllm-project/vllm/issues/3310) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> AsyncEngineDeadError when LoRA loading fails

### Issue 正文摘录

**Error**: when client requesting a LoRA model that cannot be loaded, AsyncLLMEngine would crash with AsyncEngineDeadError. Client HTTP session would hang indefinitely. **Expected Behavior**: VLLM should either prevent unloadable LoRA during init phase to avoid user running into this error OR return 500 error immediately. **Stacktrace**: ``` Exception in callback functools.partial( , request_tracker= ) handle: , request_tracker= )> Traceback (most recent call last): File " /vllm/engine/async_llm_engine.py", line 29, in _raise_exception_on_finish task.result() File " /vllm/engine/async_llm_engine.py", line 414, in run_engine_loop has_requests_in_progress = await self.engine_step() File " /vllm/engine/async_llm_engine.py", line 393, in engine_step request_outputs = await self.engine.step_async() File " /vllm/engine/async_llm_engine.py", line 189, in step_async all_outputs = await self._run_workers_async( File " /vllm/engine/async_llm_engine.py", line 276, in _run_workers_async all_outputs = await asyncio.gather(*coros) File "/home/ /Repos/hello-vllm/.conda/lib/python3.10/concurrent/futures/thread.py", line 58, in run result = self.fn(*self.args, **self.kwargs) File " /torch/utils/_c...

## 候选优化模式

- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: in execute_model output = self.model_runner.execute_model(seq_group_metadata_list, File " /torch/utils/_contextlib.py", line 115, in decorate_context return func(*args, **kwargs) File " /vllm/worker/model_runner.py", li...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: AsyncEngineDeadError when LoRA loading fails stale **Error**: when client requesting a LoRA model that cannot be loaded, AsyncLLMEngine would crash with AsyncEngineDeadError. Client HTTP session would hang indefinitely....
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: _engine.py", line 276, in _run_workers_async all_outputs = await asyncio.gather(*coros) File "/home/ /Repos/hello-vllm/.conda/lib/python3.10/concurrent/futures/thread.py", line 58, in run result = self.fn(*self.args, **...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: r when LoRA loading fails stale **Error**: when client requesting a LoRA model that cannot be loaded, AsyncLLMEngine would crash with AsyncEngineDeadError. Client HTTP session would hang indefinitely. **Expected Behavio...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
