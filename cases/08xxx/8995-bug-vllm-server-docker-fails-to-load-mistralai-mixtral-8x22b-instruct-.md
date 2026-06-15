# vllm-project/vllm#8995: [Bug]: Vllm server (docker) fails to load mistralai/Mixtral-8x22B-Instruct-v0.1

| 字段 | 值 |
| --- | --- |
| Issue | [#8995](https://github.com/vllm-project/vllm/issues/8995) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;frontend_api;model_support;quantization |
| 子分类 | install |
| Operator 关键词 | cuda;fp8;quantization |
| 症状 | crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Vllm server (docker) fails to load mistralai/Mixtral-8x22B-Instruct-v0.1

### Issue 正文摘录

### Your current environment docker pull vllm/vllm-openai:v0.6.2 ### Model Input Dumps docker run --runtime nvidia --gpus all \ -v ~/.cache/huggingface:/root/.cache/huggingface \ --env "HUGGING_FACE_HUB_TOKEN= " \ -p 8000:8000 \ --ipc=host \ vllm/vllm-openai:latest \ --model mistralai/Mixtral-8x22B-Instruct-v0.1 \ --tokenizer-mode mistral ### 🐛 Describe the bug INFO 10-01 10:05:31 llm_engine.py:226] Initializing an LLM engine (v0.6.1.dev238+ge2c6e0a82) with config: model='mistralai/Mixtral-8x22B-Instruct-v0.1', speculative_config=None, tokenizer='mistralai/Mixtral-8x22B-Instruct-v0.1', skip_tokenizer_init=False, tokenizer_mode=mistral, revision=main, override_neuron_config=None, rope_scaling=None, rope_theta=None, tokenizer_revision=main, trust_remote_code=True, dtype=torch.bfloat16, max_seq_len=4096, download_dir=None, load_format=LoadFormat.AUTO, tensor_parallel_size=4, pipeline_parallel_size=1, disable_custom_all_reduce=False, quantization=fp8, enforce_eager=False, kv_cache_dtype=auto, quantization_param_path=None, device_config=cuda, decoding_config=DecodingConfig(guided_decoding_backend='outlines'), observability_config=ObservabilityConfig(otlp_traces_endpoint=None, collect_m...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: =None, rope_theta=None, tokenizer_revision=main, trust_remote_code=True, dtype=torch.bfloat16, max_seq_len=4096, download_dir=None, load_format=LoadFormat.AUTO, tensor_parallel_size=4, pipeline_parallel_size=1, disable_...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: g ### Your current environment docker pull vllm/vllm-openai:v0.6.2 ### Model Input Dumps docker run --runtime nvidia --gpus all \ -v ~/.cache/huggingface:/root/.cache/huggingface \ --env "HUGGING_FACE_HUB_TOKEN= " \ -p...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [Bug]: Vllm server (docker) fails to load mistralai/Mixtral-8x22B-Instruct-v0.1 bug ### Your current environment docker pull vllm/vllm-openai:v0.6.2 ### Model Input Dumps docker run --runtime nvidia --gpus all \ -v ~/.c...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: =False, kv_cache_dtype=auto, quantization_param_path=None, device_config=cuda, decoding_config=DecodingConfig(guided_decoding_backend='outlines'), observability_config=ObservabilityConfig(otlp_traces_endpoint=None, coll...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: tokenizer='mistralai/Mixtral-8x22B-Instruct-v0.1', skip_tokenizer_init=False, tokenizer_mode=mistral, revision=main, override_neuron_config=None, rope_scaling=None, rope_theta=None, tokenizer_revision=main, trust_remote...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
