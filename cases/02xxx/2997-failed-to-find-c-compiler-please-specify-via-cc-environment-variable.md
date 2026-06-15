# vllm-project/vllm#2997: Failed to find C compiler. Please specify via CC environment variable

| 字段 | 值 |
| --- | --- |
| Issue | [#2997](https://github.com/vllm-project/vllm/issues/2997) |
| 状态 | closed |
| 标签 |  |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Failed to find C compiler. Please specify via CC environment variable

### Issue 正文摘录

Below is the error I am getting while using generate api with below params. First time it is able to generate with **prefix_pos** but next call I am getting below error. "use_beam_search": false, "n": 1, "temperature": 0.0, "max_tokens" : 200, "skip_special_tokens" : true, "prefix_pos" : 504 ``` Future exception was never retrieved future: Traceback (most recent call last): File "/usr/local/lib/python3.10/dist-packages/vllm/engine/async_llm_engine.py", line 29, in _raise_exception_on_finish task.result() File "/usr/local/lib/python3.10/dist-packages/vllm/engine/async_llm_engine.py", line 411, in run_engine_loop has_requests_in_progress = await self.engine_step() File "/usr/local/lib/python3.10/dist-packages/vllm/engine/async_llm_engine.py", line 390, in engine_step request_outputs = await self.engine.step_async() File "/usr/local/lib/python3.10/dist-packages/vllm/engine/async_llm_engine.py", line 189, in step_async all_outputs = await self._run_workers_async( File "/usr/local/lib/python3.10/dist-packages/vllm/engine/async_llm_engine.py", line 276, in _run_workers_async all_outputs = await asyncio.gather(*coros) File "/usr/lib/python3.10/concurrent/futures/thread.py", line 58, in r...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: Failed to find C compiler. Please specify via CC environment variable Below is the error I am getting while using generate api with below params. First time it is able to generate with **prefix_pos** but next call I am...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: File "/usr/local/lib/python3.10/dist-packages/vllm/model_executor/layers/triton_kernel/prefix_prefill.py", line 685, in context_attention_fwd _fwd_kernel[grid]( File " ", line 63, in _fwd_kernel File "/usr/local/lib/pyt...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: fix_pos** but next call I am getting below error. "use_beam_search": false, "n": 1, "temperature": 0.0, "max_tokens" : 200, "skip_special_tokens" : true, "prefix_pos" : 504 ``` Future exception was never retrieved futur...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ib/python3.10/dist-packages/vllm/worker/worker.py", line 223, in execute_model output = self.model_runner.execute_model(seq_group_metadata_list, File "/usr/local/lib/python3.10/dist-packages/torch/utils/_contextlib.py",...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: s/vllm/engine/async_llm_engine.py", line 411, in run_engine_loop has_requests_in_progress = await self.engine_step() File "/usr/local/lib/python3.10/dist-packages/vllm/engine/async_llm_engine.py", line 390, in engine_st...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
