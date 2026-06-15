# vllm-project/vllm#14593: [Bug]: model not load to vram

| 字段 | 值 |
| --- | --- |
| Issue | [#14593](https://github.com/vllm-project/vllm/issues/14593) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: model not load to vram

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I get an infinite wait when I use a multi asynchronous engine in vllm to raise it to multi gpu. Util is being used for gpu but it doesn't load to vram. this is my code ```python model_id = "/workspace/share/model/gemma2-9b-it" engine_args = AsyncEngineArgs( model=model_id, dtype=torch.bfloat16, trust_remote_code=True, quantization="bitsandbytes", load_format="bitsandbytes", gpu_memory_utilization=0.75, tensor_parallel_size=2, ) engine = AsyncLLMEngine.from_engine_args(engine_args) ``` this is log ```text INFO 03-11 02:12:06 config.py:2444] Downcasting torch.float32 to torch.bfloat16. INFO 03-11 02:12:11 config.py:549] This model supports multiple tasks: {'embed', 'classify', 'score', 'reward', 'generate'}. Defaulting to 'generate'. WARNING 03-11 02:12:11 config.py:628] bitsandbytes quantization is not fully optimized yet. The speed can be slower than non-quantized models. INFO 03-11 02:12:11 config.py:1382] Defaulting to use mp for distributed inference INFO 03-11 02:12:12 llm_engine.py:234] Initializing a V0 LLM engine (v0.7.3) with config: model='/workspace/share/model/gemma2-9b-it', speculative_config=None, tokenizer='/workspa...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: l/gemma2-9b-it" engine_args = AsyncEngineArgs( model=model_id, dtype=torch.bfloat16, trust_remote_code=True, quantization="bitsandbytes", load_format="bitsandbytes", gpu_memory_utilization=0.75, tensor_parallel_size=2,...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: [Bug]: model not load to vram bug;stale ### Your current environment ### 🐛 Describe the bug I get an infinite wait when I use a multi asynchronous engine in vllm to raise it to multi gpu. Util is being used for gpu but...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: kwargs=None, pooler_config=None, compilation_config={"splitting_ops":[],"compile_sizes":[],"cudagraph_capture_sizes":[256,248,240,232,224,216,208,200,192,184,176,168,160,152,144,136,128,120,112,104,96,88,80,72,64,56,48,...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: model not load to vram bug;stale ### Your current environment ### 🐛 Describe the bug I get an infinite wait when I use a multi asynchronous engine in vllm to raise it to multi gpu. Util is being used for gpu but...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: uto, device_config=cuda, decoding_config=DecodingConfig(guided_decoding_backend='xgrammar'), observability_config=ObservabilityConfig(otlp_traces_endpoint=None, collect_model_forward_time=False, collect_model_execute_ti...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
