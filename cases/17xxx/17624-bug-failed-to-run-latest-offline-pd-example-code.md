# vllm-project/vllm#17624: [Bug]: failed to run latest offline PD example code

| 字段 | 值 |
| --- | --- |
| Issue | [#17624](https://github.com/vllm-project/vllm/issues/17624) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;distributed_parallel;frontend_api;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;operator;quantization;sampling |
| 症状 | nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: failed to run latest offline PD example code

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug here is my error code ``` (lmvllm) root@salab-hpedl380g11-02:/mnt/nvme2n1/wayne/lmvllm/vllm/examples/offline_inference/disaggregated-prefill-v1# sh run_wayne.sh rm: cannot remove 'output.txt': No such file or directory INFO 05-04 06:51:34 [__init__.py:239] Automatically detected platform cuda. INFO 05-04 06:51:42 [config.py:751] This model supports multiple tasks: {'reward', 'classify', 'embed', 'score', 'generate'}. Defaulting to 'generate'. WARNING 05-04 06:51:42 [cuda.py:93] To see benefits of async output processing, enable CUDA graph. Since, enforce-eager is enabled, async output processor cannot be used INFO 05-04 06:51:42 [llm_engine.py:240] Initializing a V0 LLM engine (v0.8.5.dev404+g98060b001) with config: model='mistralai/Mistral-7B-Instruct-v0.2', speculative_config=None, tokenizer='mistralai/Mistral-7B-Instruct-v0.2', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, override_neuron_config={}, tokenizer_revision=None, trust_remote_code=False, dtype=torch.bfloat16, max_seq_len=32768, download_dir=None, load_format=LoadFormat.AUTO, tensor_parallel_size=1, pipeline_parallel_size=1, disable_custom_all_reduce...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: ride_neuron_config={}, tokenizer_revision=None, trust_remote_code=False, dtype=torch.bfloat16, max_seq_len=32768, download_dir=None, load_format=LoadFormat.AUTO, tensor_parallel_size=1, pipeline_parallel_size=1, disable...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Bug]: failed to run latest offline PD example code bug;stale ### Your current environment ### 🐛 Describe the bug here is my error code ``` (lmvllm) root@salab-hpedl380g11-02:/mnt/nvme2n1/wayne/lmvllm/vllm/examples/offl...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: kv_cache_dtype=auto, device_config=cuda, decoding_config=DecodingConfig(backend='xgrammar', disable_fallback=False, disable_any_whitespace=False, disable_additional_properties=False, reasoning_backend=''), observability...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: nd=''), observability_config=ObservabilityConfig(show_hidden_metrics_for_version=None, otlp_traces_endpoint=None, collect_detailed_traces=None), seed=None, served_model_name=mistralai/Mistral-7B-Instruct-v0.2, num_sched...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: nit__.py:239] Automatically detected platform cuda. INFO 05-04 06:51:42 [config.py:751] This model supports multiple tasks: {'reward', 'classify', 'embed', 'score', 'generate'}. Defaulting to 'generate'. WARNING 05-04 0...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
