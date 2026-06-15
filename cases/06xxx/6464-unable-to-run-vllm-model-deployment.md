# vllm-project/vllm#6464: unable to run vllm model deployment 

| 字段 | 值 |
| --- | --- |
| Issue | [#6464](https://github.com/vllm-project/vllm/issues/6464) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 19; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> unable to run vllm model deployment 

### Issue 正文摘录

### Your current environment Failed to import from vllm._C with ImportError("/usr/lib/x86_64-linux-gnu/libc.so.6: version `GLIBC_2.32' not found (required by /tmp/.conda/envs/vllm_env/lib/python3.10/site-packages/vllm/_C.abi3.so)") INFO 07-16 09:29:50 custom_cache_manager.py:17] Setting Triton cache manager to: vllm.triton_utils.custom_cache_manager:CustomCacheManager (VllmWorkerProcess pid=658) INFO 07-16 09:29:52 multiproc_worker_utils.py:215] Worker ready; awaiting tasks (VllmWorkerProcess pid=656) INFO 07-16 09:29:52 multiproc_worker_utils.py:215] Worker ready; awaiting tasks (VllmWorkerProcess pid=657) INFO 07-16 09:29:53 multiproc_worker_utils.py:215] Worker ready; awaiting tasks INFO 07-16 09:29:53 utils.py:737] Found nccl from library libnccl.so.2 (VllmWorkerProcess pid=656) INFO 07-16 09:29:53 utils.py:737] Found nccl from library libnccl.so.2 (VllmWorkerProcess pid=658) INFO 07-16 09:29:53 utils.py:737] Found nccl from library libnccl.so.2 INFO 07-16 09:29:53 pynccl.py:63] vLLM is using nccl==2.20.5 (VllmWorkerProcess pid=657) INFO 07-16 09:29:53 utils.py:737] Found nccl from library libnccl.so.2 (VllmWorkerProcess pid=656) INFO 07-16 09:29:53 pynccl.py:63] vLLM is using...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: vllm model deployment bug;stale ### Your current environment Failed to import from vllm._C with ImportError("/usr/lib/x86_64-linux-gnu/libc.so.6: version `GLIBC_2.32' not found (required by /tmp/.conda/envs/vllm_env/lib...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: worker VllmWorkerProcess while processing method determine_num_available_blocks: '_OpNamespace' '_C' object has no attribute 'rms_norm', Traceback (most recent call last): (VllmWorkerProcess pid=656) (VllmWorkerProcess...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: unable to run vllm model deployment bug;stale ### Your current environment Failed to import from vllm._C with ImportError("/usr/lib/x86_64-linux-gnu/libc.so.6: version `GLIBC_2.32' not found (required by /tmp/.conda/env...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: m/_C.abi3.so)") INFO 07-16 09:29:50 custom_cache_manager.py:17] Setting Triton cache manager to: vllm.triton_utils.custom_cache_manager:CustomCacheManager (VllmWorkerProcess pid=658) INFO 07-16 09:29:52 multiproc_worker...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: e-packages/vllm/model_executor/layers/layernorm.py", line 62, in forward_cuda ERROR 07-16 09:31:45 multiproc_worker_utils.py:226] return self._forward_method(*args, **kwargs) (VllmWorkerProcess pid=658) ERROR 07-16 09:3...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
