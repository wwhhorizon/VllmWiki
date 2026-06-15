# vllm-project/vllm#43596: [Bug]: DeepSeek-V4-Pro DP+EP with deepep_low_latency fails during startup: expected scalar type Long but found Int

| 字段 | 值 |
| --- | --- |
| Issue | [#43596](https://github.com/vllm-project/vllm/issues/43596) |
| 状态 | open |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;moe;quantization |
| 子分类 | cold_start |
| Operator 关键词 | cache;fp8;kernel;moe |
| 症状 | build_error;crash |
| 根因提示 | dtype;memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: DeepSeek-V4-Pro DP+EP with deepep_low_latency fails during startup: expected scalar type Long but found Int

### Issue 正文摘录

### Your current environment Model: DeepSeek-V4-Pro local checkpoint Hardware: 2 nodes × 8× NVIDIA H100 Network: InfiniBand between nodes Parallelism: Tensor parallel size: 8 Data parallel size: 2 Expert parallel: enabled Effective EP size: 16 KV cache dtype: fp8 Block size: 256 Max model length: 262144 Backend that triggers the issue: --all2all-backend deepep_low_latency ### 🐛 Describe the bug ```markdown DeepSeek-V4-Pro fails during engine startup when running with TP=8, DP=2, expert parallel enabled, and `--all2all-backend deepep_low_latency` on a 2-node H100 InfiniBand setup. The failure happens before serving any requests, during engine initialization / memory profiling / KV cache initialization. One worker process is terminated after TileLang kernels are compiled, and then the engine core fails with: ```text RuntimeError: Worker failed with error 'expected scalar type Long but found Int' RuntimeError: Engine core initialization failed. See root cause above. Reproduce script: export VLLM_ENGINE_READY_TIMEOUT_S=3600 export VLLM_MEMORY_PROFILER_ESTIMATE_CUDAGRAPHS=0 export CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7 export NCCL_IB_DISABLE=0 export GLOO_SOCKET_IFNAME=eth0 export VLLM_L...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: t Model: DeepSeek-V4-Pro local checkpoint Hardware: 2 nodes × 8× NVIDIA H100 Network: InfiniBand between nodes Parallelism: Tensor parallel size: 8 Data parallel size: 2 Expert parallel: enabled Effective EP size: 16 KV...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: [Bug]: DeepSeek-V4-Pro DP+EP with deepep_low_latency fails during startup: expected scalar type Long but found Int bug ### Your current environment Model: DeepSeek-V4-Pro local checkpoint Hardware: 2 nodes × 8× NVIDIA H...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: tialization. One worker process is terminated after TileLang kernels are compiled, and then the engine core fails with: ```text RuntimeError: Worker failed with error 'expected scalar type Long but found Int' RuntimeErr...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: parallel size: 2 Expert parallel: enabled Effective EP size: 16 KV cache dtype: fp8 Block size: 256 Max model length: 262144 Backend that triggers the issue: --all2all-backend deepep_low_latency ### 🐛 Describe the bug `...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 3: : 8 Data parallel size: 2 Expert parallel: enabled Effective EP size: 16 KV cache dtype: fp8 Block size: 256 Max model length: 262144 Backend that triggers the issue: --all2all-backend deepep_low_latency ### 🐛 Describe...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
