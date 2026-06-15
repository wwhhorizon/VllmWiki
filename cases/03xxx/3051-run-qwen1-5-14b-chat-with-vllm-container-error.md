# vllm-project/vllm#3051: run qwen1.5-14b-chat with vllm container error.

| 字段 | 值 |
| --- | --- |
| Issue | [#3051](https://github.com/vllm-project/vllm/issues/3051) |
| 状态 | closed |
| 标签 |  |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;frontend_api;model_support;quantization |
| 子分类 | install |
| Operator 关键词 | cache;cuda;quantization |
| 症状 | crash |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> run qwen1.5-14b-chat with vllm container error.

### Issue 正文摘录

INFO 02-27 08:13:58 api_server.py:229] args: Namespace(host=None, port=8000, allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, served_model_name=None, lora_modules=None, chat_template=None, response_role='assistant', ssl_keyfile=None, ssl_certfile=None, root_path=None, middleware=[], model='/root/.cache/huggingface/Qwen1.5-14B-Chat', tokenizer=None, revision=None, code_revision=None, tokenizer_revision=None, tokenizer_mode='auto', trust_remote_code=True, download_dir=None, load_format='auto', dtype='auto', kv_cache_dtype='auto', max_model_len=None, worker_use_ray=False, pipeline_parallel_size=1, tensor_parallel_size=1, max_parallel_loading_workers=None, block_size=16, seed=0, swap_space=4, gpu_memory_utilization=0.9, max_num_batched_tokens=None, max_num_seqs=256, max_paddings=256, disable_log_stats=False, quantization=None, enforce_eager=False, max_context_len_to_capture=8192, disable_custom_all_reduce=False, enable_lora=False, max_loras=1, max_lora_rank=16, lora_extra_vocab_size=256, lora_dtype='auto', max_cpu_loras=None, device='cuda', engine_use_ray=False, disable_log_requests=False, max_log_len=None) INFO 02-27 08:13:58...

## 现有链接修复摘要

#40082 Integrate flashinfer b12x MoE and FP4 GEMM kernels for SM120/121

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: e='auto', trust_remote_code=True, download_dir=None, load_format='auto', dtype='auto', kv_cache_dtype='auto', max_model_len=None, worker_use_ray=False, pipeline_parallel_size=1, tensor_parallel_size=1, max_parallel_load...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: run qwen1.5-14b-chat with vllm container error. INFO 02-27 08:13:58 api_server.py:229] args: Namespace(host=None, port=8000, allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'],...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: enforce_eager=False, kv_cache_dtype=auto, device_config=cuda, seed=0) Special tokens have been added in the vocabulary, make sure the associated word embeddings are fine-tuned or trained. INFO 02-27 08:14:19 llm_engine....
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ora_extra_vocab_size=256, lora_dtype='auto', max_cpu_loras=None, device='cuda', engine_use_ray=False, disable_log_requests=False, max_log_len=None) INFO 02-27 08:13:58 llm_engine.py:79] Initializing an LLM engine with c...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: server.py:229] args: Namespace(host=None, port=8000, allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, served_model_name=None, lora_modules=None, chat_template=N...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#40082](https://github.com/vllm-project/vllm/pull/40082) | mentioned | 0.6 | Integrate flashinfer b12x MoE and FP4 GEMM kernels for SM120/121 | 1 GPU (DGX Spark GB10 / RTX Pro 6000 Blackwell) - FlashInfer with PRs flashinfer-ai/flashinfer#3051, flashinfer-ai/flashinfer#3066, and flashinfer-ai/flashinfer#3080 - `nvidia-cut… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
