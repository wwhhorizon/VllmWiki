# vllm-project/vllm#2075: Qwen-7b-chat infer fail 

| 字段 | 值 |
| --- | --- |
| Issue | [#2075](https://github.com/vllm-project/vllm/issues/2075) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Qwen-7b-chat infer fail 

### Issue 正文摘录

vllm==0.2.3 prompt is: ``` A chat between a curious user and an artificial intelligence assistant. The assistant gives helpful, detailed, and polite answers to the user's questions. Human: hello Assistant: ``` log is: ``` Future exception was never retrieved future: Traceback (most recent call last): File "/usr/local/lib/python3.8/dist-packages/vllm/engine/async_llm_engine.py", line 28, in _raise_exception_on_finish task.result() File "/usr/local/lib/python3.8/dist-packages/vllm/engine/async_llm_engine.py", line 359, in run_engine_loop has_requests_in_progress = await self.engine_step() File "/usr/local/lib/python3.8/dist-packages/vllm/engine/async_llm_engine.py", line 338, in engine_step request_outputs = await self.engine.step_async() File "/usr/local/lib/python3.8/dist-packages/vllm/engine/async_llm_engine.py", line 191, in step_async output = await self._run_workers_async( File "/usr/local/lib/python3.8/dist-packages/vllm/engine/async_llm_engine.py", line 219, in _run_workers_async all_outputs = await asyncio.gather(*coros) File "/usr/lib/python3.8/concurrent/futures/thread.py", line 57, in run result = self.fn(*self.args, **self.kwargs) File "/usr/local/lib/python3.8/dist-pac...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: Qwen-7b-chat infer fail vllm==0.2.3 prompt is: ``` A chat between a curious user and an artificial intelligence assistant. The assistant gives helpful, detailed, and polite answers to the user's questions. Human: hello
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: l vllm==0.2.3 prompt is: ``` A chat between a curious user and an artificial intelligence assistant. The assistant gives helpful, detailed, and polite answers to the user's questions. Human: hello Assistant: ``` log is:...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: in execute_model output = self.model_runner.execute_model(seq_group_metadata_list, File "/usr/local/lib/python3.8/dist-packages/torch/utils/_contextlib.py", line 115, in decorate_context return func(*args, **kwargs) Fil...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: s/vllm/engine/async_llm_engine.py", line 359, in run_engine_loop has_requests_in_progress = await self.engine_step() File "/usr/local/lib/python3.8/dist-packages/vllm/engine/async_llm_engine.py", line 338, in engine_ste...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
