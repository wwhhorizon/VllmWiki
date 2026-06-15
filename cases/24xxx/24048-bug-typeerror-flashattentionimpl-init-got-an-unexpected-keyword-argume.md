# vllm-project/vllm#24048: [Bug]: TypeError: FlashAttentionImpl.__init__() got an unexpected keyword argument 'layer_idx' in Qwen/Qwen2.5-14B-Instruct-1M

| 字段 | 值 |
| --- | --- |
| Issue | [#24048](https://github.com/vllm-project/vllm/issues/24048) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;moe;quantization;sampling_logits;scheduler_memory |
| 子分类 | cold_start |
| Operator 关键词 | attention;cuda;operator;quantization;sampling |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: TypeError: FlashAttentionImpl.__init__() got an unexpected keyword argument 'layer_idx' in Qwen/Qwen2.5-14B-Instruct-1M

### Issue 正文摘录

### Your current environment ``` INFO 09-01 13:49:38 [__init__.py:241] Automatically detected platform cuda. (APIServer pid=91) INFO 09-01 13:49:38 [api_server.py:1805] vLLM API server version 0.10.1.1 (APIServer pid=91) INFO 09-01 13:49:38 [utils.py:326] non-default args: {'port': 8001, 'uvicorn_log_level': 'error', 'api_key': ['key_123'], 'model': 'Qwen/Qwen2.5-14B-Instruct-1M', 'dtype': 'half', 'max_model_len': 1010000, 'enforce_eager': True, 'served_model_name': ['model'], 'gpu_memory_utilization': 0.8, 'max_num_batched_tokens': 131072, 'max_num_seqs': 32, 'enable_chunked_prefill': True} (APIServer pid=91) INFO 09-01 13:49:43 [__init__.py:711] Resolved architecture: Qwen2ForCausalLM (APIServer pid=91) `torch_dtype` is deprecated! Use `dtype` instead! (APIServer pid=91) WARNING 09-01 13:49:43 [__init__.py:2819] Casting torch.bfloat16 to torch.float16. (APIServer pid=91) INFO 09-01 13:49:43 [__init__.py:1750] Using max model len 1010000 (APIServer pid=91) INFO 09-01 13:49:43 [scheduler.py:222] Chunked prefill is enabled with max_num_batched_tokens=131072. (APIServer pid=91) INFO 09-01 13:49:45 [weight_utils.py:254] Loaded sparse attention config from /root/.cache/huggingface/hub...

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 5: [Bug]: TypeError: FlashAttentionImpl.__init__() got an unexpected keyword argument 'layer_idx' in Qwen/Qwen2.5-14B-Instruct-1M bug ### Your current environment ``` INFO 09-01 13:49:38 [__init__.py:241] Automatically det...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: IServer pid=91) INFO 09-01 13:49:38 [api_server.py:1805] vLLM API server version 0.10.1.1 (APIServer pid=91) INFO 09-01 13:49:38 [utils.py:326] non-default args: {'port': 8001, 'uvicorn_log_level': 'error', 'api_key': [...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: rror', 'api_key': ['key_123'], 'model': 'Qwen/Qwen2.5-14B-Instruct-1M', 'dtype': 'half', 'max_model_len': 1010000, 'enforce_eager': True, 'served_model_name': ['model'], 'gpu_memory_utilization': 0.8, 'max_num_batched_t...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: tentionImpl.__init__() got an unexpected keyword argument 'layer_idx' in Qwen/Qwen2.5-14B-Instruct-1M bug ### Your current environment ``` INFO 09-01 13:49:38 [__init__.py:241] Automatically detected platform cuda. (API...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: 8, 'max_num_batched_tokens': 131072, 'max_num_seqs': 32, 'enable_chunked_prefill': True} (APIServer pid=91) INFO 09-01 13:49:43 [__init__.py:711] Resolved architecture: Qwen2ForCausalLM (APIServer pid=91) `torch_dtype`...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
