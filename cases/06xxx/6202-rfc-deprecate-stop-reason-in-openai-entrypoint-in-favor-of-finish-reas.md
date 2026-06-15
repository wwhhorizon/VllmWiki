# vllm-project/vllm#6202: [RFC]: Deprecate stop_reason in OpenAI Entrypoint in favor of finish_reason; fix implementation of finish_reason

| 字段 | 值 |
| --- | --- |
| Issue | [#6202](https://github.com/vllm-project/vllm/issues/6202) |
| 状态 | closed |
| 标签 | RFC;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Deprecate stop_reason in OpenAI Entrypoint in favor of finish_reason; fix implementation of finish_reason

### Issue 正文摘录

### Motivation. This RFC is motivated by a desire to ensure full OpenAI compatibility in Completions & chat completions endpoints by deprecating `stop_reason` which is not part of the OpenAI specification, and fixing the `finish_reason` field's implementation to be OpenAI-compatibile even though doing so may (or may not) be a breaking change for a small number of existing users. ### Proposed Change. ## Suggestion: recommend deprecating `stop_reason` The [Chat Completion Object in OpenAI's Documentation](https://platform.openai.com/docs/api-reference/chat/object) indicates a `finish_reason` field, but not a `stop_reason`. While the `stop_reason` doesn't break the OpenAI compatibility since it's just an extra property, it is a source of confusion for contributors such as myself, as well as implementers & users of vLLM. It is unclear when `stop_reason` was introduced to the project or why, although I am sure this could be determined by going back through old issues. Perhaps it is an artifact of an older version of OpenAI, or it was merely a typo? Currently, `stop_reason` is almost always `null`/`None` - it does not seem to add any value to the project. Please share your feedback on d...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ndpoints by deprecating `stop_reason` which is not part of the OpenAI specification, and fixing the `finish_reason` field's implementation to be OpenAI-compatibile even though doing so may (or may not) be a breaking cha...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: point in favor of finish_reason; fix implementation of finish_reason RFC;stale ### Motivation. This RFC is motivated by a desire to ensure full OpenAI compatibility in Completions & chat completions endpoints by depreca...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: atibile even though doing so may (or may not) be a breaking change for a small number of existing users. ### Proposed Change. ## Suggestion: recommend deprecating `stop_reason` The [Chat Completion Object in OpenAI's Do...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: so that I can implement this fix/change and so that it doesn't become a blocker on that PR. ### CC List. @mgoin @WoosukKwon @simon-mo ### Any Other Things. This RFC is pertinent to PR #5649 as the `tool_call` value for...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: se is terminated early due to a requested maximum length - `stop` if the model stops naturally or a stop sequence is reached - `tool_calls` if the model generates tool calls - `content_filter` if the content filter term...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
