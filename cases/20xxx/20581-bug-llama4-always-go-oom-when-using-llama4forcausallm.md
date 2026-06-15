# vllm-project/vllm#20581: [Bug]: Llama4 always go OOM when using LLama4ForCausalLM

| 字段 | 值 |
| --- | --- |
| Issue | [#20581](https://github.com/vllm-project/vllm/issues/20581) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | activation_norm;attention_kv_cache;ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | activation;attention;cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf;oom |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Llama4 always go OOM when using LLama4ForCausalLM

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I have a fine-tuned text-only version of meta-llama/Llama-4-Scout-17B-16E, and I would like to inference with it on one node of 8xA100. The config.json file of this model is the following: ```{ "architectures": [ "Llama4ForCausalLM" ], "attention_bias": false, "attention_chunk_size": 8192, "attention_dropout": 0.0, "attn_scale": 0.1, "attn_temperature_tuning": 4, "bos_token_id": 200000, "cache_implementation": "hybrid", "eos_token_id": [ 200001, 200007, 200008 ], "floor_scale": 8192, "for_llm_compressor": false, "head_dim": 128, "hidden_act": "silu", "hidden_size": 5120, "initializer_range": 0.02, "interleave_moe_layer_step": 1, "intermediate_size": 8192, "intermediate_size_mlp": 16384, "max_position_embeddings": 262144, "model_type": "llama4_text", "moe_layers": [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47 ], "no_rope_layers": [ 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0 ], "num_attention_heads"...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: nt environment ### 🐛 Describe the bug I have a fine-tuned text-only version of meta-llama/Llama-4-Scout-17B-16E, and I would like to inference with it on one node of 8xA100. The config.json file of this model is the fol...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: lse, "attention_chunk_size": 8192, "attention_dropout": 0.0, "attn_scale": 0.1, "attn_temperature_tuning": 4, "bos_token_id": 200000, "cache_implementation": "hybrid", "eos_token_id": [ 200001, 200007, 200008 ], "floor_...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: -4-Scout-17B-16E, and I would like to inference with it on one node of 8xA100. The config.json file of this model is the following: ```{ "architectures": [ "Llama4ForCausalLM" ], "attention_bias": false, "attention_chun...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: Llama4 always go OOM when using LLama4ForCausalLM bug;stale ### Your current environment ### 🐛 Describe the bug I have a fine-tuned text-only version of meta-llama/Llama-4-Scout-17B-16E, and I would like to infer...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 4: silu", "hidden_size": 5120, "initializer_range": 0.02, "interleave_moe_layer_step": 1, "intermediate_size": 8192, "intermediate_size_mlp": 16384, "max_position_embeddings": 262144, "model_type": "llama4_text", "moe_laye...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
