# vllm-project/vllm#32897: [Bug]: PaddleOCR-VL crash

| 字段 | 值 |
| --- | --- |
| Issue | [#32897](https://github.com/vllm-project/vllm/issues/32897) |
| 状态 | open |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;multimodal_vlm;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | env_compat |
| Operator 关键词 | cuda;gemm;operator;quantization;sampling;triton |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: PaddleOCR-VL crash

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I server paddleocr-vl model, it runs but any request will crash server. `vllm serve /PaddlePaddle/PaddleOCR-VL --served-model-name PaddleOCR-VL --trust-remote-code --max-num-batched-tokens 16384 --no-enable-prefix-caching --mm-processor-cache-gb 0 --tensor-parallel-size 1` error log: ``` [dump_input.py:72] Dumping input data for V1 LLM engine (v0.14.0) with config: model='/PaddlePaddle/PaddleOCR-VL', speculative_config=None, tokenizer='/PaddlePaddle/PaddleOCR-VL', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, tokenizer_revision=None, trust_remote_code=True, dtype=torch.float16, max_seq_len=131072, download_dir=None, load_format=auto, tensor_parallel_size=1, pipeline_parallel_size=1, data_parallel_size=1, disable_custom_all_reduce=False, quantization=None, enforce_eager=False, enable_return_routed_experts=False, kv_cache_dtype=auto, device_config=cuda, structured_outputs_config=StructuredOutputsConfig(backend='auto', disable_fallback=False, disable_any_whitespace=False, disable_additional_properties=False, reasoning_parser='', reasoning_parser_plugin='', enable_in_reasoning=False), observability_config=Observabili...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 8: [Bug]: PaddleOCR-VL crash bug;stale ### Your current environment ### 🐛 Describe the bug I server paddleocr-vl model, it runs but any request will crash server. `vllm serve /PaddlePaddle/PaddleOCR-VL --served-model-name...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: False), observability_config=ObservabilityConfig(show_hidden_metrics_for_version=None, otlp_traces_endpoint=None, collect_detailed_traces=None, kv_cache_metrics=False, kv_cache_metrics_sample=0.01, cudagraph_metrics=Fal...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: ur current environment ### 🐛 Describe the bug I server paddleocr-vl model, it runs but any request will crash server. `vllm serve /PaddlePaddle/PaddleOCR-VL --served-model-name PaddleOCR-VL --trust-remote-code --max-num...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: o, device_config=cuda, structured_outputs_config=StructuredOutputsConfig(backend='auto', disable_fallback=False, disable_any_whitespace=False, disable_additional_properties=False, reasoning_parser='', reasoning_parser_p...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: de=auto, revision=None, tokenizer_revision=None, trust_remote_code=True, dtype=torch.float16, max_seq_len=131072, download_dir=None, load_format=auto, tensor_parallel_size=1, pipeline_parallel_size=1, data_parallel_size...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
