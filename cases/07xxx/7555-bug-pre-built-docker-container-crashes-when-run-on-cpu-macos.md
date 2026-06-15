# vllm-project/vllm#7555: [Bug]: Pre-built Docker container crashes when run on CPU/MacOS

| 字段 | 值 |
| --- | --- |
| Issue | [#7555](https://github.com/vllm-project/vllm/issues/7555) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;ci_build;frontend_api;hardware_porting;model_support;quantization |
| 子分类 | env_compat |
| Operator 关键词 | attention;cuda;quantization |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Pre-built Docker container crashes when run on CPU/MacOS

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug **Disclaimer:** Not sure if this is a bug or the `vllm/vllm-openai` image from Docker Hub is simply not built for non-CUDA environments. Running the Docker image on CPU on my M1 Mac fails due to what seems to be an attempt at loading Nvidia/CUDA libraries (which are obviously not present). ``` ❯ docker pull vllm/vllm-openai [...] ❯ docker run --ipc=host vllm/vllm-openai --model microsoft/phi-2 --device cpu WARNING: The requested image's platform (linux/amd64) does not match the detected host platform (linux/arm64/v8) and no specific platform was requested [...] INFO 08-15 12:17:58 llm_engine.py:174] Initializing an LLM engine (v0.5.4) with config: model='microsoft/phi-2', speculative_config=None, tokenizer='microsoft/phi-2', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, rope_scaling=None, rope_theta=None, tokenizer_revision=None, trust_remote_code=True, dtype=torch.float16, max_seq_len=2048, download_dir=None, load_format=LoadFormat.AUTO, tensor_parallel_size=1, pipeline_parallel_size=1, disable_custom_all_reduce=False, quantization=None, enforce_eager=False, kv_cache_dtype=auto, quantization_param_path=None, dev...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [Bug]: Pre-built Docker container crashes when run on CPU/MacOS bug ### Your current environment ### 🐛 Describe the bug **Disclaimer:** Not sure if this is a bug or the `vllm/vllm-openai` image from Docker Hub is simply...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: =None, rope_theta=None, tokenizer_revision=None, trust_remote_code=True, dtype=torch.float16, max_seq_len=2048, download_dir=None, load_format=LoadFormat.AUTO, tensor_parallel_size=1, pipeline_parallel_size=1, disable_c...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: pull vllm/vllm-openai [...] ❯ docker run --ipc=host vllm/vllm-openai --model microsoft/phi-2 --device cpu WARNING: The requested image's platform (linux/amd64) does not match the detected host platform (linux/arm64/v8)...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: =None, device_config=cpu, decoding_config=DecodingConfig(guided_decoding_backend='outlines'), observability_config=ObservabilityConfig(otlp_traces_endpoint=None), seed=0, served_model_name=microsoft/phi-2, use_v2_block_...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: the `vllm/vllm-openai` image from Docker Hub is simply not built for non-CUDA environments. Running the Docker image on CPU on my M1 Mac fails due to what seems to be an attempt at loading Nvidia/CUDA libraries (which a...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
