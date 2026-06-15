# vllm-project/vllm#19069: [Bug]: Device selection broken in v0.9

| 字段 | 值 |
| --- | --- |
| Issue | [#19069](https://github.com/vllm-project/vllm/issues/19069) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
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

> [Bug]: Device selection broken in v0.9

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Create a new instance of LLM with device specified in a multi-gpu machine ``` from vllm import LLM llm = LLM(device="cuda:1", quantization='bitsandbytes', load_format='bitsandbytes', model='unsloth/Mistral-Small-3.1-24B-Instruct-2503-bnb-4bit') ``` in v0.9.0.1 the model is then placed on cuda instead of cuda:1 as can also be seen in the log output (look for device_config): ``` ... INFO 06-03 08:36:34 [core.py:65] Initializing a V1 LLM engine (v0.9.0.1) with config: model='unsloth/Mistral-Small-3.1-24B-Instruct-2503-bnb-4bit', speculative_config=None, tokenizer='unsloth/Mistral-Small-3.1-24B-Instruct-2503-bnb-4bit', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, override_neuron_config={}, tokenizer_revision=None, trust_remote_code=False, dtype=torch.bfloat16, max_seq_len=14500, download_dir=None, load_format=LoadFormat.BITSANDBYTES, tensor_parallel_size=1, pipeline_parallel_size=1, disable_custom_all_reduce=False, quantization=bitsandbytes, enforce_eager=False, kv_cache_dtype=auto, device_config=cuda, decoding_config=DecodingConfig(backend='auto', disable_fallback=False, disable_any_whitespace=False, disable_additi...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: ### 🐛 Describe the bug Create a new instance of LLM with device specified in a multi-gpu machine ``` from vllm import LLM llm = LLM(device="cuda:1", quantization='bitsandbytes', load_format='bitsandbytes', model='unslot...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: a multi-gpu machine ``` from vllm import LLM llm = LLM(device="cuda:1", quantization='bitsandbytes', load_format='bitsandbytes', model='unsloth/Mistral-Small-3.1-24B-Instruct-2503-bnb-4bit') ``` in v0.9.0.1 the model is...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: kv_cache_dtype=auto, device_config=cuda, decoding_config=DecodingConfig(backend='auto', disable_fallback=False, disable_any_whitespace=False, disable_additional_properties=False, reasoning_backend=''), observability_con...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: cified in a multi-gpu machine ``` from vllm import LLM llm = LLM(device="cuda:1", quantization='bitsandbytes', load_format='bitsandbytes', model='unsloth/Mistral-Small-3.1-24B-Instruct-2503-bnb-4bit') ``` in v0.9.0.1 th...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: import LLM llm = LLM(device="cuda:1", quantization='bitsandbytes', load_format='bitsandbytes', model='unsloth/Mistral-Small-3.1-24B-Instruct-2503-bnb-4bit') ``` in v0.9.0.1 the model is then placed on cuda instead of cu...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
