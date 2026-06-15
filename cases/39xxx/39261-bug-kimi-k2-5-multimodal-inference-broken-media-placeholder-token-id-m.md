# vllm-project/vllm#39261: [Bug]: Kimi K2.5 multimodal inference broken — media_placeholder_token_id mismatch with runtime tokenizer

| 字段 | 值 |
| --- | --- |
| Issue | [#39261](https://github.com/vllm-project/vllm/issues/39261) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;frontend_api;hardware_porting;model_support;multimodal_vlm;sampling_logits;speculative_decoding |
| 子分类 | wrong_output |
| Operator 关键词 | cuda |
| 症状 | build_error;mismatch;slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Kimi K2.5 multimodal inference broken — media_placeholder_token_id mismatch with runtime tokenizer

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Kimi K2.5 multimodal inference (images/video) is completely broken. Any request with image or video input fails with: ``` AssertionError: Failed to apply prompt replacement for mm_items['vision_chunk'][0] ``` The root cause: `KimiK25Config.media_placeholder_token_id` is set to 163605, but at runtime the tokenizer maps ` ` to token ID 163602. Token 163605 is actually `[UNK]`. When `_get_prompt_updates` builds a `PromptReplacement` targeting `[163605]`, it searches the tokenized input for a token that doesn't exist — the actual ` ` tokens are at 163602, so the target is never found and the assertion fires. #### Why this happens `vllm/transformers_utils/configs/kimi_k25.py` hardcodes: ```python media_placeholder_token_id: int = 163605 ``` This value comes from Kimi K2.5's `config.json`, which was written for the slow `TikTokenTokenizer`. However, transformers v5 auto-converts the slow tokenizer to a fast `TokenizersBackend`, compacting gaps in the special token ID range. After compaction, ` ` is at **163602** and `[UNK]` moves down to occupy 163605. In `KimiK25MultiModalProcessor._get_prompt_updates`, the `PromptReplacement` target...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 8: [Bug]: Kimi K2.5 multimodal inference broken — media_placeholder_token_id mismatch with runtime tokenizer bug ### Your current environment ### 🐛 Describe the bug Kimi K2.5 multimodal inference (images/video) is complete...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ID 163602. Token 163605 is actually `[UNK]`. When `_get_prompt_updates` builds a `PromptReplacement` targeting `[163605]`, it searches the tokenized input for a token that doesn't exist — the actual ` ` tokens are at 16...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: g]: Kimi K2.5 multimodal inference broken — media_placeholder_token_id mismatch with runtime tokenizer bug ### Your current environment ### 🐛 Describe the bug Kimi K2.5 multimodal inference (images/video) is completely...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: Kimi K2.5 multimodal inference (images/video) is completely broken. Any request with image or video input fails with: ``` AssertionError: Failed to apply prompt replacement for mm_items['vision_chunk'][0] ``` The root c...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: Bug]: Kimi K2.5 multimodal inference broken — media_placeholder_token_id mismatch with runtime tokenizer bug ### Your current environment ### 🐛 Describe the bug Kimi K2.5 multimodal inference (images/video) is completel...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
