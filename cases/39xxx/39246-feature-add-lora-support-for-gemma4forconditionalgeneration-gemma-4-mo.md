# vllm-project/vllm#39246: [Feature]: Add LoRA support for Gemma4ForConditionalGeneration / Gemma 4 models

| 字段 | 值 |
| --- | --- |
| Issue | [#39246](https://github.com/vllm-project/vllm/issues/39246) |
| 状态 | closed |
| 标签 | good first issue;feature request |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Add LoRA support for Gemma4ForConditionalGeneration / Gemma 4 models

### Issue 正文摘录

### 🚀 The feature, motivation and pitch ## Motivation vLLM recently added support for Gemma 4 (v0.19.0), but LoRA adapters do not appear to be supported yet for Gemma 4 model classes such as: - Gemma4ForCausalLM - Gemma4ForConditionalGeneration (multimodal) Currently, LoRA support in vLLM is model-specific, and there is no indication that Gemma 4 has been wired into the LoRA adapter system. ## Problem Attempting to load LoRA adapters for Gemma 4 models is either unsupported or undocumented. Previous Gemma-family models required explicit LoRA integration: - #3044 → initial Gemma LoRA request - #3050 → implementation - #32758 → Gemma 3 multimodal LoRA discussion - #21746 → Gemma3n LoRA support missing Gemma 4 seems to be in a similar state. ## Proposal Extend vLLM LoRA support to Gemma 4 models: ### Phase 1 (text-only) - Enable LoRA for Gemma4ForCausalLM - Add mapping for: - q_proj, k_proj, v_proj, o_proj - gate_up_proj, down_proj - Ensure compatibility with fused/packed projections ### Phase 2 (multimodal) - Enable LoRA for Gemma4ForConditionalGeneration - Implement: - get_num_mm_connector_tokens - get_num_mm_encoder_tokens - Support LoRA on: - language backbone (first) - connector...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Feature]: Add LoRA support for Gemma4ForConditionalGeneration / Gemma 4 models good first issue;feature request ### 🚀 The feature, motivation and pitch ## Motivation vLLM recently added support for Gemma 4 (v0.19.0), b...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: [Feature]: Add LoRA support for Gemma4ForConditionalGeneration / Gemma 4 models good first issue;feature request ### 🚀 The feature, motivation and pitch ## Motivation vLLM recently added support for Gemma 4 (v0.19.0), b...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: dels: ### Phase 1 (text-only) - Enable LoRA for Gemma4ForCausalLM - Add mapping for: - q_proj, k_proj, v_proj, o_proj - gate_up_proj, down_proj - Ensure compatibility with fused/packed projections ### Phase 2 (multimoda...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: Is LoRA support for Gemma 4 planned? - Are there any blockers (e.g., MoE routing, multimodal token handling)? ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: onalGeneration (multimodal) Currently, LoRA support in vLLM is model-specific, and there is no indication that Gemma 4 has been wired into the LoRA adapter system. ## Problem Attempting to load LoRA adapters for Gemma 4...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
