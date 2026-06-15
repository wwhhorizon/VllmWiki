# vllm-project/vllm#27979: [Bug]:model response repeat same sentence and never stop on v0.11.x version, v0.10.2 is ok

| 字段 | 值 |
| --- | --- |
| Issue | [#27979](https://github.com/vllm-project/vllm/issues/27979) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | kernel_eff |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]:model response repeat same sentence and never stop on v0.11.x version, v0.10.2 is ok

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug After upgrading to v0.11.x, vllm often triggers endless repetitive output that never terminates When switching back to version 0.10.2, this issue doesn’t occur. The tested model is gpt-oss-20b, here's some vllm log info: vllm serve /model --tensor-parallel-size 1 --trust-remote-code --gpu-memory-utilization 0.92 --enable-auto-tool-choice --tool-call-parser openai --tool-call-parser openai --host 0.0.0.0 --port 8669 --served-model-name gpt-oss-20b --uvicorn-log-level debug --enable-log-requests Initializing a V1 LLM engine (v0.11.0rc2.dev420+gc5c8f5ea5) with config: model='/model', speculative_config=None, tokenizer='/model', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, tokenizer_revision=None, trust_remote_code=True, dtype=torch.bfloat16, max_seq_len=131072, download_dir=None, load_format=auto, tensor_parallel_size=1, pipeline_parallel_size=1, data_parallel_size=1, disable_custom_all_reduce=False, quantization=None, enforce_eager=False, kv_cache_dtype=auto, device_config=cuda, structured_outputs_config=StructuredOutputsConfig(backend='auto', disable_fallback=False, disable_any_whitespace=False, disable_additiona...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: [Bug]:model response repeat same sentence and never stop on v0.11.x version, v0.10.2 is ok bug;stale ### Your current environment ### 🐛 Describe the bug After upgrading to v0.11.x, vllm often triggers endless repetitive...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: de=auto, revision=None, tokenizer_revision=None, trust_remote_code=True, dtype=torch.bfloat16, max_seq_len=131072, download_dir=None, load_format=auto, tensor_parallel_size=1, pipeline_parallel_size=1, data_parallel_siz...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]:model response repeat same sentence and never stop on v0.11.x version, v0.10.2 is ok bug;stale ### Your current environment ### 🐛 Describe the bug After upgrading to v0.11.x, vllm often triggers endless repetitive...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: epeat same sentence and never stop on v0.11.x version, v0.10.2 is ok bug;stale ### Your current environment ### 🐛 Describe the bug After upgrading to v0.11.x, vllm often triggers endless repetitive output that never ter...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: o, device_config=cuda, structured_outputs_config=StructuredOutputsConfig(backend='auto', disable_fallback=False, disable_any_whitespace=False, disable_additional_properties=False, reasoning_parser='openai_gptoss'), obse...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
