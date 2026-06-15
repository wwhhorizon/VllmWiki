# vllm-project/vllm#7561: [Bug]: Llama3.1 casting torch.bfloat16 to torch.float16

| 字段 | 值 |
| --- | --- |
| Issue | [#7561](https://github.com/vllm-project/vllm/issues/7561) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Llama3.1 casting torch.bfloat16 to torch.float16

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I've downloaded Llama 3.1 8B Instruct from Huggingface and am attempting to host using Ray and vLLM. Examining the snapshot's `config.json`, I can confirm that the underlying `torch_dtype` is `bfloat16`. ``` { "architectures": [ "LlamaForCausalLM" ], "attention_bias": false, "attention_dropout": 0.0, "bos_token_id": 128000, "eos_token_id": [ 128001, 128008, 128009 ], "hidden_act": "silu", "hidden_size": 8192, "initializer_range": 0.02, "intermediate_size": 28672, "max_position_embeddings": 131072, "mlp_bias": false, "model_type": "llama", "num_attention_heads": 64, "num_hidden_layers": 80, "num_key_value_heads": 8, "pretraining_tp": 1, "rms_norm_eps": 1e-05, "rope_scaling": { "factor": 8.0, "low_freq_factor": 1.0, "high_freq_factor": 4.0, "original_max_position_embeddings": 8192, "rope_type": "llama3" }, "rope_theta": 500000.0, "tie_word_embeddings": false, "torch_dtype": "bfloat16", "transformers_version": "4.42.3", "use_cache": true, "vocab_size": 128256 } ``` In addition, I'm passing `--dtype=bfloat16` to `vllm serve`. ``` vllm serve "/root/.cache/huggingface/hub/models--${SNAPSHOT_DIR}/snapshots/$SNAPSHOT" \ --tensor-parallel...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: Llama3.1 casting torch.bfloat16 to torch.float16 bug ### Your current environment ### 🐛 Describe the bug I've downloaded Llama 3.1 8B Instruct from Huggingface and am attempting to host using Ray and vLLM. Examin...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Bug]: Llama3.1 casting torch.bfloat16 to torch.float16 bug ### Your current environment ### 🐛 Describe the bug I've downloaded Llama 3.1 8B Instruct from Huggingface and am attempting to host using Ray and vLLM. Examin...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: I can confirm that the underlying `torch_dtype` is `bfloat16`. ``` { "architectures": [ "LlamaForCausalLM" ], "attention_bias": false, "attention_dropout": 0.0, "bos_token_id": 128000, "eos_token_id": [ 128001, 128008,...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: =4 \ --pipeline-parallel-size=1 \ --distributed-executor-backend=ray \ --dtype=bfloat16 ``` However, for some reason, I'm seeing this log line: `WARNING 08-15 16:32:35 config.py:1454] Casting torch.bfloat16 to torch.flo...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ie_word_embeddings": false, "torch_dtype": "bfloat16", "transformers_version": "4.42.3", "use_cache": true, "vocab_size": 128256 } ``` In addition, I'm passing `--dtype=bfloat16` to `vllm serve`. ``` vllm serve "/root/....

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
