# vllm-project/vllm#29360: [Bug]: Qwen3-Coder-480B-FP8 running on 8*H20,deepgemm warmup OOM

| 字段 | 值 |
| --- | --- |
| Issue | [#29360](https://github.com/vllm-project/vllm/issues/29360) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;fp8;moe;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf;oom |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Qwen3-Coder-480B-FP8 running on 8*H20,deepgemm warmup OOM

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug INFO 11-25 08:00:36 [scheduler.py:216] Chunked prefill is enabled with max_num_batched_tokens=2048. (APIServer pid=1) INFO 11-25 08:00:36 [api_server.py:1977] vLLM API server version 0.11.1 (APIServer pid=1) INFO 11-25 08:00:36 [utils.py:253] non-default args: {'model_tag': '/models', 'port': 8003, 'uvicorn_log_level': ' debug', 'enable_auto_tool_choice': True, 'tool_call_parser': 'qwen3_coder', 'model': '/models', 'max_model_len': 131072, 'enforce_ea ger': True, 'served_model_name': ['qwen3-coder-480b'], 'tensor_parallel_size': 8, 'enable_expert_parallel': True, 'gpu_memory_utili zation': 0.98, 'max_num_seqs': 30, 'enable_chunked_prefill': True, 'enable_log_requests': True} (APIServer pid=1) INFO 11-25 08:00:42 [model.py:631] Resolved architecture: Qwen3MoeForCausalLM (APIServer pid=1) INFO 11-25 08:00:42 [model.py:1745] Using max model len 131072 (APIServer pid=1) INFO 11-25 08:00:42 [scheduler.py:216] Chunked prefill is enabled with max_num_batched_tokens=8192. (APIServer pid=1) INFO 11-25 08:00:42 [vllm.py:500] Cudagraph is disabled under eager mode (EngineCore_DP0 pid=270) INFO 11-25 08:00:48 [core.py:93] Initializing a V1 L...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: PIServer pid=1) INFO 11-25 08:00:36 [api_server.py:1977] vLLM API server version 0.11.1 (APIServer pid=1) INFO 11-25 08:00:36 [utils.py:253] non-default args: {'model_tag': '/models', 'port': 8003, 'uvicorn_log_level':...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: [Bug]: Qwen3-Coder-480B-FP8 running on 8*H20,deepgemm warmup OOM bug;stale ### Your current environment ### 🐛 Describe the bug INFO 11-25 08:00:36 [scheduler.py:216] Chunked prefill is enabled with max_num_batched_token...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: [Bug]: Qwen3-Coder-480B-FP8 running on 8*H20,deepgemm warmup OOM bug;stale ### Your current environment ### 🐛 Describe the bug INFO 11-25 08:00:36 [scheduler.py:216] Chunked prefill is enabled with max_num_batched_token...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: , device_ config=cuda, structured_outputs_config=StructuredOutputsConfig(backend='auto', disable_fallback=False, disable_any_whitespace=False, dis able_additional_properties=False, reasoning_parser='', reasoning_parser_...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 4: s', specu lative_config=None, tokenizer='/models', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, tokenizer_revision=None, tru st_remote_code=False, dtype=torch.bfloat16, max_seq_len=131072, download_dir...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
