# vllm-project/vllm#36389: [Bug]: Multi-node MP backend with vllm v17 - inner dp world group is not initialized

| 字段 | 值 |
| --- | --- |
| Issue | [#36389](https://github.com/vllm-project/vllm/issues/36389) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | distributed_parallel |
| 子分类 | env_compat |
| Operator 关键词 | cuda;triton |
| 症状 | crash |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Multi-node MP backend with vllm v17 - inner dp world group is not initialized

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Running with pp >1 using the backend 'mp' results in an error `inner dp world group is not initialized` on every worker. ``` (Worker pid=35) ERROR 03-08 07:47:52 [multiproc_executor.py:800] WorkerProc failed to start. (Worker pid=35) ERROR 03-08 07:47:52 [multiproc_executor.py:800] Traceback (most recent call last): (Worker pid=35) ERROR 03-08 07:47:52 [multiproc_executor.py:800] File "/opt/vllm/vllm/v1/executor/multiproc_executor.py", line 771, in worker_main (Worker pid=35) ERROR 03-08 07:47:52 [multiproc_executor.py:800] worker = WorkerProc(*args, **kwargs) (Worker pid=35) ERROR 03-08 07:47:52 [multiproc_executor.py:800] ^^^^^^^^^^^^^^^^^^^^^^^^^^^ (Worker pid=35) ERROR 03-08 07:47:52 [multiproc_executor.py:800] File "/opt/vllm/vllm/tracing/otel.py", line 178, in sync_wrapper (Worker pid=35) ERROR 03-08 07:47:52 [multiproc_executor.py:800] return func(*args, **kwargs) (Worker pid=35) ERROR 03-08 07:47:52 [multiproc_executor.py:800] ^^^^^^^^^^^^^^^^^^^^^ (Worker pid=35) ERROR 03-08 07:47:52 [multiproc_executor.py:800] File "/opt/vllm/vllm/v1/executor/multiproc_executor.py", line 589, in __init__ (Worker pid=35) ERROR 03-08 07:4...

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: [Bug]: Multi-node MP backend with vllm v17 - inner dp world group is not initialized bug ### Your current environment ### 🐛 Describe the bug Running with pp >1 using the backend 'mp' results in an error `inner dp world...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ROR 03-08 07:47:52 [multiproc_executor.py:800] File "/opt/vllm/vllm/tracing/otel.py", line 178, in sync_wrapper (Worker pid=35) ERROR 03-08 07:47:52 [multiproc_executor.py:800] return func(*args, **kwargs) (Worker pid=3...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: oc_executor.py:800] self._init_message_queues(input_shm_handle, vllm_config) (Worker pid=35) ERROR 03-08 07:47:52 [multiproc_executor.py:800] File "/opt/vllm/vllm/v1/executor/multiproc_executor.py", line 527, in _init_m...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ERROR 03-08 07:47:52 [multiproc_executor.py:800] self._init_message_queues(input_shm_handle, vllm_config) (Worker pid=35) ERROR 03-08 07:47:52 [multiproc_executor.py:800] File "/opt/vllm/vllm/v1/executor/multiproc_execu...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
