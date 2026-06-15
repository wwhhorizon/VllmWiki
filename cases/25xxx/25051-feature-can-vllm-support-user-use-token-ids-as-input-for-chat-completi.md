# vllm-project/vllm#25051: [Feature]: Can vllm support user use token_ids as input for `chat completions` interface?

| 字段 | 值 |
| --- | --- |
| Issue | [#25051](https://github.com/vllm-project/vllm/issues/25051) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Can vllm support user use token_ids as input for `chat completions` interface?

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Since more and more LLM schedulers are starting to use the KV cache router as part of their scheduling strategy, we need to tokenize the inputs before passing them to vLLM. This is because we must obtain the token IDs (consistent with vLLM’s tokenizer) in order to leverage vLLM’s KV events and select the instance that contains the largest number of cached KV blocks. As a result, we end up applying the chat template and running tokenization twice. I tried applying the chat template and tokenizing the input within my scheduler, then passing the result to completions. However, this caused some tool-call features to be missed. Even more confusing, the function [_normalize_prompt_tokens_to_input](https://github.com/vllm-project/vllm/blob/b77bf34e531abb32c054a38747fa817d08395ae7/vllm/entrypoints/openai/serving_engine.py#L594) converts token IDs back into input text, which means the pipeline still performs input_text -> token_ids -> input_text. So my question is: can we support passing token IDs directly to the chat completions interface? Or is there any other recommended approach? ### Alternatives _No response_ ### Additional context _No response_...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: rt user use token_ids as input for `chat completions` interface? feature request;stale ### 🚀 The feature, motivation and pitch Since more and more LLM schedulers are starting to use the KV cache router as part of their...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: on and pitch Since more and more LLM schedulers are starting to use the KV cache router as part of their scheduling strategy, we need to tokenize the inputs before passing them to vLLM. This is because we must obtain th...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: ts and select the instance that contains the largest number of cached KV blocks. As a result, we end up applying the chat template and running tokenization twice. I tried applying the chat template and tokenizing the in...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: tch Since more and more LLM schedulers are starting to use the KV cache router as part of their scheduling strategy, we need to tokenize the inputs before passing them to vLLM. This is because we must obtain the token I...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
