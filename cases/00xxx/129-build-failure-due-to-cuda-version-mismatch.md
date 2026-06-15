# vllm-project/vllm#129: Build failure due to CUDA version mismatch

| 字段 | 值 |
| --- | --- |
| Issue | [#129](https://github.com/vllm-project/vllm/issues/129) |
| 状态 | closed |
| 标签 | installation |
| 评论 | 25; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build |
| 子分类 | wrong_output |
| Operator 关键词 | cuda |
| 症状 | build_error;mismatch |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> Build failure due to CUDA version mismatch

### Issue 正文摘录

I failed to build the system with the latest NVIDIA PyTorch docker image. The reason is PyTorch installed by `pip` is built with CUDA 11.7 while the container uses CUDA 12.1. ``` RuntimeError: The detected CUDA version (12.1) mismatches the version that was used to compile PyTorch (11.7). Please make sure to use the same CUDA versions. ```

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: Build failure due to CUDA version mismatch installation I failed to build the system with the latest NVIDIA PyTorch docker image. The reason is PyTorch installed by `pip` is built with CUDA 11.7 while the container uses
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: Build failure due to CUDA version mismatch installation I failed to build the system with the latest NVIDIA PyTorch docker image. The reason is PyTorch installed by `pip` is built with CUDA 11.7 while the container uses...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: Build failure due to CUDA version mismatch installation I failed to build the system with the latest NVIDIA PyTorch docker image. The reason is PyTorch installed by `pip` is built with CUDA 11.7 while the container uses...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: DA version mismatch installation I failed to build the system with the latest NVIDIA PyTorch docker image. The reason is PyTorch installed by `pip` is built with CUDA 11.7 while the container uses CUDA 12.1. ``` Runtime...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
