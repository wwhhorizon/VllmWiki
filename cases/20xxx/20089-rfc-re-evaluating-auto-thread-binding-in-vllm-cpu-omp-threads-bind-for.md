# vllm-project/vllm#20089: [RFC]: Re-evaluating `auto` Thread Binding in `VLLM_CPU_OMP_THREADS_BIND` for SMT Architectures

| 字段 | 值 |
| --- | --- |
| Issue | [#20089](https://github.com/vllm-project/vllm/issues/20089) |
| 状态 | closed |
| 标签 | RFC |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Re-evaluating `auto` Thread Binding in `VLLM_CPU_OMP_THREADS_BIND` for SMT Architectures

### Issue 正文摘录

### Motivation. The current implementation of the `auto` ([PR #17930](https://github.com/vllm-project/vllm/pull/17930)) mode in `VLLM_CPU_OMP_THREADS_BIND` estimates thread binding based on the number of **physical cores per NUMA node**, using logic like: ```python psutil.cpu_count(logical=False) // numa_nodes ``` This approach ignores logical CPUs enabled via Simultaneous Multithreading (SMT), which is present in IBM POWER systems. They have 2,4 and 8 threads per core As a result, auto mode often ends up using only a fraction of available compute resources. For instance, on a 4-socket POWER10 system with 384 logical CPUs (96 per NUMA node), only 12 CPUs were being bound per worker — leading to 2–3x lower throughput compared to manually binding all logical CPUs. ```bash Architecture: ppc64le Byte Order: Little Endian CPU(s): 384 On-line CPU(s) list: 0-383 Model name: POWER10 (architected), altivec supported Model: 2.0 (pvr 0080 0200) Thread(s) per core: 8 Core(s) per socket: 12 Socket(s): 4 Virtualization features: Hypervisor vendor: pHyp Virtualization type: para Caches (sum of all): L1d: 3 MiB (96 instances) L1i: 4.5 MiB (96 instances) L2: 96 MiB (96 instances) L3: 384 MiB (96 i...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: Mitigation; Software count cache flush (hardware accelerated), Software link stack flush Srbds: Not affected Tsx async abort: Not affected ``` ```bash INFO 06-23 06:52:34 [cpu_worker.py:443] auto thread-binding list: 0,...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: [RFC]: Re-evaluating `auto` Thread Binding in `VLLM_CPU_OMP_THREADS_BIND` for SMT Architectures RFC ### Motivation. The current implementation of the `auto` ([PR #17930](https://github.com/vllm-project/vllm/pull/17930))...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: ,4,5,6,7,8,9,10,11 -- INFO 06-23 06:52:34 [cpu.py:69] Using Torch SDPA backend. INFO 06-23 06:52:34 [cpu_worker.py:226] OMP threads binding of Process 1755761: INFO 06-23 06:52:34 [cpu_worker.py:226] OMP tid: 1755761, c...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: : Re-evaluating `auto` Thread Binding in `VLLM_CPU_OMP_THREADS_BIND` for SMT Architectures RFC ### Motivation. The current implementation of the `auto` ([PR #17930](https://github.com/vllm-project/vllm/pull/17930)) mode...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: size_bytes(self) -> int: """Return the size in bytes of a single KV cache block. """ return CPUCacheEngine.get_cache_block_size( self.cache_config.block_size, self.cache_config.cache_dtype, self.model_config, self.paral...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
