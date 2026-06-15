# vllm-project/vllm#11560: [Usage]:  torch.OutOfMemoryError: CUDA out of memory.

| 字段 | 值 |
| --- | --- |
| Issue | [#11560](https://github.com/vllm-project/vllm/issues/11560) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 18; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;distributed_parallel;frontend_api;gemm_linear;model_support;quantization;scheduler_memory |
| 子分类 | memory |
| Operator 关键词 | attention;cuda;operator;quantization |
| 症状 | build_error;crash;oom |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]:  torch.OutOfMemoryError: CUDA out of memory.

### Issue 正文摘录

### Your current environment ``` I get this error when load "Qwen2-VL-72B-Instruct" Here is the detail of error : ``` ``` INFO 12-27 08:52:17 config.py:350] This model supports multiple tasks: {'embedding', 'generate'}. Defaulting to 'generate'. INFO 12-27 08:52:17 llm_engine.py:249] Initializing an LLM engine (v0.6.4) with config: model='/data/fffan/model/Qwen2-VL-72B-Instruct', speculative_config=None, tokenizer='/data/fffan/model/Qwen2-VL-72B-Instruct', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, override_neuron_config=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.bfloat16, max_seq_len=32768, download_dir=None, load_format=LoadFormat.AUTO, tensor_parallel_size=1, pipeline_parallel_size=1, disable_custom_all_reduce=False, quantization=None, enforce_eager=False, kv_cache_dtype=auto, quantization_param_path=None, device_config=cuda, decoding_config=DecodingConfig(guided_decoding_backend='outlines'), observability_config=ObservabilityConfig(otlp_traces_endpoint=None, collect_model_forward_time=False, collect_model_execute_time=False), seed=0, served_model_name=/data/fffan/model/Qwen2-VL-72B-Instruct, num_scheduler_steps=1, chunked_prefill_en...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: CUDA out of memory. Tried to allocate 462.00 MiB. GPU 0 has a total capacity of 79.25 GiB of which 278.75 MiB is free. Including non-PyTorch memory, this process has 78.97 GiB memory in use. Of the allocated memory 78.3...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: de_neuron_config=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.bfloat16, max_seq_len=32768, download_dir=None, load_format=LoadFormat.AUTO, tensor_parallel_size=1, pipeline_parallel_size=1, disable...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: ry. usage ### Your current environment ``` I get this error when load "Qwen2-VL-72B-Instruct" Here is the detail of error : ``` ``` INFO 12-27 08:52:17 config.py:350] This model supports multiple tasks: {'embedding', 'g...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: e (v0.6.4) with config: model='/data/fffan/model/Qwen2-VL-72B-Instruct', speculative_config=None, tokenizer='/data/fffan/model/Qwen2-VL-72B-Instruct', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, overr...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: kenizer='/data/fffan/model/Qwen2-VL-72B-Instruct', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, override_neuron_config=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.bfloat16, max_...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
