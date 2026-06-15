# vllm-project/vllm#1623: Top p or temperature == 0.0001 RuntimeError: probability tensor contains either `inf`, `nan` or element < 0

| 字段 | 值 |
| --- | --- |
| Issue | [#1623](https://github.com/vllm-project/vllm/issues/1623) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Top p or temperature == 0.0001 RuntimeError: probability tensor contains either `inf`, `nan` or element < 0

### Issue 正文摘录

The following error occurs when either top-p or temperature is 0.0001 ``` 2023-11-10 17:45:27 | ERROR | asyncio | Future exception was never retrieved future: Traceback (most recent call last): File "/home/tan/tjtanaa/vllm/vllm/engine/async_llm_engine.py", line 28, in _raise_exception_on_finish task.result() File "/home/tan/tjtanaa/vllm/vllm/engine/async_llm_engine.py", line 351, in run_engine_loop has_requests_in_progress = await self.engine_step() File "/home/tan/tjtanaa/vllm/vllm/engine/async_llm_engine.py", line 330, in engine_step request_outputs = await self.engine.step_async() File "/home/tan/tjtanaa/vllm/vllm/engine/async_llm_engine.py", line 191, in step_async output = await self._run_workers_async( File "/home/tan/tjtanaa/vllm/vllm/engine/async_llm_engine.py", line 220, in _run_workers_async all_outputs = await asyncio.gather(*all_outputs) File "/home/tan/anaconda3/envs/fastchat/lib/python3.10/asyncio/tasks.py", line 650, in _wrap_awaitable return (yield from awaitable.__await__()) ray.exceptions.RayTaskError(RuntimeError): ray::RayWorker.execute_method() (pid=2116950, ip=192.168.1.84, actor_id=976706caabd3119cc468097101000000, repr= ) File "/home/tan/tjtanaa/vllm/vllm/e...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ile "/home/tan/tjtanaa/vllm/vllm/worker/worker.py", line 332, in execute_model output = self.model(
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: er top-p or temperature is 0.0001 ``` 2023-11-10 17:45:27 | ERROR | asyncio | Future exception was never retrieved future: Traceback (most recent call last):
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: line 86, in forward sample_results = _sample(probs, logprobs, input_metadata) File "/home/tan/tjtanaa/vllm/vllm/model_executor/layers/sampler.py", line 441, in _sample sample_results = _random_sample(seq_groups, is_prom...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: has_requests_in_progress = await self.engine_step() File "/home/tan/tjtanaa/vllm/vllm/engine/async_llm_engine.py", line

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
