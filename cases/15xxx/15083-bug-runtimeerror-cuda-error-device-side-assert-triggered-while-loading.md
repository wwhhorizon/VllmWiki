# vllm-project/vllm#15083: [Bug]: RuntimeError: CUDA error: device-side assert triggered, while loading whisper quantized model (W4A16 GPTQ Method)

| 字段 | 值 |
| --- | --- |
| Issue | [#15083](https://github.com/vllm-project/vllm/issues/15083) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;crash;mismatch;nan_inf |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: RuntimeError: CUDA error: device-side assert triggered, while loading whisper quantized model (W4A16 GPTQ Method)

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ``` llm = LLM( model="Bakht123/whisper-medium-gptq-W4A16-G128", max_model_len=448, max_num_seqs=5, limit_mm_per_prompt={"audio": 1}, # enforce_eager=True # gpu_memory_utilization=0.20 ) print("model 1 is loaded") ``` ``` INFO 03-19 08:39:05 [__init__.py:256] Automatically detected platform cuda. INFO 03-19 08:39:08 [config.py:2595] Downcasting torch.float32 to torch.float16. INFO 03-19 08:39:16 [config.py:583] This model supports multiple tasks: {'embed', 'reward', 'generate', 'score', 'classify', 'transcription'}. Defaulting to 'transcription'. WARNING 03-19 08:39:17 [arg_utils.py:1754] --task transcription is not supported by the V1 Engine. Falling back to V0. INFO 03-19 08:39:17 [llm_engine.py:241] Initializing a V0 LLM engine (v0.8.0) with config: model='Bakht123/whisper-medium-gptq-W4A16-G128', speculative_config=None, tokenizer='Bakht123/whisper-medium-gptq-W4A16-G128', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, override_neuron_config=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.float16, max_seq_len=448, download_dir=None, load_format=LoadFormat.AUTO, tensor_parallel_size=1, pipeli...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: triggered, while loading whisper quantized model (W4A16 GPTQ Method) bug;stale ### Your current environment ### 🐛 Describe the bug ``` llm = LLM( model="Bakht123/whisper-medium-gptq-W4A16-G128", max_model_len=448, max_n...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: kwargs=None, pooler_config=None, compilation_config={"splitting_ops":[],"compile_sizes":[],"cudagraph_capture_sizes":[8,4,2,1],"max_capture_size":8}, use_cached_outputs=False, INFO 03-19 08:39:19 [cuda.py:285] Using Fla...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: meError: CUDA error: device-side assert triggered, while loading whisper quantized model (W4A16 GPTQ Method) bug;stale ### Your current environment ### 🐛 Describe the bug ``` llm = LLM( model="Bakht123/whisper-medium-gp...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: uto, device_config=cuda, decoding_config=DecodingConfig(guided_decoding_backend='xgrammar', reasoning_backend=None), observability_config=ObservabilityConfig(show_hidden_metrics=False, otlp_traces_endpoint=None, collect...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: RuntimeError: CUDA error: device-side assert triggered, while loading whisper quantized model (W4A16 GPTQ Method) bug;stale ### Your current environment ### 🐛 Describe the bug ``` llm = LLM( model="Bakht123/whisp...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
