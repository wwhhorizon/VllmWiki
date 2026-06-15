# vllm-project/vllm#3033: Qwen 14B AWQ deploy: AttributeError: 'ndarray' object has no attribute '_torch_dtype'

| 字段 | 值 |
| --- | --- |
| Issue | [#3033](https://github.com/vllm-project/vllm/issues/3033) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;model_support;quantization |
| 子分类 | latency_reg |
| Operator 关键词 | cuda;kernel;quantization |
| 症状 | crash;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> Qwen 14B AWQ deploy: AttributeError: 'ndarray' object has no attribute '_torch_dtype'

### Issue 正文摘录

$ python -m vllm.entrypoints.openai.api_server --host 0.0.0.0 --port 8001 --model Qwen1.5-14B-Chat-AWQ --tensor-parallel-size 2 --quantization awq --trust-remote-code --dtype half INFO 02-26 10:32:53 api_server.py:229] args: Namespace(host='0.0.0.0', port=8061, allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, served_model_name=None, lora_modules=None, chat_template=None, response_role='assistant', ssl_keyfile=None, ssl_certfile=None, root_path=None, middleware=[], model='Qwen1.5-14B-Chat-AWQ', tokenizer=None, revision=None, code_revision=None, tokenizer_revision=None, tokenizer_mode='auto', trust_remote_code=True, download_dir=None, load_format='auto', dtype='half', kv_cache_dtype='auto', max_model_len=None, worker_use_ray=False, pipeline_parallel_size=1, tensor_parallel_size=2, max_parallel_loading_workers=None, block_size=16, seed=0, swap_space=4, gpu_memory_utilization=0.9, max_num_batched_tokens=None, max_num_seqs=256, max_paddings=256, disable_log_stats=False, quantization='awq', enforce_eager=False, max_context_len_to_capture=8192, disable_custom_all_reduce=False, enable_lora=False, max_loras=1, max_lora_rank=16, lor...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: Qwen 14B AWQ deploy: AttributeError: 'ndarray' object has no attribute '_torch_dtype' stale $ python -m vllm.entrypoints.openai.api_server --host 0.0.0.0 --port 8001 --model Qwen1.5-14B-Chat-AWQ --tensor-parallel-size 2
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: enforce_eager=False, kv_cache_dtype=auto, device_config=cuda, seed=0) Special tokens have been added in the vocabulary, make sure the associated word embeddings are fine-tuned or trained. Traceback (most recent call las...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: 4B AWQ deploy: AttributeError: 'ndarray' object has no attribute '_torch_dtype' stale $ python -m vllm.entrypoints.openai.api_server --host 0.0.0.0 --port 8001 --model Qwen1.5-14B-Chat-AWQ --tensor-parallel-size 2 --qua...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: r.py:229] args: Namespace(host='0.0.0.0', port=8061, allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, served_model_name=None, lora_modules=None, chat_template=N...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: deploy: AttributeError: 'ndarray' object has no attribute '_torch_dtype' stale $ python -m vllm.entrypoints.openai.api_server --host 0.0.0.0 --port 8001 --model Qwen1.5-14B-Chat-AWQ --tensor-parallel-size 2 --quantizati...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
