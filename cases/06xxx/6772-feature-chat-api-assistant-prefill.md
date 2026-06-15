# vllm-project/vllm#6772: [Feature]: chat API assistant prefill

| 字段 | 值 |
| --- | --- |
| Issue | [#6772](https://github.com/vllm-project/vllm/issues/6772) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: chat API assistant prefill

### Issue 正文摘录

### 🚀 The feature, motivation and pitch https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/prefill-claudes-response https://www.anthropic.com/news/claude-2-1-prompting I expected I could prefill the assistant response, but seems like it doesn't work. I should be able to do: ``` messages = [ { "role": "user", "content": prompt, }, "role": "assistant", "content": 'According to ', } ] ``` And it should use this to generate up through assistant's response but not ending it, so the model continues Anthropic has this feature, and it helps to control the responses. ### Alternatives Yes, one can avoid the chat API, but since the chat template work is so pervasive and useful, it would be great to add this extension. ### Additional context I'm unclear if it's even possible within the general chat framework. Maybe the jinja2 template would support it OOTB or not, I'm not sure how much it depends upon the template writer, but even if one had to tweak an existing template, still would require the chat API to handle.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Feature]: chat API assistant prefill feature request;stale ### 🚀 The feature, motivation and pitch https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/prefill-claudes-response https://www.anthropic....
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: 🚀 The feature, motivation and pitch https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/prefill-claudes-response https://www.anthropic.com/news/claude-2-1-prompting I expected I could prefill the ass...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: is to generate up through assistant's response but not ending it, so the model continues Anthropic has this feature, and it helps to control the responses. ### Alternatives Yes, one can avoid the chat API, but since the...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
