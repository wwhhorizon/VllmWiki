# vllm-project/vllm#16984: [Bug]: /usr/bin/ld: cannot find -lcuda: No such file or directory, when running inference

| 字段 | 值 |
| --- | --- |
| Issue | [#16984](https://github.com/vllm-project/vllm/issues/16984) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: /usr/bin/ld: cannot find -lcuda: No such file or directory, when running inference

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug when I'm running inference with LLMengine, it crashed. I think the reason is: /usr/bin/ld: cannot find -lcuda: No such file or directory. issue(https://github.com/vllm-project/vllm/issues/15992) also meet the same problem and says it has been fixed in vllm0.7.1. but I still have this problem then I'm using 0.7.4. WARNING 04-22 21:40:14 [cuda.py:95] To see benefits of async output processing, enable CUDA graph. Since, enforce-eager is enabled, async output processor cannot be used INFO 04-22 21:40:14 [llm_engine.py:237] Initializing a V0 LLM engine (v0.7.4.dev199+gf78c0be80.d20250422) with config: model='dlss2/model/normal/mixtral', speculative_config=None, tokenizer='cached_data/tokenizer/mixtral', skip_tokenizer_init=False, tokenizer_mode=slow, revision=None, override_neuron_config=None, tokenizer_revision=None, trust_remote_code=True, dtype=torch.float16, max_seq_len=1024, download_dir=None, load_format=dummy, tensor_parallel_size=2, pipeline_parallel_size=1, disable_custom_all_reduce=False, quantization=None, enforce_eager=True, kv_cache_dtype=auto, device_config=cuda, decoding_config=DecodingConfig(guided_decoding_backend='xg...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: 9+gf78c0be80.d20250422) with config: model='dlss2/model/normal/mixtral', speculative_config=None, tokenizer='cached_data/tokenizer/mixtral', skip_tokenizer_init=False, tokenizer_mode=slow, revision=None, override_neuron...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: uto, device_config=cuda, decoding_config=DecodingConfig(guided_decoding_backend='xgrammar', reasoning_backend=None), observability_config=ObservabilityConfig(show_hidden_metrics=False, otlp_traces_endpoint=None, collect...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: kwargs=None, pooler_config=None, compilation_config={"splitting_ops":[],"compile_sizes":[],"cudagraph_capture_sizes":[],"max_capture_size":0}, use_cached_outputs=False, WARNING 04-22 21:40:14 [tokenizer.py:237] Using a...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: ide_neuron_config=None, tokenizer_revision=None, trust_remote_code=True, dtype=torch.float16, max_seq_len=1024, download_dir=None, load_format=dummy, tensor_parallel_size=2, pipeline_parallel_size=1, disable_custom_all_...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: /usr/bin/ld: cannot find -lcuda: No such file or directory, when running inference bug ### Your current environment ### 🐛 Describe the bug when I'm running inference with LLMengine, it crashed. I think the reason...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
