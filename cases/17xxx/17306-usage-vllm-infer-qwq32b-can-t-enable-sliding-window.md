# vllm-project/vllm#17306: [Usage]:  vllm infer QWQ32B can‘t enable sliding window

| 字段 | 值 |
| --- | --- |
| Issue | [#17306](https://github.com/vllm-project/vllm/issues/17306) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]:  vllm infer QWQ32B can‘t enable sliding window

### Issue 正文摘录

### Your current environment 工具： Vllm=0.8.4 模型：Qwq32B 配置： { "architectures": [ "Qwen2ForCausalLM" ], "attention_dropout": 0.0, "bos_token_id": 151643, "eos_token_id": 151645, "hidden_act": "silu", "hidden_size": 5120, "initializer_range": 0.02, "intermediate_size": 27648, "max_position_embeddings": 40960, "max_window_layers": 64, "model_type": "qwen2", "num_attention_heads": 40, "num_hidden_layers": 64, "num_key_value_heads": 8, "rms_norm_eps": 1e-05, "rope_theta": 1000000.0, "sliding_window": 40960, "tie_word_embeddings": false, "torch_dtype": "bfloat16", "transformers_version": "4.43.1", "use_cache": true, "use_sliding_window": true, "vocab_size": 152064 } 启动命令： python -m vllm.entrypoints.openai.api_server --model /home/user/Models/QwQ-32B --host "::" --port 8600 --tensor-parallel-size 8 --gpu-memory-utilization 0.95 --max-model-len 40960 --dtype bfloat16 --max-num-seqs 16 --served-model-name qwq32b --swap-space 10 --enable_prefix_caching --enable-chunked-prefill --use-v2-block-manager --enforce-eager --disable-custom-all-reduce --trust-remote-code 错误信息： (VllmWorker rank=1 pid=3457224) raise ValueError("Sliding window for some but all layers is not " (VllmWorker rank=1 pid=34572...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: 1000000.0, "sliding_window": 40960, "tie_word_embeddings": false, "torch_dtype": "bfloat16", "transformers_version": "4.43.1", "use_cache": true, "use_sliding_window": true, "vocab_size": 152064 } 启动命令： python -m vllm.e...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: current environment 工具： Vllm=0.8.4 模型：Qwq32B 配置： { "architectures": [ "Qwen2ForCausalLM" ], "attention_dropout": 0.0, "bos_token_id": 151643, "eos_token_id": 151645, "hidden_act": "silu", "hidden_size": 5120, "initializ...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: ope_theta": 1000000.0, "sliding_window": 40960, "tie_word_embeddings": false, "torch_dtype": "bfloat16", "transformers_version": "4.43.1", "use_cache": true, "use_sliding_window": true, "vocab_size": 152064 } 启动命令： pyth...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: , "tie_word_embeddings": false, "torch_dtype": "bfloat16", "transformers_version": "4.43.1", "use_cache": true, "use_sliding_window": true, "vocab_size": 152064 } 启动命令： python -m vllm.entrypoints.openai.api_server --mod...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ndow usage ### Your current environment 工具： Vllm=0.8.4 模型：Qwq32B 配置： { "architectures": [ "Qwen2ForCausalLM" ], "attention_dropout": 0.0, "bos_token_id": 151643, "eos_token_id": 151645, "hidden_act": "silu", "hidden_siz...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
