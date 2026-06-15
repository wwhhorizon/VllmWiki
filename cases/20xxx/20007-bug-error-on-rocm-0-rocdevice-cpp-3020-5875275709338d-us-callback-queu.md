# vllm-project/vllm#20007: [Bug]: error on ROCM :0:rocdevice.cpp            :3020: 5875275709338d us:  Callback: Queue 0x7f4580c00000 aborting with error : HSA_STATUS_ERROR_EXCEPTION: An HSAIL operation resulted in a hardware exception. code: 0x1016

| 字段 | 值 |
| --- | --- |
| Issue | [#20007](https://github.com/vllm-project/vllm/issues/20007) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization;speculative_decoding |
| 子分类 |  |
| Operator 关键词 | attention;cuda;kernel;operator;quantization;triton |
| 症状 | build_error |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: error on ROCM :0:rocdevice.cpp            :3020: 5875275709338d us:  Callback: Queue 0x7f4580c00000 aborting with error : HSA_STATUS_ERROR_EXCEPTION: An HSAIL operation resulted in a hardware exception. code: 0x1016

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug log output: ``` INFO 06-11 11:07:19 [config.py:224] Replacing legacy 'type' key with 'rope_type' WARNING 06-11 11:07:19 [config.py:231] Replacing legacy rope_type 'su' with 'longrope' INFO 06-11 11:07:44 [config.py:823] This model supports multiple tasks: {'classify', 'generate', 'score', 'embed', 'reward'}. Defaulting to 'generate'. INFO 06-11 11:07:44 [arg_utils.py:1653] rocm is experimental on VLLM_USE_V1=1. Falling back to V0 Engine. INFO 06-11 11:07:44 [config.py:1980] Disabled the custom all-reduce kernel because it is not supported on current platform. INFO 06-11 11:07:44 [llm_engine.py:230] Initializing a V0 LLM engine (v0.9.1) with config: model='/tmp/f077afb5-1558-4271-8c48-28509d8ee3e5', speculative_config=None, tokenizer='/tmp/f077afb5-1558-4271-8c48-28509d8ee3e5', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, override_neuron_config={}, tokenizer_revision=None, trust_remote_code=True, dtype=torch.bfloat16, max_seq_len=10240, download_dir=None, load_format=auto, tensor_parallel_size=1, pipeline_parallel_size=1, disable_custom_all_reduce=True, quantization=None, enforce_eager=False, kv_cache_dtype=auto,...

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 5: kv_cache_dtype=auto, device_config=cuda, decoding_config=DecodingConfig(backend='auto', disable_fallback=False, disable_any_whitespace=False, disable_additional_properties=False, reasoning_backend=''), observability_con...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: scribe the bug log output: ``` INFO 06-11 11:07:19 [config.py:224] Replacing legacy 'type' key with 'rope_type' WARNING 06-11 11:07:19 [config.py:231] Replacing legacy rope_type 'su' with 'longrope' INFO 06-11 11:07:44...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: on ROCM :0:rocdevice.cpp :3020: 5875275709338d us: Callback: Queue 0x7f4580c00000 aborting with error : HSA_STATUS_ERROR_EXCEPTION: An HSAIL operation resulted in a hardware exception. code: 0x1016 bug;stale ### Your cu...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: rride_neuron_config={}, tokenizer_revision=None, trust_remote_code=True, dtype=torch.bfloat16, max_seq_len=10240, download_dir=None, load_format=auto, tensor_parallel_size=1, pipeline_parallel_size=1, disable_custom_all...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: error on ROCM :0:rocdevice.cpp :3020: 5875275709338d us: Callback: Queue 0x7f4580c00000 aborting with error : HSA_STATUS_ERROR_EXCEPTION: An HSAIL operation resulted in a hardware exception. code: 0x1016 bug;stal...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
