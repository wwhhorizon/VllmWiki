# vllm-project/vllm#14397: [Bug]: `triton_scaled_mm` never used on ROCm

| 字段 | 值 |
| --- | --- |
| Issue | [#14397](https://github.com/vllm-project/vllm/issues/14397) |
| 状态 | closed |
| 标签 | bug;good first issue;unstale |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;kernel;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: `triton_scaled_mm` never used on ROCm

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I found an issue with vLLM and block fp8 linear, where the ROCm platform is incorrectly using a cutlass execution path. Because the cutlass path is always disabled on ROCm, this kernel is never reached, and instead we fall back on either `w8a8_block_fp8_matmul` or `torch.scaled_mm`. The way we got there: - @rasmith added the triton kernel `triton_scaled_mm` into `custom_ops.cutlass_scaled_mm` (not the right place for it in my opinion) in [127c074](https://github.com/vllm-project/vllm/commit/127c07480ecea15e4c2990820c457807ff78a057) - @hongxiayang added DeepSeek support, using the cutlass path where cutlass_block_fp8_supported was True by default in [c36ac98](https://github.com/vllm-project/vllm/commit/c36ac98d0118537ec5f3f405a68311a10f9b59a5) - @LucasWilkinson fixed the default of `cutlass_block_fp8_supported` param to `cutlass_block_fp8_supported()` which always returns False on ROCm in [76abd0c](https://github.com/vllm-project/vllm/commit/76abd0c88143419826bfc13d2cd29669d0fdfa1b). The effect of this is that triton_scaled_mm is currently never used. I think the path forward is to move `triton_scaled_mm` out of the `custom_ops.cu...

## 现有链接修复摘要

#26668 [ROCm] Enable Triton ScaledMM fallback + kernel selection fix

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: [Bug]: `triton_scaled_mm` never used on ROCm bug;good first issue;unstale ### Your current environment ### 🐛 Describe the bug I found an issue with vLLM and block fp8 linear, where the ROCm platform is incorrectly using...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [Bug]: `triton_scaled_mm` never used on ROCm bug;good first issue;unstale ### Your current environment ### 🐛 Describe the bug I found an issue with vLLM and block fp8 linear, where the ROCm platform is incorrectly using...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: [Bug]: `triton_scaled_mm` never used on ROCm bug;good first issue;unstale ### Your current environment ### 🐛 Describe the bug I found an issue with vLLM and block fp8 linear, where the ROCm platform is incorrectly using...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding cuda;fp8;kernel;operator;sampling;triton bui...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: t environment ### 🐛 Describe the bug I found an issue with vLLM and block fp8 linear, where the ROCm platform is incorrectly using a cutlass execution path. Because the cutlass path is always disabled on ROCm, this kern...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#26668](https://github.com/vllm-project/vllm/pull/26668) | closes_keyword | 0.95 | [ROCm] Enable Triton ScaledMM fallback + kernel selection fix | Fixes #14397 — <code inline="">triton_scaled_mm</code> was never used on ROCm due to missing dispatch and checks.<br> This PR:</p> <ul> <li> <p>Enables <strong>Triton fallback</str |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
