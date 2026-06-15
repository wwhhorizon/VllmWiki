# vllm-project/vllm#14181: [Bug][V1]: Kernel crashed when running  qwen2.5_vl model

| 字段 | 值 |
| --- | --- |
| Issue | [#14181](https://github.com/vllm-project/vllm/issues/14181) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;model_support;quantization;sampling_logits |
| 子分类 | runtime_err |
| Operator 关键词 | cuda;fp8;kernel;operator;quantization |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency;memory_layout;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug][V1]: Kernel crashed when running  qwen2.5_vl model

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I'm using the vllm 0.7.3 (enable_vllm_v1) to run qwen2_5_vl model. ```shell Initializing a V1 LLM engine (v0.7.3) with config: model='/qwen2_5-vl-72b', speculative_config=None, tokenizer='/qwen2_5-vl-72b', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, override_neuron_config=None, tokenizer_revision=None, trust_remote_code=True, dtype=torch.bfloat16, max_seq_len=32000, download_dir=None, load_format=auto, tensor_parallel_size=4, pipeline_parallel_size=1, disable_custom_all_reduce=False, quantization=fp8, enforce_eager=False, kv_cache_dtype=auto, device_config=cuda, decoding_config=DecodingConfig(guided_decoding_backend='xgrammar'), observability_config=ObservabilityConfig(otlp_traces_endpoint=None, collect_model_forward_time=False, collect_model_execute_time=False), seed=0, served_model_name=/qwen2_5-vl-72b, num_scheduler_steps=1, multi_step_stream_outputs=True, enable_prefix_caching=False, chunked_prefill_enabled=True, use_async_output_proc=True, disable_mm_preprocessor_cache=False, mm_processor_kwargs=None, pooler_config=None, compilation_config={"splitting_ops":[],"compile_sizes":[],"cudagraph_capture_sizes":[2...

## 现有链接修复摘要

#4 Use FlashAttention for `multi_query_kv_attention` | #6 Automatically configure KV cache size | #7 Support beam search & parallel generation

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: ide_neuron_config=None, tokenizer_revision=None, trust_remote_code=True, dtype=torch.bfloat16, max_seq_len=32000, download_dir=None, load_format=auto, tensor_parallel_size=4, pipeline_parallel_size=1, disable_custom_all...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: kwargs=None, pooler_config=None, compilation_config={"splitting_ops":[],"compile_sizes":[],"cudagraph_capture_sizes":[256,248,240,232,224,216,208,200,192,184,176,168,160,152,144,136,128,120,112,104,96,88,80,72,64,56,48,...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug][V1]: Kernel crashed when running qwen2.5_vl model bug ### Your current environment ### 🐛 Describe the bug I'm using the vllm 0.7.3 (enable_vllm_v1) to run qwen2_5_vl model. ```shell Initializing a V1 LLM engine (v...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: tializing a V1 LLM engine (v0.7.3) with config: model='/qwen2_5-vl-72b', speculative_config=None, tokenizer='/qwen2_5-vl-72b', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, override_neuron_config=None,...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: culative_config=None, tokenizer='/qwen2_5-vl-72b', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, override_neuron_config=None, tokenizer_revision=None, trust_remote_code=True, dtype=torch.bfloat16, max_s...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#4](https://github.com/vllm-project/vllm/pull/4) | mentioned | 0.45 | Use FlashAttention for `multi_query_kv_attention` | nction> + 0x93fb (0x7f9274ebc3fb in /usr/lib64/libpthread.so.0) frame #4: clone + 0x43 (0x7f927471be83 in /usr/lib64/libc.so.6) what(): [pg id 2 pg guid 3 rank 3] process group w |
| [#6](https://github.com/vllm-project/vllm/pull/6) | mentioned | 0.45 | Automatically configure KV cache size | .10.14/lib/python3.10/site-packages/torch/lib/libtorch_cuda.so) frame #6: c10d::processgroupnccl::ncclcommwatchdog() + 0x14d (0x7f92241d561d in /usr/local/python-3.10.14/lib/pytho… |
| [#7](https://github.com/vllm-project/vllm/pull/7) | mentioned | 0.45 | Support beam search & parallel generation | .10.14/lib/python3.10/site-packages/torch/lib/libtorch_cuda.so) frame #7: <unknown function> + 0x145c0 (0x7f9274e225c0 in /usr/local/python-3.10.14/lib/python3.10/site-packages/to… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
