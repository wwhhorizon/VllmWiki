# vllm-project/vllm#16121: [Bug]: assert self.quant_method is not None error when using llama scout 4bit

| 字段 | 值 |
| --- | --- |
| Issue | [#16121](https://github.com/vllm-project/vllm/issues/16121) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;moe;quantization |
| 子分类 | debug |
| Operator 关键词 | attention;cuda;moe;operator;quantization |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: assert self.quant_method is not None error when using llama scout 4bit

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Error while running vllm 0.8.3 llama scout 4bit I am running vllm like so: "python3 -m vllm.entrypoints.openai.api_server --model unsloth/Llama-4-Scout-17B-16E-Instruct-unsloth-bnb-4bit --served-model-name Llama-4-Scout --port 9000 --max-model-len 100000" And also like so: "python3 -m vllm.entrypoints.openai.api_server --model unsloth/Llama-4-Scout-17B-16E-Instruct-unsloth-bnb-4bit --served-model-name Llama-4-Scout --port 9000 --max-model-len 100000 --quantization bitsandbytes" But both give me the following error ``` INFO 04-06 00:57:19 [core.py:61] Initializing a V1 LLM engine (v0.8.3) with config: model='unsloth/Llama-4-Scout-17B-16E-Instruct-unsloth-bnb-4bit', speculative_config=None, tokenizer='unsloth/Llama-4-Scout-17B-16E-Instruct-unsloth-bnb-4bit', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, override_neuron_config=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.bfloat16, max_seq_len=100000, download_dir=None, load_format=LoadFormat.BITSANDBYTES, tensor_parallel_size=1, pipeline_parallel_size=1, disable_custom_all_reduce=False, quantization=bitsandbytes, enforce_eager=False, kv_cache_...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: ed_attention","vllm.unified_attention_with_output"],"use_inductor":true,"compile_sizes":[],"use_cudagraph":true,"cudagraph_num_of_warmups":1,"cudagraph_capture_sizes":[512,504,496,488,480,472,464,456,448,440,432,424,416...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: [Bug]: assert self.quant_method is not None error when using llama scout 4bit bug ### Your current environment ### 🐛 Describe the bug Error while running vllm 0.8.3 llama scout 4bit I am running vllm like so: "python3 -...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: assert self.quant_method is not None error when using llama scout 4bit bug ### Your current environment ### 🐛 Describe the bug Error while running vllm 0.8.3 llama scout 4bit I am running vllm like so: "python3 -...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: uto, device_config=cuda, decoding_config=DecodingConfig(guided_decoding_backend='xgrammar', reasoning_backend=None), observability_config=ObservabilityConfig(show_hidden_metrics=False, otlp_traces_endpoint=None, collect...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: vllm like so: "python3 -m vllm.entrypoints.openai.api_server --model unsloth/Llama-4-Scout-17B-16E-Instruct-unsloth-bnb-4bit --served-model-name Llama-4-Scout --port 9000 --max-model-len 100000" And also like so: "pytho...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
