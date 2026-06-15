# vllm-project/vllm#7772: [Bug]: Connection closed by peer.

| 字段 | 值 |
| --- | --- |
| Issue | [#7772](https://github.com/vllm-project/vllm/issues/7772) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Connection closed by peer.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug 2024-08-22 13:50:25 ERROR 200507 [worker_base.py:148] Error executing method start_worker_execution_loop. This might cause deadlock in distributed execution. 2024-08-22 13:50:25 ERROR 200507 [worker_base.py:148] Traceback (most recent call last): 2024-08-22 13:50:25 ERROR 200507 [worker_base.py:148] File "/opt/conda/lib/python3.8/site-packages/vllm/worker/worker_base.py", line 140, in execute_method 2024-08-22 13:50:25 ERROR 200507 [worker_base.py:148] return executor(*args, **kwargs) 2024-08-22 13:50:25 ERROR 200507 [worker_base.py:148] File "/opt/conda/lib/python3.8/site-packages/torch/utils/_contextlib.py", line 115, in decorate_context 2024-08-22 13:50:25 ERROR 200507 [worker_base.py:148] return func(*args, **kwargs) 2024-08-22 13:50:25 ERROR 200507 [worker_base.py:148] File "/opt/conda/lib/python3.8/site-packages/vllm/spec_decode/spec_decode_worker.py", line 313, in start_worker_execution_loop 2024-08-22 13:50:25 ERROR 200507 [worker_base.py:148] while self._run_non_driver_rank(): 2024-08-22 13:50:25 ERROR 200507 [worker_base.py:148] File "/opt/conda/lib/python3.8/site-packages/vllm/spec_decode/spec_decode_worker.py", line 3...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: oo/gloo/transport/tcp/pair.cc:534] Connection closed by peer development ci_build;distributed_parallel;frontend_api;hardware_porting;model_support cuda;operator;triton build_error;crash env_dependency Your current envir...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: Connection closed by peer. bug;stale ### Your current environment ### 🐛 Describe the bug 2024-08-22 13:50:25 ERROR 200507 [worker_base.py:148] Error executing method start_worker_execution_loop. This might cause...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: buted_parallel;frontend_api;hardware_porting;model_support cuda;operator;triton build_error;crash env_dependency Your current environment
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: i_build;distributed_parallel;frontend_api;hardware_porting;model_support cuda;operator;triton build_error;crash env_dependency Your current environment
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: 07 [worker_base.py:148] torch.distributed.broadcast_object_list(recv_metadata_list, 2024-08-22 13:50:25 ERROR 200507 [worker_base.py:148] File "/opt/conda/lib/python3.8/site-packages/torch/distributed/c10d_logger.py", l...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
