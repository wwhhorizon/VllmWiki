# vllm-project/vllm#24237: [Bug]: Xformers is not available, falling back, even though I have Xformers installed

| 字段 | 值 |
| --- | --- |
| Issue | [#24237](https://github.com/vllm-project/vllm/issues/24237) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;moe;multimodal_vlm;quantization;sampling_logits;scheduler_memory |
| 子分类 | throughput |
| Operator 关键词 | attention;cache;cuda;gemm;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;import_error;slowdown |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Xformers is not available, falling back, even though I have Xformers installed

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Even though I have Xformers installaled, vllm reports as unavailable and my tps becomes very slow. ``` vllm serve models/MiniCPM-V-4_5-AWQ \ --dtype bfloat16 \ --gpu-memory-utilization 0.95 \ --max-model-len 6000 \ --max-num-seqs 16 \ --max-num-batched-tokens 10000 \ --trust-remote-code \ --limit-mm-per-prompt '{"image": 30, "video": 1}' \ --allowed-local-media-path "/path/to/ \ --tensor-parallel-size 1 \ --pipeline-parallel-size 1 \ --enable-prefix-caching \ --enable-chunked-prefill \ --max-logprobs 0 \ --cpu-offload-gb 0 \ --port 8000 \ --host 0.0.0.0 \ --scheduling-policy priority \ --media-io-kwargs '{"video":{"num_frames":60}}' \ --chat-template /path/to//MiniCPM-V-4_5-AWQ/custom_template.jinja2 INFO 09-04 17:19:30 [__init__.py:241] Automatically detected platform cuda. (APIServer pid=2045731) INFO 09-04 17:19:35 [api_server.py:1894] vLLM API server version 0.10.2rc2.dev75+g51d5e9be7 (APIServer pid=2045731) INFO 09-04 17:19:35 [utils.py:328] non-default args: {'model_tag': 'models/MiniCPM-V-4_5-AWQ', 'host': '0.0.0.0', 'chat_template': '/path/to/MiniCPM-V-4_5-AWQ/custom_template.jinja2', 'model': 'models/MiniCPM-V-4_5-AWQ',...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: g]: Xformers is not available, falling back, even though I have Xformers installed bug;stale ### Your current environment ### 🐛 Describe the bug Even though I have Xformers installaled, vllm reports as unavailable and m...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 5: kv_cache_dtype=auto, device_config=cuda, decoding_config=DecodingConfig(backend='auto', disable_fallback=False, disable_any_whitespace=False, disable_additional_properties=False, reasoning_backend=''), observability_con...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: ps becomes very slow. ``` vllm serve models/MiniCPM-V-4_5-AWQ \ --dtype bfloat16 \ --gpu-memory-utilization 0.95 \ --max-model-len 6000 \ --max-num-seqs 16 \ --max-num-batched-tokens 10000 \ --trust-remote-code \ --limi...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: llm reports as unavailable and my tps becomes very slow. ``` vllm serve models/MiniCPM-V-4_5-AWQ \ --dtype bfloat16 \ --gpu-memory-utilization 0.95 \ --max-model-len 6000 \ --max-num-seqs 16 \ --max-num-batched-tokens 1...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: s not available, falling back, even though I have Xformers installed bug;stale ### Your current environment ### 🐛 Describe the bug Even though I have Xformers installaled, vllm reports as unavailable and my tps becomes...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
