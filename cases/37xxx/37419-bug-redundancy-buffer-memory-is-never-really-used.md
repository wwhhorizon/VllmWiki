# vllm-project/vllm#37419: [Bug]: `redundancy_buffer_memory` is Never really used

| 字段 | 值 |
| --- | --- |
| Issue | [#37419](https://github.com/vllm-project/vllm/issues/37419) |
| 状态 | open |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: `redundancy_buffer_memory` is Never really used

### Issue 正文摘录

### Your current environment vLLM 0.17.1 ### 🐛 Describe the bug redundancy_buffer_memory (150 MiB) is never subtracted from KV cache allocation. The 150 MiB `redundancy_buffer_memory` in `gpu_worker.py` (introduced to leave headroom for memory profiling inaccuracy) is **not applied to the actual KV cache allocation**. It is only used to compute a suggested `--kv-cache-memory=` value in a `logger.debug()` message inside `compile_or_warm_up_model()`. The actual KV cache size is determined in `determine_available_memory()`: ```python # gpu_worker.py, determine_available_memory() self.available_kv_cache_memory_bytes = ( self.requested_memory - profile_result.non_kv_cache_memory - cudagraph_memory_estimate_applied # ← redundancy_buffer_memory is NOT subtracted here ) ``` While `redundancy_buffer_memory` is computed much later in a completely different method: ```python # gpu_worker.py, compile_or_warm_up_model() redundancy_buffer_memory = 150 * (1 --gpu-memory-utilization=0.95 --max-num-batched-tokens=65536 ``` Under load, if PyTorch caching allocator fragmentation exceeds the implicit margin from `1.0 - gpu_memory_utilization`, the process OOMs despite the code claiming to reserve 150...

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: ffer_memory` in `gpu_worker.py` (introduced to leave headroom for memory profiling inaccuracy) is **not applied to the actual KV cache allocation**. It is only used to compute a suggested `--kv-cache-memory=` value in a...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 3: be the bug redundancy_buffer_memory (150 MiB) is never subtracted from KV cache allocation. The 150 MiB `redundancy_buffer_memory` in `gpu_worker.py` (introduced to leave headroom for memory profiling inaccuracy) is **n...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ggested `--kv-cache-memory=` value in a `logger.debug()` message inside `compile_or_warm_up_model()`. The actual KV cache size is determined in `determine_available_memory()`: ```python # gpu_worker.py, determine_availa...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: self.requested_memory - profile_result.non_kv_cache_memory - cudagraph_memory_estimate_applied # ← redundancy_buffer_memory is NOT subtracted here ) ``` While `redundancy_buffer_memory` is computed much later in a compl...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: in `gpu_worker.py` (introduced to leave headroom for memory profiling inaccuracy) is **not applied to the actual KV cache allocation**. It is only used to compute a suggested `--kv-cache-memory=` value in a `logger.debu...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
