# vllm-project/vllm#11608: [Bug]: Can Not load model Qwen2-VL-72B-Instruct in Vllm

| 字段 | 值 |
| --- | --- |
| Issue | [#11608](https://github.com/vllm-project/vllm/issues/11608) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Can Not load model Qwen2-VL-72B-Instruct in Vllm

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I can not load `Qwen2-VL-72B-Instruct` model in vllm。 Does anybody know how to solve it? Here is the detail when load model: ``` (fffan_debug) root@ubuntu:/data/fffan# python fffan_test_file.py ##### 开始加载。。。 INFO 12-30 00:48:39 config.py:510] This model supports multiple tasks: {'score', 'embed', 'reward', 'classify', 'generate'}. Defaulting to 'generate'. INFO 12-30 00:48:39 config.py:1310] Defaulting to use mp for distributed inference INFO 12-30 00:48:39 llm_engine.py:234] Initializing an LLM engine (v0.6.6) with config: model='/data/fffan/model/Qwen2-VL-72B-Instruct', speculative_config=None, tokenizer='/data/fffan/model/Qwen2-VL-72B-Instruct', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, override_neuron_config=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.bfloat16, max_seq_len=32768, download_dir=None, load_format=auto, tensor_parallel_size=8, pipeline_parallel_size=1, disable_custom_all_reduce=False, quantization=None, enforce_eager=False, kv_cache_dtype=auto, quantization_param_path=None, device_config=cuda, decoding_config=DecodingConfig(guided_de...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: [Bug]: Can Not load model Qwen2-VL-72B-Instruct in Vllm bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I can not load `Qwen2-VL-72B-Instruct` model in vllm。 Does anybod...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: vllm.unified_attention","vllm.unified_attention_with_output"],"candidate_compile_sizes":[],"compile_sizes":[],"capture_sizes":[256,248,240,232,224,216,208,200,192,184,176,168,160,152,144,136,128,120,112,104,96,88,80,72,...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: de_neuron_config=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.bfloat16, max_seq_len=32768, download_dir=None, load_format=auto, tensor_parallel_size=8, pipeline_parallel_size=1, disable_custom_all...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: Can Not load model Qwen2-VL-72B-Instruct in Vllm bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I can not load `Qwen2-VL-72B-Instruct` model in vllm。 Does anybod...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: None, device_config=cuda, decoding_config=DecodingConfig(guided_decoding_backend='xgrammar'), observability_config=ObservabilityConfig(otlp_traces_endpoint=None, collect_model_forward_time=False, collect_model_execute_t...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
