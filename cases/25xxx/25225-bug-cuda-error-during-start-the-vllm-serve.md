# vllm-project/vllm#25225: [Bug]: CUDA error during start the vllm serve

| 字段 | 值 |
| --- | --- |
| Issue | [#25225](https://github.com/vllm-project/vllm/issues/25225) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;multimodal_vlm;quantization;sampling_logits;scheduler_memory |
| 子分类 | cold_start |
| Operator 关键词 | attention;cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: CUDA error during start the vllm serve

### Issue 正文摘录

### Your current environment **model**: official Qwen2.5-vl-7B after loading the checkpoints, it raised: (RTX 5090) INFO 09-19 11:15:42 [__init__.py:216] Automatically detected platform cuda. (APIServer pid=4031749) INFO 09-19 11:15:43 [api_server.py:1896] vLLM API server version 0.10.2 (APIServer pid=4031749) INFO 09-19 11:15:43 [utils.py:328] non-default args: {'model_tag': './Qwen2.5-VL/qwen2_5VL_7B', 'model': './Qwen2.5-VL/qwen2_5VL_7B'} (APIServer pid=4031749) INFO 09-19 11:15:46 [__init__.py:742] Resolved architecture: Qwen2_5_VLForConditionalGeneration (APIServer pid=4031749) `torch_dtype` is deprecated! Use `dtype` instead! (APIServer pid=4031749) INFO 09-19 11:15:46 [__init__.py:1815] Using max model len 128000 (APIServer pid=4031749) INFO 09-19 11:15:46 [scheduler.py:222] Chunked prefill is enabled with max_num_batched_tokens=2048. INFO 09-19 11:15:49 [__init__.py:216] Automatically detected platform cuda. (EngineCore_DP0 pid=4032464) INFO 09-19 11:15:50 [core.py:654] Waiting for init message from front-end. (EngineCore_DP0 pid=4032464) INFO 09-19 11:15:50 [core.py:76] Initializing a V1 LLM engine (v0.10.2) with config: model='./Qwen2.5-VL/qwen2_5VL_7B', speculative_conf...

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 6: kv_cache_dtype=auto, device_config=cuda, decoding_config=DecodingConfig(backend='auto', disable_fallback=False, disable_any_whitespace=False, disable_additional_properties=False, reasoning_backend=''), observability_con...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: rt the vllm serve bug;stale ### Your current environment **model**: official Qwen2.5-vl-7B after loading the checkpoints, it raised: (RTX 5090) INFO 09-19 11:15:42 [__init__.py:216] Automatically detected platform cuda....
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: or during start the vllm serve bug;stale ### Your current environment **model**: official Qwen2.5-vl-7B after loading the checkpoints, it raised: (RTX 5090) INFO 09-19 11:15:42 [__init__.py:216] Automatically detected p...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: [Bug]: CUDA error during start the vllm serve bug;stale ### Your current environment **model**: official Qwen2.5-vl-7B after loading the checkpoints, it raised: (RTX 5090) INFO 09-19 11:15:42 [__init__.py:216] Automatic...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: cture: Qwen2_5_VLForConditionalGeneration (APIServer pid=4031749) `torch_dtype` is deprecated! Use `dtype` instead! (APIServer pid=4031749) INFO 09-19 11:15:46 [__init__.py:1815] Using max model len 128000 (APIServer pi...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
