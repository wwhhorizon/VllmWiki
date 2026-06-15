# vllm-project/vllm#19018: [Bug]:RuntimeError: CUDA error: no kernel image is available for execution on the device

| 字段 | 值 |
| --- | --- |
| Issue | [#19018](https://github.com/vllm-project/vllm/issues/19018) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 14; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;crash;mismatch;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]:RuntimeError: CUDA error: no kernel image is available for execution on the device

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When I run this code, my machine reports an error examples/offline_inference/prompt_embed_inference.py error: ```python INFO 06-02 16:56:19 [__init__.py:243] Automatically detected platform cuda. Loading checkpoint shards: 100%|██████████████████| 4/4 [00:02 vllm.plugins.lora_resolvers.filesystem_resolver:register_filesystem_resolver INFO 06-02 16:56:23 [__init__.py:36] All plugins in this group will be loaded. Set `VLLM_PLUGINS` to control which plugins to load. INFO 06-02 16:56:28 [config.py:793] This model supports multiple tasks: {'generate', 'reward', 'classify', 'embed', 'score'}. Defaulting to 'generate'. WARNING 06-02 16:56:28 [arg_utils.py:1583] --enable-prompt-embeds is not supported by the V1 Engine. Falling back to V0. WARNING 06-02 16:56:28 [arg_utils.py:1420] Chunked prefill is enabled by default for models with max_model_len > 32K. Chunked prefill might not work with some features or models. If you encounter any issues, please disable by launching with --enable-chunked-prefill=False. INFO 06-02 16:56:28 [config.py:2118] Chunked prefill is enabled with max_num_batched_tokens=2048. INFO 06-02 16:56:28 [llm_engine.py:...

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 5: kv_cache_dtype=auto, device_config=cuda, decoding_config=DecodingConfig(backend='auto', disable_fallback=False, disable_any_whitespace=False, disable_additional_properties=False, reasoning_backend=''), observability_con...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: nd=''), observability_config=ObservabilityConfig(show_hidden_metrics_for_version=None, otlp_traces_endpoint=None, collect_detailed_traces=None), seed=0, served_model_name=Meta-Llama-3.1-8B, num_scheduler_steps=1, multi_...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: ride_neuron_config={}, tokenizer_revision=None, trust_remote_code=False, dtype=torch.bfloat16, max_seq_len=131072, download_dir=None, load_format=LoadFormat.AUTO, tensor_parallel_size=1, pipeline_parallel_size=1, disabl...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: et `VLLM_PLUGINS` to control which plugins to load. INFO 06-02 16:56:28 [config.py:793] This model supports multiple tasks: {'generate', 'reward', 'classify', 'embed', 'score'}. Defaulting to 'generate'. WARNING 06-02 1...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: CUDA error: no kernel image is available for execution on the device bug;stale ### Your current environment ### 🐛 Describe the bug When I run this code, my machine reports an error examples/offline_inference/prompt_embe...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
