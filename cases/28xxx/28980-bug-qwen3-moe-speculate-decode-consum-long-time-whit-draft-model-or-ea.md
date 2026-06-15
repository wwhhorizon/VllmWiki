# vllm-project/vllm#28980: [Bug]: Qwen3 Moe Speculate decode consum long time whit draft model or eagle3

| 字段 | 值 |
| --- | --- |
| Issue | [#28980](https://github.com/vllm-project/vllm/issues/28980) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;moe;quantization;scheduler_memory;speculative_decoding |
| 子分类 | cold_start |
| Operator 关键词 | cache;cuda;fp8;moe;quantization;triton |
| 症状 | build_error |
| 根因提示 | dtype;env_dependency;memory_layout;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Qwen3 Moe Speculate decode consum long time whit draft model or eagle3

### Issue 正文摘录

### Your current environment H20 * 4 CUDA：12.4 vllm: v0.11.1rc7.dev262+gb9489f51e ### 🐛 Describe the bug its take about 1h from the last load eagle to start compile. and gpu unit is 1% or always 0% ``` (APIServer pid=3358568) INFO 11-19 02:13:25 [model.py:631] Resolved architecture: Qwen3MoeForCausalLM (APIServer pid=3358568) INFO 11-19 02:13:25 [model.py:1745] Using max model len 65536 (APIServer pid=3358568) INFO 11-19 02:13:30 [model.py:631] Resolved architecture: LlamaForCausalLMEagle3 (APIServer pid=3358568) INFO 11-19 02:13:30 [model.py:1745] Using max model len 40960 (APIServer pid=3358568) INFO 11-19 02:13:30 [scheduler.py:216] Chunked prefill is enabled with max_num_batched_tokens=8192. (EngineCore_DP0 pid=3358913) INFO 11-19 02:13:36 [core.py:93] Initializing a V1 LLM engine (v0.11.1rc7.dev262+gb9489f51e) with config: model='/data/models/Qwen3-235B-A22B-Instruct-2507-FP8', speculative_config=SpeculativeConfig(method='eagle3', model=' /data/models/Qwen3-Moe-Eagle3', num_spec_tokens=3), tokenizer='/data/models/Qwen3-235B-A22B-Instruct-2507-FP8', skip_tokenizer _init=False, tokenizer_mode=auto, revision=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.bfl...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: [Bug]: Qwen3 Moe Speculate decode consum long time whit draft model or eagle3 bug ### Your current environment H20 * 4 CUDA：12.4 vllm: v0.11.1rc7.dev262+gb9489f51e ### 🐛 Describe the bug its take about 1h from the last...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: 🐛 Describe the bug its take about 1h from the last load eagle to start compile. and gpu unit is 1% or always 0% ``` (APIServer pid=3358568) INFO 11-19 02:13:25 [model.py:631] Resolved architecture: Qwen3MoeForCausalLM (...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: with config: model='/data/models/Qwen3-235B-A22B-Instruct-2507-FP8', speculative_config=SpeculativeConfig(method='eagle3', model=' /data/models/Qwen3-Moe-Eagle3', num_spec_tokens=3), tokenizer='/data/models/Qwen3-235B-A...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: Qwen3 Moe Speculate decode consum long time whit draft model or eagle3 bug ### Your current environment H20 * 4 CUDA：12.4 vllm: v0.11.1rc7.dev262+gb9489f51e ### 🐛 Describe the bug its take about 1h from the last...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: _config=cuda, structured_outpu ts_config=StructuredOutputsConfig(backend='auto', disable_fallback=False, disable_any_whitespace=False, disable_additional_pro perties=False, reasoning_parser='', reasoning_parser_plugin='...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
