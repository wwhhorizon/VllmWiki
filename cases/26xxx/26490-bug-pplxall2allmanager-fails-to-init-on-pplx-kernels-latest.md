# vllm-project/vllm#26490: [Bug]:  `PPLXAll2AllManager` fails to init on pplx-kernels latest

| 字段 | 值 |
| --- | --- |
| Issue | [#26490](https://github.com/vllm-project/vllm/issues/26490) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]:  `PPLXAll2AllManager` fails to init on pplx-kernels latest

### Issue 正文摘录

### 🐛 Describe the bug The pplx-kernels all2all backend fails to initialize when using the latest pplx-kernels on main due to an interface change following the nvshmem4py integration: https://github.com/vllm-project/vllm/blob/main/vllm/distributed/device_communicators/all2all.py#L158-L162 Last working commit: https://github.com/perplexityai/pplx-kernels/blob/12cecfda252e4e646417ac263d96e994d476ee5d/src/pplx_kernels/nvshmem.py ``` (APIServer pid=317) (EngineCore_DP7 pid=606) self._target(*self._args, **self._kwargs) (APIServer pid=317) (EngineCore_DP7 pid=606) File "/opt/vllm-source/vllm/v1/engine/core.py", line 712, in run_engine_core (APIServer pid=317) (EngineCore_DP7 pid=606) raise e (APIServer pid=317) (EngineCore_DP7 pid=606) File "/opt/vllm-source/vllm/v1/engine/core.py", line 695, in run_engine_core (APIServer pid=317) (EngineCore_DP7 pid=606) engine_core = DPEngineCoreProc(*args, **kwargs) (APIServer pid=317) (EngineCore_DP7 pid=606) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ (APIServer pid=317) (EngineCore_DP7 pid=606) File "/opt/vllm-source/vllm/v1/engine/core.py", line 965, in __init__ (APIServer pid=317) (EngineCore_DP7 pid=606) super().__init__(vllm_config, local_client, hands...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: pid=606) File "/opt/vllm-source/vllm/distributed/device_communicators/cuda_communicator.py", line 107, in __init__ (APIServer pid=317) (EngineCore_DP7 pid=606) self.all2all_manager = PPLXAll2AllManager(self.cpu_group) (...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: _ (APIServer pid=317) (EngineCore_DP7 pid=606) super().__init__(vllm_config, local_client, handshake_address, (APIServer pid=317) (EngineCore_DP7 pid=606) File "/opt/vllm-source/vllm/v1/engine/core.py", line 498, in __i...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ernels latest bug;stale ### 🐛 Describe the bug The pplx-kernels all2all backend fails to initialize when using the latest pplx-kernels on main due to an interface change following the nvshmem4py integration: https://git...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: PIServer pid=317) (EngineCore_DP7 pid=606) from pplx_kernels.nvshmem import (nvshmem_alloc_empty_unique_id, (APIServer pid=317) (EngineCore_DP7 pid=606) ImportError: cannot import name 'nvshmem_alloc_empty_unique_id' fr...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: `PPLXAll2AllManager` fails to init on pplx-kernels latest bug;stale ### 🐛 Describe the bug The pplx-kernels all2all backend fails to initialize when using the latest pplx-kernels on main due to an interface chang...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
