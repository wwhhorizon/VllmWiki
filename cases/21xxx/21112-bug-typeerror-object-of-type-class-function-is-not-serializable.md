# vllm-project/vllm#21112: [Bug]: TypeError: Object of type <class 'function'> is not serializable

| 字段 | 值 |
| --- | --- |
| Issue | [#21112](https://github.com/vllm-project/vllm/issues/21112) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency;race_condition |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: TypeError: Object of type <class 'function'> is not serializable

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ``` ray.get(actor.collective_rpc.remote("update_weight_by_cpu_handles",args=(cpu_handles,tile))) [rank0]: File "/mnt/e/conda-py311-cu124-torch27/lib/python3.11/site-packages/ray/_private/auto_init_hook.py", line 22, in auto_init_wrapper [rank0]: return fn(*args, **kwargs) [rank0]: ^^^^^^^^^^^^^^^^^^^ [rank0]: File "/mnt/e/conda-py311-cu124-torch27/lib/python3.11/site-packages/ray/_private/client_mode_hook.py", line 104, in wrapper [rank0]: return func(*args, **kwargs) [rank0]: ^^^^^^^^^^^^^^^^^^^^^ [rank0]: File "/mnt/e/conda-py311-cu124-torch27/lib/python3.11/site-packages/ray/_private/worker.py", line 2849, in get [rank0]: values, debugger_breakpoint = worker.get_objects(object_refs, timeout=timeout) [rank0]: ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ [rank0]: File "/mnt/e/conda-py311-cu124-torch27/lib/python3.11/site-packages/ray/_private/worker.py", line 937, in get_objects [rank0]: raise value.as_instanceof_cause() [rank0]: ray.exceptions.RayTaskError(TypeError): ray::vLLM.collective_rpc() (pid=755, ip=172.31.202.67, actor_id=9f52d0baa7a6cc1d4a34e13805000000, repr= ) [rank0]: ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ [rank0...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ERIALIZATION=1 to allow fallback to pickle-based serialization. ``` ``` import os import ray import torch from ray.util.placement_group import placement_group from ray.util.scheduling_strategies import PlacementGroupSch...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: pe is not serializableSet VLLM_ALLOW_INSECURE_SERIALIZATION=1 to allow fallback to pickle-based serialization. ``` ``` import os import ray import torch from ray.util.placement_group import placement_group from ray.util...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: t[int], **kwargs): # Prevent Ray from manipulating the top-level CUDA_VISIBLE_DEVICES variable # so that vLLM can its own device placement inside the worker. os.environ.pop("CUDA_VISIBLE_DEVICES", None) # Each worker us...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: tGroupSchedulingStrategy from vllm import LLM class MyLLM(LLM): """Configure the vLLM worker for Ray placement group execution. The constructor sets environment variables that allow multiple vLLM workers to share a sing...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: t.py", line 595, in call_utility [rank0]: self._send_input(EngineCoreRequestType.UTILITY, [rank0]: File "/mnt/e/conda-py311-cu124-torch27/lib/python3.11/site-packages/vllm/v1/engine/core_client.py", line 581, in _send_i...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
