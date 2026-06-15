# vllm-project/vllm#33697: [Bug]: Model architectures ['CostWiseGemmaForCausalLM'] are not supported for now.

| 字段 | 值 |
| --- | --- |
| Issue | [#33697](https://github.com/vllm-project/vllm/issues/33697) |
| 状态 | open |
| 标签 | bug;stale |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Model architectures ['CostWiseGemmaForCausalLM'] are not supported for now.

### Issue 正文摘录

### Your current environment Trying to Eror info: ValueError: Model architectures ['CostWiseGemmaForCausalLM'] are not supported for now I'm using Python3.10 ### 🐛 Describe the bug Here is config.json from HF: { "_name_or_path": "BAAI/bge-reranker-v2.5-gemma2-lightweight", "architectures": [ "CostWiseGemmaForCausalLM" ], "auto_map": { "AutoConfig": "BAAI/bge-reranker-v2.5-gemma2-lightweight--gemma_config.CostWiseGemmaConfig", "AutoModel": "BAAI/bge-reranker-v2.5-gemma2-lightweight--gemma_model.CostWiseGemmaModel", "AutoModelForCausalLM": "BAAI/bge-reranker-v2.5-gemma2-lightweight--gemma_model.CostWiseGemmaForCausalLM" }, "attention_bias": false, "attention_dropout": 0.0, "attn_logit_softcapping": 50.0, "bos_token_id": 2, "cache_implementation": "hybrid", "eos_token_id": 1, "final_logit_softcapping": 30.0, "head_dim": 256, "hidden_act": "gelu_pytorch_tanh", "hidden_activation": "gelu_pytorch_tanh", "hidden_size": 3584, "initializer_range": 0.02, "intermediate_size": 14336, "layer_sep": 1, "layer_wise": true, "max_position_embeddings": 8192, "model_type": "cost_wise_gemma", "num_attention_heads": 16, "num_hidden_layers": 42, "num_key_value_heads": 8, "pad_token_id": 0, "query_pre_at...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: Model architectures ['CostWiseGemmaForCausalLM'] are not supported for now. bug;stale ### Your current environment Trying to Eror info: ValueError: Model architectures ['CostWiseGemmaForCausalLM'] are not support...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: ndow": 4096, "sliding_window_size": 4096, "start_layer": 8, "torch_dtype": "float32", "transformers_version": "4.42.2", "use_cache": true, "vocab_size": 256000 } ### Before submitting a new issue... - [x] Make sure you...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ": 4096, "start_layer": 8, "torch_dtype": "float32", "transformers_version": "4.42.2", "use_cache": true, "vocab_size": 256000 } ### Before submitting a new issue... - [x] Make sure you already searched for relevant iss...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: [Bug]: Model architectures ['CostWiseGemmaForCausalLM'] are not supported for now. bug;stale ### Your current environment Trying to Eror info: ValueError: Model architectures ['CostWiseGemmaForCausalLM'] are not support...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: weight--gemma_model.CostWiseGemmaForCausalLM" }, "attention_bias": false, "attention_dropout": 0.0, "attn_logit_softcapping": 50.0, "bos_token_id": 2, "cache_implementation": "hybrid", "eos_token_id": 1, "final_logit_so...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
