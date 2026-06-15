# vllm-project/vllm#44098: [Bug]: GLM tool-call streaming final chunks repeat metadata and combine arguments with finish_reason

| 字段 | 值 |
| --- | --- |
| Issue | [#44098](https://github.com/vllm-project/vllm/issues/44098) |
| 状态 | open |
| 标签 |  |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: GLM tool-call streaming final chunks repeat metadata and combine arguments with finish_reason

### Issue 正文摘录

### Your current environment Current local upstream main: ```text commit 6bdabbad5 [CI/Build] Enable Step3p7ForConditionalGeneration testing (#43956) ``` The relevant code path is `vllm/entrypoints/openai/chat_completion/serving.py` with GLM tool parsers such as `glm45` / `glm47` used for GLM-4.5 / GLM-5 style tool-call streaming. ### 🐛 Describe the bug There are still two GLM tool-call streaming protocol issues on current main. #### 1. Final remaining-argument chunks can re-emit tool-call metadata When `OpenAIServingChat` computes remaining tool arguments at finish time, `_create_remaining_args_delta()` preserves `id`, `type`, and `function.name` from the original delta: ```python return DeltaMessage( tool_calls=[ DeltaToolCall( index=index, id=original_tc.id if original_tc else None, type=original_tc.type if original_tc else None, function=DeltaFunctionCall( name=original_fn.name if original_fn else None, arguments=remaining_call, ), ) ] ) ``` For continuation / final remaining-argument chunks, this can send `id`, `type`, and `function.name` again even though those fields were already emitted in the first chunk for that tool-call index. OpenAI-compatible clients generally expect...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ent environment Current local upstream main: ```text commit 6bdabbad5 [CI/Build] Enable Step3p7ForConditionalGeneration testing (#43956) ``` The relevant code path is `vllm/entrypoints/openai/chat_completion/serving.py`...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: [Bug]: GLM tool-call streaming final chunks repeat metadata and combine arguments with finish_reason ### Your current environment Current local upstream main: ```text commit 6bdabbad5 [CI/Build] Enable Step3p7ForConditi...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: on: "tool_calls"`. ### Before submitting a new issue... - [x] I have searched existing issues and PRs and listed the nearest related ones above.
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ent main shows the metadata is still preserved: ```text remaining_delta.model_dump= {'id': 'call_current', 'type': 'function', 'index': 0, 'function': {'name': 'current_name', 'arguments': ']}'}} ``` #### 2. A terminal...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: `text commit 6bdabbad5 [CI/Build] Enable Step3p7ForConditionalGeneration testing (#43956) ``` The relevant code path is `vllm/entrypoints/openai/chat_completion/serving.py` with GLM tool parsers such as `glm45` / `glm47...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
