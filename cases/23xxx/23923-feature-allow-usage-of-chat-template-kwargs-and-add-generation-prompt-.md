# vllm-project/vllm#23923: [Feature]: Allow usage of chat_template_kwargs and add_generation_prompt in /embeddings endpoint

| 字段 | 值 |
| --- | --- |
| Issue | [#23923](https://github.com/vllm-project/vllm/issues/23923) |
| 状态 | open |
| 标签 | feature request;unstale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Allow usage of chat_template_kwargs and add_generation_prompt in /embeddings endpoint

### Issue 正文摘录

### 🚀 The feature, motivation and pitch ### Feature Description When generating embeddings with chat-based models, the `/embeddings` endpoint currently has two limitations: - `add_generation_prompt` is always forced to `False `when using EmbeddingChatRequest. - `chat_template_kwargs` is ignored in `EmbeddingChatRequest`. ### Why this matters For some models, embeddings differ significantly depending on whether the generation prompt is included. We have observed that setting `add_generation_prompt=True` improves performance on certain IR tasks compared to the default `False`. Additionally, enabling setting of `add_generation_prompt` in embedding requests would allow consistent use of chat template parameters across both `/chat/completions` and `/embeddings`. ### Proposed Solution - Expose an option to set `add_generation_prompt` in `/embeddings` requests. or - Ensure `chat_template_kwargs` is applied when building inputs in `EmbeddingChatRequest`. ### Benefits - Better control over embedding behaviour, matching what’s possible in `/chat/completions`. - Improved retrieval/IR performance for models that benefit from `add_generation_prompt=True`. - More consistent API design across en...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: emplate_kwargs and add_generation_prompt in /embeddings endpoint feature request;unstale ### 🚀 The feature, motivation and pitch ### Feature Description When generating embeddings with chat-based models, the `/embedding...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: aviour, matching what’s possible in `/chat/completions`. - Improved retrieval/IR performance for models that benefit from `add_generation_prompt=True`. - More consistent API design across endpoints. ### Alternatives _No...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: embeddings` requests. or - Ensure `chat_template_kwargs` is applied when building inputs in `EmbeddingChatRequest`. ### Benefits - Better control over embedding behaviour, matching what’s possible in `/chat/completions`...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: ly has two limitations: - `add_generation_prompt` is always forced to `False `when using EmbeddingChatRequest. - `chat_template_kwargs` is ignored in `EmbeddingChatRequest`. ### Why this matters For some models, embeddi...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
