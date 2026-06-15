# vllm-project/vllm#4114: [Bug]: failed to run vllm on two nodes

| 字段 | 值 |
| --- | --- |
| Issue | [#4114](https://github.com/vllm-project/vllm/issues/4114) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
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

> [Bug]: failed to run vllm on two nodes

### Issue 正文摘录

### Your current environment I have two machines each with 4 V100, and they have different cuda driver versions. I init ray before launch vllm, and then the error is ``` (RayWorkerVllm pid=23078, ip=10.12.3.163) INFO 04-17 09:00:32 pynccl_utils.py:45] vLLM is using nccl==2.18.1 [31/357] (RayWorkerVllm pid=14289) Exception ignored in: (RayWorkerVllm pid=14289) Traceback (most recent call last): (RayWorkerVllm pid=14289) File "/usr/local/lib/python3.10/dist-packages/vllm/model_executor/parallel_utils/pynccl.py", line 264, in __del__ (RayWorkerVllm pid=14289) _c_ncclCommDestroy(self.comm) (RayWorkerVllm pid=14289) AttributeError: 'NCCLCommunicator' object has no attribute 'comm' (RayWorkerVllm pid=14289) ERROR 04-17 09:00:33 ray_utils.py:44] Error executing method init_device. This might cause deadlock in distributed execution. (RayWorkerVllm pid=14289) ERROR 04-17 09:00:33 ray_utils.py:44] Traceback (most recent call last): (RayWorkerVllm pid=14289) ERROR 04-17 09:00:33 ray_utils.py:44] File "/usr/local/lib/python3.10/dist-packages/vllm/engine/ray_utils.py", line 37, in execute_method (RayWorkerVllm pid=14289) ERROR 04-17 09:00:33 ray_utils.py:44] return executor(*args, **kwargs) (R...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: have two machines each with 4 V100, and they have different cuda driver versions. I init ray before launch vllm, and then the error is ``` (RayWorkerVllm pid=23078, ip=10.12.3.163) INFO 04-17 09:00:32 pynccl_utils.py:45...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: rkerVllm pid=14289) File "/usr/local/lib/python3.10/dist-packages/vllm/model_executor/parallel_utils/pynccl.py", line 264, in __del__ (RayWorkerVllm pid=14289) _c_ncclCommDestroy(self.comm) (RayWorkerVllm pid=14289) Att...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: failed to run vllm on two nodes bug;stale ### Your current environment I have two machines each with 4 V100, and they have different cuda driver versions. I init ray before launch vllm, and then the error is ```...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: m pid=14289) ERROR 04-17 09:00:33 ray_utils.py:44] torch.distributed.DistBackendError: NCCL error in: ../torch/csrc/distributed/c10d/ProcessGroupNCCL.cpp:1333, internal error - please report this iss ue to the NCCL deve...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: vironment I have two machines each with 4 V100, and they have different cuda driver versions. I init ray before launch vllm, and then the error is ``` (RayWorkerVllm pid=23078, ip=10.12.3.163) INFO 04-17 09:00:32 pynccl...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
