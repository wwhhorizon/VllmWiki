# vllm-project/vllm#42149: [Bug]: vllm 0.11.2 the p2p_nccl_engine not support ipv6? which version is ok

| 字段 | 值 |
| --- | --- |
| Issue | [#42149](https://github.com/vllm-project/vllm/issues/42149) |
| 状态 | open |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: vllm 0.11.2 the p2p_nccl_engine not support ipv6? which version is ok

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug (Worker_TP1 pid=27102) WARNING 05-09 16:34:35 [base.py:151] Initializing KVConnectorBase_V1. This API is experimental and subject to change in the future as we iterate the design. (Worker_TP0 pid=27101) ERROR 05-09 16:34:35 [multiproc_executor.py:815] WorkerProc hit an exception. (Worker_TP0 pid=27101) ERROR 05-09 16:34:35 [multiproc_executor.py:815] Traceback (most recent call last): (Worker_TP1 pid=27102) ERROR 05-09 16:34:35 [multiproc_executor.py:815] WorkerProc hit an exception. (Worker_TP0 pid=27101) ERROR 05-09 16:34:35 [multiproc_executor.py:815] File "/usr/local/lib/python3.10/site-packages/vllm/v1/executor/multiproc_executor.py", line 810, in worker_busy_loop (Worker_TP1 pid=27102) ERROR 05-09 16:34:35 [multiproc_executor.py:815] Traceback (most recent call last): (Worker_TP0 pid=27101) ERROR 05-09 16:34:35 [multiproc_executor.py:815] output = func(*args, **kwargs) (Worker_TP1 pid=27102) ERROR 05-09 16:34:35 [multiproc_executor.py:815] File "/usr/local/lib/python3.10/site-packages/vllm/v1/executor/multiproc_executor.py", line 810, in worker_busy_loop (Worker_TP0 pid=27101) ERROR 05-09 16:34:35 [multiproc_executor.py:815...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: te-packages/vllm/v1/worker/worker_base.py", line 319, in initialize_from_config (Worker_TP1 pid=27102) ERROR 05-09 16:34:35 [multiproc_executor.py:815] output = func(*args, **kwargs) (Worker_TP0 pid=27101) ERROR 05-09 1...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: pid=27101) ERROR 05-09 16:34:35 [multiproc_executor.py:815] File "zmq/backend/cython/_zmq.py", line 1009, in zmq.backend.cython._zmq.Socket.bind (Worker_TP1 pid=27102) ERROR 05-09 16:34:35 [multiproc_executor.py:815] su...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: [Bug]: vllm 0.11.2 the p2p_nccl_engine not support ipv6? which version is ok bug ### Your current environment ### 🐛 Describe the bug (Worker_TP1 pid=27102) WARNING 05-09 16:34:35 [base.py:151] Initializing KVConnectorBa...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: use ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: EngineCore_DP0 pid=27036) ERROR 05-09 16:34:35 [core.py:842] num_gpu_blocks, num_cpu_blocks, kv_cache_config = self._initialize_kv_caches( (EngineCore_DP0 pid=27036) ERROR 05-09 16:34:35 [core.py:842] File "/usr/local/l...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
