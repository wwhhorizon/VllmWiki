# vllm-project/vllm#15992: [Bug]: Fail to load LLM either using offline inference or vllm serve

| 字段 | 值 |
| --- | --- |
| Issue | [#15992](https://github.com/vllm-project/vllm/issues/15992) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Fail to load LLM either using offline inference or vllm serve

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Here is the code I use: ``` from vllm import LLM llm = LLM(model="/home/ubuntu/model/Llama-2-7b-chat-hf") ``` I got the following errors. ``` INFO 04-03 05:54:48 [config.py:598] This model supports multiple tasks: {'classify', 'reward', 'generate', 'embed', 'score'}. Defaulting to 'generate'. INFO 04-03 05:54:48 [config.py:1766] Chunked prefill is enabled with max_num_batched_tokens=8192. INFO 04-03 05:54:49 [core.py:61] Initializing a V1 LLM engine (v0.8.3.dev218+g01b61136.d20250403) with config: model='/home/ubuntu/model/Llama-2-7b-chat-hf', speculative_config=None, tokenizer='/home/ubuntu/model/Llama-2-7b-chat-hf', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, override_neuron_config=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.float16, max_seq_len=4096, download_dir=None, load_format=LoadFormat.AUTO, tensor_parallel_size=1, pipeline_parallel_size=1, disable_custom_all_reduce=False, quantization=None, enforce_eager=False, kv_cache_dtype=auto, device_config=cuda, decoding_config=DecodingConfig(guided_decoding_backend='xgrammar', reasoning_backend=None), observability_config=ObservabilityCo...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: onment ### 🐛 Describe the bug Here is the code I use: ``` from vllm import LLM llm = LLM(model="/home/ubuntu/model/Llama-2-7b-chat-hf") ``` I got the following errors. ``` INFO 04-03 05:54:48 [config.py:598] This model...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: ibe the bug Here is the code I use: ``` from vllm import LLM llm = LLM(model="/home/ubuntu/model/Llama-2-7b-chat-hf") ``` I got the following errors. ``` INFO 04-03 05:54:48 [config.py:598] This model supports multiple...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: uto, device_config=cuda, decoding_config=DecodingConfig(guided_decoding_backend='xgrammar', reasoning_backend=None), observability_config=ObservabilityConfig(show_hidden_metrics=False, otlp_traces_endpoint=None, collect...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Bug]: Fail to load LLM either using offline inference or vllm serve bug;stale ### Your current environment ### 🐛 Describe the bug Here is the code I use: ``` from vllm import LLM llm = LLM(model="/home/ubuntu/model/Lla...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: de_neuron_config=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.float16, max_seq_len=4096, download_dir=None, load_format=LoadFormat.AUTO, tensor_parallel_size=1, pipeline_parallel_size=1, disable_c...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
