# vllm-project/vllm#15120: [Installation]: v0.8.0 model_type error

| 字段 | 值 |
| --- | --- |
| Issue | [#15120](https://github.com/vllm-project/vllm/issues/15120) |
| 状态 | closed |
| 标签 | installation |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Installation]: v0.8.0 model_type error

### Issue 正文摘录

Even though Gemma2-27b model has model_type set in config.json, vllm docker container gives below error after v0.8.0: "ValueError: Unrecognized model in /app/model/gemma2. Should have a `model_type` key in its config.json" This is the default content on config.json: Model was downloaded from hf. { "architectures": [ "Gemma2ForCausalLM" ], "attention_bias": false, "attention_dropout": 0.0, "attn_logit_softcapping": 50.0, "bos_token_id": 2, "cache_implementation": "hybrid", "eos_token_id": 1, "final_logit_softcapping": 30.0, "head_dim": 128, "hidden_act": "gelu_pytorch_tanh", "hidden_activation": "gelu_pytorch_tanh", "hidden_size": 4608, "initializer_range": 0.02, "intermediate_size": 36864, "max_position_embeddings": 32768, "model_type": "gemma2", "num_attention_heads": 32, "num_hidden_layers": 46, "num_key_value_heads": 16, "pad_token_id": 0, "query_pre_attn_scalar": 144, "rms_norm_eps": 1e-06, "rope_theta": 160000.0, "sliding_window": 32768, "sliding_window_size": 4096, "torch_dtype": "bfloat16", "transformers_version": "4.42.0.dev0", "use_cache": true, "vocab_size": 256000, "_attn_implementation": "eager" } ### How you are installing vllm This is how i run vllm docker container:...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Installation]: v0.8.0 model_type error installation Even though Gemma2-27b model has model_type set in config.json, vllm docker container gives below error after v0.8.0: "ValueError: Unrecognized model in /app/model/ge...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [Installation]: v0.8.0 model_type error installation Even though Gemma2-27b model has model_type set in config.json, vllm docker container gives below error after v0.8.0: "ValueError: Unrecognized model in /app/model/gem
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: 00.0, "sliding_window": 32768, "sliding_window_size": 4096, "torch_dtype": "bfloat16", "transformers_version": "4.42.0.dev0", "use_cache": true, "vocab_size": 256000, "_attn_implementation": "eager" } ### How you are in...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: the default content on config.json: Model was downloaded from hf. { "architectures": [ "Gemma2ForCausalLM" ], "attention_bias": false, "attention_dropout": 0.0, "attn_logit_softcapping": 50.0, "bos_token_id": 2, "cache_...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: "architectures": [ "Gemma2ForCausalLM" ], "attention_bias": false, "attention_dropout": 0.0, "attn_logit_softcapping": 50.0, "bos_token_id": 2, "cache_implementation": "hybrid", "eos_token_id": 1, "final_logit_softcappi...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
