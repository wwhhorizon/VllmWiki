# vllm-project/vllm#6385: [Bug]: Runtime AssertionError: 32768 is not divisible by 3, multiproc_worker_utils.py:120, when using 3 GPUs for tensor-parallel 

| 字段 | 值 |
| --- | --- |
| Issue | [#6385](https://github.com/vllm-project/vllm/issues/6385) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Runtime AssertionError: 32768 is not divisible by 3, multiproc_worker_utils.py:120, when using 3 GPUs for tensor-parallel 

### Issue 正文摘录

Some LLM models have assertion error, in multiproc_worker_utils.py:120 - especially when using 3 GPUs This bug is critical and preventing deployment for client. This is a run-time error, not a shut down error --- 1. model: AI-ModelScope/Mixtral-8x22B-Instruct-v0.1 --- 2. Settings: tensor-parallel-size 3 - for 3 GPU --- 3. Error: [rank0]: AssertionError: 32768 is not divisible by 3 ERROR 07-13 02:56:30 multiproc_worker_utils.py:120] Worker VllmWorkerProcess pid 382811 died, exit code: -15 INFO 07-13 02:56:30 multiproc_worker_utils.py:123] Killing local vLLM worker processes --- Also (VllmWorkerProcess pid=412146) WARNING 07-13 03:43:42 custom_all_reduce.py:129] Custom allreduce is disabled due to an unsupported world size: 3. Supported world sizes: [2, 4, 6, 8]. To silence this warning, specify disable_custom_all_reduce=True explicitly. WARNING 07-13 03:43:42 custom_all_reduce.py:129] Custom allreduce is disabled due to an unsupported world size: 3. Supported world sizes: [2, 4, 6, 8]. To silence this warning, specify disable_custom_all_reduce=True explicitly. Traceback (most recent call last): File "/usr/lib/python3.8/multiprocessing/resource_tracker.py", line 201, in main cache[r...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: LLM models have assertion error, in multiproc_worker_utils.py:120 - especially when using 3 GPUs This bug is critical and preventing deployment for client. This is a run-time error, not a shut down error --- 1. model: A...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: racker.py", line 201, in main cache[rtype].remove(name) KeyError: '/psm_dea5b192' Traceback (most recent call last): File "/usr/lib/python3.8/multiprocessing/resource_tracker.py", line 201, in main cache[rtype].remove(n...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: _utils.py:120, when using 3 GPUs for tensor-parallel bug;stale Some LLM models have assertion error, in multiproc_worker_utils.py:120 - especially when using 3 GPUs This bug is critical and preventing deployment for cli...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ultiproc_worker_utils.py:120, when using 3 GPUs for tensor-parallel bug;stale Some LLM models have assertion error, in multiproc_worker_utils.py:120 - especially when using 3 GPUs This bug is critical and preventing dep...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
