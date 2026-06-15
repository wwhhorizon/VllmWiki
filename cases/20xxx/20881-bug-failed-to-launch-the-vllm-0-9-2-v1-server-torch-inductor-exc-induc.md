# vllm-project/vllm#20881: [Bug]: Failed to launch the vllm 0.9.2 v1 server: torch._inductor.exc.InductorError: SystemError: PY_SSIZE_T_CLEAN macro must be defined for '#' formats

| 字段 | 值 |
| --- | --- |
| Issue | [#20881](https://github.com/vllm-project/vllm/issues/20881) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Failed to launch the vllm 0.9.2 v1 server: torch._inductor.exc.InductorError: SystemError: PY_SSIZE_T_CLEAN macro must be defined for '#' formats

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I installed vllm from source code according to the tutorial in the document, but the following error occurred when starting the server through： ```python vllm server Qwen/Qwen3-1.7B ``` ```text INFO 07-13 14:06:41 [__init__.py:253] Automatically detected platform cuda. INFO 07-13 14:06:43 [api_server.py:1641] vLLM API server version 0.9.2rc2.dev208+g247102f07 INFO 07-13 14:06:43 [cli_args.py:325] non-default args: {'model': 'Qwen/Qwen3-1.7B'} INFO 07-13 14:06:49 [config.py:1560] Using max model len 40960 INFO 07-13 14:06:49 [config.py:2374] Chunked prefill is enabled with max_num_batched_tokens=2048. INFO 07-13 14:06:54 [__init__.py:253] Automatically detected platform cuda. INFO 07-13 14:06:55 [core.py:526] Waiting for init message from front-end. INFO 07-13 14:06:55 [core.py:69] Initializing a V1 LLM engine (v0.9.2rc2.dev208+g247102f07) with config: model='Qwen/Qwen3-1.7B', speculative_config=None, tokenizer='Qwen/Qwen3-1.7B', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, override_neuron_config={}, tokenizer_revision=None, trust_remote_code=False, dtype=torch.bfloat16, max_seq_len=40960, download_dir=None, load...

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 6: kv_cache_dtype=auto, device_config=cuda, decoding_config=DecodingConfig(backend='auto', disable_fallback=False, disable_any_whitespace=False, disable_additional_properties=False, reasoning_backend=''), observability_con...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: ' formats bug ### Your current environment ### 🐛 Describe the bug I installed vllm from source code according to the tutorial in the document, but the following error occurred when starting the server through： ```python...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: ride_neuron_config={}, tokenizer_revision=None, trust_remote_code=False, dtype=torch.bfloat16, max_seq_len=40960, download_dir=None, load_format=LoadFormat.AUTO, tensor_parallel_size=1, pipeline_parallel_size=1, disable...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: ductorError: SystemError: PY_SSIZE_T_CLEAN macro must be defined for '#' formats bug ### Your current environment ### 🐛 Describe the bug I installed vllm from source code according to the tutorial in the document, but t...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: ] Using max model len 40960 INFO 07-13 14:06:49 [config.py:2374] Chunked prefill is enabled with max_num_batched_tokens=2048. INFO 07-13 14:06:54 [__init__.py:253] Automatically detected platform cuda. INFO 07-13 14:06:...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
