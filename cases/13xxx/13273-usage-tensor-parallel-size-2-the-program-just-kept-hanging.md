# vllm-project/vllm#13273: [Usage]: tensor-parallel-size=2，The program just kept hanging

| 字段 | 值 |
| --- | --- |
| Issue | [#13273](https://github.com/vllm-project/vllm/issues/13273) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 25; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: tensor-parallel-size=2，The program just kept hanging

### Issue 正文摘录

### parameters **node=1 gpu=2 tensor-parallel-size=2** **The program just kept hanging** ### How would you like to use vllm `CUDA_VISIBLE_DEVICES=0,1 python3 -m vllm.entrypoints.openai.api_server --tensor-parallel-size 2 --model Qwen/Qwen2-VL-7B` ### log info as follow ![Image](https://github.com/user-attachments/assets/9e0cd09c-07f2-41ad-8f29-5adc4534404f) `INFO 02-14 08:59:06 __init__.py:186] Automatically detected platform cuda. INFO 02-14 08:59:08 api_server.py:841] vLLM API server version 0.1.dev4487+gbbd2f98.d20250213 INFO 02-14 08:59:08 api_server.py:842] args: Namespace(host=None, port=8000, uvicorn_log_level='info', allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, lora_modules=None, prompt_adapters=None, chat_template='/app/qwen25-vl-chat_template.jinja', chat_template_content_format='auto', response_role='assistant', ssl_keyfile=None, ssl_certfile=None, ssl_ca_certs=None, ssl_cert_reqs=0, root_path=None, middleware=[], return_tokens_as_token_ids=False, disable_frontend_multiprocessing=False, enable_request_id_headers=False, enable_auto_tool_choice=False, enable_reasoning=False, reasoning_parser=None, tool_call_pa...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 7: [Usage]: tensor-parallel-size=2，The program just kept hanging usage;stale ### parameters **node=1 gpu=2 tensor-parallel-size=2** **The program just kept hanging** ### How would you like to use vllm `CUDA_VISIBLE_DEVICES...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: media_path=None, download_dir=None, load_format='auto', config_format= , dtype='auto', kv_cache_dtype='auto', max_model_len=16384, guided_decoding_backend='xgrammar', logits_processor_pattern=None, model_impl='auto', di...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: python3 -m vllm.entrypoints.openai.api_server --tensor-parallel-size 2 --model Qwen/Qwen2-VL-7B` ### log info as follow ![Image](https://github.com/user-attachments/assets/9e0cd09c-07f2-41ad-8f29-5adc4534404f) `INFO 02-...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: type='auto', kv_cache_dtype='auto', max_model_len=16384, guided_decoding_backend='xgrammar', logits_processor_pattern=None, model_impl='auto', distributed_executor_backend=None, pipeline_parallel_size=1, tensor_parallel...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: ed platform cuda. INFO 02-14 08:59:08 api_server.py:841] vLLM API server version 0.1.dev4487+gbbd2f98.d20250213 INFO 02-14 08:59:08 api_server.py:842] args: Namespace(host=None, port=8000, uvicorn_log_level='info', allo...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
