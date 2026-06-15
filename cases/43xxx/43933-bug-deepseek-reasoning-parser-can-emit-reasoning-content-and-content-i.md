# vllm-project/vllm#43933: [Bug]: DeepSeek reasoning parser can emit reasoning_content and content in the same streaming chunk

| 字段 | 值 |
| --- | --- |
| Issue | [#43933](https://github.com/vllm-project/vllm/issues/43933) |
| 状态 | open |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: DeepSeek reasoning parser can emit reasoning_content and content in the same streaming chunk

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug `DeepSeekR1ReasoningParser.extract_reasoning_streaming()` can return a single streaming delta with both `reasoning` and `content` populated when ` ` and the first answer tokens are produced in the same decode delta. That becomes a Chat Completions streaming chunk where the same `choices[0].delta` may contain both `reasoning_content` and `content`. This can break DeepSeek-compatible clients that follow DeepSeek's official thinking-mode streaming example, because the example treats `reasoning_content` and `content` as mutually exclusive per chunk: DeepSeek official docs: https://api-docs.deepseek.com/guides/thinking_mode ```python if chunk.choices[0].delta.reasoning_content: reasoning_content += chunk.choices[0].delta.reasoning_content else: content += chunk.choices[0].delta.content ``` With a mixed chunk, that client takes the `reasoning_content` branch and drops `delta.content`. For comparison, Z.ai's official GLM streaming tool-call docs use independent checks for reasoning, content, and tool calls, so a GLM client following that example can tolerate a mixed chunk: Z.ai official docs: https://docs.z.ai/guides/tools/stream-tool `...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: `. This can break DeepSeek-compatible clients that follow DeepSeek's official thinking-mode streaming example, because the example treats `reasoning_content` and `content` as mutually exclusive per chunk: DeepSeek offic...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ta. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: tent: reasoning_content += chunk.choices[0].delta.reasoning_content else: content += chunk.choices[0].delta.content ``` With a mixed chunk, that client takes the `reasoning_content` branch and drops `delta.content`. For...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: delta_token_ids=[102, 2, 103], ) print(cls.__name__, delta.model_dump(exclude_none=True)) ``` Actual output: ```text DeepSeekR1ReasoningParser {'content': '我是', 'reasoning': '诚意。', 'tool_calls': []} DeepSeekV3ReasoningW...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: populated when ` ` and the first answer tokens are produced in the same decode delta. That becomes a Chat Completions streaming chunk where the same `choices[0].delta` may contain both `reasoning_content` and `content`....

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
