# vllm-project/vllm#37255: [Bug]: Failed to run distributed inference due to error list index out of range in omp_cpuids_list

| 字段 | 值 |
| --- | --- |
| Issue | [#37255](https://github.com/vllm-project/vllm/issues/37255) |
| 状态 | open |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Failed to run distributed inference due to error list index out of range in omp_cpuids_list

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug it would fail when running with distributed inference (with 2 nodes), failed with "list index out of range" on node 1. @fadara01 Failed message: ``` (Worker pid=4035378) ERROR 03-17 05:18:29 [multiproc_executor.py:852] WorkerProc failed to start. (Worker pid=4035378) ERROR 03-17 05:18:29 [multiproc_executor.py:852] Traceback (most recent call last): (Worker pid=4035378) ERROR 03-17 05:18:29 [multiproc_executor.py:852] File "/home/lialiu01/latest/vllm/vllm/v1/executor/multiproc_executor.py", line 821, in worker_main (Worker pid=4035378) ERROR 03-17 05:18:29 [multiproc_executor.py:852] worker = WorkerProc(*args, **kwargs) (Worker pid=4035378) ERROR 03-17 05:18:29 [multiproc_executor.py:852] ^^^^^^^^^^^^^^^^^^^^^^^^^^^ (Worker pid=4035378) ERROR 03-17 05:18:29 [multiproc_executor.py:852] File "/home/lialiu01/latest/vllm/vllm/tracing/otel.py", line 178, in sync_wrapper (Worker pid=4035378) ERROR 03-17 05:18:29 [multiproc_executor.py:852] return func(*args, **kwargs) (Worker pid=4035378) ERROR 03-17 05:18:29 [multiproc_executor.py:852] ^^^^^^^^^^^^^^^^^^^^^ (Worker pid=4035378) ERROR 03-17 05:18:29 [multiproc_executor.py:852] File "/h...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: 9 [multiproc_executor.py:852] File "/home/lialiu01/latest/vllm/vllm/tracing/otel.py", line 178, in sync_wrapper (Worker pid=4035378) ERROR 03-17 05:18:29 [multiproc_executor.py:852] return func(*args, **kwargs) (Worker...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: hen / 陳昭儒 Date: Wed Jan 21 15:27:30 2026 +0800 [Bugfix] Support HF sharded weights for Mistral3/Pixtral models (#32673) Signed-off-by: ricky-chaoju Signed-off-by: vllm-dev ``` Reproduce method: run on node 0: ``` #!/bin...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: RROR 03-17 05:18:29 [multiproc_executor.py:852] File "/home/lialiu01/latest/vllm/vllm/v1/executor/multiproc_executor.py", line 821, in worker_main (Worker pid=4035378) ERROR 03-17 05:18:29 [multiproc_executor.py:852] wo...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: Signed-off-by: ricky-chaoju Signed-off-by: vllm-dev ``` Reproduce method: run on node 0: ``` #!/bin/bash MODEL=Qwen/Qwen2.5-14B-Instruct MASTER_IP=192.168.1.2 PORT=29508 export GLOO_SOCKET_IFNAME=enp1s0f1np1 export VLLM...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
