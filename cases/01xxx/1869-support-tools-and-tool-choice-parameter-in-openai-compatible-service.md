# vllm-project/vllm#1869: Support `tools` and `tool_choice` parameter in OpenAI compatible service 

| 字段 | 值 |
| --- | --- |
| Issue | [#1869](https://github.com/vllm-project/vllm/issues/1869) |
| 状态 | closed |
| 标签 | help wanted;good first issue;feature request |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Support `tools` and `tool_choice` parameter in OpenAI compatible service 

### Issue 正文摘录

Also aliased as `functions` and `function_call` in deprecated parameters. https://platform.openai.com/docs/api-reference/chat/create#chat-create-tools After #1756 is merged (thanks @Tostino!), it should be straightforward to add this as a core parameter to OpenAI compatible service. This will help unlock client libraries using similar interface. Do note that the underlying model need to support function calling (e.g. OpenHermes) and prompt engineering might be needed. Also see @dongxiaolong's example here: https://github.com/vllm-project/vllm/pull/1756#issuecomment-1827064922

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ck client libraries using similar interface. Do note that the underlying model need to support function calling (e.g. OpenHermes) and prompt engineering might be needed. Also see @dongxiaolong's example here: https://gi...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: meter in OpenAI compatible service help wanted;good first issue;feature request Also aliased as `functions` and `function_call` in deprecated parameters. https://platform.openai.com/docs/api-reference/chat/create#chat-c...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
