# vllm-project/vllm#14528: [Bug]: [V1] qwen2-vl broken for video inputs

| 字段 | 值 |
| --- | --- |
| Issue | [#14528](https://github.com/vllm-project/vllm/issues/14528) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;multimodal_vlm;quantization;sampling_logits |
| 子分类 | cold_start |
| Operator 关键词 | attention;cache;cuda;quantization;sampling |
| 症状 | crash;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: [V1] qwen2-vl broken for video inputs

### Issue 正文摘录

### Your current environment As per comment. other video models are fine (e.g. llava-next-video) ### 🐛 Describe the bug ```bash VLLM_USE_V1=1 pytest -v -s models/decoder_only/vision_language/test_models.py::test_video_models -k qwen2_vl ``` ```bash models/decoder_only/vision_language/test_models.py::test_video_models[qwen2_vl-test_case1] WARNING 03-10 01:17:17 [config.py:2571] Casting torch.bfloat16 to torch.float16. INFO 03-10 01:17:17 [config.py:576] This model supports multiple tasks: {'score', 'embed', 'classify', 'generate', 'reward'}. Defaulting to 'generate'. INFO 03-10 01:17:17 [config.py:1670] Chunked prefill is enabled with max_num_batched_tokens=16384. WARNING 03-10 01:17:17 [cuda.py:95] To see benefits of async output processing, enable CUDA graph. Since, enforce-eager is enabled, async output processor cannot be used INFO 03-10 01:17:21 [__init__.py:256] Automatically detected platform cuda. INFO 03-10 01:17:24 [core.py:51] Initializing a V1 LLM engine (v0.7.2) with config: model='Qwen/Qwen2-VL-2B-Instruct', speculative_config=None, tokenizer='Qwen/Qwen2-VL-2B-Instruct', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, override_neuron_config=None, tokeni...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: [Bug]: [V1] qwen2-vl broken for video inputs bug ### Your current environment As per comment. other video models are fine (e.g. llava-next-video) ### 🐛 Describe the bug ```bash VLLM_USE_V1=1 pytest -v -s models/decoder_...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: kwargs=None, pooler_config=None, compilation_config={"splitting_ops":[],"compile_sizes":[],"cudagraph_capture_sizes":[],"max_capture_size":0} INFO 03-10 01:17:24 [__init__.py:30] Available plugins for group vllm.general...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: en2_vl-test_case1] WARNING 03-10 01:17:17 [config.py:2571] Casting torch.bfloat16 to torch.float16. INFO 03-10 01:17:17 [config.py:576] This model supports multiple tasks: {'score', 'embed', 'classify', 'generate', 'rew...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: ideo) ### 🐛 Describe the bug ```bash VLLM_USE_V1=1 pytest -v -s models/decoder_only/vision_language/test_models.py::test_video_models -k qwen2_vl ``` ```bash models/decoder_only/vision_language/test_models.py::test_vide...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: uto, device_config=cuda, decoding_config=DecodingConfig(guided_decoding_backend='xgrammar', reasoning_backend=None), observability_config=ObservabilityConfig(show_hidden_metrics=False, otlp_traces_endpoint=None, collect...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
