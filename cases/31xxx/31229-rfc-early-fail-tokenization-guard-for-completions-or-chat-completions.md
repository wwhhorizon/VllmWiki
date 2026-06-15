# vllm-project/vllm#31229: [RFC]: Early-Fail Tokenization Guard for Completions or Chat Completions

| 字段 | 值 |
| --- | --- |
| Issue | [#31229](https://github.com/vllm-project/vllm/issues/31229) |
| 状态 | closed |
| 标签 | RFC |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Early-Fail Tokenization Guard for Completions or Chat Completions

### Issue 正文摘录

## Motivation. ### Problem Extremely long chat inputs (e.g., hundreds of millions of tokens) are fully tokenized before length checks, causing CPU OOM (e.g., ~300GB per vllm instance) and hanging the single-threaded async tokenizer, blocking all other requests. More concretely, in RL scenarios, many request inputs come from agent–environment interactions and can sometimes become huge. This should ideally be mitigated by client-side validation before sending the request, but in practice callers often aren’t aware of it. We also need safeguards in vLLM itself, because diagnosing a service hang after it occurs can be time-consuming and difficult. ### Root Cause `_normalize_prompt_text_to_input` (chat path) always tokenizes the entire prompt, then checks `max_model_len` afterward. `Tokenizer `runs in a single-thread `AsyncMicrobatchTokenizer` executor; huge prompts monopolize it and allocate large intermediate buffers. `truncate_prompt_tokens` is optional and usually unset, so no protective truncation/early stop is applied. ## Proposed Change. ### Recommended Fixes #### 1) Protective truncation during tokenization (default path) In `_normalize_prompt_text_to_input` and `InputPreproces...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: _input` (chat path) always tokenizes the entire prompt, then checks `max_model_len` afterward. `Tokenizer `runs in a single-thread `AsyncMicrobatchTokenizer` executor; huge prompts monopolize it and allocate large inter...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ### Effects Long requests fail fast with clear errors; tokenizer never builds gigantic BatchEncodings or stalls the executor thread. Normal requests are unchanged; near-limit requests still get the same validation error...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: illions of tokens) are fully tokenized before length checks, causing CPU OOM (e.g., ~300GB per vllm instance) and hanging the single-threaded async tokenizer, blocking all other requests. More concretely, in RL scenario...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: 00GB per vllm instance) and hanging the single-threaded async tokenizer, blocking all other requests. More concretely, in RL scenarios, many request inputs come from agent–environment interactions and can sometimes beco...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: nce) and hanging the single-threaded async tokenizer, blocking all other requests. More concretely, in RL scenarios, many request inputs come from agent–environment interactions and can sometimes become huge. This shoul...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
