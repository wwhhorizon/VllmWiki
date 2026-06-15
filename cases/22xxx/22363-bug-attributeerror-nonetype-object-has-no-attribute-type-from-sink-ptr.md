# vllm-project/vllm#22363: [Bug]: AttributeError("'NoneType' object has no attribute 'type'") from `sink_ptr` of `unified_attention` when running spec dec with Triton Attention Backend V1

| 字段 | 值 |
| --- | --- |
| Issue | [#22363](https://github.com/vllm-project/vllm/issues/22363) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;kernel;operator;quantization;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: AttributeError("'NoneType' object has no attribute 'type'") from `sink_ptr` of `unified_attention` when running spec dec with Triton Attention Backend V1

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ``` tests/v1/spec_decode/test_max_len.py::test_ngram_max_len[1] INFO 08-06 13:50:49 [utils.py:326] non-default args: {'model': 'facebook/opt-125m', 'max_model_len': 100, 'disable_log_stats': True, 'enforce_eager': True, 'speculative_config': {'method': 'ngram', 'prompt_lookup_max': 5, 'prompt_lookup_min': 3, 'num_speculative_tokens': 1}} INFO 08-06 13:51:06 [config.py:726] Resolved architecture: OPTForCausalLM INFO 08-06 13:51:06 [config.py:1765] Using max model len 100 INFO 08-06 13:51:06 [config.py:2594] Chunked prefill is enabled with max_num_batched_tokens=16384. WARNING 08-06 13:51:06 [__init__.py:2862] We must use the `spawn` multiprocessing start method. Overriding VLLM_WORKER_MULTIPROC_METHOD to 'spawn'. See https://docs.vllm.ai/en/latest/usage/troubleshooting.html#python-multiprocessing for more information. Reasons: CUDA is initialized INFO 08-06 13:51:16 [__init__.py:241] Automatically detected platform rocm. INFO 08-06 13:51:17 [core.py:619] Waiting for init message from front-end. INFO 08-06 13:51:17 [core.py:71] Initializing a V1 LLM engine (v0.1.dev8331+g74e7551.d20250806) with config: model='facebook/opt-125m', sp...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: nd=''), observability_config=ObservabilityConfig(show_hidden_metrics_for_version=None, otlp_traces_endpoint=None, collect_detailed_traces=None), seed=0, served_model_name=facebook/opt-125m, num_scheduler_steps=1, multi_...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: um_speculative_tokens': 1}} INFO 08-06 13:51:06 [config.py:726] Resolved architecture: OPTForCausalLM INFO 08-06 13:51:06 [config.py:1765] Using max model len 100 INFO 08-06 13:51:06 [config.py:2594] Chunked prefill is...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: # Your current environment ### 🐛 Describe the bug ``` tests/v1/spec_decode/test_max_len.py::test_ngram_max_len[1] INFO 08-06 13:50:49 [utils.py:326] non-default args: {'model': 'facebook/opt-125m', 'max_model_len': 100,...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: ype'") from `sink_ptr` of `unified_attention` when running spec dec with Triton Attention Backend V1 bug ### Your current environment ### 🐛 Describe the bug ``` tests/v1/spec_decode/test_max_len.py::test_ngram_max_len[1...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: ride_neuron_config={}, tokenizer_revision=None, trust_remote_code=False, dtype=torch.float16, max_seq_len=100, download_dir=None, load_format=auto, tensor_parallel_size=1, pipeline_parallel_size=1, disable_custom_all_re...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
