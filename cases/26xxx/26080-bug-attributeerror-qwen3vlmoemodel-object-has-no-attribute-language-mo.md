# vllm-project/vllm#26080: [Bug]: AttributeError: 'Qwen3VLMoeModel' object has no attribute 'language_model.embed_tokens'

| 字段 | 值 |
| --- | --- |
| Issue | [#26080](https://github.com/vllm-project/vllm/issues/26080) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: AttributeError: 'Qwen3VLMoeModel' object has no attribute 'language_model.embed_tokens'

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ```python llm_config = LLMConfig( model_loading_config=dict( model_id=MODEL_ID, model_source=Qwen/Qwen3-VL-235B-A22B-Instruct, model_kwargs={"trust_remote_code": True}, ), deployment_config=dict( autoscaling_config=dict( min_replicas=1, max_replicas=1, target_ongoing_requests=TARGET_ONGOING_REQUESTS, target_num_ongoing_requests_per_replica=TARGET_NUM_ONGOING_REQUESTS_PER_REPLICA, ), max_ongoing_requests=MAX_ONGOING_REQUESTS, name=DEPLOYMENT_NAME, ), engine_kwargs=dict( quantization=fp8, worker_use_ray=False, tensor_parallel_size=1, pipeline_parallel_size=7, gpu_memory_utilization=GPU_MEMORY_UTILIZATION, dtype=bfloat16, max_num_batched_tokens=MAX_NUM_BATCHED_TOKENS, max_model_len=MAX_MODEL_LEN, max_num_seqs=MAX_NUM_SEQS, ) ) deployment = build_openai_app({"llm_configs": [llm_config]}) ``` Error logs: ``` INFO 10-02 06:06:01 [gpu_model_runner.py:1953] Starting to load model Qwen/Qwen3-VL-235B-A22B-Instruct... INFO 10-02 06:06:01 [gpu_model_runner.py:1985] Loading model from scratch... INFO 10-02 06:06:01 [transformers.py:400] Using Transformers backend. ERROR 10-02 06:06:02 [worker_base.py:619] Error executing method 'load_model'....

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 6: TS, name=DEPLOYMENT_NAME, ), engine_kwargs=dict( quantization=fp8, worker_use_ray=False, tensor_parallel_size=1, pipeline_parallel_size=7, gpu_memory_utilization=GPU_MEMORY_UTILIZATION, dtype=bfloat16, max_num_batched_t...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: AttributeError: 'Qwen3VLMoeModel' object has no attribute 'language_model.embed_tokens' bug ### Your current environment ### 🐛 Describe the bug ```python llm_config = LLMConfig( model_loading_config=dict( model_i...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: =MAX_MODEL_LEN, max_num_seqs=MAX_NUM_SEQS, ) ) deployment = build_openai_app({"llm_configs": [llm_config]}) ``` Error logs: ``` INFO 10-02 06:06:01 [gpu_model_runner.py:1953] Starting to load model Qwen/Qwen3-VL-235B-A2...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: min_replicas=1, max_replicas=1, target_ongoing_requests=TARGET_ONGOING_REQUESTS, target_num_ongoing_requests_per_replica=TARGET_NUM_ONGOING_REQUESTS_PER_REPLICA, ), max_ongoing_requests=MAX_ONGOING_REQUESTS, name=DEPLOY...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: scratch... INFO 10-02 06:06:01 [transformers.py:400] Using Transformers backend. ERROR 10-02 06:06:02 [worker_base.py:619] Error executing method 'load_model'. This might cause deadlock in distributed execution. ERROR 1...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
