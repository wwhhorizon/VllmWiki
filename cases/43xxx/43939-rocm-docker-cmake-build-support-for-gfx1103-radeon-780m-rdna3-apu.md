# vllm-project/vllm#43939: [ROCm]: Docker/CMake build support for gfx1103 (Radeon 780M / RDNA3 APU)

| 字段 | 值 |
| --- | --- |
| Issue | [#43939](https://github.com/vllm-project/vllm/issues/43939) |
| 状态 | open |
| 标签 | rocm |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;hardware_porting |
| 子分类 | install |
| Operator 关键词 | kernel |
| 症状 | build_error |
| 根因提示 |  |
| 硬件范围 | amd |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [ROCm]: Docker/CMake build support for gfx1103 (Radeon 780M / RDNA3 APU)

### Issue 正文摘录

### 🚀 The feature, motivation and pitch vLLM's ROCm Docker images (`docker/Dockerfile.rocm_base`) and the CMake build (`CMakeLists.txt` → `HIP_SUPPORTED_ARCHS`) do not currently support **gfx1103** (Radeon 780M and related RDNA3 APUs). Users on these integrated GPUs hit two distinct problems when trying to build/run vLLM in a container: 1. **CMake rejects the arch.** `gfx1103` is not listed in `HIP_SUPPORTED_ARCHS`, so the build fails early even when `PYTORCH_ROCM_ARCH=gfx1103` is set. 2. **rocBLAS `TensileLibrary.dat`** does not ship gfx1103 kernels in current ROCm releases — this is an upstream AMD limitation rather than a vLLM bug, but it affects the end-to-end experience and is worth documenting. A proposed patch for (1) — adding `gfx1103` to `HIP_SUPPORTED_ARCHS` plus the corresponding Docker build wiring — was drafted in #31062 (closing in favor of this tracking issue, since I can't validate gfx1103 end-to-end on my current hardware). The diff there can serve as a starting point for anyone with gfx1103 access who wants to pick this up. Prior testing and reproduction details were contributed by @yurikhan in the #31062 thread. ### Alternatives - Document gfx1103 as explicitly...

## 现有链接修复摘要

#31062 [ROCm][Docker] Add gfx1103 support to Docker builds

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [ROCm]: Docker/CMake build support for gfx1103 (Radeon 780M / RDNA3 APU) rocm ### 🚀 The feature, motivation and pitch vLLM's ROCm Docker images (`docker/Dockerfile.rocm_base`) and the CMake build (`CMakeLists.txt` → `HI...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [ROCm]: Docker/CMake build support for gfx1103 (Radeon 780M / RDNA3 APU) rocm ### 🚀 The feature, motivation and pitch vLLM's ROCm Docker images (`docker/Dockerfile.rocm_base`) and the CMake build (`CMakeLists.txt` → `HIP
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: o `HIP_SUPPORTED_ARCHS` plus the corresponding Docker build wiring — was drafted in #31062 (closing in favor of this tracking issue, since I can't validate gfx1103 end-to-end on my current hardware). The diff there can...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: g point for anyone with gfx1103 access who wants to pick this up. Prior testing and reproduction details were contributed by @yurikhan in the #31062 thread. ### Alternatives - Document gfx1103 as explicitly unsupported...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#31062](https://github.com/vllm-project/vllm/pull/31062) | mentioned | 0.45 | [ROCm][Docker] Add gfx1103 support to Docker builds | testing and reproduction details were contributed by @yurikhan in the #31062 thread. ### alternatives - document gfx1103 as explicitly unsupported until rocblas ships kernels for… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
