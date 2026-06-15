# vllm-project/vllm#41961: [ROCm/MI325X] DeepSeek-V4-Flash: NotImplementedError: mul_cuda not implemented for Float8_e8m0fnu in normalize_e4m3fn_to_e4m3fnuz

| 字段 | 值 |
| --- | --- |
| Issue | [#41961](https://github.com/vllm-project/vllm/issues/41961) |
| 状态 | open |
| 标签 | rocm |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;hardware_porting;model_support;moe;quantization |
| 子分类 | env_compat |
| Operator 关键词 | fp8;kernel;moe;quantization |
| 症状 | crash |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [ROCm/MI325X] DeepSeek-V4-Flash: NotImplementedError: mul_cuda not implemented for Float8_e8m0fnu in normalize_e4m3fn_to_e4m3fnuz

### Issue 正文摘录

## Environment - **Hardware**: AMD MI325X × 8 (255.98 GiB HBM each) - **vLLM version**: 0.20.2rc1.dev90+g7a576e2c7 (rocm/vllm-dev:nightly, 2026-05-06) - **ROCm version**: as shipped in the nightly image - **Model**: deepseek-ai/DeepSeek-V4-Flash - **Config**: TP=8, EP=8, `--kv-cache-dtype fp8`, `--block-size 256` ## Bug When loading DeepSeek-V4-Flash on ROCm, weight loading fails in `normalize_e4m3fn_to_e4m3fnuz` because `Float8_e8m0fnu` (the MXFP4 scale format, `ue8m0`) has no `mul_cuda` kernel on HIP: ``` NotImplementedError: "mul_cuda" not implemented for 'Float8_e8m0fnu' ``` ## Root Cause In `vllm/model_executor/layers/quantization/utils/w8a8_utils.py`, `normalize_e4m3fn_to_e4m3fnuz` does: ```python weight_scale = weight_scale * 2.0 # line ~130 if input_scale is not None: input_scale = input_scale * 2.0 ``` When `weight_scale` dtype is `Float8_e8m0fnu` (used as the MXFP4 expert scale format), HIP/ROCm does not implement `mul_cuda` for that dtype, causing a crash. ## Fix Cast to `float32` before multiplying: ```python weight_scale = (weight_scale.float() * 2.0).to(weight_scale.dtype) if input_scale is not None: input_scale = (input_scale.float() * 2.0).to(input_scale.dtype) ```...

## 现有链接修复摘要

#40871 [New Model][ROCm] Add AMD support for DeepSeek V4 | #42247 [ROCm] Normalize fp8 scales through float32

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 7: l**: deepseek-ai/DeepSeek-V4-Flash - **Config**: TP=8, EP=8, `--kv-cache-dtype fp8`, `--block-size 256` ## Bug When loading DeepSeek-V4-Flash on ROCm, weight loading fails in `normalize_e4m3fn_to_e4m3fnuz` because `Floa...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: vironment - **Hardware**: AMD MI325X × 8 (255.98 GiB HBM each) - **vLLM version**: 0.20.2rc1.dev90+g7a576e2c7 (rocm/vllm-dev:nightly, 2026-05-06) - **ROCm version**: as shipped in the nightly image - **Model**: deepseek...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [ROCm/MI325X] DeepSeek-V4-Flash: NotImplementedError: mul_cuda not implemented for Float8_e8m0fnu in normalize_e4m3fn_to_e4m3fnuz rocm ## Environment - **Hardware**: AMD MI325X × 8 (255.98 GiB HBM each) - **vLLM version*
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: tly, 2026-05-06) - **ROCm version**: as shipped in the nightly image - **Model**: deepseek-ai/DeepSeek-V4-Flash - **Config**: TP=8, EP=8, `--kv-cache-dtype fp8`, `--block-size 256` ## Bug When loading DeepSeek-V4-Flash...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: i/DeepSeek-V4-Flash - **Config**: TP=8, EP=8, `--kv-cache-dtype fp8`, `--block-size 256` ## Bug When loading DeepSeek-V4-Flash on ROCm, weight loading fails in `normalize_e4m3fn_to_e4m3fnuz` because `Float8_e8m0fnu` (th...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#40871](https://github.com/vllm-project/vllm/pull/40871) | mentioned | 0.45 | [New Model][ROCm] Add AMD support for DeepSeek V4 | as an inline patch and confirmed to fix the issue. ## related - pr #40871 "add amd support for deepseek v4" (merged 2026-05-05) — introduced the rocm path but did not include this… |
| [#42247](https://github.com/vllm-project/vllm/pull/42247) | closes_keyword | 0.95 | [ROCm] Normalize fp8 scales through float32 | Fixes #41961. Summary: - Avoid direct multiplication on fp8 scale tensors while normalizing e4m3fn weights to e4m3fnuz. - Route fp8 scale doubling through float32 arithmetic, then |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
