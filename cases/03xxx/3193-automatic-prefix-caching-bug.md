# vllm-project/vllm#3193: Automatic Prefix Caching Bug

| 字段 | 值 |
| --- | --- |
| Issue | [#3193](https://github.com/vllm-project/vllm/issues/3193) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Automatic Prefix Caching Bug

### Issue 正文摘录

If I enable automatic prefix caching, it occasionally crashes. ``` Future exception was never retrieved future: Traceback (most recent call last): File "/root/vllm/vllm/engine/async_llm_engine.py", line 29, in _raise_exception_on_finish task.result() File "/root/vllm/vllm/engine/async_llm_engine.py", line 412, in run_engine_loop has_requests_in_progress = await self.engine_step() File "/root/vllm/vllm/engine/async_llm_engine.py", line 391, in engine_step request_outputs = await self.engine.step_async() File "/root/vllm/vllm/engine/async_llm_engine.py", line 189, in step_async all_outputs = await self._run_workers_async( File "/root/vllm/vllm/engine/async_llm_engine.py", line 274, in _run_workers_async all_outputs = await asyncio.gather(*coros) File "/root/miniconda3/envs/vllm/lib/python3.10/concurrent/futures/thread.py", line 58, in run result = self.fn(*self.args, **self.kwargs) File "/root/miniconda3/envs/vllm/lib/python3.10/site-packages/torch/utils/_contextlib.py", line 115, in decorate_context return func(*args, **kwargs) File "/root/vllm/vllm/worker/worker.py", line 223, in execute_model output = self.model_runner.execute_model(seq_group_metadata_list, File "/root/miniconda3...

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: File "/root/miniconda3/envs/vllm/lib/python3.10/site-packages/starlette/routing.py", line 758, in __call__ | await self.middleware_stack(scope, receive, send) | File "/root/miniconda3/envs/vllm/lib/python3.10/site-packa...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: in execute_model output = self.model_runner.execute_model(seq_group_metadata_list, File "/root/miniconda3/envs/vllm/lib/python3.10/site-packages/torch/utils/_contextlib.py", line 115, in decorate_context return func(*ar...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: _engine.py", line 274, in _run_workers_async all_outputs = await asyncio.gather(*coros) File "/root/miniconda3/envs/vllm/lib/python3.10/concurrent/futures/thread.py", line 58, in run result = self.fn(*self.args, **self....
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: nch Model: openbuddy-deepseek-67b-v18.1-4k-gptq (Marlin Kernel) GPU: 4 x RTX3090
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: *kwargs) File "/root/vllm/vllm/worker/worker.py", line 223, in execute_model output = self.model_runner.execute_model(seq_group_metadata_list, File "/root/miniconda3/envs/vllm/lib/python3.10/site-packages/torch/utils/_c...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
