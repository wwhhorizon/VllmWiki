# vllm-project/vllm#29625: [Bug][CPU Backend]: EngineCore crashes on ARM CPU when enforce_eager=False

| 字段 | 值 |
| --- | --- |
| Issue | [#29625](https://github.com/vllm-project/vllm/issues/29625) |
| 状态 | closed |
| 标签 | bug;cpu |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;frontend_api;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug][CPU Backend]: EngineCore crashes on ARM CPU when enforce_eager=False

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When running vLLM on ARM CPU with `enforce_eager=False` the engine crashes during initialization, before any model execution occurs. Command: ``` vllm bench throughput \ --num-prompts 64 \ --seed 0 \ --dataset-name sharegpt \ --max-model-len 4096 \ --input-len 512 \ --model meta-llama/Llama-3.1-8B-Instruct ``` (Default behavior: enforce_eager=False) Full Logs: ``` INFO 11-27 18:54:56 [scheduler.py:207] Chunked prefill is enabled with max_num_batched_tokens=4096. WARNING 11-27 18:54:57 [cpu.py:390] Pin memory is not supported on CPU. INFO 11-27 18:54:59 [importing.py:68] Triton not installed or not compatible; certain GPU-related functions will not be available. (EngineCore_DP0 pid=511518) INFO 11-27 18:55:02 [core.py:93] Initializing a V1 LLM engine (v0.11.2.dev188+g730bd3537.d20251126) with config: model='meta-llama/Llama-3.1-8B-Instruct', speculative_config=None, tokenizer='meta-llama/Llama-3.1-8B-Instruct', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.bfloat16, max_seq_len=4096, download_dir=None, load_format=auto, tensor_parallel_size=1, pipeline_...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: 57 [cpu.py:390] Pin memory is not supported on CPU. INFO 11-27 18:54:59 [importing.py:68] Triton not installed or not compatible; certain GPU-related functions will not be available. (EngineCore_DP0 pid=511518) INFO 11-...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: [Bug][CPU Backend]: EngineCore crashes on ARM CPU when enforce_eager=False bug;cpu ### Your current environment ### 🐛 Describe the bug When running vLLM on ARM CPU with `enforce_eager=False` the engine crashes during in...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: e=auto, revision=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.bfloat16, max_seq_len=4096, download_dir=None, load_format=auto, tensor_parallel_size=1, pipeline_parallel_size=1, data_parallel_size=...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: nforce_eager=False` the engine crashes during initialization, before any model execution occurs. Command: ``` vllm bench throughput \ --num-prompts 64 \ --seed 0 \ --dataset-name sharegpt \ --max-model-len 4096 \ --inpu...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: ault behavior: enforce_eager=False) Full Logs: ``` INFO 11-27 18:54:56 [scheduler.py:207] Chunked prefill is enabled with max_num_batched_tokens=4096. WARNING 11-27 18:54:57 [cpu.py:390] Pin memory is not supported on C...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
