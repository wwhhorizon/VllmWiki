# vllm-project/vllm#2300: A faster (tested only on V100) GEMM kernel dedicated for small batch-size

| 字段 | 值 |
| --- | --- |
| Issue | [#2300](https://github.com/vllm-project/vllm/issues/2300) |
| 状态 | closed |
| 标签 |  |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | distributed_parallel;gemm_linear |
| 子分类 | race_cond |
| Operator 关键词 | cuda;gemm;kernel |
| 症状 |  |
| 根因提示 | dtype;env_dependency;race_condition;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> A faster (tested only on V100) GEMM kernel dedicated for small batch-size

### Issue 正文摘录

Inspired by https://github.com/wangsiping97/FastGEMV, I took some time to implement a custom GEMM kernel. Compared to FastGEMV, it does not use shared memory and supports batch size larger than 1. - For small batch size (in the decoding stage), it seems to be faster than `F.linear` currently used in vllm, and should be easy to fuse with the custom allreduce kernels here (https://github.com/vllm-project/vllm/pull/2192). - Only tested on V100, torch=='2.0.1+cu117'. Not sure about the performance on other GPUs or other CUDA versions. Here is implementation (https://github.com/ZiyueHuang/vllm/commit/20e83b0a8b7518eb905cdc8b99fba32fc7d7c96d). Below is the reproducible script for performance benchmarks (including the correctness checking at the warmup stage). Performance report for different shapes of GEMM used in Qwen-7B, Qwen-14B, Qwen-14B (with tensor-parallel-size=2), where `oc` is the number of output channels and `ic` is the number of input channels, and the numbers are `time(custom-gemm) / time(F.linear)` (numbers smaller than 1 implies better performance of custom-gemm): | batch_size / (oc, ic) | (22016, 4096) | (4096, 11008) | (12288, 4096) | (4096, 4096) | | :----------------:...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: 2.0.1+cu117'. Not sure about the performance on other GPUs or other CUDA versions. Here is implementation (https://github.com/ZiyueHuang/vllm/commit/20e83b0a8b7518eb905cdc8b99fba32fc7d7c96d). Below is the reproducible s...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: A faster (tested only on V100) GEMM kernel dedicated for small batch-size Inspired by https://github.com/wangsiping97/FastGEMV, I took some time to implement a custom GEMM kernel. Compared to FastGEMV, it does not use s...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: A faster (tested only on V100) GEMM kernel dedicated for small batch-size Inspired by https://github.com/wangsiping97/FastGEMV, I took some time to implement a custom GEMM kernel. Compared to FastGEMV, it does not use s...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: uang/vllm/commit/20e83b0a8b7518eb905cdc8b99fba32fc7d7c96d). Below is the reproducible script for performance benchmarks (including the correctness checking at the warmup stage). Performance report for different shapes o...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: | 0.792 | correctness distributed_parallel;gemm_linear cuda;gemm;kernel dtype;env_dependency;race_condition;shape Inspired by https://github.com/wangsiping97/FastGEMV, I took some time to implement a custom GEMM kernel....

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
