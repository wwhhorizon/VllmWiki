# vllm-project/vllm#24929: [Bug]: KeyError in apply_grammar_bitmask for structured outputs

| 字段 | 值 |
| --- | --- |
| Issue | [#24929](https://github.com/vllm-project/vllm/issues/24929) |
| 状态 | closed |
| 标签 | bug;structured-output |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: KeyError in apply_grammar_bitmask for structured outputs

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug This crash happens rarely but it kills vllm when it happens. My understanding is that sometimes `scheduler_output.structured_output_request_ids` gets a request that is missing in `model_runner.input_batch.req_id_to_index`. That is probably not expected. And the current code in `apply_grammar_bitmask` is not prepared for such cases. This bug is hard to reproduce. Stack trace: ``` (Worker_TP2 pid=405) ERROR 09-15 20:18:35 [multiproc_executor.py:654] Traceback (most recent call last): (Worker_TP2 pid=405) ERROR 09-15 20:18:35 [multiproc_executor.py:654] File "/opt/venv/lib/python3.13/site-packages/vllm/v1/executor/multiproc_executor.py", line 649, in worker_busy_loop (Worker_TP2 pid=405) ERROR 09-15 20:18:35 [multiproc_executor.py:654] output = func(*args, **kwargs) (Worker_TP2 pid=405) ERROR 09-15 20:18:35 [multiproc_executor.py:654] File "/opt/venv/lib/python3.13/site-packages/torch/utils/_contextlib.py", line 120, in decorate_context (Worker_TP2 pid=405) ERROR 09-15 20:18:35 [multiproc_executor.py:654] return func(*args, **kwargs) (Worker_TP2 pid=405) ERROR 09-15 20:18:35 [multiproc_executor.py:654] File "/opt/venv/lib/python3.13...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: but it kills vllm when it happens. My understanding is that sometimes `scheduler_output.structured_output_request_ids` gets a request that is missing in `model_runner.input_batch.req_id_to_index`. That is probably not e...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: nd=''), observability_config=ObservabilityConfig(show_hidden_metrics_for_version=None, otlp_traces_endpoint=None, collect_detailed_traces=None), seed=0, served_model_name=meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: 197b0) with config: model='meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8', speculative_config=None, tokenizer='meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8', skip_tokenizer_init=False, tokenizer_mode=auto, revi...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: output.structured_output_request_ids` gets a request that is missing in `model_runner.input_batch.req_id_to_index`. That is probably not expected. And the current code in `apply_grammar_bitmask` is not prepared for such...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: kv_cache_dtype=auto, device_config=cuda, decoding_config=DecodingConfig(backend='auto', disable_fallback=False, disable_any_whitespace=False, disable_additional_properties=False, reasoning_backend=''), observability_con...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
