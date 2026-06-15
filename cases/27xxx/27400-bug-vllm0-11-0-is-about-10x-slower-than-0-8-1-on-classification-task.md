# vllm-project/vllm#27400: [Bug]: vLLM0.11.0 is about 10x slower than 0.8.1 on classification task

| 字段 | 值 |
| --- | --- |
| Issue | [#27400](https://github.com/vllm-project/vllm/issues/27400) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | activation_norm;attention_kv_cache;ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits |
| 子分类 | precision |
| Operator 关键词 | activation;cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vLLM0.11.0 is about 10x slower than 0.8.1 on classification task

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I am comparing v0.11.0 and v0.8.1 on a very simple classification usage the code is ``` llm = LLM(model_path, task="classify", dtype="half", gpu_memory_utilization=0.8, max_num_seqs=32768, max_num_batched_tokens = 32768, max_model_len=8192, ) llm.classify(prompts) ``` On v0.11.0 I got 1.43it/s and on v0.8.1, I got 10it/s. The difference is huge. I tried it several times on different machine. The input and model are exactly the same and the only difference is vllm version (transformers version are also changed since the latest transformers cannot work together with v0.11.0). I can't share the model itself, but below is the config of the model ```{ "architectures": [ "MistralForCausalLM" ], "attention_dropout": 0.0, "bos_token_id": 1, "eos_token_id": 2, "hidden_act": "silu", "hidden_size": 4096, "initializer_range": 0.02, "intermediate_size": 14336, "max_position_embeddings": 32768, "model_type": "mistral", "num_attention_heads": 32, "num_hidden_layers": 32, "num_key_value_heads": 8, "rms_norm_eps": 1e-05, "rope_theta": 10000.0, "sliding_window": 4096, "tie_word_embeddings": false, "torch_dtype": "bfloat16", "transformers_version":...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: The input and model are exactly the same and the only difference is vllm version (transformers version are also changed since the latest transformers cannot work together with v0.11.0). I can't share the model itself, b...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: is ``` llm = LLM(model_path, task="classify", dtype="half", gpu_memory_utilization=0.8, max_num_seqs=32768, max_num_batched_tokens = 32768, max_model_len=8192, ) llm.classify(prompts) ``` On v0.11.0 I go
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: n't share the model itself, but below is the config of the model ```{ "architectures": [ "MistralForCausalLM" ], "attention_dropout": 0.0, "bos_token_id": 1, "eos_token_id": 2, "hidden_act": "silu", "hidden_size": 4096,...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: d v0.8.1 on a very simple classification usage the code is ``` llm = LLM(model_path, task="classify", dtype="half", gpu_memory_utilization=0.8, max_num_seqs=32768, max_num_batched_tokens = 32768, max_model_len=8192,
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: _porting;model_support;sampling_logits activation;cuda;operator;sampling;triton build_error;nan_inf;slowdown dtype;env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
