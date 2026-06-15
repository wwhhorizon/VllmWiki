# vllm-project/vllm#7991: [Bug]: name 'vllm_ops' is not defined using offline build from source vllm 0.4.3

| 字段 | 值 |
| --- | --- |
| Issue | [#7991](https://github.com/vllm-project/vllm/issues/7991) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | activation_norm;attention_kv_cache;ci_build;frontend_api;hardware_porting;model_support;quantization;speculative_decoding |
| 子分类 | latency_reg |
| Operator 关键词 | activation;attention;cuda;operator;quantization;triton |
| 症状 | build_error;crash;import_error;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: name 'vllm_ops' is not defined using offline build from source vllm 0.4.3

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I built vllm=0.4.3+cu124 on Nvidia NGC docker container pytorch:24.04-py3 with xformers=0.0.26.post1 and without vllm-flash-attn (not supported on T4 gpu) . Building process was successful, but throws this error when I try to start an openai server. Here is full stacktrace. ```python INFO 08-29 09:39:48 llm_engine.py:161] Initializing an LLM engine (v0.4.3) with config: model='chatglm3-6b/', speculative_config=None, tokenizer='chatglm3-6b/', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, rope_scaling=None, tokenizer_revision=None, trust_remote_code=True, dtype=torch.float16, max_seq_len=8192, download_dir=None, load_format=LoadFormat.AUTO, tensor_parallel_size=1, disable_custom_all_reduce=False, quantization=None, enforce_eager=False, kv_cache_dtype=auto, quantization_param_path=None, device_config=cuda, decoding_config=DecodingConfig(guided_decoding_backend='outlines'), seed=0, served_model_name=chatglm3-6b/) WARNING 08-29 09:39:49 tokenizer.py:126] Using a slow tokenizer. This might cause a significant slowdown. Consider using a fast tokenizer instead. INFO 08-29 09:39:49 selector.py:120] Cannot use FlashAttenti...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: [Bug]: name 'vllm_ops' is not defined using offline build from source vllm 0.4.3 bug;stale ### Your current environment ### 🐛 Describe the bug I built vllm=0.4.3+cu124 on Nvidia NGC docker container pytorch:24.04-py3 wi...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: None, device_config=cuda, decoding_config=DecodingConfig(guided_decoding_backend='outlines'), seed=0, served_model_name=chatglm3-6b/) WARNING 08-29 09:39:49 tokenizer.py:126] Using a slow tokenizer. This might cause a s...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: one, rope_scaling=None, tokenizer_revision=None, trust_remote_code=True, dtype=torch.float16, max_seq_len=8192, download_dir=None, load_format=LoadFormat.AUTO, tensor_parallel_size=1, disable_custom_all_reduce=False, qu...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: -29 09:39:48 llm_engine.py:161] Initializing an LLM engine (v0.4.3) with config: model='chatglm3-6b/', speculative_config=None, tokenizer='chatglm3-6b/', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, ro...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: =False, kv_cache_dtype=auto, quantization_param_path=None, device_config=cuda, decoding_config=DecodingConfig(guided_decoding_backend='outlines'), seed=0, served_model_name=chatglm3-6b/) WARNING 08-29 09:39:49 tokenizer...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
