# vllm-project/vllm#29670: [Bug]: single node 8 h20,ebo failed!

| 字段 | 值 |
| --- | --- |
| Issue | [#29670](https://github.com/vllm-project/vllm/issues/29670) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;moe;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: single node 8 h20,ebo failed!

### Issue 正文摘录

### ENV ### 🐛 Describe the bug ``` export VLLM_ALL2ALL_BACKEND=deepep_low_latency vllm serve deepseek-ai/DeepSeek-V2-Lite --trust-remote-code --data-parallel-size 2 --enable-expert-parallel --enable-dbo ``` ### output ``` WARNING 11-28 19:08:15 [parallel.py:470] VLLM_ALL2ALL_BACKEND environment variable is deprecated and will be removed in a future release. Please use the --all2all-backend command-line argument instead. INFO 11-28 19:08:15 [scheduler.py:216] Chunked prefill is enabled with max_num_batched_tokens=2048. (APIServer pid=927159) INFO 11-28 19:08:15 [api_server.py:1977] vLLM API server version 0.11.2 (APIServer pid=927159) INFO 11-28 19:08:15 [utils.py:253] non-default args: {'model_tag': 'deepseek-ai/DeepSeek-V2-Lite', 'model': 'deepseek-ai/DeepSeek-V2-Lite', 'trust_remote_code': True, 'data_parallel_size': 2, 'enable_expert_parallel': True, 'enable_dbo': True} (APIServer pid=927159) WARNING 11-28 19:08:15 [system_utils.py:222] Found ulimit of 65530 and failed to automatically increase with error current limit exceeds maximum limit. This can cause fd limit errors like `OSError: [Errno 24] Too many open files`. Consider increasing with ulimit -n (APIServer pid=927159) T...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: ver pid=927159) INFO 11-28 19:08:15 [api_server.py:1977] vLLM API server version 0.11.2 (APIServer pid=927159) INFO 11-28 19:08:15 [utils.py:253] non-default args: {'model_tag': 'deepseek-ai/DeepSeek-V2-Lite', 'model':...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: de=auto, revision=None, tokenizer_revision=None, trust_remote_code=True, dtype=torch.bfloat16, max_seq_len=163840, download_dir=None, load_format=auto, tensor_parallel_size=1, pipeline_parallel_size=1, data_parallel_siz...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Bug]: single node 8 h20,ebo failed! bug;stale ### ENV ### 🐛 Describe the bug ``` export VLLM_ALL2ALL_BACKEND=deepep_low_latency vllm serve deepseek-ai/DeepSeek-V2-Lite --trust-remote-code --data-parallel-size 2 --enabl...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: led! bug;stale ### ENV ### 🐛 Describe the bug ``` export VLLM_ALL2ALL_BACKEND=deepep_low_latency vllm serve deepseek-ai/DeepSeek-V2-Lite --trust-remote-code --data-parallel-size 2 --enable-expert-parallel --enable-dbo `...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: APIServer pid=927159) INFO 11-28 19:08:18 [cuda.py:210] Forcing kv cache block size to 64 for FlashMLA backend. (APIServer pid=927159) WARNING 11-28 19:08:18 [vllm.py:693] Disabling cascade attention when DBO is enabled...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
