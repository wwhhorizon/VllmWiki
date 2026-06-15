# vllm-project/vllm#19882: Issue 1: Incorrect comparison with MAIN_CUDA_VERSION for CPU target

| 字段 | 值 |
| --- | --- |
| Issue | [#19882](https://github.com/vllm-project/vllm/issues/19882) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;hardware_porting |
| 子分类 |  |
| Operator 关键词 | cuda |
| 症状 | mismatch |
| 根因提示 |  |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> Issue 1: Incorrect comparison with MAIN_CUDA_VERSION for CPU target

### Issue 正文摘录

``` The `get_vllm_version` function compares device-specific versions (CUDA, ROCm, etc.) against `MAIN_CUDA_VERSION` regardless of the target device. This comparison is irrelevant and potentially misleading when the target device is CPU, as it could lead to the inclusion of `sep` (e.g., "+") in the version string even when no CUDA-related components are involved. The condition `gaudi_sw_version != MAIN_CUDA_VERSION` should only be evaluated for specific devices, not for general cases. ```

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: Issue 1: Incorrect comparison with MAIN_CUDA_VERSION for CPU target stale ``` The `get_vllm_version` function compares device-specific versions (CUDA, ROCm, etc.) against `MAIN_CUDA_VERSION` regardless of the target dev...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: Issue 1: Incorrect comparison with MAIN_CUDA_VERSION for CPU target stale ``` The `get_vllm_version` function compares device-specific versions (CUDA, ROCm, etc.) against `MAIN_CUDA_VERSION` regardless of the target dev...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: s, not for general cases. ``` correctness ci_build;hardware_porting cuda mismatch ```
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: Issue 1: Incorrect comparison with MAIN_CUDA_VERSION for CPU target stale ``` The `get_vllm_version` function compares device-specific versions (CUDA, ROCm, etc.) against `MAIN_CUDA_VERSION` regardless of the target dev...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ed. The condition `gaudi_sw_version != MAIN_CUDA_VERSION` should only be evaluated for specific devices, not for general cases. ``` correctness ci_build;hardware_porting cuda mismatch ```

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
