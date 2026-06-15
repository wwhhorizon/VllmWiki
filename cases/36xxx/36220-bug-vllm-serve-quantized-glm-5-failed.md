# vllm-project/vllm#36220: [Bug]: vllm serve quantized GLM-5 failed

| 字段 | 值 |
| --- | --- |
| Issue | [#36220](https://github.com/vllm-project/vllm/issues/36220) |
| 状态 | open |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | activation_norm;attention_kv_cache;distributed_parallel;gemm_linear;model_support;moe;quantization |
| 子分类 | runtime_err |
| Operator 关键词 | activation;attention;cuda;moe;operator;quantization |
| 症状 | crash |
| 根因提示 | dtype |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vllm serve quantized GLM-5 failed

### Issue 正文摘录

### Your current environment 1. vllm serve指令 ``` vllm serve /mnt/nvme/liaotj/zhujy/llm-compressor/examples/awq/glm5_bf16-W4A16-SYM-AWQ-cuda-compressed-tensors \ --tensor-parallel-size 8 \ --host \ --port \ --no-enable-prefix-caching \ --max_num_seqs 32 \ ``` 2. 使用llm-compressor量化工具quantized GLM-5(awq+int4)‘s config.json ``` "architectures": [ "GlmMoeDsaForCausalLM" ], "attention_bias": false, "attention_dropout": 0.0, "bos_token_id": 0, "dtype": "bfloat16", "eos_token_id": [ 154820, 154827, 154829 ], "ep_size": 1, "first_k_dense_replace": 3, "head_dim": 64, "hidden_act": "silu", "hidden_size": 6144, "index_head_dim": 128, "index_n_heads": 32, "index_topk": 2048, "indexer_rope_interleave": true, "initializer_range": 0.02, "intermediate_size": 12288, "kv_lora_rank": 512, "max_position_embeddings": 202752, "mlp_layer_types": [ "dense", "dense", "dense", "sparse", "sparse", "sparse", "sparse", "sparse", "sparse", "sparse", "sparse", "sparse", "sparse", "sparse", "sparse", "sparse", "sparse", "sparse", "sparse", "sparse", "sparse", "sparse", "sparse", "sparse", "sparse", "sparse", "sparse", "sparse", "sparse", "sparse", "sparse", "sparse", "sparse", "sparse", "sparse", "sparse", "spars...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 7: [Bug]: vllm serve quantized GLM-5 failed bug ### Your current environment 1. vllm serve指令 ``` vllm serve /mnt/nvme/liaotj/zhujy/llm-compressor/examples/awq/glm5_bf16-W4A16-SYM-AWQ-cuda-compressed-tensors \ --tensor-para...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 4: uantized GLM-5(awq+int4)‘s config.json ``` "architectures": [ "GlmMoeDsaForCausalLM" ], "attention_bias": false, "attention_dropout": 0.0, "bos_token_id": 0, "dtype": "bfloat16", "eos_token_id": [ 154820, 154827, 154829...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ax_num_seqs 32 \ ``` 2. 使用llm-compressor量化工具quantized GLM-5(awq+int4)‘s config.json ``` "architectures": [ "GlmMoeDsaForCausalLM" ], "attention_bias": false, "attention_dropout": 0.0, "bos_token_id": 0, "dtype": "bfloat...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: 55282) INFO 03-04 10:54:11 [cuda.py:367] Using FLASHMLA_SPARSE attention backend out of potential backends: ['FLASHMLA_SPARSE']. (Worker_TP6 pid=1955291) INFO 03-04 10:54:11 [compressed_tensors_moe.py:198] Using Compres...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: compressed", "sparsity_config": {}, "transform_config": {}, "version": "0.13.1.a20260225" }, "rms_norm_eps": 1e-05, "rope_interleave": true, "rope_parameters": { "rope_theta": 1000000, "rope_type": "default" }, "routed_...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
