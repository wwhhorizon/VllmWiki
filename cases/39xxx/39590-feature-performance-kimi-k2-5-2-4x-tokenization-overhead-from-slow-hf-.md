# vllm-project/vllm#39590: [Feature][Performance]: Kimi K2.5: 2.4x tokenization overhead from slow HF pipeline

| 字段 | 值 |
| --- | --- |
| Issue | [#39590](https://github.com/vllm-project/vllm/issues/39590) |
| 状态 | open |
| 标签 | feature request |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature][Performance]: Kimi K2.5: 2.4x tokenization overhead from slow HF pipeline

### Issue 正文摘录

### 🚀 The feature, motivation and pitch # [Performance] Kimi K2.5: 2.4x tokenization overhead from HF pipeline bypass ## TLDR [`Inferact/Kimi-K2.5-NVFP4`](https://huggingface.co/Inferact/Kimi-K2.5-NVFP4) now ships an updated `tokenization_kimi.py` that fixes a **2.4x tokenization overhead** in vLLM. No model weight changes. No vLLM code changes needed. Tokenization output is identical (verified on 69k+ comparisons across 6 code paths, zero mismatches). The fix overrides `_encode_plus` to call tiktoken (Rust) directly, bypassing an unnecessary Python pipeline (`tokenize()` → `_tokenize()` → `convert_tokens_to_ids()`) that was converting int→str→int on every token. ## Problem Kimi K2.5's `TikTokenTokenizer` has a fast `encode()` that calls tiktoken (Rust) directly, but vLLM never uses it. The `AsyncMicrobatchTokenizer.encode()` routes through HF's `__call__()` → `_encode_plus()`, which forces a slow Python pipeline: ``` _encode_plus → get_input_ids: → tokenize(text): → tokens_trie.split(text) ← 76% of overhead: O(n*k) trie scan → _tokenize(segment): → self.encode(segment) [tiktoken/Rust → list[int]] → [self.decoder[t] for t ...] ← 3%: int→str → convert_tokens_to_ids(strings) ← 21%:...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: gs) ← 21%: str→int → prepare_for_model(ids, truncation, special tokens) ``` Kimi's `encode(text)` already produces the final `list[int]` with proper trie split included — the `tokenize()` → `_tokenize()` → `convert_toke...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: nization overhead from HF pipeline bypass ## TLDR [`Inferact/Kimi-K2.5-NVFP4`](https://huggingface.co/Inferact/Kimi-K2.5-NVFP4) now ships an updated `tokenization_kimi.py` that fixes a **2.4x tokenization overhead** in...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: /Kimi-K2.5-NVFP4`](https://huggingface.co/Inferact/Kimi-K2.5-NVFP4) now ships an updated `tokenization_kimi.py` that fixes a **2.4x tokenization overhead** in vLLM. No model weight changes. No vLLM code changes needed....
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: gy=TruncationStrategy.DO_NOT_TRUNCATE, max_length=None, stride=0, is_split_into_words=False, pad_to_multiple_of=None, padding_side=None, return_tensors=None, return_token_type_ids=None, return_attention_mask=None, retur...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Feature][Performance]: Kimi K2.5: 2.4x tokenization overhead from slow HF pipeline feature request ### 🚀 The feature, motivation and pitch # [Performance] Kimi K2.5: 2.4x tokenization overhead from HF pipeline bypass #...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
