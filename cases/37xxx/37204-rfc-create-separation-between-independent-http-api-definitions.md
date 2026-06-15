# vllm-project/vllm#37204: [RFC]: Create separation between independent HTTP API definitions

| 字段 | 值 |
| --- | --- |
| Issue | [#37204](https://github.com/vllm-project/vllm/issues/37204) |
| 状态 | open |
| 标签 | RFC |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Create separation between independent HTTP API definitions

### Issue 正文摘录

### Motivation. Right now we have overloaded the "OpenAI-compatible" API server with APIs that come from many different sources. As a recent example, PR #37074 proposes support for `v2/embed` from Cohere. It is added to our existing API server. If OpenAI were to introduce a `v2/embed` API in the future, we would have a non-backwards-compatible problem to resolve if we wanted to support that. https://docs.vllm.ai/en/latest/serving/openai_compatible_server/#supported-apis In the "Supported APIs" section of the docs, the APIs in question are under "In addition, we have the following custom APIs:". Another reason this is problematic is that we regularly get security reports about how APIs within the same server have such drastically different security considerations. For example: - Some APIs support API tokens, while others do not - Some APIs are intended for end users, while others are for internal usage only and would be a major security risk if exposed. Having cleaner separation of the APIs would help us maintain cleaner security boundaries between APIs based on their intended usage and exposure. ### Proposed Change. Split APIs based on their source into their own HTTP endpoints. D...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: pected API endpoints would include, at least: - OpenAI APIs only - Specific APIs may include vLLM custom extensions, but the APIs are explicitly OpenAI's definition - Cohere APIs - v1/rerank also includes some extension...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: blem to resolve if we wanted to support that. https://docs.vllm.ai/en/latest/serving/openai_compatible_server/#supported-apis In the "Supported APIs" section of the docs, the APIs in question are under "In addition, we...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
