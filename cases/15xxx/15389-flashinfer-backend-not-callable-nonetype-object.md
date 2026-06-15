# vllm-project/vllm#15389: flashinfer backend, not callable NoneType object

| 字段 | 值 |
| --- | --- |
| Issue | [#15389](https://github.com/vllm-project/vllm/issues/15389) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> flashinfer backend, not callable NoneType object

### Issue 正文摘录

> Hey I have the same error with Qwen/Qwen2.5-7B-Instruct. > > ``` > export VLLM_ATTENTION_BACKEND=FLASHINFER > vllm serve Qwen/Qwen2.5-7B-Instruct --max-model-len 8196 --gpu-memory-utilization 0.95 > ``` > > > ``` > File "/home/daniel/vllm/lib/python3.12/site-packages/vllm/attention/backends/flashinfer.py", line 199, in _get_prefill_wrapper > self._prefill_wrapper = BatchPrefillWithPagedKVCacheWrapper( > ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ > TypeError: 'NoneType' object is not callable > [rank0]:[W324 10:53:37.985081939 ProcessGroupNCCL.cpp:1250] Warning: WARNING: process group has NOT been destroyed before we destruct ProcessGroupNCCL. On normal program exit, the application should call destroy_process_group to ensure that any pending NCCL operations have finished in this process. In rare cases this process can exit before this point and block the progress of another member of the process group. This constraint has always been present, but this warning has only been added since PyTorch 2.4 (function operator()) > Traceback (most recent call last): > File "/home/daniel/vllm/bin/vllm", line 8, in > sys.exit(main()) > ^^^^^^ > File "/home/daniel/vllm/lib/python3.12/site-packages/v...

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: flashinfer backend, not callable NoneType object > Hey I have the same error with Qwen/Qwen2.5-7B-Instruct. > > ``` > export VLLM_ATTENTION_BACKEND=FLASHINFER > vllm serve Qwen/Qwen2.5-7B-Instruct --max-model-len 8196
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: 2/site-packages/uvloop/__init__.py", line 109, in run > return __asyncio.run( > ^^^^^^^^^^^^^^ > File "/usr/lib/python3.12/asyncio/runners.py", line 195, in run > return runner.run(main) > ^^^^^^^^^^^^^^^^ > File "/usr/...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: r backend, not callable NoneType object > Hey I have the same error with Qwen/Qwen2.5-7B-Instruct. > > ``` > export VLLM_ATTENTION_BACKEND=FLASHINFER > vllm serve Qwen/Qwen2.5-7B-Instruct --max-model-len 8196 --gpu-memo...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: this process. In rare cases this process can exit before this point and block the progress of another member of the process group. This constraint has always been present, but this warning has only been added since PyTo...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: /site-packages/vllm/attention/backends/flashinfer.py", line 199, in _get_prefill_wrapper > self._prefill_wrapper = BatchPrefillWithPagedKVCacheWrapper( > ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ > TypeError: 'NoneType' obje...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
