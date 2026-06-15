# vllm-project/vllm#10548: [Usage]: Can we extend the context length of gemma2 model or other models?

| 字段 | 值 |
| --- | --- |
| Issue | [#10548](https://github.com/vllm-project/vllm/issues/10548) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Can we extend the context length of gemma2 model or other models?

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm I need to extend the context length of gemma2-9b model along also with other models like llama3.1-8b can we do it with ROPE SCALING? if so how to use these args `--rope-scaling ` & `--rope-theta` ? plus does these configs has different things to considered for rope scaling? I need to extend up to **128k** tokens. ***$ cat models--google--gemma-2-9b-it/config.json*** ``` { "architectures": [ "Gemma2ForCausalLM" ], "attention_bias": false, "attention_dropout": 0.0, "attn_logit_softcapping": 50.0, "bos_token_id": 2, "cache_implementation": "hybrid", "eos_token_id": 1, "final_logit_softcapping": 30.0, "head_dim": 256, "hidden_act": "gelu_pytorch_tanh", "hidden_activation": "gelu_pytorch_tanh", "hidden_size": 3584, "initializer_range": 0.02, "intermediate_size": 14336, "max_position_embeddings": 8192, "model_type": "gemma2", "num_attention_heads": 16, "num_hidden_layers": 42, "num_key_value_heads": 8, "pad_token_id": 0, "query_pre_attn_scalar": 256, "rms_norm_eps": 1e-06, "rope_theta": 10000.0, "sliding_window": 4096, "sliding_window_size": 4096, "torch_dtype": "bfloat16",...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Usage]: Can we extend the context length of gemma2 model or other models? usage;stale ### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm I need to extend t...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: 000.0, "sliding_window": 4096, "sliding_window_size": 4096, "torch_dtype": "bfloat16", "transformers_version": "4.42.0.dev0", "use_cache": true, "vocab_size": 256000 } ``` ***$ cat NousResearch--Meta-Llama-3-8B-Instruct...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: sliding_window_size": 4096, "torch_dtype": "bfloat16", "transformers_version": "4.42.0.dev0", "use_cache": true, "vocab_size": 256000 } ``` ***$ cat NousResearch--Meta-Llama-3-8B-Instruct/config.json *** ``` { "architec...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: tokens. ***$ cat models--google--gemma-2-9b-it/config.json*** ``` { "architectures": [ "Gemma2ForCausalLM" ], "attention_bias": false, "attention_dropout": 0.0, "attn_logit_softcapping": 50.0, "bos_token_id": 2, "cache_...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: "architectures": [ "Gemma2ForCausalLM" ], "attention_bias": false, "attention_dropout": 0.0, "attn_logit_softcapping": 50.0, "bos_token_id": 2, "cache_implementation": "hybrid", "eos_token_id": 1, "final_logit_softcappi...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
