# vllm-project/vllm#25865: [Bug]: vLLM recognize the bge-m3-korean (embedding model) max length, 512 tokens.

| 字段 | 值 |
| --- | --- |
| Issue | [#25865](https://github.com/vllm-project/vllm/issues/25865) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: vLLM recognize the bge-m3-korean (embedding model) max length, 512 tokens.

### Issue 正文摘录

### Your current environment vLLM 0.10.2 ### 🐛 Describe the bug bge-m3-korean config.json { -- "architectures": [ "XLMRobertaModel" ], "attention_probs_dropout_prob": 0.1, "bos_token_id": 0, "classifier_dropout": null, "eos_token_id": 2, "hidden_act": "gelu", "hidden_dropout_prob": 0.1, "hidden_size": 1024, "initializer_range": 0.02, "intermediate_size": 4096, "layer_norm_eps": 1e-05, "max_position_embeddings": 8194, "model_type": "xlm-roberta", "num_attention_heads": 16, "num_hidden_layers": 24, "output_past": true, "pad_token_id": 1, "position_embedding_type": "absolute", "torch_dtype": "float32", "transformers_version": "4.42.4", "type_vocab_size": 1, "use_cache": true, "vocab_size": 250002 } vLLM recognize the bge-m3-korean (embedding model) max length, 512 tokens despite of the config.json above. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: : true, "pad_token_id": 1, "position_embedding_type": "absolute", "torch_dtype": "float32", "transformers_version": "4.42.4", "type_vocab_size": 1, "use_cache": true, "vocab_size": 250002 } vLLM recognize the bge-m3-kor...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: vLLM recognize the bge-m3-korean (embedding model) max length, 512 tokens. bug;stale ### Your current environment vLLM 0.10.2 ### 🐛 Describe the bug bge-m3-korean config.json { -- "architectures": [ "XLMRobertaMo...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ion_embedding_type": "absolute", "torch_dtype": "float32", "transformers_version": "4.42.4", "type_vocab_size": 1, "use_cache": true, "vocab_size": 250002 } vLLM recognize the bge-m3-korean (embedding model) max length,...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: nt vLLM 0.10.2 ### 🐛 Describe the bug bge-m3-korean config.json { -- "architectures": [ "XLMRobertaModel" ], "attention_probs_dropout_prob": 0.1, "bos_token_id": 0, "classifier_dropout": null, "eos_token_id": 2, "hidden...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ecognize the bge-m3-korean (embedding model) max length, 512 tokens. bug;stale ### Your current environment vLLM 0.10.2 ### 🐛 Describe the bug bge-m3-korean config.json { -- "architectures": [ "XLMRobertaModel" ], "atte...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
