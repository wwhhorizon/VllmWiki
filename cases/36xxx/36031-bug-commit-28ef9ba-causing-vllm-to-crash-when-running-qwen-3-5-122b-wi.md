# vllm-project/vllm#36031: [Bug]: Commit 28ef9ba causing VLLM to crash when running Qwen 3.5 122B with Speculative Decoding enabled

| 字段 | 值 |
| --- | --- |
| Issue | [#36031](https://github.com/vllm-project/vllm/issues/36031) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;kernel;moe;operator;quantization;sampling;triton |
| 症状 | build_error;crash;mismatch;nan_inf |
| 根因提示 | dtype;env_dependency;race_condition |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Commit 28ef9ba causing VLLM to crash when running Qwen 3.5 122B with Speculative Decoding enabled

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Commit 28ef9ba399340ea7013df8cd1c359b07acc0a302 introduces or triggers a bug that is causing VLLM to crash when running Qwen 3.5 122B with Speculative Decoding enabled This was pushed as part of this PR: https://github.com/vllm-project/vllm/pull/34552 The bug does not appear to be present fb7fdc49c4a0c629fd92a5e49c08ec86f5dd8ff9 Launch command: ``` vllm serve olka-fi/Qwen3.5-122B-A10B-MXFP4 \ --max-num-seqs 128 \ --max-model-len 262144 \ --enable-auto-tool-choice \ --tool-call-parser qwen3_xml \ --port 11434 \ --reasoning-parser qwen3 \ --served-model-name qwen/qwen3.5-122B \ --speculative-config '{"method":"qwen3_next_mtp","num_speculative_tokens": 5}' ``` Error: ``` (EngineCore_DP0 pid=2190886) ERROR 03-04 10:04:29 [dump_input.py:72] Dumping input data for V1 LLM engine (v0.16.1rc1.dev224+g289fc48ab) with config: model='olka-fi/Qwen3.5-122B-A10B-MXFP4', speculative_config=SpeculativeConfig(method='mtp', model='olka-fi/Qwen3.5-122B-A10B-MXFP4', num_spec_tokens=5), tokenizer='olka-fi/Qwen3.5-122B-A10B-MXFP4', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, tokenizer_revision=None, trust_remote_code=False, dtype=tor...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 7: g]: Commit 28ef9ba causing VLLM to crash when running Qwen 3.5 122B with Speculative Decoding enabled bug ### Your current environment ### 🐛 Describe the bug Commit 28ef9ba399340ea7013df8cd1c359b07acc0a302 introduces or...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 6: 08ec86f5dd8ff9 Launch command: ``` vllm serve olka-fi/Qwen3.5-122B-A10B-MXFP4 \ --max-num-seqs 128 \ --max-model-len 262144 \ --enable-auto-tool-choice \ --tool-call-parser qwen3_xml \ --port 11434 \ --reasoning-parser...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: False), observability_config=ObservabilityConfig(show_hidden_metrics_for_version=None, otlp_traces_endpoint=None, collect_detailed_traces=None, kv_cache_metrics=False, kv_cache_metrics_sample=0.01, cudagraph_metrics=Fal...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: o, device_config=cuda, structured_outputs_config=StructuredOutputsConfig(backend='auto', disable_fallback=False, disable_any_whitespace=False, disable_additional_properties=False, reasoning_parser='qwen3', reasoning_par...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: , enable_return_routed_experts=False, kv_cache_dtype=auto, device_config=cuda, structured_outputs_config=StructuredOutputsConfig(backend='auto', disable_fallback=False, disable_any_whitespace=False, disable_additional_p...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
