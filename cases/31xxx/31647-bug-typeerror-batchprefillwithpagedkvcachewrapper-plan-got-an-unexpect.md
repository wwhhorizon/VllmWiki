# vllm-project/vllm#31647: [Bug]: TypeError: BatchPrefillWithPagedKVCacheWrapper.plan() got an unexpected keyword argument 'fixed_split_size'

| 字段 | 值 |
| --- | --- |
| Issue | [#31647](https://github.com/vllm-project/vllm/issues/31647) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;fp8;kernel;moe;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: TypeError: BatchPrefillWithPagedKVCacheWrapper.plan() got an unexpected keyword argument 'fixed_split_size'

### Issue 正文摘录

### Your current environment NOTE: I did my best, but given that this is NixOS, I am not 100% sure I got the exact same environment vLLM runs in. 🙈 It does, generally, work and infer well using CUDA. ### 🐛 Describe the bug `vllm serve`ing `openai/gpt-oss-20b` with speculation results in `TypeError: BatchPrefillWithPagedKVCacheWrapper.plan() got an unexpected keyword argument 'fixed_split_size'` when the first inference is performed. I adapted the command to run from https://huggingface.co/RedHatAI/gpt-oss-20b-speculator.eagle3: ``` $ vllm serve openai/gpt-oss-20b -tp 1 --speculative-config '{ "model": "RedHatAI/gpt-oss-20b-speculator.eagle3", "num_speculative_tokens": 3, "method": "eagle3" }' --max-model-len 8192 --kv-cache-dtype fp8 --gpu-memory-utilization 0.90 --port 8080 INFO 01-03 14:58:06 [scheduler.py:216] Chunked prefill is enabled with max_num_batched_tokens=2048. (APIServer pid=125611) INFO 01-03 14:58:06 [api_server.py:1977] vLLM API server version 0.11.2 (APIServer pid=125611) INFO 01-03 14:58:06 [utils.py:253] non-default args: {'model_tag': 'openai/gpt-oss-20b', 'port': 8080, 'model': 'openai/gpt-oss-20b', 'max_model_len': 8192, 'kv_cache_dtype': 'fp8', 'speculative_...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 7: [Bug]: TypeError: BatchPrefillWithPagedKVCacheWrapper.plan() got an unexpected keyword argument 'fixed_split_size' bug;stale ### Your current environment NOTE: I did my best, but given that this is NixOS, I am not 100%...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: ver pid=125611) INFO 01-03 14:58:06 [api_server.py:1977] vLLM API server version 0.11.2 (APIServer pid=125611) INFO 01-03 14:58:06 [utils.py:253] non-default args: {'model_tag': 'openai/gpt-oss-20b', 'port': 8080, 'mode...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: _tokens": 3, "method": "eagle3" }' --max-model-len 8192 --kv-cache-dtype fp8 --gpu-memory-utilization 0.90 --port 8080 INFO 01-03 14:58:06 [scheduler.py:216] Chunked prefill is enabled with max_num_batched_tokens=2048....
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: fer well using CUDA. ### 🐛 Describe the bug `vllm serve`ing `openai/gpt-oss-20b` with speculation results in `TypeError: BatchPrefillWithPagedKVCacheWrapper.plan() got an unexpected keyword argument 'fixed_split_size'`...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: mp_path': None, 'cache_dir': '', 'compile_cache_save_format': 'binary', 'backend': 'inductor', 'custom_ops': ['none'], 'splitting_ops': ['vllm::unified_attention', 'vllm::unified_attention_with_output', 'vllm::unified_m...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
