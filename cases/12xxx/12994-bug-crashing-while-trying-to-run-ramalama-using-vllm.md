# vllm-project/vllm#12994: [Bug]: Crashing while trying to run ramalama using vllm

| 字段 | 值 |
| --- | --- |
| Issue | [#12994](https://github.com/vllm-project/vllm/issues/12994) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | activation_norm;attention_kv_cache;distributed_parallel;frontend_api;model_support;quantization;scheduler_memory |
| 子分类 | memory |
| Operator 关键词 | attention;cache;cuda;operator;quantization |
| 症状 | crash;import_error;oom;slowdown |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Crashing while trying to run ramalama using vllm

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When I run vllm using ramalama, it crashes on startup. Also filed at https://github.com/containers/ramalama/issues/774 ``` ❯ ramalama --runtime vllm --gpu serve deepseek-r1 INFO 02-09 18:59:41 __init__.py:190] Automatically detected platform cuda. INFO 02-09 18:59:43 api_server.py:206] Started engine process with PID 70 INFO 02-09 18:59:49 __init__.py:190] Automatically detected platform cuda. INFO 02-09 18:59:59 config.py:2382] Downcasting torch.float32 to torch.float16. INFO 02-09 19:00:06 config.py:2382] Downcasting torch.float32 to torch.float16. INFO 02-09 19:00:08 config.py:542] This model supports multiple tasks: {'reward', 'score', 'classify', 'generate', 'embed'}. Defaulting to 'generate'. WARNING 02-09 19:00:08 config.py:621] gguf quantization is not fully optimized yet. The speed can be slower than non-quantized models. INFO 02-09 19:00:15 config.py:542] This model supports multiple tasks: {'reward', 'embed', 'score', 'classify', 'generate'}. Defaulting to 'generate'. WARNING 02-09 19:00:15 config.py:621] gguf quantization is not fully optimized yet. The speed can be slower than non-quantized models. INFO 02-09 19:00:1...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: [Bug]: Crashing while trying to run ramalama using vllm bug;stale ### Your current environment ### 🐛 Describe the bug When I run vllm using ramalama, it crashes on startup. Also filed at https://github.com/containers/ra...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: kwargs=None, pooler_config=None, compilation_config={"splitting_ops":[],"compile_sizes":[],"cudagraph_capture_sizes":[256,248,240,232,224,216,208,200,192,184,176,168,160,152,144,136,128,120,112,104,96,88,80,72,64,56,48,...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: ted platform cuda. INFO 02-09 18:59:59 config.py:2382] Downcasting torch.float32 to torch.float16. INFO 02-09 19:00:06 config.py:2382] Downcasting torch.float32 to torch.float16. INFO 02-09 19:00:08 config.py:542] This...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: uto, device_config=cuda, decoding_config=DecodingConfig(guided_decoding_backend='xgrammar'), observability_config=ObservabilityConfig(otlp_traces_endpoint=None, collect_model_forward_time=False, collect_model_execute_ti...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: e_config=None, tokenizer='/mnt/models/model.file', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, override_neuron_config=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.float16, max_s...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
