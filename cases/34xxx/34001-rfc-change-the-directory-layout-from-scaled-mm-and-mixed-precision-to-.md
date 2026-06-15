# vllm-project/vllm#34001: [RFC] Change the directory layout from `scaled_mm/` and `mixed_precision/` to backend-first .

| 字段 | 值 |
| --- | --- |
| Issue | [#34001](https://github.com/vllm-project/vllm/issues/34001) |
| 状态 | open |
| 标签 | stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;gemm_linear;hardware_porting;quantization |
| 子分类 |  |
| Operator 关键词 | cuda;gemm;kernel;quantization;triton |
| 症状 | build_error |
| 根因提示 | memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [RFC] Change the directory layout from `scaled_mm/` and `mixed_precision/` to backend-first .

### Issue 正文摘录

After implementing https://github.com/vllm-project/vllm/issues/33872 Before starting to snowball the Kernel Abstraction, we should align the semantics of the directory to make sure they are easy to follow and use. We would like to propose the following directory structure to organize the kernel abstraction of linear gemm based on the following pattern: 1. based on providers if the kernels are imported from third party library 2. if the kernels are implemented in `vllm/csrc`, they are organized based on their implementations. 3. CPU kernels in `vllm/csrc` is a special case, it is cpp, so we just leave it as `cpu`. (Updated) Following the comment in https://github.com/vllm-project/vllm/issues/34001#issuecomment-3861239107, the first step we first reorganize the `scaled_mm` first. ``` vllm/ └── vllm/ └── model_executor/ └── kernels/ # Kernel Abstraction RFC https://github.com/vllm-project/vllm/issues/33872 ├── __init__.py └── linear/ ├── __init__.py ├── mixed_precision/ ├── cutlass/ # Cutlass kernels that are build in tree within vLLM | | # Given that marlin and machete are also Cutlass kernels, | | # we plan to list time under cutlass implementation folder │ │ # marlin (marlin A100)...

## 现有链接修复摘要

#41883 [Perf][Refactor] Port W16A16 Linear Kernels to Kernel Abstraction

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: cutlass implementation folder │ │ # marlin (marlin A100) Cutlass kernels that are build in tree within vLLM │ │ # machete (machete H100) Cutlass kernels that are build in tree within vLLM │ ├── __init__.py │ ├── w
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: Change the directory layout from `scaled_mm/` and `mixed_precision/` to backend-first . stale After implementing https://github.com/vllm-project/vllm/issues/33872 Before starting to snowball the Kernel Abstraction, we s...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [RFC] Change the directory layout from `scaled_mm/` and `mixed_precision/` to backend-first . stale After implementing https://github.com/vllm-project/vllm/issues/33872 Before starting to snowball the Kernel Abstraction...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: [RFC] Change the directory layout from `scaled_mm/` and `mixed_precision/` to backend-first . stale After implementing https://github.com/vllm-project/vllm/issues/33872 Before starting to snowball the Kernel Abstraction...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: [RFC] Change the directory layout from `scaled_mm/` and `mixed_precision/` to backend-first . stale After implementing https://github.com/vllm-project/vllm/issues/33872 Before starting to snowball the Kernel Abstraction...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#41883](https://github.com/vllm-project/vllm/pull/41883) | mentioned | 0.6 | [Perf][Refactor] Port W16A16 Linear Kernels to Kernel Abstraction | near kernel abstraction directory. Following the design mentioned in #34001 The new code lives under `vllm/model_executor/kernels/linear/`. Abstract base classes are in `base/comm… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
