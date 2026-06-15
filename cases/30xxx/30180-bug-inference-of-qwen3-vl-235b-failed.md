# vllm-project/vllm#30180: [Bug]: Inference of Qwen3-VL-235B failed

| 字段 | 值 |
| --- | --- |
| Issue | [#30180](https://github.com/vllm-project/vllm/issues/30180) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;gemm;moe;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf;oom;slowdown |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Inference of Qwen3-VL-235B failed

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Using v;;m to infer Qwem3-VL-235B, the log shows that the request was successful, but the model failed to generate a response. This is my startup command： vllm serve /root/.cache/huggingface/Qwen3-VL-235B-A22B-Instruct/ \ --tensor-parallel-size 4 \ --pipeline-parallel-size 3 \ --max-model-len 10240 \ --max_num_seqs 20 \ --gpu_memory_utilization 0.95 \ --max_num_batched_tokens 2048 \ --trust-remote-code \ --block-size 32 \ --enable-chunked-prefill \ --enable-prefix-caching \ --distributed-executor-backend ray \ --enforce-eager \ --served-model-name Qwen3-VL-235B-A22B-Instruct-QX \ | tee /root/.cache/huggingface/test_235b__251205.log ' & Below is the error log: 12-05 22:34:04 [loggers.py:236] Engine 000: Avg prompt throughput: 0.0 tokens/s, Avg generation throughput: 0.0 tokens/s, Running: 1 reqs, Waiting: 0 reqs, GPU KV cache usage: 0.0%, Prefix cache hit rate: 0.0%, MM cache hit rate: 0.0% (EngineCore_DP0 pid=579) ERROR 12-05 22:43:45 [dump_input.py:72] Dumping input data for V1 LLM engine (v0.12.0) with config: model='/root/.cache/huggingface/Qwen3-VL-235B-A22B-Instruct/', speculative_config=None, tokenizer='/root/.cache/hugging...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 8: [Bug]: Inference of Qwen3-VL-235B failed bug;stale ### Your current environment ### 🐛 Describe the bug Using v;;m to infer Qwem3-VL-235B, the log shows that the request was successful, but the model failed to generate a...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: False), observability_config=ObservabilityConfig(show_hidden_metrics_for_version=None, otlp_traces_endpoint=None, collect_detailed_traces=None, kv_cache_metrics=False, kv_cache_metrics_sample=0.01), seed=0, served_model...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: Inference of Qwen3-VL-235B failed bug;stale ### Your current environment ### 🐛 Describe the bug Using v;;m to infer Qwem3-VL-235B, the log shows that the request was successful, but the model failed to generate a...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: de=auto, revision=None, tokenizer_revision=None, trust_remote_code=True, dtype=torch.bfloat16, max_seq_len=10240, download_dir=None, load_format=auto, tensor_parallel_size=4, pipeline_parallel_size=3, data_parallel_size...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 4: ion 0.95 \ --max_num_batched_tokens 2048 \ --trust-remote-code \ --block-size 32 \ --enable-chunked-prefill \ --enable-prefix-caching \ --distributed-executor-backend ray \ --enforce-eager \ --served-model-name Qwen3-VL...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
