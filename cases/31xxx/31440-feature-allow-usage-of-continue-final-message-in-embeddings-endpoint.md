# vllm-project/vllm#31440: [Feature]: Allow usage of continue_final_message in /embeddings endpoint

| 字段 | 值 |
| --- | --- |
| Issue | [#31440](https://github.com/vllm-project/vllm/issues/31440) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Allow usage of continue_final_message in /embeddings endpoint

### Issue 正文摘录

### 🚀 The feature, motivation and pitch ### Problem Statement When generating embeddings with chat-based models, the `/embeddings` endpoint does not currently support the addition of a prefilled assistant message. This lack of support limits the usefulness of the `/embeddings` endpoint because we have found that prefilling the assistant message improves performance on select retrieval tasks. ### Feature Description Congruent to the parameter accepted by the `/chat/completions` endpoint, the requested feature would add a `continue_final_message` parameter to the parameters accepted by the `/embeddings` endpoint such that the `messages` object could contain a final `assistant` message that has been partially filled and would render to, for example: ` assistant\nBased on the evidence provided, I conclude that `. ### Feature Benefits - Better control over embedding behaviour resulting in improved retrieval task performance. - More consistent API design matches the `/chat/completions` endpoint. ### Alternatives We currently hardcode the prefilled assistant message into custom jinja chat templates, but this workaround requires that we create separate custom chat templates for each model...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ]: Allow usage of continue_final_message in /embeddings endpoint feature request ### 🚀 The feature, motivation and pitch ### Problem Statement When generating embeddings with chat-based models, the `/embeddings` endpoin...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: hat prefilling the assistant message improves performance on select retrieval tasks. ### Feature Description Congruent to the parameter accepted by the `/chat/completions` endpoint, the requested feature would add a `co...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: en. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: pitch ### Problem Statement When generating embeddings with chat-based models, the `/embeddings` endpoint does not currently support the addition of a prefilled assistant message. This lack of support limits the usefuln...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
