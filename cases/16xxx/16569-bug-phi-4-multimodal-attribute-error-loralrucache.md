# vllm-project/vllm#16569: [Bug]: Phi-4-Multimodal Attribute error LoRALRUCache

| 字段 | 值 |
| --- | --- |
| Issue | [#16569](https://github.com/vllm-project/vllm/issues/16569) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm;quantization;sampling_logits |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Phi-4-Multimodal Attribute error LoRALRUCache

### Issue 正文摘录

### 🐛 Describe the bug vLLM Engine Version 0. Parameters: ``` {"tensor_parallel_size": 1, "limit_mm_per_prompt": {"image": 2}, "max_seq_len_to_capture": 131072, "enable_lora": true, "max_loras":1, "max_lora_rank": 320, "lora_modules": {"vision": "vision-lora"}} ``` Attribute error in LoRALRUCache ``` INFO 04-14 05:43:09 [__init__.py:239] Automatically detected platform cuda. INFO 04-14 05:43:10 [config.py:209] Replacing legacy 'type' key with 'rope_type' INFO 04-14 05:43:17 [config.py:600] This model supports multiple tasks: {'classify', 'generate', 'score', 'reward', 'embed'}. Defaulting to 'generate'. WARNING 04-14 05:43:17 [arg_utils.py:1708] ['Phi4MMForCausalLM'] is not supported by the V1 Engine. Falling back to V0. WARNING 04-14 05:43:17 [arg_utils.py:1581] The model has a long context length (131072). This may causeOOM during the initial memory profiling phase, or result in low performance due to small KV cache size. Consider setting --max-model-len to a smaller value. INFO 04-14 05:43:17 [llm_engine.py:242] Initializing a V0 LLM engine (v0.8.3) with config: model='/models/Phi-4-multimodal-instruct', speculative_config=None, tokenizer='/models/Phi-4-multimodal-instruct', sk...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: dal Attribute error LoRALRUCache bug ### 🐛 Describe the bug vLLM Engine Version 0. Parameters: ``` {"tensor_parallel_size": 1, "limit_mm_per_prompt": {"image": 2}, "max_seq_len_to_capture": 131072, "enable_lora": true,...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: Phi-4-Multimodal Attribute error LoRALRUCache bug ### 🐛 Describe the bug vLLM Engine Version 0. Parameters: ``` {"tensor_parallel_size": 1, "limit_mm_per_prompt": {"image": 2}, "max_seq_len_to_capture": 131072, "...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: uto, device_config=cuda, decoding_config=DecodingConfig(guided_decoding_backend='xgrammar', reasoning_backend=None), observability_config=ObservabilityConfig(show_hidden_metrics=False, otlp_traces_endpoint=None, collect...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: ide_neuron_config=None, tokenizer_revision=None, trust_remote_code=True, dtype=torch.bfloat16, max_seq_len=131072, download_dir=None, load_format=auto, tensor_parallel_size=1, pipeline_parallel_size=1, disable_custom_al...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: engine (v0.8.3) with config: model='/models/Phi-4-multimodal-instruct', speculative_config=None, tokenizer='/models/Phi-4-multimodal-instruct', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, override_neu...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
