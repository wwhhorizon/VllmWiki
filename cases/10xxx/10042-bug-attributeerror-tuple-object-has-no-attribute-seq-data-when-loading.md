# vllm-project/vllm#10042: [Bug]: AttributeError: 'tuple' object has no attribute 'seq_data' when loading Molmo7B on two Nvidia L4

| 字段 | 值 |
| --- | --- |
| Issue | [#10042](https://github.com/vllm-project/vllm/issues/10042) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency;race_condition |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: AttributeError: 'tuple' object has no attribute 'seq_data' when loading Molmo7B on two Nvidia L4

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Ran ``` model_name = "allenai/Molmo-7B-D-0924" llm = LLM( model=model_name, trust_remote_code=True, dtype="bfloat16", tensor_parallel_size=2 ) ``` Got ``` INFO 11-05 15:45:50 config.py:1764] Downcasting torch.float32 to torch.bfloat16. INFO 11-05 15:45:55 config.py:991] Defaulting to use mp for distributed inference INFO 11-05 15:45:55 llm_engine.py:247] Initializing an LLM engine (v0.6.3.post2.dev235+g93dee88f) with config: model='allenai/Molmo-7B-D-0924', speculative_config=None, tokenizer='allenai/Molmo-7B-D-0924', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, override_neuron_config=None, rope_scaling=None, rope_theta=None, tokenizer_revision=None, trust_remote_code=True, dtype=torch.bfloat16, max_seq_len=4096, download_dir=None, load_format=LoadFormat.AUTO, tensor_parallel_size=2, pipeline_parallel_size=1, disable_custom_all_reduce=False, quantization=None, enforce_eager=False, kv_cache_dtype=auto, quantization_param_path=None, device_config=cuda, decoding_config=DecodingConfig(guided_decoding_backend='outlines'), observability_config=ObservabilityConfig(otlp_traces_endpoin...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: .3.post2.dev235+g93dee88f) with config: model='allenai/Molmo-7B-D-0924', speculative_config=None, tokenizer='allenai/Molmo-7B-D-0924', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, override_neuron_confi...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: -0924" llm = LLM( model=model_name, trust_remote_code=True, dtype="bfloat16", tensor_parallel_size=2 ) ``` Got ``` INFO 11-05 15:45:50 config.py:1764] Downcasting torch.float32 to torch.bfloat16. INFO 11-05 15:45:55 con...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: er_config=None) WARNING 11-05 15:45:56 multiproc_gpu_executor.py:53] Reducing Torch parallelism from 12 threads to 1 to avoid unnecessary CPU contention. Set OMP_NUM_THREADS in the external environment to tune this valu...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: oading Molmo7B on two Nvidia L4 bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Ran ``` model_name = "allenai/Molmo-7B-D-0924" llm = LLM( model=model_name, trust_remote_code=T...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: None, device_config=cuda, decoding_config=DecodingConfig(guided_decoding_backend='outlines'), observability_config=ObservabilityConfig(otlp_traces_endpoint=None, collect_model_forward_time=False, collect_model_execute_t...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
