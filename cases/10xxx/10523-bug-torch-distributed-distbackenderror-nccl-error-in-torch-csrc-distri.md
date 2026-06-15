# vllm-project/vllm#10523: [Bug]: torch.distributed.DistBackendError: NCCL error in: ../torch/csrc/distributed/c10d/ProcessGroupNCCL.cpp:1333, unhandled system error (run with NCCL_DEBUG=INFO for details), NCCL version 2.18.1

| 字段 | 值 |
| --- | --- |
| Issue | [#10523](https://github.com/vllm-project/vllm/issues/10523) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 |  |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: torch.distributed.DistBackendError: NCCL error in: ../torch/csrc/distributed/c10d/ProcessGroupNCCL.cpp:1333, unhandled system error (run with NCCL_DEBUG=INFO for details), NCCL version 2.18.1

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug ``` NCCL version 2.18.1+cuda12.1 (RayWorkerWrapper pid=111470) PID 111470 ERROR 11-21 06:56:55.481 worker_base.py:149]Thread MainThread: Error executing method init_device. This might cause deadlock in distributed execution. (RayWorkerWrapper pid=111470) PID 111470 ERROR 11-21 06:56:55.481 worker_base.py:149]Thread MainThread: Traceback (most recent call last): (RayWorkerWrapper pid=111470) PID 111470 ERROR 11-21 06:56:55.481 worker_base.py:149]Thread MainThread: File "/function/vllm/worker/worker_base.py", line 141, in execute_method (RayWorkerWrapper pid=111470) PID 111470 ERROR 11-21 06:56:55.481 worker_base.py:149]Thread MainThread: return executor(*args, **kwargs) (RayWorkerWrapper pid=111470) PID 111470 ERROR 11-21 06:56:55.481 worker_base.py:149]Thread MainThread: File "/function/vllm/worker/worker.py", line 122, in init_device (RayWorkerWrapper pid=111470) PID 111470 ERROR 11-21 06:56:55.481 worker_base.py:149]Thread MainThread: init_worker_distributed_environment(self.parallel_config, self.rank, (RayWorkerWrapper pid=111470) PID 111470 ERROR 11-21 06:56:55.481 worker_base.py:149]Thread...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: 333, unhandled system error (run with NCCL_DEBUG=INFO for details), NCCL version 2.18.1 bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug ``` NCCL version 2.18.1+cuda12.1...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: em error (run with NCCL_DEBUG=INFO for details), NCCL version 2.18.1 bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug ``` NCCL version 2.18.1+cuda12.1 (RayWorkerWrapper p...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: [Bug]: torch.distributed.DistBackendError: NCCL error in: ../torch/csrc/distributed/c10d/ProcessGroupNCCL.cpp:1333, unhandled system error (run with NCCL_DEBUG=INFO for details), NCCL version 2.18.1 bug;stale ### Your c...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ut Dumps _No response_ ### 🐛 Describe the bug ``` NCCL version 2.18.1+cuda12.1 (RayWorkerWrapper pid=111470) PID 111470 ERROR 11-21 06:56:55.481 worker_base.py:149]Thread MainThread: Error executing method init_device....
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ils), NCCL version 2.18.1 bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug ``` NCCL version 2.18.1+cuda12.1 (RayWorkerWrapper pid=111470) PID 111470 ERROR 11-21 06:56:55....

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
