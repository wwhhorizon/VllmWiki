# vllm-project/vllm#19284: [Feature]: Generic HIP compiler flags support for cross-project compatibility

| 字段 | 值 |
| --- | --- |
| Issue | [#19284](https://github.com/vllm-project/vllm/issues/19284) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Generic HIP compiler flags support for cross-project compatibility

### Issue 正文摘录

### 🚀 The feature, motivation and pitch This feature request proposes adding generic support for additional HIP compiler flags in vLLM's CMake build system, following the same pattern used in ROCm/PyTorch projects. Motivation: Currently, vLLM users working with ROCm/HIP builds may need to pass additional compiler flags (such as --offload-compress for memory optimization, or other project-specific flags). However, there's no standardized way to inject these flags into the build process. This creates inconsistency across ROCm projects and makes it difficult for users to maintain unified build configurations. **The Problem:** Users cannot easily pass additional HIP compiler flags to vLLM builds No standardized mechanism exists for HIP flag injection across ROCm ecosystem projects Build configurations cannot be easily shared between vLLM and other ROCm projects like PyTorch Proposed Solution: Implement support for the HIP_EXTRA_FLAGS variable (both as CMake variable and environment variable) in vLLM's build system, following the same pattern used in ROCm/PyTorch's Dependencies.cmake. ### Alternatives - Project-specific variables: Create vLLM-specific variables like VLLM_HIP_EXTRA_FLAG...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [Feature]: Generic HIP compiler flags support for cross-project compatibility feature request ### 🚀 The feature, motivation and pitch This feature request proposes adding generic support for additional HIP compiler flag...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [Feature]: Generic HIP compiler flags support for cross-project compatibility feature request ### 🚀 The feature, motivation and pitch This feature request proposes adding generic support for additional HIP compiler flag...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: th ROCm/HIP builds may need to pass additional compiler flags (such as --offload-compress for memory optimization, or other project-specific flags). However, there's no standardized way to inject these flags into the bu...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ROCm projects and makes it difficult for users to maintain unified build configurations. **The Problem:** Users cannot easily pass additional HIP compiler flags to vLLM builds No standardized mechanism exists for HIP fl...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: neric HIP compiler flags support for cross-project compatibility feature request ### 🚀 The feature, motivation and pitch This feature request proposes adding generic support for additional HIP compiler flags in vLLM's C...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
