# vllm-project/vllm#27575: [Bug]: p2pNccl 3P1，D-Node nccl receives data and triggers a crash

| 字段 | 值 |
| --- | --- |
| Issue | [#27575](https://github.com/vllm-project/vllm/issues/27575) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;distributed_parallel;frontend_api;model_support;quantization;sampling_logits;scheduler_memory |
| 子分类 | runtime_err |
| Operator 关键词 | cuda;operator;quantization;sampling |
| 症状 | crash |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: p2pNccl 3P1，D-Node nccl receives data and triggers a crash

### Issue 正文摘录

### Your current environment vllm：0.11.0 ### 🐛 Describe the bug 2P1D service is normal 3P1D service error stack: (APIServer pid=42075) INFO: 33.93.136.212:58726 - "POST /v1/completions HTTP/1.1" 200 OK (APIServer pid=42075) INFO: 33.93.136.212:59446 - "POST /v1/completions HTTP/1.1" 200 OK (APIServer pid=42075) INFO: 33.93.136.212:59516 - "POST /v1/completions HTTP/1.1" 200 OK (EngineCore_DP0 pid=42228) INFO 10-27 20:33:03 [p2p_nccl_engine.py:45] set_p2p_nccl_context, original_values: {'NCCL_MAX_NCHANNELS': None, 'NCCL_MIN_NCHANNELS': None, 'NCCL_CUMEM_ENABLE': None, 'NCCL_BUFFSIZE': None, 'NCCL_PROTO': None, 'NCCL_ALGO': None} (EngineCore_DP0 pid=42228) INFO 10-27 20:33:04 [p2p_nccl_engine.py:193] 🤝ncclCommInitRank Success, 33.93.157.202:22001👉33.93.136.212:21002, MyRank:0 (EngineCore_DP0 pid=42228) ERROR 10-27 20:33:04 [dump_input.py:69] Dumping input data for V1 LLM engine (v0.11.0) with config: model='/data/Qwen3-14B/', speculative_config=None, tokenizer='/data/Qwen3-14B/', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, tokenizer_revision=None, trust_remote_code=True, dtype=torch.float16, max_seq_len=25000, download_dir=None, load_format=auto, tensor_parallel_s...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 7: [Bug]: p2pNccl 3P1，D-Node nccl receives data and triggers a crash bug;stale ### Your current environment vllm：0.11.0 ### 🐛 Describe the bug 2P1D service is normal 3P1D service error stack: (APIServer pid=42075) INFO: 33...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: er=''), observability_config=ObservabilityConfig(show_hidden_metrics_for_version=None, otlp_traces_endpoint=None, collect_detailed_traces=None), seed=1024, served_model_name=/data/Qwen3-14B/, enable_prefix_caching=True,...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: 4 [dump_input.py:69] Dumping input data for V1 LLM engine (v0.11.0) with config: model='/data/Qwen3-14B/', speculative_config=None, tokenizer='/data/Qwen3-14B/', skip_tokenizer_init=False, tokenizer_mode=auto, revision=...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: de=auto, revision=None, tokenizer_revision=None, trust_remote_code=True, dtype=torch.float16, max_seq_len=25000, download_dir=None, load_format=auto, tensor_parallel_size=1, pipeline_parallel_size=1, data_parallel_size=...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: ulative_config=None, tokenizer='/data/Qwen3-14B/', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, tokenizer_revision=None, trust_remote_code=True, dtype=torch.float16, max_seq_len=25000, download_dir=Non...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
