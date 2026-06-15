# vllm-project/vllm#42688: [Bug]: forced to hit `Fast` suffix deprecation from `qwen3_vl` import

| 字段 | 值 |
| --- | --- |
| Issue | [#42688](https://github.com/vllm-project/vllm/issues/42688) |
| 状态 | open |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;multimodal_vlm;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: forced to hit `Fast` suffix deprecation from `qwen3_vl` import

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Since https://github.com/huggingface/transformers/pull/43514 from `transformers==5.4.0`, either of these imports: ```python from vllm.model_executor.models.qwen3_vl import Qwen3VLForConditionalGeneration # Or any module that transitively imports from qwen3_vl: from vllm.model_executor.models.qwen3_5 import Qwen3_5MoeForCausalLM ``` Are now forced to eat: ```none [transformers] `Qwen2VLImageProcessorFast` is deprecated. The `Fast` suffix for image processors has been removed; use `Qwen2VLImageProcessor` instead. ``` This issue about is resolving this internal deprecation by renaming to a non-`Fast` class: ```diff ---from transformers.models.qwen2_vl import Qwen2VLImageProcessorFast +++from transformers.models.qwen2_vl import Qwen2VLImageProcessor ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: forced to hit `Fast` suffix deprecation from `qwen3_vl` import bug ### Your current environment ### 🐛 Describe the bug Since https://github.com/huggingface/transformers/pull/43514 from `transformers==5.4.0`, eith...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [Bug]: forced to hit `Fast` suffix deprecation from `qwen3_vl` import bug ### Your current environment ### 🐛 Describe the bug Since https://github.com/huggingface/transformers/pull/43514 from `transformers==5.4.0`, eith...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: rts from qwen3_vl: from vllm.model_executor.models.qwen3_5 import Qwen3_5MoeForCausalLM ``` Are now forced to eat: ```none [transformers] `Qwen2VLImageProcessorFast` is deprecated. The `Fast` suffix for image processors...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ltimodal_vlm;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
