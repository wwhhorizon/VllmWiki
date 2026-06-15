# vllm-project/vllm#26318: [Bug]: Pipeline parallelism hangs on multi-node when using Slurm on a slingshot network

| 字段 | 值 |
| --- | --- |
| Issue | [#26318](https://github.com/vllm-project/vllm/issues/26318) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency;memory_layout;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Pipeline parallelism hangs on multi-node when using Slurm on a slingshot network

### Issue 正文摘录

### 🐛 Describe the bug I am trying to run the `vllm bench latency` with tensor parallelism within the node and pipeline parallel inter-node (tensor-parallel-size =4, pipeline-parallel-size=2). I get the following error: ``` (EngineCore_DP0 pid=635544) 2025-10-06 13:20:06,152 INFO torch_tensor_accelerator_channel.py:833 -- Communicator group initialized. (EngineCore_DP0 pid=635544) ERROR 10-06 13:28:27 [logging_utils/dump_input.py:69] Dumping input data for V1 LLM engine (v0.11.1.dev0+gf71952c1c.d20251005) with config: model='meta-llama/Llama-3.1-8B-Instruct', speculative_config=None, tokenizer='meta-llama/Llama-3.1-8B-Instruct', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.bfloat16, max_seq_len=131072, download_dir=None, load_format=auto, tensor_parallel_size=4, pipeline_parallel_size=2, data_parallel_size=1, disable_custom_all_reduce=False, quantization=None, enforce_eager=False, kv_cache_dtype=auto, device_config=cuda, structured_outputs_config=StructuredOutputsConfig(backend='auto', disable_fallback=False, disable_any_whitespace=False, disable_additional_properties=False, reasoning_parser=''), obser...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: er=''), observability_config=ObservabilityConfig(show_hidden_metrics_for_version=None, otlp_traces_endpoint=None, collect_detailed_traces=None), seed=0, served_model_name=meta-llama/Llama-3.1-8B-Instruct, enable_prefix_...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: ng input data for V1 LLM engine (v0.11.1.dev0+gf71952c1c.d20251005) with config: model='meta-llama/Llama-3.1-8B-Instruct', speculative_config=None, tokenizer='meta-llama/Llama-3.1-8B-Instruct', skip_tokenizer_init=False...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: e=auto, revision=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.bfloat16, max_seq_len=131072, download_dir=None, load_format=auto, tensor_parallel_size=4, pipeline_parallel_size=2, data_parallel_siz...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: allelism hangs on multi-node when using Slurm on a slingshot network bug;stale ### 🐛 Describe the bug I am trying to run the `vllm bench latency` with tensor parallelism within the node and pipeline parallel inter-node...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: o, device_config=cuda, structured_outputs_config=StructuredOutputsConfig(backend='auto', disable_fallback=False, disable_any_whitespace=False, disable_additional_properties=False, reasoning_parser=''), observability_con...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
