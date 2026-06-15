# vllm-project/vllm#27116: [Bug]: vLLM failure (ray.exceptions.RayChannelTimeoutError) observed since v0.10.2, with tp=8, pp=4

| 字段 | 值 |
| --- | --- |
| Issue | [#27116](https://github.com/vllm-project/vllm/issues/27116) |
| 状态 | closed |
| 标签 | bug;ray;stale |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;fp8;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vLLM failure (ray.exceptions.RayChannelTimeoutError) observed since v0.10.2, with tp=8, pp=4

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug vLLM is crashing when I start inference workload, i.e. first chatbot request, on a distributed AI rig. ./launch_vllm.sh openai/gpt-oss-120b --tp 8 --pp 4 --max-model-len 64k --max-num-batched-tokens 64k --max-num-seqs 16 --gpu-memory-utilization 0.95 The same problem happens with Qwen/Qwen3-32B-FP8 APIServer pid=426) INFO 10-07 12:50:14 [loggers.py:123] Engine 000: Avg prompt throughput: 0.0 tokens/s, Avg generation throughput: 0.0 tokens/s, Running: 1 reqs, Waiting: 0 reqs, GPU KV cache u sage: 0.1%, Prefix cache hit rate: 5.6% (EngineCore_DP0 pid=610) ERROR 10-07 12:51:42 [dump_input.py:69] Dumping input data for V1 LLM engine (v0.10.2) with config: model='openai/gpt-oss-120b', speculative_config=None, tokenizer='opena i/gpt-oss-120b', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.bfloat16, max_seq_len=64000, download_dir=None, load_ format=auto, tensor_parallel_size=8, pipeline_parallel_size=2, data_parallel_size=1, disable_custom_all_reduce=False, quantization=mxfp4, enforce_eager=False, kv_cache_dtype=auto, device_config=c uda, decoding_config=Dec...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 7: pu-memory-utilization 0.95 The same problem happens with Qwen/Qwen3-32B-FP8 APIServer pid=426) INFO 10-07 12:50:14 [loggers.py:123] Engine 000: Avg prompt throughput: 0.0 tokens/s, Avg generation throughput: 0.0 tokens/...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 7: .RayChannelTimeoutError) observed since v0.10.2, with tp=8, pp=4 bug;ray;stale ### Your current environment ### 🐛 Describe the bug vLLM is crashing when I start inference workload, i.e. first chatbot request, on a distr...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: oss'), observability_co nfig=ObservabilityConfig(show_hidden_metrics_for_version=None, otlp_traces_endpoint=None, collect_detailed_traces=None), seed=0, served_model_name=openai/gpt-oss-120b, enable_prefix_caching=True,...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: first chatbot request, on a distributed AI rig. ./launch_vllm.sh openai/gpt-oss-120b --tp 8 --pp 4 --max-model-len 64k --max-num-batched-tokens 64k --max-num-seqs 16 --gpu-memory-utilization 0.95 The same problem happen...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: le_config":{"enable_auto_functionalized_v2":false},"inductor_passes":{},"cudagraph_mode":1,"use_cudagraph":true,"cudagraph_num_of_warmups":1,"cudagr aph_capture_sizes":[1024,1008,992,976,960,944,928,912,896,880,864,848,...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
