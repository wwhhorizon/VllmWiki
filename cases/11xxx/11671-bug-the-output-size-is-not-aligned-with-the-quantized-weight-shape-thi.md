# vllm-project/vllm#11671: [Bug]: The output size is not aligned with the quantized weight shape. This can be caused by too large tensor parallel size.

| 字段 | 值 |
| --- | --- |
| Issue | [#11671](https://github.com/vllm-project/vllm/issues/11671) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 17; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: The output size is not aligned with the quantized weight shape. This can be caused by too large tensor parallel size.

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I use the AWQ and GPTQ methods to quantify qwen2.5-32b for Qwen2ForSequenceClassification. And use vLLM-0.6.6 infer them. It should work in theory, but they don't seem to support it. group_size=128/64/32 ```python from vllm import LLM os.environ["CUDA_VISIBLE_DEVICES"] = "0,1" llm = LLM( model=qwen2.2-32b-cls-awq, task="classify", dtype="half", tensor_parallel_size=2, gpu_memory_utilization=0.98, trust_remote_code=True, max_model_len=1024, enforce_eager=True, ) tokenizer = llm.get_tokenizer() ``` ```json { "_name_or_path": "qwen2.5_32b_cls2", "architectures": [ "Qwen2ForSequenceClassification" ], "attention_dropout": 0.0, "bos_token_id": 151643, "eos_token_id": 151645, "hidden_act": "silu", "hidden_size": 5120, "initializer_range": 0.02, "intermediate_size": 27648, "max_position_embeddings": 32768, "max_window_layers": 70, "model_type": "qwen2", "num_attention_heads": 40, "num_hidden_layers": 64, "num_key_value_heads": 8, "quantization_config": { "bits": 4, "group_size": 128, "modules_to_not_convert": null, "quant_method": "awq", "version": "gemm", "zero_point": true }, "rms_norm_eps": 1e-06, "...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: [Bug]: The output size is not aligned with the quantized weight shape. This can be caused by too large tensor parallel size. bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: rge tensor parallel size. bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I use the AWQ and GPTQ methods to quantify qwen2.5-32b for Qwen2ForSequenceClassification. And...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: hey don't seem to support it. group_size=128/64/32 ```python from vllm import LLM os.environ["CUDA_VISIBLE_DEVICES"] = "0,1" llm = LLM( model=qwen2.2-32b-cls-awq, task="classify", dtype="half", tensor_parallel_size=2, g...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: rt it. group_size=128/64/32 ```python from vllm import LLM os.environ["CUDA_VISIBLE_DEVICES"] = "0,1" llm = LLM( model=qwen2.2-32b-cls-awq, task="classify", dtype="half", tensor_parallel_size=2, gpu_memory_utilization=0...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: _theta": 1000000.0, "sliding_window": null, "tie_word_embeddings": false, "torch_dtype": "bfloat16", "transformers_version": "4.46.3", "use_cache": false, "use_sliding_window": false, "vocab_size": 152064 } ``` ```sh --...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
