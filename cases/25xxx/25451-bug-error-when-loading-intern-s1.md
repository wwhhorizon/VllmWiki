# vllm-project/vllm#25451: [Bug]: Error when loading Intern-S1

| 字段 | 值 |
| --- | --- |
| Issue | [#25451](https://github.com/vllm-project/vllm/issues/25451) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Error when loading Intern-S1

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug The compatibility issue of vllm and transformers library makes hosting intern-s1 fail. I am tried to use vllm==0.10.1/0.10/2, and transformers 0.56.2/0.55.2 Using vlllm to host intern-s1 will get error as follows (except for vllm=0.10.1 x transformers=0.55.2), but no issue hosting intern-s1-mini ``` (VllmWorker TP7 pid=2537683) ERROR 09-23 05:01:41 [multiproc_executor.py:559] WorkerProc failed to start. (VllmWorker TP7 pid=2537683) ERROR 09-23 05:01:41 [multiproc_executor.py:559] Traceback (most recent call last): (VllmWorker TP7 pid=2537683) ERROR 09-23 05:01:41 [multiproc_executor.py:559] File "/home/nsl/miniconda3/envs/sos-test/lib/python3.11/site-packages/vllm/inputs/registry.py", line 173, in call_hf_processor (VllmWorker TP7 pid=2537683) ERROR 09-23 05:01:41 [multiproc_executor.py:559] output = hf_processor(**data, (VllmWorker TP7 pid=2537683) ERROR 09-23 05:01:41 [multiproc_executor.py:559] ^^^^^^^^^^^^^^^^^^^^ (VllmWorker TP7 pid=2537683) ERROR 09-23 05:01:41 [multiproc_executor.py:559] File "/home/nsl/miniconda3/envs/sos-test/lib/python3.11/site-packages/transformers/models/internvl/processing_internvl.py", line 226, in...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: lib/python3.11/site-packages/vllm/inputs/registry.py", line 173, in call_hf_processor (VllmWorker TP7 pid=2537683) ERROR 09-23 05:01:41 [multiproc_executor.py:559] output = hf_processor(**data, (VllmWorker TP7 pid=25376...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: eoProcessor._preprocess() missing 1 required positional argument: 'video_metadata' (VllmWorker TP7 pid=2537683) ERROR 09-23 05:01:41 [multiproc_executor.py:559] (VllmWorker TP7 pid=2537683) ERROR 09-23 05:01:41 [multipr...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: :01:41 [multiproc_executor.py:559] File "/home/nsl/miniconda3/envs/sos-test/lib/python3.11/site-packages/vllm/inputs/registry.py", line 173, in call_hf_processor (VllmWorker TP7 pid=2537683) ERROR 09-23 05:01:41 [multip...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: d=2536403) File "/home/nsl/miniconda3/envs/sos-test/lib/python3.11/asyncio/runners.py", line 118, in run (APIServer pid=2536403) return self._loop.run_until_complete(task) (APIServer pid=2536403) ^^^^^^^^^^^^^^^^^^^^^^^...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: rypoints/cli/main.py", line 54, in main (APIServer pid=2536403) args.dispatch_function(args) (APIServer pid=2536403) File "/home/nsl/miniconda3/envs/sos-test/lib/python3.11/site-packages/vllm/entrypoints/cli/serve.py",...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
