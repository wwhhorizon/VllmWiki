# vllm-project/vllm#24147: [Bug]: model failure for OpenGVLab/InternVL3-38B-hf

| 字段 | 值 |
| --- | --- |
| Issue | [#24147](https://github.com/vllm-project/vllm/issues/24147) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;multimodal_vlm;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;mismatch;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: model failure for OpenGVLab/InternVL3-38B-hf

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Model failure on running OpenGVLab/InternVL3-38B-hf ``` base_model_path = "OpenGVLab/InternVL3-38B-hf" max_model_len = 65536 llm = LLM( model=base_model_path, dtype=torch.bfloat16, tensor_parallel_size=4, enable_chunked_prefill=True, enable_prefix_caching=True, max_model_len=max_model_len, rope_scaling={"factor": 2.0, "rope_type": "dynamic"}, rope_theta=1000000.0, trust_remote_code=True, download_dir='/mnt/efs/models_cache/' ) ``` ``` INFO 09-02 18:30:51 [__init__.py:241] Automatically detected platform cuda. INFO 09-02 18:32:21 [utils.py:326] non-default args: {'model': 'OpenGVLab/InternVL3_5-38B-HF', 'trust_remote_code': True, 'download_dir': '/mnt/efs/models_cache/', 'dtype': torch.bfloat16, 'max_model_len': 65536, 'tensor_parallel_size': 4, 'enable_prefix_caching': True, 'disable_log_stats': True, 'rope_scaling': {'factor': 2.0, 'rope_type': 'dynamic'}, 'rope_theta': 1000000.0, 'enable_chunked_prefill': True} The argument `trust_remote_code` is to be used with Auto classes. It has no effect here and is ignored. INFO 09-02 18:32:29 [__init__.py:742] Resolved architecture: InternVLForConditionalGeneration `torch_dtype` is depre...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 7: [Bug]: model failure for OpenGVLab/InternVL3-38B-hf bug;stale ### Your current environment ### 🐛 Describe the bug Model failure on running OpenGVLab/InternVL3-38B-hf ``` base_model_path = "OpenGVLab/InternVL3-38B-hf" ma...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: [Bug]: model failure for OpenGVLab/InternVL3-38B-hf bug;stale ### Your current environment ### 🐛 Describe the bug Model failure on running OpenGVLab/InternVL3-38B-hf ``` base_model_path = "OpenGVLab/InternVL3-38B-hf" ma...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 5: kv_cache_dtype=auto, device_config=cuda, decoding_config=DecodingConfig(backend='auto', disable_fallback=False, disable_any_whitespace=False, disable_additional_properties=False, reasoning_backend=''), observability_con...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: ! Use `dtype` instead! WARNING 09-02 18:32:29 [__init__.py:3012] User-specified max_model_len (65536) is greater than the derived max_model_len (max_position_embeddings=40960 or model_max_length=None in model's config.j...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: -38B-hf" max_model_len = 65536 llm = LLM( model=base_model_path, dtype=torch.bfloat16, tensor_parallel_size=4, enable_chunked_prefill=True, enable_prefix_caching=True, max_model_len=max_model_len, rope_scaling={"factor"...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
