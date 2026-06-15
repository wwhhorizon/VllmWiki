# vllm-project/vllm#42632: [Feature]: Async cudaHostRegister in SimpleCPUOffloadConnector to unblock  startup

| 字段 | 值 |
| --- | --- |
| Issue | [#42632](https://github.com/vllm-project/vllm/issues/42632) |
| 状态 | open |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;distributed_parallel;frontend_api;quantization;scheduler_memory |
| 子分类 |  |
| Operator 关键词 | kernel |
| 症状 | crash;slowdown |
| 根因提示 | dtype;env_dependency;race_condition |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Feature]: Async cudaHostRegister in SimpleCPUOffloadConnector to unblock  startup

### Issue 正文摘录

## Motivation `KVConnectorBase_V1.register_kv_caches()` is called synchronously from the worker init path (`vllm/v1/worker/gpu_model_runner.py:7041`, inside `initialize_kv_cache`). For `SimpleCPUOffloadConnector`, the worker-side handler issues a single `cudaHostRegister` over the entire CPU KV region: ```python # vllm/v1/simple_kv_offload/worker.py:165-167 tensor = torch.zeros(cpu_shape, dtype=gpu_tensor.dtype, device="cpu") if pin_memory: pin_tensor(tensor) # -> cudaHostRegister, vllm/v1/simple_kv_offload/cuda_mem_ops.py:24 ``` **At TB-scale this is operationally fatal.** Modern offload deployments are sizing `cpu_bytes_to_use` into the multi-TB range to maximize prefix reuse. `cudaHostRegister` over that much memory is dominated by the kernel pinning every page (NVIDIA driver lock + RDMA cgroup accounting + page-table walks) and we have observed this single call running for many minutes on commodity hardware. For the entire pin window: - `register_kv_caches()` does not return. - Worker `initialize_cache` collective_rpc does not return → engine startup does not finish. - The HTTP server cannot accept *any* request, even short prompts that would never touch the offload tier. - `/...

## 现有链接修复摘要

#44127 [KV Offload] Async CPU memory pinning for SimpleCPUOffloadConnector

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: and `_ready_ranks: set[int]`. - `get_num_new_matched_tokens(...)` short-circuits to `(0, False)` while `not self._ready` — requests are served, just without prefix hits from CPU offload, until the gate opens. - `build_c...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: m/v1/simple_kv_offload/worker.py:165-167 tensor = torch.zeros(cpu_shape, dtype=gpu_tensor.dtype, device="cpu") if pin_memory: pin_tensor(tensor) # -> cudaHostRegister, vllm/v1/simple_kv_offload/cuda_mem_ops.py:24 ``` **...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: [Feature]: Async cudaHostRegister in SimpleCPUOffloadConnector to unblock startup ## Motivation `KVConnectorBase_V1.register_kv_caches()` is called synchronously from the worker init path (`vllm/v1/worker/gpu_model_runn...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ` is called synchronously from the worker init path (`vllm/v1/worker/gpu_model_runner.py:7041`, inside `initialize_kv_cache`). For `SimpleCPUOffloadConnector`, the worker-side handler issues a single `cudaHostRegister`...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: → engine startup does not finish. - The HTTP server cannot accept *any* request, even short prompts that would never touch the offload tier. - `/health` stays un-ready; autoscaler readiness probes time out. **This break...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#44127](https://github.com/vllm-project/vllm/pull/44127) | mentioned | 0.6 | [KV Offload] Async CPU memory pinning for SimpleCPUOffloadConnector | SimpleCPUOffloadConnector ## Purpose Implements request form issue #42632 `SimpleCPUOffloadConnector` pins its CPU buffer via cudaHostRegister on startup. This was done synchrono |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
