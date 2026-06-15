# vllm-project/vllm#39638: Gemma 4 31B bnb-4bit: _Gemma4KVSharedSafeProxy AttributeError + weight shape mismatch

| 字段 | 值 |
| --- | --- |
| Issue | [#39638](https://github.com/vllm-project/vllm/issues/39638) |
| 状态 | open |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;frontend_api;gemm_linear;model_support |
| 子分类 | wrong_output |
| Operator 关键词 | cuda |
| 症状 | build_error;crash;mismatch |
| 根因提示 | env_dependency;memory_layout;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> Gemma 4 31B bnb-4bit: _Gemma4KVSharedSafeProxy AttributeError + weight shape mismatch

### Issue 正文摘录

Two bugs when loading `unsloth/gemma-4-31B-it-unsloth-bnb-4bit` via Unsloth's `fast_inference=True` which calls vllm internally. Bug 1: tie_word_embeddings proxy error `vllm/config/vllm.py` line 597 does: ```python hf_config.get_text_config().tie_word_embeddings = tie_word_embeddings ``` For Gemma 4, `get_text_config()` returns `_Gemma4KVSharedSafeProxy` which does not support attribute writes. Raises `AttributeError: '_Gemma4KVSharedSafeProxy' object has no attribute 'tie_word_embeddings'`. Workaround applied locally: ```python try: hf_config.get_text_config().tie_word_embeddings = tie_word_embeddings except AttributeError: if hasattr(hf_config, "text_config"): hf_config.text_config.tie_word_embeddings = tie_word_embeddings ``` Bug 2: bnb-4bit weight shape assertion After patching Bug 1, loading crashes at `vllm/model_executor/layers/linear.py` line 1365: ``` assert param_data.shape == loaded_weight.shape AssertionError ``` The bitsandbytes 4-bit weight layout in the safetensors does not match what vllm expects for Gemma 4 linear layers. ```python from unsloth import FastModel model, tokenizer = FastModel.from_pretrained( model_name="unsloth/gemma-4-31B-it-unsloth-bnb-4bit", max_...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: tch what vllm expects for Gemma 4 linear layers. ```python from unsloth import FastModel model, tokenizer = FastModel.from_pretrained( model_name="unsloth/gemma-4-31B-it-unsloth-bnb-4bit", max_seq_length=2048, load_in_4...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: Gemma 4 31B bnb-4bit: _Gemma4KVSharedSafeProxy AttributeError + weight shape mismatch Two bugs when loading `unsloth/gemma-4-31B-it-unsloth-bnb-4bit` via Unsloth's `fast_inference=True` which calls vllm internally. Bug
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: a 4 31B bnb-4bit: _Gemma4KVSharedSafeProxy AttributeError + weight shape mismatch Two bugs when loading `unsloth/gemma-4-31B-it-unsloth-bnb-4bit` via Unsloth's `fast_inference=True` which calls vllm internally. Bug 1: t...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: 4 31B bnb-4bit: _Gemma4KVSharedSafeProxy AttributeError + weight shape mismatch Two bugs when loading `unsloth/gemma-4-31B-it-unsloth-bnb-4bit` via Unsloth's `fast_inference=True` which calls vllm internally. Bug 1: tie...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: afeProxy AttributeError + weight shape mismatch Two bugs when loading `unsloth/gemma-4-31B-it-unsloth-bnb-4bit` via Unsloth's `fast_inference=True` which calls vllm internally. Bug 1: tie_word_embeddings proxy error `vl...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
