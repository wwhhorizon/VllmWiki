# vllm-project/vllm#35426: [Bug]: AllReduceRMSFusionPass crashes with PP

| 字段 | 值 |
| --- | --- |
| Issue | [#35426](https://github.com/vllm-project/vllm/issues/35426) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | distributed_parallel |
| 子分类 | env_compat |
| Operator 关键词 | cuda |
| 症状 | crash |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: AllReduceRMSFusionPass crashes with PP

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ``` vllm serve Qwen/Qwen3.5-35B-A3B -tp 2 -pp 2 -cc.pass_config.fuse_allreduce_rms=True ``` ``` (Worker_PP1_TP0 pid=3954408) ERROR 02-27 00:29:48 [multiproc_executor.py:863] torch.distributed.DistBackendError: NCCL error in: /pytorch/torch/csrc/distributed/c10d/NCCLUtils.cpp:93, invalid usage (run with NCCL_DEBUG=WARN for details), NCCL version 2.27.5 (Worker_PP0_TP0 pid=3954406) ERROR 02-27 00:29:48 [multiproc_executor.py:863] self._socket = self._init_ipc_socket() (Worker_PP1_TP0 pid=3954408) ERROR 02-27 00:29:48 [multiproc_executor.py:863] ncclInvalidUsage: This usually reflects invalid usage of NCCL library. (Worker_PP0_TP0 pid=3954406) ERROR 02-27 00:29:48 [multiproc_executor.py:863] ^^^^^^^^^^^^^^^^^^^^^^^ (Worker_PP1_TP0 pid=3954408) ERROR 02-27 00:29:48 [multiproc_executor.py:863] Last error: (Worker_PP0_TP0 pid=3954406) ERROR 02-27 00:29:48 [multiproc_executor.py:863] File "/mnt/data1/zjy/code/vllm-src/.venv/lib/python3.12/site-packages/flashinfer/comm/mnnvl.py", line 809, in _init_ipc_socket (Worker_PP1_TP0 pid=3954408) ERROR 02-27 00:29:48 [multiproc_executor.py:863] Duplicate GPU detected : rank 2 and rank 0 both on C...

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: ) ERROR 02-27 00:29:48 [multiproc_executor.py:863] torch.distributed.DistBackendError: NCCL error in: /pytorch/torch/csrc/distributed/c10d/NCCLUtils.cpp:93, invalid usage (run with NCCL_DEBUG=WARN for details), NCCL ver...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: Utils.cpp:93, invalid usage (run with NCCL_DEBUG=WARN for details), NCCL version 2.27.5 (Worker_PP0_TP0 pid=3954406) ERROR 02-27 00:29:48 [multiproc_executor.py:863] self._socket = self._init_ipc_socket() (Worker_PP1_TP...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: proc_executor.py:863] Duplicate GPU detected : rank 2 and rank 0 both on CUDA device 109000 (Worker_PP0_TP0 pid=3954406) ERROR 02-27 00:29:48 [multiproc_executor.py:863] opId = self.comm.bcast(opId, root=0) ``` ### Befo...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ### Your current environment ### 🐛 Describe the bug ``` vllm serve Qwen/Qwen3.5-35B-A3B -tp 2 -pp 2 -cc.pass_config.fuse_allreduce_rms=True ``` ``` (Worker_PP1_TP0 pid=3954408) ERROR 02-27 00:29:48 [multiproc_executor.p...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions. development distributed_parallel cuda crash env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
