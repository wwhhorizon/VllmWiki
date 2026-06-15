# vllm-project/vllm#8101: [Bug]: ValueError: Queue <multiprocessing.queues.Queue object at 0x7f5703d2d0f0> is closed;zipfile.BadZipFile: Bad magic number for file header

| 字段 | 值 |
| --- | --- |
| Issue | [#8101](https://github.com/vllm-project/vllm/issues/8101) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | distributed_parallel;frontend_api;model_support;quantization |
| 子分类 | env_compat |
| Operator 关键词 | cuda;quantization;triton |
| 症状 | crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: ValueError: Queue <multiprocessing.queues.Queue object at 0x7f5703d2d0f0> is closed;zipfile.BadZipFile: Bad magic number for file header

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug My env is ready, **Only!!!!!** it works successfully **at first time**。 If running after time, there always got the error bellow: ```text INFO 09-03 15:47:02 config.py:813] Defaulting to use mp for distributed inference INFO 09-03 15:47:02 llm_engine.py:184] Initializing an LLM engine (v0.5.5) with config: model='/root/paddlejob/workspace/env_run/output/ckpts/qwen2-7b-instruct', speculative_config=None, tokenizer='/root/paddlejob/workspace/env_run/output/ckpts/qwen2-7b-instruct', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, rope_scaling=None, rope_theta=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.bfloat16, max_seq_len=32768, download_dir=None, load_format=LoadFormat.AUTO, tensor_parallel_size=4, pipeline_parallel_size=1, disable_custom_all_reduce=False, quantization=None, enforce_eager=False, kv_cache_dtype=auto, quantization_param_path=None, device_config=cuda, decoding_config=DecodingConfig(guided_decoding_backend='outlines'), observability_config=ObservabilityConfig(otlp_traces_endpoint=None, collect_model_forward_time=False, collect_model_execute_time=False), seed=0, served_model_name...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: None, rope_theta=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.bfloat16, max_seq_len=32768, download_dir=None, load_format=LoadFormat.AUTO, tensor_parallel_size=4, pipeline_parallel_size=1, disable...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: ter time, there always got the error bellow: ```text INFO 09-03 15:47:02 config.py:813] Defaulting to use mp for distributed inference INFO 09-03 15:47:02 llm_engine.py:184] Initializing an LLM engine (v0.5.5) with conf...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: workspace/env_run/output/ckpts/qwen2-7b-instruct', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, rope_scaling=None, rope_theta=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.bfloat1...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: ValueError: Queue <multiprocessing.queues.Queue object at 0x7f5703d2d0f0> is closed;zipfile.BadZipFile: Bad magic number for file header bug;stale ### Your current environment ### 🐛 Describe the bug My env is rea...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: None, device_config=cuda, decoding_config=DecodingConfig(guided_decoding_backend='outlines'), observability_config=ObservabilityConfig(otlp_traces_endpoint=None, collect_model_forward_time=False, collect_model_execute_t...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
