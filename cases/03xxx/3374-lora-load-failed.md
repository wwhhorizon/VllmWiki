# vllm-project/vllm#3374: lora load failed

| 字段 | 值 |
| --- | --- |
| Issue | [#3374](https://github.com/vllm-project/vllm/issues/3374) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | distributed_parallel |
| 子分类 | runtime_err |
| Operator 关键词 | cuda |
| 症状 | crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> lora load failed

### Issue 正文摘录

``` Exception in callback functools.partial( , request_tracker= ) handle: , request_tracker= )> Traceback (most recent call last): File "/usr/local/lib/python3.10/dist-packages/vllm/engine/async_llm_engine.py", line 29, in _raise_exception_on_finish task.result() File "/usr/local/lib/python3.10/dist-packages/vllm/engine/async_llm_engine.py", line 414, in run_engine_loop has_requests_in_progress = await self.engine_step() File "/usr/local/lib/python3.10/dist-packages/vllm/engine/async_llm_engine.py", line 393, in engine_step request_outputs = await self.engine.step_async() File "/usr/local/lib/python3.10/dist-packages/vllm/engine/async_llm_engine.py", line 189, in step_async all_outputs = await self._run_workers_async( File "/usr/local/lib/python3.10/dist-packages/vllm/engine/async_llm_engine.py", line 276, in _run_workers_async all_outputs = await asyncio.gather(*coros) File "/usr/lib/python3.10/asyncio/tasks.py", line 650, in _wrap_awaitable return (yield from awaitable.__await__()) ray.exceptions.RayTaskError(RuntimeError): ray::RayWorkerVllm.execute_method() (pid=59396, ip=10.192.82.3, actor_id=81f1bd9d1e1f68a1ddb5a26301000000, repr= ) File "/usr/local/lib/python3.10/dist-packa...

## 现有链接修复摘要

#7129 [Bugfix] Specify device when loading LoRA and embedding tensors

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: 00000, repr= ) File "/usr/local/lib/python3.10/dist-packages/vllm/lora/models.py", line 212, in from_local_checkpoint tensors = torch.load(lora_bin_file_path) File "/usr/local/lib/python3.10/dist-packages/torch/serializ...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: _engine.py", line 276, in _run_workers_async all_outputs = await asyncio.gather(*coros) File "/usr/lib/python3.10/asyncio/tasks.py", line 650, in _wrap_awaitable return (yield from awaitable.__await__()) ray.exceptions....
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: in execute_model output = self.model_runner.execute_model(seq_group_metadata_list, File "/usr/local/lib/python3.10/dist-packages/torch/utils/_contextlib.py", line 115, in decorate_context return func(*args, **kwargs) Fi...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: lora load failed ``` Exception in callback functools.partial( , request_tracker= ) handle: , request_tracker= )> Traceback (most recent call last): File "/usr/local/lib/python3.10/dist-packages/vllm/engine/async_llm_eng...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: ation.py", line 1392, in persistent_load typed_storage = load_tensor(dtype, nbytes, key, _maybe_decode_ascii(location)) File "/usr/local/lib/python3.10/dist-packages/torch/serialization.py", line 1366, in load_tensor wr...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#7129](https://github.com/vllm-project/vllm/pull/7129) | closes_keyword | 0.95 | [Bugfix] Specify device when loading LoRA and embedding tensors | Fixes [#3374](https://github.com/vllm-project/vllm/issues/3374). Note — existing PR to address this issue got stale; so bumping with some light updates. This PR addresses the is |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
