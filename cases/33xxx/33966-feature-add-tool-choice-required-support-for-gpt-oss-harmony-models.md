# vllm-project/vllm#33966: [Feature]: Add tool_choice="required" support for GPT-OSS Harmony models

| 字段 | 值 |
| --- | --- |
| Issue | [#33966](https://github.com/vllm-project/vllm/issues/33966) |
| 状态 | open |
| 标签 | feature request;stale |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Add tool_choice="required" support for GPT-OSS Harmony models

### Issue 正文摘录

### 🚀 The feature, motivation and pitch GPT-OSS models use the Harmony chat format, which differs from standard models in its response generation behavior. Even when tool_choice="required" is set, these models tend to generate direct text responses instead of tool calls, resulting in only 91% success rate for tool call generation. Harmony format models select one of three channels (final, analysis, commentary) after completing their internal processing. Tool calls are only generated through the commentary channel with a specified recipient. Currently, there is no mechanism to enforce the tool call path when tool_choice="required" is set for these models. The proposed solution uses a LogitsProcessor-based enforcement approach: - Detect the response pattern assistant in generated tokens - Force the next tokens to be commentary to=, guaranteeing the tool call path - Uses a PatternForcedSequenceLogitsProcessor with a state machine pattern (NORMAL → FORCING → NORMAL) This positive enforcement approach is more robust than a bad_words blocking approach, which cannot guarantee 100% blocking (edge cases like " final", " finally" tokens can slip through). Related PR: #33306 --- ### Alternat...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Feature]: Add tool_choice="required" support for GPT-OSS Harmony models feature request;stale ### 🚀 The feature, motivation and pitch GPT-OSS models use the Harmony chat format, which differs from standard models in it...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: entary channel with a specified recipient. Currently, there is no mechanism to enforce the tool call path when tool_choice="required" is set for these models. The proposed solution uses a LogitsProcessor-based enforceme...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ]: Add tool_choice="required" support for GPT-OSS Harmony models feature request;stale ### 🚀 The feature, motivation and pitch GPT-OSS models use the Harmony chat format, which differs from standard models in its respon...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: Tool calls are only generated through the commentary channel with a specified recipient. Currently, there is no mechanism to enforce the tool call path when tool_choice="required" is set for these models. The proposed s...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: L) This positive enforcement approach is more robust than a bad_words blocking approach, which cannot guarantee 100% blocking (edge cases like " final", " finally" tokens can slip through). Related PR: #33306 --- ### Al...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
