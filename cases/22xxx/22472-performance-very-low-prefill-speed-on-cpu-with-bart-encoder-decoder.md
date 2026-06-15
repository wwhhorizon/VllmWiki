# vllm-project/vllm#22472: [Performance]: Very low prefill speed on CPU with BART (encoder-decoder)

| 字段 | 值 |
| --- | --- |
| Issue | [#22472](https://github.com/vllm-project/vllm/issues/22472) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;frontend_api;hardware_porting;model_support;quantization;sampling_logits |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Performance]: Very low prefill speed on CPU with BART (encoder-decoder)

### Issue 正文摘录

### Proposal to improve performance _No response_ ### Report of performance regression Hi team, I am using v0.9.2 with v0 engine (since v1 doesn't support encoder-decoder) I found my cpu inference is extremely slow than torch. "POST /summarize HTTP/1.1" | 1/2 [00:01<00:01, 1.86s/it, est. speed input: 1.08 toks/s, output: 26.93 toks/s] It took 2000ms to finish the process where torch process under 600ms Is there anything I should check to make sure it is running correctly? ```text Initializing a V0 LLM engine (v0.9.2) with config: model='facebook/bart-base', speculative_config=None, tokenizer='facebook/bart-base', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, override_neuron_config={}, tokenizer_revision=None, trust_remote_code=False, dtype=torch.bfloat16, max_seq_len=512, download_dir=None, load_format=auto, tensor_parallel_size=1, pipeline_parallel_size=1, disable_custom_all_reduce=True, quantization=None, enforce_eager=True, kv_cache_dtype=auto, device_config=cpu, decoding_config=DecodingConfig(backend='auto', disable_fallback=False, disable_any_whitespace=False, disable_additional_properties=False, reasoning_backend=''), observability_config=ObservabilityConfig...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: nd=''), observability_config=ObservabilityConfig(show_hidden_metrics_for_version=None, otlp_traces_endpoint=None, collect_detailed_traces=None), seed=0, served_model_name=facebook/bart-base, num_scheduler_steps=1, multi...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: onfig":{"enable_auto_functionalized_v2":false},"inductor_passes":{},"use_cudagraph":true,"cudagraph_num_of_warmups":0," cudagraph_capture_sizes": [], "cudagraph_copy_inputs":false,"full_cuda_graph":false,"max_capture_si...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: [Performance]: Very low prefill speed on CPU with BART (encoder-decoder) performance;stale ### Proposal to improve performance _No response_ ### Report of performance regression Hi team, I am using v0.9.2 with v0 engine...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: ide_neuron_config={}, tokenizer_revision=None, trust_remote_code=False, dtype=torch.bfloat16, max_seq_len=512, download_dir=None, load_format=auto, tensor_parallel_size=1, pipeline_parallel_size=1, disable_custom_all_re...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: is running correctly? ```text Initializing a V0 LLM engine (v0.9.2) with config: model='facebook/bart-base', speculative_config=None, tokenizer='facebook/bart-base', skip_tokenizer_init=False, tokenizer_mode=auto, revis...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
