# vllm-project/vllm#40080: [Bug]: Gemma 4 (31B / 26B-A4B) generates infinite repetition loops, especially with structured output (JSON schema)

| 字段 | 值 |
| --- | --- |
| Issue | [#40080](https://github.com/vllm-project/vllm/issues/40080) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;fp8;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Gemma 4 (31B / 26B-A4B) generates infinite repetition loops, especially with structured output (JSON schema)

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Gemma 4 models (both `google/gemma-4-31B-it` and `google/gemma-4-26B-A4B-it`) fall into infinite repetition loops during generation. The issue occurs significantly more frequently when structured output (JSON schema / grammar constraints) is enabled, but has also been observed in unconstrained generation. **Example output (with JSON schema):** {"patient_information": "Patient reports a 2-week duration of a...", "diagnosis_and_complaints": "General/Systemic-related symptoms: General/Systemic-related symptoms: General/Systemic-related symptoms: General/System-related symptoms: General/Systemic-related symptoms: General/System/related-related symptoms: General/Systemic-related symptoms: General/Systemic-related symptoms: General/System-related symptoms: General/Systemic-related symptoms: ... The model generates a valid prefix, then enters a degenerate loop repeating a phrase with minor variations indefinitely until `max_tokens` is hit. **Observations:** - Occurs with both BF16 and quantized (FP8, NVFP4) weights - Much higher frequency when grammar/JSON schema constraints are applied via xgrammar - Not specific to tensor parallelism...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 6: initely until `max_tokens` is hit. **Observations:** - Occurs with both BF16 and quantized (FP8, NVFP4) weights - Much higher frequency when grammar/JSON schema constraints are applied via xgrammar - Not specific to ten...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: Gemma 4 (31B / 26B-A4B) generates infinite repetition loops, especially with structured output (JSON schema) bug ### Your current environment ### 🐛 Describe the bug Gemma 4 models (both `google/gemma-4-31B-it` an...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [Bug]: Gemma 4 (31B / 26B-A4B) generates infinite repetition loops, especially with structured output (JSON schema) bug ### Your current environment ### 🐛 Describe the bug Gemma 4 models (both `google/gemma-4-31B-it` an...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: a constraints are applied via xgrammar - Not specific to tensor parallelism configuration - Occurs on both vLLM v0.19.x and latest main - **Not a vLLM-specific issue** — the same behavior has been reported across multip...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: s;speculative_decoding attention;cuda;fp8;operator;quantization;sampling;triton build_error;nan_inf dtype;env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
