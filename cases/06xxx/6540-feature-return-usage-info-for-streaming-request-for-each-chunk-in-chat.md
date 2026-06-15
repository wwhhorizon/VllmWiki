# vllm-project/vllm#6540: [Feature]: return Usage info for streaming request for each chunk in ChatCompletion

| 字段 | 值 |
| --- | --- |
| Issue | [#6540](https://github.com/vllm-project/vllm/issues/6540) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: return Usage info for streaming request for each chunk in ChatCompletion

### Issue 正文摘录

### 🚀 The feature, motivation and pitch in entrypoints.openai.serving_completions.py I see OpenAIServingCompletion holds the method completion_stream_generator that can return usage info for each chunk by using StreamOptions `continuous_usage_stats`. line 297. > ``if (request.stream_options > and request.stream_options.include_usage): > if (request.stream_options.continuous_usage_stats > or output.finish_reason is not None): > prompt_tokens = len(res.prompt_token_ids) > completion_tokens = len(output.token_ids) > usage = UsageInfo( > prompt_tokens=prompt_tokens, > completion_tokens=completion_tokens, > total_tokens=prompt_tokens + completion_tokens, > ) > Somehow, this is not the case in entrypoints.openai.serving_chat.py. I propose to add this feature for OpenAIServingChat. What do you think ? ### Alternatives _No response_ ### Additional context _No response_

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature]: return Usage info for streaming request for each chunk in ChatCompletion feature request ### 🚀 The feature, motivation and pitch in entrypoints.openai.serving_completions.py I see OpenAIServingCompletion hold...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
