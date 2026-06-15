# vllm-project/vllm#35522: [Bug]: Music Flamingo `ValueError: Following weights were not initialized from checkpoint: {'audio_tower.pos_emb.freqs'}`

| 字段 | 值 |
| --- | --- |
| Issue | [#35522](https://github.com/vllm-project/vllm/issues/35522) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Music Flamingo `ValueError: Following weights were not initialized from checkpoint: {'audio_tower.pos_emb.freqs'}`

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug vllm 0.15.2 and 0.16 I am testing this model for research purposes and it seems that the implementation of music flamingo is wrong. The model correctly works on hf code ``` from vllm import LLM model_path = "nvidia/music-flamingo-hf" model = LLM( model=model_path, trust_remote_code=True, limit_mm_per_prompt={"audio": 1}, max_model_len=4096, seed=1234, ) ``` Error: ``` (EngineCore_DP0 pid=5853) INFO 02-27 15:33:28 [core.py:97] Initializing a V1 LLM engine (v0.16.0) with config: model='nvidia/music-flamingo-hf', speculative_config=None, tokenizer='nvidia/music-flamingo-hf', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, tokenizer_revision=None, trust_remote_code=True, dtype=torch.bfloat16, max_seq_len=4096, download_dir=None, load_format=auto, tensor_parallel_size=1, pipeline_parallel_size=1, data_parallel_size=1, disable_custom_all_reduce=False, quantization=None, enforce_eager=False, enable_return_routed_experts=False, kv_cache_dtype=auto, device_config=cuda, structured_outputs_config=StructuredOutputsConfig(backend='auto', disable_fallback=False, disable_any_whitespace=False, disable_additional_properties=False,...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: c flamingo is wrong. The model correctly works on hf code ``` from vllm import LLM model_path = "nvidia/music-flamingo-hf" model = LLM( model=model_path, trust_remote_code=True, limit_mm_per_prompt={"audio": 1}, max_mod...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 5: o, device_config=cuda, structured_outputs_config=StructuredOutputsConfig(backend='auto', disable_fallback=False, disable_any_whitespace=False, disable_additional_properties=False, reasoning_parser='', reasoning_parser_p...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: a V1 LLM engine (v0.16.0) with config: model='nvidia/music-flamingo-hf', speculative_config=None, tokenizer='nvidia/music-flamingo-hf', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, tokenizer_revision=N...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: de=auto, revision=None, tokenizer_revision=None, trust_remote_code=True, dtype=torch.bfloat16, max_seq_len=4096, download_dir=None, load_format=auto, tensor_parallel_size=1, pipeline_parallel_size=1, data_parallel_size=...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: nment ### 🐛 Describe the bug vllm 0.15.2 and 0.16 I am testing this model for research purposes and it seems that the implementation of music flamingo is wrong. The model correctly works on hf code ``` from vllm import...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
