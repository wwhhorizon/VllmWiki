# vllm-project/vllm#17144: Missing Opening <think> for Qwen32B

| 字段 | 值 |
| --- | --- |
| Issue | [#17144](https://github.com/vllm-project/vllm/issues/17144) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | distributed_parallel;frontend_api;model_support;quantization |
| 子分类 | kernel_eff |
| Operator 关键词 | cuda;quantization |
| 症状 |  |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> Missing Opening <think> for Qwen32B

### Issue 正文摘录

### Your current environment vllm 0.8.4 ### 🐛 Describe the bug I need to serve Qwen32B model without passing reasoning parser from vllm as I need to do parsing on my end. However the issue here is that the deepseek model provide two tags for reasoning` ` and ` ` in the content output when we dont pass reasoning parser. But Qwen32 can only provide the ending ` ` but miss the opening ` `. such as ``` hello, my reason to this is my content. ``` How to solve this please? I don't want to use the reasoning parser args here. - command: ``` VLLM_USE_V1=0 vllm serve Qwen/QwQ-32B --max-model-len 32000 --gpu-memory-utilization 0.95 --distributed-executor-backend mp --tensor-parallel-size 4 ``` - console ``` INFO 04-24 22:07:43 [llm_engine.py:243] Initializing a V0 LLM engine (v0.8.4) with config: model='Qwen/QwQ-32B', speculative_config=None, tokenizer='Qwen/QwQ-32B', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, override_neuron_config=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.bfloat16, max_seq_len=32000, download_dir=None, load_format=auto, tensor_parallel_size=4, pipeline_parallel_size=1, disable_custom_all_reduce=False, quantization=None, enforce...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: de_neuron_config=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.bfloat16, max_seq_len=32000, download_dir=None, load_format=auto, tensor_parallel_size=4, pipeline_parallel_size=1, disable_custom_all...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: Missing Opening <think> for Qwen32B bug ### Your current environment vllm 0.8.4 ### 🐛 Describe the bug I need to serve Qwen32B model without passing reasoning parser from vllm as I need to do parsing on my end. However...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: Initializing a V0 LLM engine (v0.8.4) with config: model='Qwen/QwQ-32B', speculative_config=None, tokenizer='Qwen/QwQ-32B', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, override_neuron_config=None, tok...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: kwargs=None, pooler_config=None, compilation_config={"splitting_ops":[],"compile_sizes":[],"cudagraph_capture_sizes":[256,248,240,232,224,216,208,200,192,184,176,168,160,152,144,136,128,120,112,104,96,88,80,72,64,56,48,...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ntization=None, enforce_eager=False, kv_cache_dtype=auto, device_config=cuda, decoding_config=DecodingConfig(guided_decoding_backend='xgrammar', reasoning_backend=None), observability_config=ObservabilityConfig(show_hid...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
