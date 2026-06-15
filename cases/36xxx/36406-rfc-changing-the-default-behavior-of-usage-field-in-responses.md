# vllm-project/vllm#36406: [RFC]: Changing the Default Behavior of usage Field in Responses

| 字段 | 值 |
| --- | --- |
| Issue | [#36406](https://github.com/vllm-project/vllm/issues/36406) |
| 状态 | open |
| 标签 | RFC |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Changing the Default Behavior of usage Field in Responses

### Issue 正文摘录

### Motivation. Currently, vLLM's behavior regarding the `usage` field in streaming responses strictly follows the OpenAI API specification [OpenAI ChatCompletion StreamOptions](https://developers.openai.com/api/reference/resources/chat/subresources/completions/methods/create#:~:text=the%20streaming%20events.-,stream_options,-%3A%20optional%20ChatCompletionStreamOptions), meaning that token usage data is not returned by default. In issues #6705 and #7179, @DarkLight1337 explained that vLLM's behavior regarding the `usage` return value is consistent with the OpenAI API standard. However, at present, vLLM, as a publicly available inference engine, does not fully align with the practical needs of production environments. The core issue is that in scenarios where API services are provided externally, `usage` is typically the data source for billing and cost monitoring, yet this relies on a client-side parameter. This demand has led to solutions like `--enforce-include-usage` in PR #19695. At the same time, most service providers offering similar APIs have, in practice, defaulted to or enforced the return of `usage` information. Many AI application clients also rely on this metric. For...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ble choice that better serves the majority of users? 2. How to achieve a smooth transition? If the default behavior is changed, providing a clear configuration option (e.g., `stream_usage_policy`, with possible values l...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: APIs have, in practice, defaulted to or enforced the return of `usage` information. Many AI application clients also rely on this metric. For example, tools like CherryStudio require token usage for context statistics,...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: `usage` field in streaming responses strictly follows the OpenAI API specification [OpenAI ChatCompletion StreamOptions](https://developers.openai.com/api/reference/resources/chat/subresources/completions/methods/create...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: ons, would adjusting the default behavior in streaming responses from "false" to "true" be a more reasonable choice that better serves the majority of users? 2. How to achieve a smooth transition? If the default behavio...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: s configuration option should also control the behavior of non-streaming requests to avoid confusing inconsistencies (where non-streaming requests always return `usage`, while streaming requests may not). Additionally,...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
