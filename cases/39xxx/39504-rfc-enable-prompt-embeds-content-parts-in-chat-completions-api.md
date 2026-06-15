# vllm-project/vllm#39504: [RFC]: Enable prompt_embeds content parts in Chat Completions API

| 字段 | 值 |
| --- | --- |
| Issue | [#39504](https://github.com/vllm-project/vllm/issues/39504) |
| 状态 | closed |
| 标签 | RFC |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Enable prompt_embeds content parts in Chat Completions API

### Issue 正文摘录

### Motivation. vLLM supports `prompt_embeds` (pre-computed embeddings) in the Completions API (`/v1/completions`) [via the --enable-prompt-embeds flag](https://docs.vllm.ai/en/stable/features/prompt_embeds/). This allows users to bypass the model's embedding layer by providing a serialized tensor of shape `(num_tokens, hidden_size)`. However, the Chat Completions API (`/v1/chat/completions`) does not support `prompt_embeds`. Users who need to mix pre-computed embeddings with plain text content in a multi-turn conversation are forced manually apply chat-templates/tokenize/embed outside of vLLM to use the completions endpoint. Additionally, they cannot take advantage of features of `/v1/chat/completions` such as tool call parsing. This RFC proposes adding `prompt_embeds` as a new content part type in the Chat Completions API, allowing users to interleave pre-computed embeddings with text within any message role. ### Proposed Change. #### API Surface A new content part type `"prompt_embeds"` is added to chat messages, following the same pattern as `"image_embeds"` and other multimodal content parts: ```json { "messages": [ { "role": "user", "content": [ {"type": "text", "text": "Let...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: m.ai/en/stable/features/prompt_embeds/). This allows users to bypass the model's embedding layer by providing a serialized tensor of shape `(num_tokens, hidden_size)`. However, the Chat Completions API (`/v1/chat/comple...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ension) copies of a dedicated placeholder token (` `, registered as a special token in the tokenizer). **Template rendering**: The chat template sees only text (including placeholder tokens) and renders normally. **Posi...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: gs from buffer ``` ## Prefix Caching The existing prefix caching mechanism works correctly for mixed mode without modification: - `request.all_token_ids` will include both real and placeholder token IDs (primary hash ke...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: ion**: A full-length `is_token_ids` mask and embedding tensor are built, mapping each position to either the model's embedding layer (`mask = True`) or the pre-computed embedding (`mask = False`). **GPU pipeline**: The...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: ensor as an extra key. Outcome: same tokens + same embeddings produce a cache hit. ### Feedback Period. 1 week ### CC List. @qthequartermasterman @Nan2018 ### Any Other Things. - This builds on the existing `--enable-pr...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
