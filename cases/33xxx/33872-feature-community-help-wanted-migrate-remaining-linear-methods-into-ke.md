# vllm-project/vllm#33872: [Feature]: Community Help Wanted: Migrate Remaining Linear Methods into Kernel Abstraction

| 字段 | 值 |
| --- | --- |
| Issue | [#33872](https://github.com/vllm-project/vllm/issues/33872) |
| 状态 | open |
| 标签 | feature request;stale |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;frontend_api;gemm_linear;hardware_porting;model_support;quantization |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;gemm;kernel;operator;quantization;triton |
| 症状 | build_error |
| 根因提示 | dtype;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Feature]: Community Help Wanted: Migrate Remaining Linear Methods into Kernel Abstraction

### Issue 正文摘录

### 🚀 The feature, motivation and pitch This issue is a continuation of “[Refactor] Make FP8 Linear Ops use kernel abstraction” #27814, which moved the FP8 scaled-mm linear path onto the `ScaledMMLinearKernelinterface` and improved consistency across FP8 execution paths. The next step is to extend that same kernel-abstraction approach to the remaining linear Methods/schemes by routing them through the kernel abstraction inside their existing `LinearMethod` implementations so that (once everything is consistently kernelized) we can easily remove the per-format `LinearMethod` layer entirely as planned by #33314. **Important design note (MP kernel refactor)** PR #32929 introduces `MarlinFP8ScaledMMLinearKernel`, which is effectively a mixed-precision (FP8 W8A16) kernel but does not inherit from `MPLinearKernel`; instead it uses a dedicated, specialized FP8 kernel interface for that path. This is done because `MPLinearKernel` is growing increasingly bloated, which makes it harder to maintain and to integrate new kernels cleanly. We want to apply the same principle to the existing mixed-precision kernel implementations: split `MPLinearKernel` into smaller, more specialized kernel base...

## 现有链接修复摘要

#27814 [Refactor] Make FP8 Linear Ops use kernel abstraction | #32929 [FP8]add FP8 WoQ kernel abstraction. | #33407 [W8A8 Block Linear Refactor][2/N] Make FP8 Block Linear Ops use kernel abstraction.

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 7: , motivation and pitch This issue is a continuation of “[Refactor] Make FP8 Linear Ops use kernel abstraction” #27814, which moved the FP8 scaled-mm linear path onto the `ScaledMMLinearKernelinterface` and improved cons...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 5: e kernel-abstraction approach to the remaining linear Methods/schemes by routing them through the kernel abstraction inside their existing `LinearMethod` implementations so that (once everything is consistently kerneliz...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: ting mixed-precision kernel implementations: split `MPLinearKernel` into smaller, more specialized kernel base classes(FP8W8A8, Int8W4A8, etc…) then move current MP kernels onto those specialized bases rather than expan...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: ve the per-format `LinearMethod` layer entirely as planned by #33314. **Important design note (MP kernel refactor)** PR #32929 introduces `MarlinFP8ScaledMMLinearKernel`, which is effectively a mixed-precision (FP8 W8A1...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: CompressedTensorsW8A8Fp8 | FP8ScaledMMLinearKernel + W8A8BlockFp8LinearOp | Partial | Keep scaled-mm on FP8ScaledMMLinearKernel; route block-scaled through the kernel abstraction. vllm​

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#27814](https://github.com/vllm-project/vllm/pull/27814) | mentioned | 0.45 | [Refactor] Make FP8 Linear Ops use kernel abstraction | ntinuation of “[refactor] make fp8 linear ops use kernel abstraction” #27814, which moved the fp8 scaled-mm linear path onto the `scaledmmlinearkernelinterface` and improved consi… |
| [#32929](https://github.com/vllm-project/vllm/pull/32929) | mentioned | 0.45 | [FP8]add FP8 WoQ kernel abstraction. | t `mplinearkernel` into specialized kernel base classes (following pr #32929’s approach where marlin fp8 w8a16 is a dedicated fp8 kernel interface rather than inheriting `mplinear… |
| [#33407](https://github.com/vllm-project/vllm/pull/33407) | mentioned | 0.45 | [W8A8 Block Linear Refactor][2/N] Make FP8 Block Linear Ops use kernel abstraction. | 8blockfp8linearop` through the kernel abstraction (block-scaled fp8). #33407 - [ ] route `awqlinearmethod` through the kernel abstraction. - [ ] route `bitsandbyteslinearmethod` t… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
