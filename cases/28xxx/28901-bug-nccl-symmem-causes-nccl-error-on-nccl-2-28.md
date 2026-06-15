# vllm-project/vllm#28901: [Bug]: nccl symmem causes nccl error on nccl 2.28+

| 字段 | 值 |
| --- | --- |
| Issue | [#28901](https://github.com/vllm-project/vllm/issues/28901) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;speculative_decoding |
| 子分类 |  |
| Operator 关键词 | cuda;kernel;operator;quantization;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: nccl symmem causes nccl error on nccl 2.28+

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Hi, I want to benchmark the nccl symmetric memory on recent nccl versions (>=2.28) using `benchmarks/kernels/benchmark_device_communicators.py`. But it causes cuda failure "[2025-11-17 19:04:11] 10-64-29-12:20967:20967 [1] dev_runtime.cc:591 NCCL WARN Cuda failure 'operation not permitted when stream is capturing'". The existing nccl version 2.27.5 in the vllm image works fine. I also evaluated with different nccl versions I built and found all nccl versions higher than 2.28 will cause this issue. | nccl | status | | ---- | ---- | | 2.27.5+cuda128 | ok | | 2.27.5+cuda129 | ok | | 2.28.3+cuda128 | failed | | 2.28.3+cuda129 | failed | | 2.28.7+cuda129 | failed | To reproduce: ``` NCCL_DEBUG=INFO NCCL_DEBUG_SUBSYS=TUNING,REG VLLM_USE_NCCL_SYMM_MEM=1 NCCL_NVLS_ENABLE=1 NCCL_CUMEM_ENABLE=1 torchrun --nproc_per_node=8 /home/vllm/vllms/vllm_upstream/benchmarks/kernels/benchmark_device_communicators.py # this works well, with existing nccl 2.27.5 VLLM_NCCL_SO_PATH=/home/vllm/nccl_2.28.3/build_cu129/lib/libnccl.so.2.28.3 VLLM_NCCL_INCLUDE_PATH=/home/vllm/nccl_2.28.3/build_cu129/include NCCL_DEBUG=INFO NCCL_DEBUG_SUBSYS=TUNING,REG VLLM_USE...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: he bug Hi, I want to benchmark the nccl symmetric memory on recent nccl versions (>=2.28) using `benchmarks/kernels/benchmark_device_communicators.py`. But it causes cuda failure "[2025-11-17 19:04:11] 10-64-29-12:20967...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: g ### Your current environment ### 🐛 Describe the bug Hi, I want to benchmark the nccl symmetric memory on recent nccl versions (>=2.28) using `benchmarks/kernels/benchmark_device_communicators.py`. But it causes cuda f...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ng `benchmarks/kernels/benchmark_device_communicators.py`. But it causes cuda failure "[2025-11-17 19:04:11] 10-64-29-12:20967:20967 [1] dev_runtime.cc:591 NCCL WARN Cuda failure 'operation not permitted when stream is...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: port;quantization;speculative_decoding cuda;kernel;operator;quantization;triton build_error env_dependency Your current environment
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: | failed | | 2.28.3+cuda129 | failed | | 2.28.7+cuda129 | failed | To reproduce: ``` NCCL_DEBUG=INFO NCCL_DEBUG_SUBSYS=TUNING,REG VLLM_USE_NCCL_SYMM_MEM=1 NCCL_NVLS_ENABLE=1 NCCL_CUMEM_ENABLE=1 torchrun --nproc_per_node...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
