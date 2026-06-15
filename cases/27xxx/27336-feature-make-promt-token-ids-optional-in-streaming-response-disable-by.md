# vllm-project/vllm#27336: [Feature]: Make promt_token_ids optional in streaming response (disable by default)

| 字段 | 值 |
| --- | --- |
| Issue | [#27336](https://github.com/vllm-project/vllm/issues/27336) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Make promt_token_ids optional in streaming response (disable by default)

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Starting with v0.10.2, the first server-sent event (SSE) in streaming responses now includes the full list of `prompt_token_ids`. While this can be useful for debugging or detailed inspection, it introduces several practical issues in production environments: 1. Large payload size: For long prompts, this significantly increases the size of the first streaming event. This can increase latency, cause network throttling, and reduce streaming responsiveness. 2. Parser and infrastructure limitations: Some clients and intermediate parsers have message size limits. The larger first event may cause them to fail or disconnect, requiring changes across multiple components in existing systems that previously handled smaller initial events. 3. Breaking change in behavior: Previously, streaming responses did not include prompt token IDs, so this change affects compatibility with existing clients expecting smaller events. ### Suggested Fix Make the inclusion of prompt_token_ids optional per request and disabled by default (same as `return_token_ids`), restoring the previous behavior. ### Alternatives Alternatively, provide an API flag or configuration opt...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: s across multiple components in existing systems that previously handled smaller initial events. 3. Breaking change in behavior: Previously, streaming responses did not include prompt token IDs, so this change affects c...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: antly increases the size of the first streaming event. This can increase latency, cause network throttling, and reduce streaming responsiveness. 2. Parser and infrastructure limitations: Some clients and intermediate pa...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: nd scanners have default buffer sizes of 64KB (which was previously sufficient). ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: vious behavior. ### Alternatives Alternatively, provide an API flag or configuration option to exclude `prompt_token_ids` globally for the entire server, so that no streaming response include this field. ### Additional...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: mt_token_ids optional in streaming response (disable by default) feature request ### 🚀 The feature, motivation and pitch Starting with v0.10.2, the first server-sent event (SSE) in streaming responses now includes the f...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
