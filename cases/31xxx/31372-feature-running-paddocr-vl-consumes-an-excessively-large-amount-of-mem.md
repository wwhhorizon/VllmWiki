# vllm-project/vllm#31372: [Feature]: Running paddocr‑vl consumes an excessively large amount of  memory.

| 字段 | 值 |
| --- | --- |
| Issue | [#31372](https://github.com/vllm-project/vllm/issues/31372) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | activation_norm;attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;multimodal_vlm;quantization;scheduler_memory |
| 子分类 | memory |
| Operator 关键词 | activation;attention;cache;cuda;gemm;operator;quantization;triton |
| 症状 | build_error;crash;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Feature]: Running paddocr‑vl consumes an excessively large amount of  memory.

### Issue 正文摘录

### 🚀 The feature, motivation and pitch I used `vllm serve /app/models/PaddleOCR-VL --served-model-name PaddleOCR-VL --trust-remote-code --max-num-batched-tokens 8192 --no-enable-prefix-caching --mm-processor-cache-gb 0 --gpu-memory-utilization 0.3` on a ROCm image, and it ran successfully, but it consumes about 30 GB of memory. However, When I set the GPU memory utilization too low, the reported memory usage becomes negative, causing the startup to fail. ### Alternatives I’m not sure why a model under 2 GB in size requires nearly 30 GB of memory when it runs—am I missing some parameters, or could there be a memory‑leak issue? ### Additional context log1 start success but use too much memory ``` (APIServer pid=1572) INFO 12-26 04:40:11 [api_server.py:1274] vLLM API server version 0.14.0rc1.dev120+gbc5ef333e (APIServer pid=1572) INFO 12-26 04:40:11 [utils.py:253] non-default args: {'model_tag': '/app/models/PaddleOCR-VL', 'model': '/app/models/PaddleOCR-VL', 'trust_remote_code': True, 'served_model_name': ['PaddleOCR-VL'], 'gpu_memory_utilization': 0.3, 'enable_prefix_caching': False, 'mm_processor_cache_gb': 0.0, 'max_num_batched_tokens': 8192} (APIServer pid=1572) The argument `t...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: erver pid=1572) INFO 12-26 04:40:11 [api_server.py:1274] vLLM API server version 0.14.0rc1.dev120+gbc5ef333e (APIServer pid=1572) INFO 12-26 04:40:11 [utils.py:253] non-default args: {'model_tag': '/app/models/PaddleOCR...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: t;stale ### 🚀 The feature, motivation and pitch I used `vllm serve /app/models/PaddleOCR-VL --served-model-name PaddleOCR-VL --trust-remote-code --max-num-batched-tokens 8192 --no-enable-prefix-caching --mm-processor-ca...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: ning paddocr‑vl consumes an excessively large amount of memory. feature request;stale ### 🚀 The feature, motivation and pitch I used `vllm serve /app/models/PaddleOCR-VL --served-model-name PaddleOCR-VL --trust-remote-c...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: o, device_config=cuda, structured_outputs_config=StructuredOutputsConfig(backend='auto', disable_fallback=False, disable_any_whitespace=False, disable_additional_properties=False, reasoning_parser='', reasoning_parser_p...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: de=auto, revision=None, tokenizer_revision=None, trust_remote_code=True, dtype=torch.bfloat16, max_seq_len=131072, download_dir=None, load_format=auto, tensor_parallel_size=1, pipeline_parallel_size=1, data_parallel_siz...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
