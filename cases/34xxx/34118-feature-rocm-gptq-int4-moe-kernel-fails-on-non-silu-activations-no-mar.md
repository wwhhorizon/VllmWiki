# vllm-project/vllm#34118: [Feature]: [ROCm]: GPTQ INT4 MoE kernel fails on non-SiLU activations - no Marlin fallback on AMD

| 字段 | 值 |
| --- | --- |
| Issue | [#34118](https://github.com/vllm-project/vllm/issues/34118) |
| 状态 | open |
| 标签 | feature request;rocm |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | activation_norm;frontend_api;hardware_porting;model_support;moe;quantization |
| 子分类 |  |
| Operator 关键词 | activation;fp8;kernel;moe;quantization |
| 症状 | crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Feature]: [ROCm]: GPTQ INT4 MoE kernel fails on non-SiLU activations - no Marlin fallback on AMD

### Issue 正文摘录

### 🚀 The feature, motivation and pitch ## Your current environment - vLLM version: 0.15.1 - GPU: AMD Instinct MI300X (192GB HBM3) × 8 - ROCm: 7.2.0 - Python: 3.12 - OS: Ubuntu (Linux 6.16.6) - Model: `QuixiAI/Step-3.5-Flash-int4-AutoRound` (INT4 GPTQ quantization of `stepfun-ai/Step-3.5-Flash`) - Quantization: GPTQ 4-bit via Intel AutoRound (`--format auto_gptq`) ## 🐛 Describe the bug Serving an INT4 GPTQ-quantized StepFun Step 3.5 Flash model fails during the profiling/dummy run with: ``` AssertionError: Only SiLU activation is supported. ``` The assertion is in `vllm/model_executor/layers/quantization/moe_wna16.py`, line 373: ```python assert layer.activation == "silu", "Only SiLU activation is supported." ``` Step 3.5 Flash is a MoE model that uses a different activation function in its MoE FFN layers (not SiLU). The `moe_wna16` quantization method currently hardcodes a SiLU-only restriction, which blocks GPTQ inference for any MoE model using a different activation. The FP8 variant (`stepfun-ai/Step-3.5-Flash-FP8`) works fine on vLLM — this is purely a quantized MoE kernel limitation. ## Additional context - `--quantization gptq_marlin` also fails because it conflicts with th...

## 现有链接修复摘要

#35302 [Bugfix][Hardware][AMD] Support all MoE activations in WNA16 quantization on ROCm

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: [Feature]: [ROCm]: GPTQ INT4 MoE kernel fails on non-SiLU activations - no Marlin fallback on AMD feature request;rocm ### 🚀 The feature, motivation and pitch ## Your current environment - vLLM version: 0.15.1 - GPU: AM...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: [Feature]: [ROCm]: GPTQ INT4 MoE kernel fails on non-SiLU activations - no Marlin fallback on AMD feature request;rocm ### 🚀 The feature, motivation and pitch ## Your current environment - vLLM version: 0.15.1 - GPU: AM...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: 🚀 The feature, motivation and pitch ## Your current environment - vLLM version: 0.15.1 - GPU: AMD Instinct MI300X (192GB HBM3) × 8 - ROCm: 7.2.0 - Python: 3.12 - OS: Ubuntu (Linux 6.16.6) - Model: `QuixiAI/Step-3.5-Flas...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: 2GB HBM3) × 8 - ROCm: 7.2.0 - Python: 3.12 - OS: Ubuntu (Linux 6.16.6) - Model: `QuixiAI/Step-3.5-Flash-int4-AutoRound` (INT4 GPTQ quantization of `stepfun-ai/Step-3.5-Flash`) - Quantization: GPTQ 4-bit via Intel AutoRo...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: [Feature]: [ROCm]: GPTQ INT4 MoE kernel fails on non-SiLU activations - no Marlin fallback on AMD feature request;rocm ### 🚀 The feature, motivation and pitch ## Your current environment - vLLM version: 0.15.1 - GPU: AM...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#35302](https://github.com/vllm-project/vllm/pull/35302) | closes_keyword | 0.95 | [Bugfix][Hardware][AMD] Support all MoE activations in WNA16 quantization on ROCm | Fixes #34118 ## Test plan - Verified `fused_experts()` accepts `activation` parameter (defaults to `MoEActivation.SILU`) - Verified `apply_moe_activation()` handles all activatio |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
