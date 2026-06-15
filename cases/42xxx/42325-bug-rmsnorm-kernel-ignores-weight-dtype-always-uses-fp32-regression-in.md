# vllm-project/vllm#42325: [Bug]: RMSNorm kernel ignores weight dtype, always uses FP32 (regression in v0.20.0)

| 字段 | 值 |
| --- | --- |
| Issue | [#42325](https://github.com/vllm-project/vllm/issues/42325) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | activation_norm;attention_kv_cache;model_support;quantization |
| 子分类 | precision |
| Operator 关键词 | activation;attention;cuda;fp8;kernel;operator;quantization |
| 症状 | mismatch |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: RMSNorm kernel ignores weight dtype, always uses FP32 (regression in v0.20.0)

### Issue 正文摘录

### Your current environment This is a kernel implementation bug affecting all platforms with CUDA. Environment details are not relevant as the issue is in the source code itself (`csrc/layernorm_kernels.cu`). **Affected versions:** v0.20.0, v0.20.1, v0.20.2, and current main branch **Last working version:** v0.19.1 ### 🐛 Describe the bug ## Summary vLLM's RMSNorm CUDA kernel (`csrc/layernorm_kernels.cu`) ignores the weight dtype and always multiplies in FP32, violating the Python reference specification in `vllm/ir/ops/layernorm.py`. This regression was introduced in v0.20.0 (commit 4d51588e23, PR #40860) and affects all subsequent versions including the current main branch. ## Actual Behavior (v0.20.0+) The kernel casts weight to FP32 and performs multiplication in FP32: ```cpp // csrc/layernorm_kernels.cu (lines 77-82, v0.20.0+) #pragma unroll for (int j = 0; j (src1.val[j]); float w = static_cast (src2.val[j]); // ❌ Always FP32 dst.val[j] = static_cast (x * s_variance * w); } ``` ## Expected Behavior (Specification) The Python reference in `vllm/ir/ops/layernorm.py` specifies that multiplication should happen in **weight dtype**, not FP32: ```python # vllm/ir/ops/layernorm.py...

## 现有链接修复摘要

#42379 [Bugfix] Fix RMSNorm kernels to multiply in weight's native dtype

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 7: [Bug]: RMSNorm kernel ignores weight dtype, always uses FP32 (regression in v0.20.0) ### Your current environment This is a kernel implementation bug affecting all platforms with CUDA. Environment details are not releva...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 6: lication is actually **correct** because the fused kernel must match the precision of the unfused composite operation (RMSNorm → BF16 cast → FP8 quant). **However**, the same pattern was applied to the **regular RMSNorm...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: is in the source code itself (`csrc/layernorm_kernels.cu`). **Affected versions:** v0.20.0, v0.20.1, v0.20.2, and current main branch **Last working version:** v0.19.1 ### 🐛 Describe the bug ## Summary vLLM's RMSNorm CU...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: onment This is a kernel implementation bug affecting all platforms with CUDA. Environment details are not relevant as the issue is in the source code itself (`csrc/layernorm_kernels.cu`). **Affected versions:** v0.20.0,...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: [Bug]: RMSNorm kernel ignores weight dtype, always uses FP32 (regression in v0.20.0) ### Your current environment This is a kernel implementation bug affecting all platforms with CUDA. Environment details are not releva...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#42379](https://github.com/vllm-project/vllm/pull/42379) | closes_keyword | 0.95 | [Bugfix] Fix RMSNorm kernels to multiply in weight's native dtype | Fixes #42325 ## Changes **`csrc/layernorm_kernels.cu`** — 3 locations: - `rms_norm_kernel` vectorized path - `fused_add_rms_norm_kernel` FP16/BF16 optimised path - `fused_ |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
