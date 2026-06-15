# vllm-project/vllm#33628: [Bug]: Failed to run distributed inference with Gloo backend on aarch64

| 字段 | 值 |
| --- | --- |
| Issue | [#33628](https://github.com/vllm-project/vllm/issues/33628) |
| 状态 | open |
| 标签 | bug;stale;cpu |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Failed to run distributed inference with Gloo backend on aarch64

### Issue 正文摘录

### Your current environment it would fail when running with distributed inference (with 2 nodes), somewhere at the open shm in SHMManager, looks like it’s a regression since the SHM is enabled in the commit https://github.com/vllm-project/vllm/pull/32792/commits as I don’t see the issue in previous version @fadara01 ### 🐛 Describe the bug failed message: ``` ERROR 02-02 09:48:15 [multiproc_executor.py:766] WorkerProc failed to start. ERROR 02-02 09:48:15 [multiproc_executor.py:766] Traceback (most recent call last): ERROR 02-02 09:48:15 [multiproc_executor.py:766] File "latest/vllm/vllm/v1/executor/multiproc_executor.py", line 737, in worker_main ERROR 02-02 09:48:15 [multiproc_executor.py:766] worker = WorkerProc(*args, **kwargs) ERROR 02-02 09:48:15 [multiproc_executor.py:766] ^^^^^^^^^^^^^^^^^^^^^^^^^^^ ERROR 02-02 09:48:15 [multiproc_executor.py:766] File "latest/vllm/vllm/v1/executor/multiproc_executor.py", line 566, in __init__ ERROR 02-02 09:48:15 [multiproc_executor.py:766] self.worker.init_device() ERROR 02-02 09:48:15 [multiproc_executor.py:766] File "latest/vllm/vllm/v1/worker/worker_base.py", line 326, in init_device ERROR 02-02 09:48:15 [multiproc_executor.py:766] se...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ed_environment ERROR 02-02 09:48:15 [multiproc_executor.py:766] ensure_model_parallel_initialized( ERROR 02-02 09:48:15 [multiproc_executor.py:766] File "latest/vllm/vllm/distributed/parallel_state.py", line 1450, in en...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: llm-project/vllm/pull/32792/commits as I don’t see the issue in previous version @fadara01 ### 🐛 Describe the bug failed message: ``` ERROR 02-02 09:48:15 [multiproc_executor.py:766] WorkerProc failed to start. ERROR 02...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: ith 2 nodes), somewhere at the open shm in SHMManager, looks like it’s a regression since the SHM is enabled in the commit https://github.com/vllm-project/vllm/pull/32792/commits as I don’t see the issue in previous ver...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: [Bug]: Failed to run distributed inference with Gloo backend on aarch64 bug;stale;cpu ### Your current environment it would fail when running with distributed inference (with 2 nodes), somewhere at the open shm in SHMMa...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: 2673) Signed-off-by: ricky-chaoju Signed-off-by: vllm-dev ``` Reproduce method: run on node 0: ``` #!/bin/bash MODEL=Qwen/Qwen2.5-14B-Instruct MASTER_IP=192.168.1.2 PORT=29508 export GLOO_SOCKET_IFNAME=enp1s0f1np1 expor...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
