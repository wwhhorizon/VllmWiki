# vllm-project/vllm#3115: ConnectionResetError: [Errno 104] Connection reset by peer

| 字段 | 值 |
| --- | --- |
| Issue | [#3115](https://github.com/vllm-project/vllm/issues/3115) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | distributed_parallel;frontend_api;model_support;quantization |
| 子分类 | latency_reg |
| Operator 关键词 | cuda;kernel;quantization |
| 症状 | crash;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> ConnectionResetError: [Errno 104] Connection reset by peer

### Issue 正文摘录

Occasionally encounter errors ``` + python3 -m vllm.entrypoints.openai.api_server --host xxxxx --port 8003 --served-model-name qwen1.5-72b-chat-int4 --model /home/vllm/model/Qwen1.5-72B-Chat-GPTQ-Int4 --trust-remote-code --tokenizer-mode auto --max-num-batched-tokens 32768 --tensor-parallel-size 4 INFO 02-29 14:28:09 api_server.py:228] args: Namespace(host='xxxxx', port=8003, allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, served_model_name='qwen1.5-72b-chat-int4', lora_modules=None, chat_template=None, response_role='assistant', ssl_keyfile=None, ssl_certfile=None, root_path=None, middleware=[], model='/home/vllm/model/Qwen1.5-72B-Chat-GPTQ-Int4', tokenizer=None, revision=None, code_revision=None, tokenizer_revision=None, tokenizer_mode='auto', trust_remote_code=True, download_dir=None, load_format='auto', dtype='auto', kv_cache_dtype='auto', max_model_len=None, worker_use_ray=False, pipeline_parallel_size=1, tensor_parallel_size=4, max_parallel_loading_workers=None, block_size=16, seed=0, swap_space=4, gpu_memory_utilization=0.9, max_num_batched_tokens=32768, max_num_seqs=256, max_paddings=256, disable_log_stats=False,...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: api_server --host xxxxx --port 8003 --served-model-name qwen1.5-72b-chat-int4 --model /home/vllm/model/Qwen1.5-72B-Chat-GPTQ-Int4 --trust-remote-code --tokenizer-mode auto --max-num-batched-tokens 32768 --tensor-paralle...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: -m vllm.entrypoints.openai.api_server --host xxxxx --port 8003 --served-model-name qwen1.5-72b-chat-int4 --model /home/vllm/model/Qwen1.5-72B-Chat-GPTQ-Int4 --trust-remote-code --tokenizer-mode auto --max-num-batched-to...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: enforce_eager=False, kv_cache_dtype=auto, device_config=cuda, seed=0) Special tokens have been added in the vocabulary, make sure the associated word embeddings are fine-tuned or trained. Traceback (most recent call las...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: ver.py:228] args: Namespace(host='xxxxx', port=8003, allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, served_model_name='qwen1.5-72b-chat-int4', lora_modules=No...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ConnectionResetError: [Errno 104] Connection reset by peer stale Occasionally encounter errors ``` + python3 -m vllm.entrypoints.openai.api_server --host xxxxx --port 8003 --served-model-name qwen1.5-72b-chat-int4 --mod...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
