# vllm-project/vllm#19467: [Bug]: Embed Task -dp > 1 stuck

| 字段 | 值 |
| --- | --- |
| Issue | [#19467](https://github.com/vllm-project/vllm/issues/19467) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Embed Task -dp > 1 stuck

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug DP ( -dp > 1 )not work when --task embed The following will stuck: ```bash vllm serve Qwen/Qwen3-Embedding-4B --max_num_batched_tokens 102400 -tp 1 -dp 4 --task embed ``` ``` INFO 06-10 23:38:35 [__init__.py:243] Automatically detected platform cuda. INFO 06-10 23:38:39 [__init__.py:31] Available plugins for group vllm.general_plugins: INFO 06-10 23:38:39 [__init__.py:33] - lora_filesystem_resolver -> vllm.plugins.lora_resolvers.filesystem_resolver:register_filesystem_resolver INFO 06-10 23:38:39 [__init__.py:36] All plugins in this group will be loaded. Set `VLLM_PLUGINS` to control which plugins to load. INFO 06-10 23:38:40 [api_server.py:1289] vLLM API server version 0.9.0 INFO 06-10 23:38:40 [cli_args.py:300] non-default args: { 'task': 'embed', 'data_parallel_size': 4} Using CUDA_VISIBLE_DEVICES=['0', '1', '2', '3'] to map device_id 0 to physical device id. WARNING 06-10 23:38:50 [arg_utils.py:1431] The model has a long context length (40960). This may causeOOM during the initial memory profiling phase, or result in low performance due to small KV cache size. Consider setting --max-model-len to a smaller value. INFO 06-10 23...

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 5: kv_cache_dtype=auto, device_config=cuda, decoding_config=DecodingConfig(backend='xgrammar', disable_fallback=False, disable_any_whitespace=False, disable_additional_properties=False, reasoning_backend=''), observability...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: lugins to load. INFO 06-10 23:38:40 [api_server.py:1289] vLLM API server version 0.9.0 INFO 06-10 23:38:40 [cli_args.py:300] non-default args: { 'task': 'embed', 'data_parallel_size': 4} Using CUDA_VISIBLE_DEVICES=['0',...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: ride_neuron_config={}, tokenizer_revision=None, trust_remote_code=False, dtype=torch.bfloat16, max_seq_len=40960, download_dir=None, load_format=LoadFormat.AUTO, tensor_parallel_size=1, pipeline_parallel_size=1, disable...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: work when --task embed The following will stuck: ```bash vllm serve Qwen/Qwen3-Embedding-4B --max_num_batched_tokens 102400 -tp 1 -dp 4 --task embed ``` ``` INFO 06-10 23:38:35 [__init__.py:243] Automatically detected p...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: g a V0 LLM engine (v0.9.0) with config: model='Qwen/Qwen3-Embedding-4B', speculative_config=None, tokenizer='Qwen/Qwen3-Embedding-4B', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, override_neuron_confi...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
