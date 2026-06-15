# vllm-project/vllm#14523: [Bug]: [V1] `llava-hf/llava-1.5-7b-hf` is broken on V1

| 字段 | 值 |
| --- | --- |
| Issue | [#14523](https://github.com/vllm-project/vllm/issues/14523) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;distributed_parallel;frontend_api;model_support;multimodal_vlm;quantization;sampling_logits |
| 子分类 | cold_start |
| Operator 关键词 | attention;cuda;fp8;quantization;sampling |
| 症状 | crash;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: [V1] `llava-hf/llava-1.5-7b-hf` is broken on V1

### Issue 正文摘录

### Your current environment `llava-hf/llava-1.5-7b-hf` is broken on V1 Other `LlavaForConditionalGeneration` models seem to work (e.g. https://huggingface.co/neuralmagic/pixtral-12b-FP8-dynamic) ### 🐛 Describe the bug ```bash VLLM_USE_V1=1 python3 examples/offline_inference/vision_language.py -m llava ``` ```bash INFO 03-09 15:25:45 [__init__.py:256] Automatically detected platform cuda. INFO 03-09 15:25:47 [__init__.py:30] Available plugins for group vllm.general_plugins: INFO 03-09 15:25:47 [__init__.py:32] name=register_dummy_model, value=vllm_add_dummy_model:register INFO 03-09 15:25:47 [__init__.py:34] all available plugins for group vllm.general_plugins will be loaded. INFO 03-09 15:25:47 [__init__.py:36] set environment variable VLLM_PLUGINS to control which plugins to load. INFO 03-09 15:25:47 [__init__.py:44] plugin register_dummy_model loaded. INFO 03-09 15:25:54 [config.py:576] This model supports multiple tasks: {'score', 'classify', 'generate', 'reward', 'embed'}. Defaulting to 'generate'. INFO 03-09 15:25:55 [config.py:1670] Chunked prefill is enabled with max_num_batched_tokens=16384. INFO 03-09 15:25:55 [core.py:51] Initializing a V1 LLM engine (v0.7.2) with confi...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 7: [Bug]: [V1] `llava-hf/llava-1.5-7b-hf` is broken on V1 bug ### Your current environment `llava-hf/llava-1.5-7b-hf` is broken on V1 Other `LlavaForConditionalGeneration` models seem to work (e.g. https://huggingface.co/n...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: models seem to work (e.g. https://huggingface.co/neuralmagic/pixtral-12b-FP8-dynamic) ### 🐛 Describe the bug ```bash VLLM_USE_V1=1 python3 examples/offline_inference/vision_language.py -m llava ``` ```bash INFO 03-09 15...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: uto, device_config=cuda, decoding_config=DecodingConfig(guided_decoding_backend='xgrammar', reasoning_backend=None), observability_config=ObservabilityConfig(show_hidden_metrics=False, otlp_traces_endpoint=None, collect...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: ed_attention","vllm.unified_attention_with_output"],"use_inductor":true,"compile_sizes":[],"use_cudagraph":true,"cudagraph_num_of_warmups":1,"cudagraph_capture_sizes":[512,504,496,488,480,472,464,456,448,440,432,424,416...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: . Defaulting to 'generate'. INFO 03-09 15:25:55 [config.py:1670] Chunked prefill is enabled with max_num_batched_tokens=16384. INFO 03-09 15:25:55 [core.py:51] Initializing a V1 LLM engine (v0.7.2) with config: model='l...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
