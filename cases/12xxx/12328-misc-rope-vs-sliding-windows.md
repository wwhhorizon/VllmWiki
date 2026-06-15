# vllm-project/vllm#12328: [Misc]: RoPE vs Sliding Windows

| 字段 | 值 |
| --- | --- |
| Issue | [#12328](https://github.com/vllm-project/vllm/issues/12328) |
| 状态 | closed |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Misc]: RoPE vs Sliding Windows

### Issue 正文摘录

Hi, As context lengths increase, it looks like different models are going about it in different ways. For example, Qwen uses a sliding window in their config.json file while Llama uses RoPE. I was curious how they work in contrast with each other, if they can be combined, what types of RoPE scaling exist, and how all of these parameters can be optimized separately or in conjunction with each other. I am also curious how setting the `--rope-scaling` and `--rope-theta` interacts with the configs if it is already set or using sliding windows. I can't find too much information regarding the combination of all of these settings so any help would be awesome. ```json { "architectures": [ "Qwen2ForCausalLM" ], "attention_dropout": 0.0, "bos_token_id": 151643, "eos_token_id": 151645, "hidden_act": "silu", "hidden_size": 5120, "initializer_range": 0.02, "intermediate_size": 27648, "max_position_embeddings": 32768, "max_window_layers": 70, "model_type": "qwen2", "num_attention_heads": 40, "num_hidden_layers": 64, "num_key_value_heads": 8, "rms_norm_eps": 1e-06, "rope_theta": 1000000.0, "sliding_window": 131072, "tie_word_embeddings": false, "torch_dtype": "bfloat16", "transformers_version":...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: liding Windows Hi, As context lengths increase, it looks like different models are going about it in different ways. For example, Qwen uses a sliding window in their config.json file while Llama uses RoPE. I was curious...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: .0, "sliding_window": 131072, "tie_word_embeddings": false, "torch_dtype": "bfloat16", "transformers_version": "4.43.1", "use_cache": true, "use_sliding_window": false, "vocab_size": 152064 } ``` ```json { "architecture...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ie_word_embeddings": false, "torch_dtype": "bfloat16", "transformers_version": "4.43.1", "use_cache": true, "use_sliding_window": false, "vocab_size": 152064 } ``` ```json { "architectures": [ "LlamaForCausalLM" ], "att...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ion of all of these settings so any help would be awesome. ```json { "architectures": [ "Qwen2ForCausalLM" ], "attention_dropout": 0.0, "bos_token_id": 151643, "eos_token_id": 151645, "hidden_act": "silu", "hidden_size"...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: heta": 1000000.0, "sliding_window": 131072, "tie_word_embeddings": false, "torch_dtype": "bfloat16", "transformers_version": "4.43.1", "use_cache": true, "use_sliding_window": false, "vocab_size": 152064 } ``` ```json {...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
