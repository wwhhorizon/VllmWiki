# vllm-project/vllm#2518: rope scaling doesn't work

| 字段 | 值 |
| --- | --- |
| Issue | [#2518](https://github.com/vllm-project/vllm/issues/2518) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> rope scaling doesn't work

### Issue 正文摘录

I'm trying to use rope scaling to increase the `max_seq_len`. I refer to #555 and modify the model's config.json to add the key `rope_scaling`: ``` json { "_name_or_path": "m42-health/med42-70b", "architectures": [ "LlamaForCausalLM" ], "bos_token_id": 1, "eos_token_id": 2, "hidden_act": "silu", "hidden_size": 8192, "initializer_range": 0.02, "intermediate_size": 28672, "max_position_embeddings": 2048, "model_type": "llama", "num_attention_heads": 64, "num_hidden_layers": 80, "num_key_value_heads": 8, "pad_token_id": 0, "rms_norm_eps": 1e-05, "tie_word_embeddings": false, "torch_dtype": "float32", "transformers_version": "4.28.1", "use_cache": true, "vocab_size": 32000, "rope_scaling": { "factor": 2.0, "type": "dynamic" } } ``` And I initiated vLLM engine by ```python cache_dir = "/secure/hf_cache" model_name_or_path = "m42-health/med42-70b" llm = LLM(model=model_name_or_path, download_dir=cache_dir, tensor_parallel_size=4, dtype="auto") ``` However, when I performed inference on long prompts, I still got the warning: ``` WARNING 01-20 16:48:15 scheduler.py:149] Input prompt (2380 tokens) is too long and exceeds limit of 2048 ``` Does anyone have this issue before? p.s., version o...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: pe scaling to increase the `max_seq_len`. I refer to #555 and modify the model's config.json to add the key `rope_scaling`: ``` json { "_name_or_path": "m42-health/med42-70b", "architectures": [ "LlamaForCausalLM" ], "b...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: d": 0, "rms_norm_eps": 1e-05, "tie_word_embeddings": false, "torch_dtype": "float32", "transformers_version": "4.28.1", "use_cache": true, "vocab_size": 32000, "rope_scaling": { "factor": 2.0, "type": "dynamic" } } ```...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: tie_word_embeddings": false, "torch_dtype": "float32", "transformers_version": "4.28.1", "use_cache": true, "vocab_size": 32000, "rope_scaling": { "factor": 2.0, "type": "dynamic" } } ``` And I initiated vLLM engine by...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: rope_scaling`: ``` json { "_name_or_path": "m42-health/med42-70b", "architectures": [ "LlamaForCausalLM" ], "bos_token_id": 1, "eos_token_id": 2, "hidden_act": "silu", "hidden_size": 8192, "initializer_range": 0.02, "in...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: "pad_token_id": 0, "rms_norm_eps": 1e-05, "tie_word_embeddings": false, "torch_dtype": "float32", "transformers_version": "4.28.1", "use_cache": true, "vocab_size": 32000, "rope_scaling": { "factor": 2.0, "type": "dynam...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
