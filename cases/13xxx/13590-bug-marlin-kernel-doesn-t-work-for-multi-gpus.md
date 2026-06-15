# vllm-project/vllm#13590: [Bug]: Marlin kernel doesn't work for multi-gpus

| 字段 | 值 |
| --- | --- |
| Issue | [#13590](https://github.com/vllm-project/vllm/issues/13590) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;distributed_parallel;frontend_api;model_support;quantization |
| 子分类 | latency_reg |
| Operator 关键词 | attention;cuda;kernel;quantization |
| 症状 | slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Marlin kernel doesn't work for multi-gpus

### Issue 正文摘录

### Your current environment n/a ### 🐛 Describe the bug For single GPU, vllm can convert https://huggingface.co/hugging-quants/Meta-Llama-3.1-70B-Instruct-GPTQ-INT4 to use gptq_marlin: ``` INFO 02-19 12:52:12 __init__.py:183] Automatically detected platform cuda. INFO 02-19 12:52:17 config.py:520] This model supports multiple tasks: {'embed', 'reward', 'classify', 'generate', 'score'}. Defaulting to 'generate'. INFO 02-19 12:52:17 gptq_marlin.py:109] The model is convertible to gptq_marlin during runtime. Using gptq_marlin kernel. INFO 02-19 12:52:17 llm_engine.py:232] Initializing an LLM engine (v0.7.0) with config: model='/tmp/tmpt2gewfl8', speculative_config=None, tokenizer='/tmp/tmpt2gewfl8', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, override_neuron_config=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.float16, max_seq_len=1024, download_dir=None, load_format= , tensor_parallel_size=1, pipeline_parallel_size=1, disable_custom_all_reduce=False, quantization=gptq_marlin, enforce_eager=False, kv_cache_dtype=auto, device_config=cuda, decoding_config=DecodingConfig(guided_decoding_backend='xgrammar'), observability_config=ObservabilityConfi...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: t n/a ### 🐛 Describe the bug For single GPU, vllm can convert https://huggingface.co/hugging-quants/Meta-Llama-3.1-70B-Instruct-GPTQ-INT4 to use gptq_marlin: ``` INFO 02-19 12:52:12 __init__.py:183] Automatically detect...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: the bug For single GPU, vllm can convert https://huggingface.co/hugging-quants/Meta-Llama-3.1-70B-Instruct-GPTQ-INT4 to use gptq_marlin: ``` INFO 02-19 12:52:12 __init__.py:183] Automatically detected platform cuda. INF...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Bug]: Marlin kernel doesn't work for multi-gpus bug;stale ### Your current environment n/a ### 🐛 Describe the bug For single GPU, vllm can convert https://huggingface.co/hugging-quants/Meta-Llama-3.1-70B-Instruct-GPTQ-...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: kwargs=None, pooler_config=None, compilation_config={"splitting_ops":[],"compile_sizes":[],"cudagraph_capture_sizes":[256,248,240,232,224,216,208,200,192,184,176,168,160,152,144,136,128,120,112,104,96,88,80,72,64,56,48,...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` INFO 02-19 12:52:12 __init__.py:183] Automatically detected platform cuda. INFO 02-19 12:52:17 config.py:520] This model supports multiple tasks: {'embed', 'reward', 'classify', 'generate', 'score'}. Defaulting to '...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
