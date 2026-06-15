# vllm-project/vllm#34505: [Bug]: Qwen 2.5 Omni cuda graph has error

| 字段 | 值 |
| --- | --- |
| Issue | [#34505](https://github.com/vllm-project/vllm/issues/34505) |
| 状态 | open |
| 标签 | bug;stale |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;multimodal_vlm;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Qwen 2.5 Omni cuda graph has error

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When running the examples/offline_inference/qwen2_5_omni/only_thinker.py, there will be a scheduler buffer size error: ```bash /scratch/dyvm6xra/dyvm6xrauser49/rebase/.venv/lib/python3.12/site-packages/transformers/utils/hub.py:110: FutureWarning: Using `TRANSFORMERS_CACHE` is deprecated and will be removed in v5 of Transformers. Use `HF_HOME` instead. warnings.warn( INFO 02-13 08:22:43 [utils.py:223] non-default args: {'max_model_len': 5632, 'max_num_seqs': 5, 'disable_log_stats': True, 'limit_mm_per_prompt': {'audio': 1, 'image': 1, 'video': 1}, 'model': 'Qwen/Qwen2.5-Omni-7B'} Unrecognized keys in `rope_scaling` for 'rope_type'='default': {'mrope_section'} INFO 02-13 08:22:59 [model.py:529] Resolved architecture: Qwen2_5OmniModel INFO 02-13 08:22:59 [model.py:1549] Using max model len 5632 INFO 02-13 08:23:00 [scheduler.py:224] Chunked prefill is enabled with max_num_batched_tokens=16384. INFO 02-13 08:23:00 [vllm.py:689] Asynchronous scheduling is enabled. The image processor of type `Qwen2VLImageProcessor` is now loaded as a fast processor by default, even if the model checkpoint was saved with a slow processor. This is a br...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 7: [Bug]: Qwen 2.5 Omni cuda graph has error bug;stale ### Your current environment ### 🐛 Describe the bug When running the examples/offline_inference/qwen2_5_omni/only_thinker.py, there will be a scheduler buffer size err...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: [Bug]: Qwen 2.5 Omni cuda graph has error bug;stale ### Your current environment ### 🐛 Describe the bug When running the examples/offline_inference/qwen2_5_omni/only_thinker.py, there will be a scheduler buffer size err...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 5: o, device_config=cuda, structured_outputs_config=StructuredOutputsConfig(backend='auto', disable_fallback=False, disable_any_whitespace=False, disable_additional_properties=False, reasoning_parser='', reasoning_parser_p...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: False), observability_config=ObservabilityConfig(show_hidden_metrics_for_version=None, otlp_traces_endpoint=None, collect_detailed_traces=None, kv_cache_metrics=False, kv_cache_metrics_sample=0.01, cudagraph_metrics=Fal...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: e=auto, revision=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.bfloat16, max_seq_len=5632, download_dir=None, load_format=auto, tensor_parallel_size=1, pipeline_parallel_size=1, data_parallel_size=...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
