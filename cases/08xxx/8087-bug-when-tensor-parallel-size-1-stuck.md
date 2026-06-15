# vllm-project/vllm#8087: [Bug]: when tensor-parallel-size>1，Stuck

| 字段 | 值 |
| --- | --- |
| Issue | [#8087](https://github.com/vllm-project/vllm/issues/8087) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 16; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: when tensor-parallel-size>1，Stuck

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug **vllm serve llm/qwen/Qwen2-0.5B-Instruct --tensor-parallel-size 2** INFO 09-02 12:45:15 api_server.py:144] Multiprocessing frontend to use ipc:///tmp/2b15b866-6a79-49e6-95c9-d1269a5952b6 for RPC Path. INFO 09-02 12:45:15 api_server.py:161] Started engine process with PID 814714 INFO 09-02 12:45:19 config.py:813] Defaulting to use mp for distributed inference INFO 09-02 12:45:19 llm_engine.py:184] Initializing an LLM engine (v0.5.5) with config: model='llm/qwen/Qwen2-0.5B-Instruct', speculative_config=None, tokenizer='llm/qwen/Qwen2-0.5B-Instruct', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, rope_scaling=None, rope_theta=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.bfloat16, max_seq_len=32768, download_dir=None, load_format=LoadFormat.AUTO, tensor_parallel_size=2, pipeline_parallel_size=1, disable_custom_all_reduce=False, quantization=None, enforce_eager=False, kv_cache_dtype=auto, quantization_param_path=None, device_config=cuda, decoding_config=DecodingConfig(guided_decoding_backend='outlines'), observability_config=ObservabilityConfig(otlp_traces_endpoint=None, collect_model_forward_ti...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: None, rope_theta=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.bfloat16, max_seq_len=32768, download_dir=None, load_format=LoadFormat.AUTO, tensor_parallel_size=2, pipeline_parallel_size=1, disable...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: ### Your current environment ### 🐛 Describe the bug **vllm serve llm/qwen/Qwen2-0.5B-Instruct --tensor-parallel-size 2** INFO 09-02 12:45:15 api_server.py:144] Multiprocessing frontend to use ipc:///tmp/2b15b866-6a79-49...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: _caching=False) WARNING 09-02 12:45:19 multiproc_gpu_executor.py:59] Reducing Torch parallelism from 32 threads to 1 to avoid unnecessary CPU contention. Set OMP_NUM_THREADS in the external environment to tune this valu...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: =False, kv_cache_dtype=auto, quantization_param_path=None, device_config=cuda, decoding_config=DecodingConfig(guided_decoding_backend='outlines'), observability_config=ObservabilityConfig(otlp_traces_endpoint=None, coll...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: when tensor-parallel-size>1，Stuck bug;stale ### Your current environment ### 🐛 Describe the bug **vllm serve llm/qwen/Qwen2-0.5B-Instruct --tensor-parallel-size 2** INFO 09-02 12:45:15 api_server.py:144] Multipro...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
