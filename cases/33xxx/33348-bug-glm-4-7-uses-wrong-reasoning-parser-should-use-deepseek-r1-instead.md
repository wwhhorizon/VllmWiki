# vllm-project/vllm#33348: [Bug] GLM-4.7 uses wrong reasoning parser (should use deepseek_r1 instead of glm45)

| 字段 | 值 |
| --- | --- |
| Issue | [#33348](https://github.com/vllm-project/vllm/issues/33348) |
| 状态 | closed |
| 标签 |  |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug] GLM-4.7 uses wrong reasoning parser (should use deepseek_r1 instead of glm45)

### Issue 正文摘录

## Summary GLM-4.7 models have a different chat template than GLM-4.5/4.6 models. The key difference is: - **GLM-4.5/4.6**: The ` ` token is NOT included in the generation prompt. The model generates ` ` as part of its output. - **GLM-4.7**: The ` ` token IS included in the generation prompt. The model starts generating reasoning content directly without outputting ` ` first. This means GLM-4.7 should use `deepseek_r1` reasoning parser (which handles the case where ` ` is already in the prompt) instead of `glm45` (which uses `DeepSeekV3ReasoningWithThinkingParser`). ## Chat Template Comparison | Model | Generation Prompt (thinking enabled) | Generation Prompt (thinking disabled) | |-------|-------------------------------------|--------------------------------------| | GLM-4.5 | ` ` (empty) | ` \n ` | | GLM-4.6 | ` ` (empty) | ` \n ` | | GLM-4.7 | ` ` | ` ` | ## Current Behavior Currently, there is no `glm47` reasoning parser registered. Users have to use `glm45` which doesn't correctly handle the GLM-4.7 chat template. ## Expected Behavior A `glm47` reasoning parser should be available that uses `DeepSeekR1ReasoningParser` to correctly handle the GLM-4.7 chat template. ## Proposed...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ing parser (should use deepseek_r1 instead of glm45) ## Summary GLM-4.7 models have a different chat template than GLM-4.5/4.6 models. The key difference is: - **GLM-4.5/4.6**: The ` ` token is NOT included in the gener...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
