# vllm-project/vllm#38006: [Feature]: Implement `TRITON_MLA_SPARSE` backend for sm80/120/121 support of Sparse MLA

| 字段 | 值 |
| --- | --- |
| Issue | [#38006](https://github.com/vllm-project/vllm/issues/38006) |
| 状态 | open |
| 标签 | feature request |
| 评论 | 13; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization |
| 子分类 | kernel_eff |
| Operator 关键词 | attention;cuda;fp8;moe;operator;quantization;triton |
| 症状 | build_error |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Feature]: Implement `TRITON_MLA_SPARSE` backend for sm80/120/121 support of Sparse MLA

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Follow-up to https://github.com/vllm-project/vllm/issues/35021. Relevant PR to implementation (probably need to re-add when `TRITON_MLA_SPARSE` is implemented): https://github.com/vllm-project/vllm/pull/37968, https://github.com/vllm-project/vllm/pull/35271, https://github.com/vllm-project/vllm/pull/38076, https://github.com/vllm-project/vllm/pull/36519 Required for sm80 support of Sparse MLA, such as GLM-5 and DeepSeek V3.2. **Argument in support of implementing this**: More and more models are likely to be released with Sparse MLA, not just GLM-5. One backwards compatibility implementation example was the Marlin FP8 E4M3 fallback for sm80, which allows FP8 models to run in Ampere (https://github.com/vllm-project/vllm/issues/17579, https://github.com/vllm-project/vllm/pull/18026, https://github.com/vllm-project/vllm/pull/19990, https://github.com/vllm-project/vllm/pull/24722). This is not supported in SGLang (https://github.com/sgl-project/sglang/issues/12887, https://github.com/sgl-project/sglang/pull/9754), where **all Ampere users of FP8 W8A8 MoE** are restricted to only vLLM. Thus, `TRITON_MLA_SPARSE` should also be implemented, as this...

## 现有链接修复摘要

#38476 [Feature] TRITON_MLA_SPARSE backend for SM8x/11x/12x DSA Sparse MLA Support

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 8: [Feature]: Implement `TRITON_MLA_SPARSE` backend for sm80/120/121 support of Sparse MLA feature request ### 🚀 The feature, motivation and pitch Follow-up to https://github.com/vllm-project/vllm/issues/35021. Relevant PR...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: used_a_gemm` in `csrc/ops.h` / `csrc/torch_bindings.cpp` unconditionally compiles sm90+ code Need `#ifdef ENABLE_DSV3_FUSED_A_GEMM` guards to skip on sm80 > **2. Attention backend** No sparse MLA attention backend avail...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: [Feature]: Implement `TRITON_MLA_SPARSE` backend for sm80/120/121 support of Sparse MLA feature request ### 🚀 The feature, motivation and pitch Follow-up to https://github.com/vllm-project/vllm/issues/35021. Relevant PR...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: LM-5. One backwards compatibility implementation example was the Marlin FP8 E4M3 fallback for sm80, which allows FP8 models to run in Ampere (https://github.com/vllm-project/vllm/issues/17579, https://github.com/vllm-pr...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: pSeek V3.2. **Argument in support of implementing this**: More and more models are likely to be released with Sparse MLA, not just GLM-5. One backwards compatibility implementation example was the Marlin FP8 E4M3 fallba...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#38476](https://github.com/vllm-project/vllm/pull/38476) | closes_keyword | 0.95 | [Feature] TRITON_MLA_SPARSE backend for SM8x/11x/12x DSA Sparse MLA Support | Closes #38006. Enables sparse MLA models (GLM-5, DeepSeek-V3.2) on SM80 (A100/A800) and SM121 (GB10/DGX Spark), where DeepGEMM / FlashMLA-Sparse / FlashInfer-MLA-Sparse are unavail |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
