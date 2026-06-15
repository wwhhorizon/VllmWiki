# vllm-project/vllm#15300: [Bug]: OPEA/Mistral-Small-3.1-24B-Instruct-2503-int4-AutoRound-awq-sym error

| 字段 | 值 |
| --- | --- |
| Issue | [#15300](https://github.com/vllm-project/vllm/issues/15300) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;gemm;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: OPEA/Mistral-Small-3.1-24B-Instruct-2503-int4-AutoRound-awq-sym error

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug CUDA_VISIBLE_DEVICES=0,1,4,7 vllm serve OPEA/Mistral-Small-3.1-24B-Instruct-2503-int4-AutoRound-awq-sym --tensor-parallel-size 4 --config-format mistral --load-format mistral --limit-mm-per-prompt 'image=4' --max-model-len 8192 --port 11435 --quantization awq --tokenizer-mode mistral ERROR: ` warnings.warn( INFO 03-22 02:03:39 [__init__.py:256] Automatically detected platform cuda. INFO 03-22 02:03:40 [api_server.py:977] vLLM API server version 0.8.1 INFO 03-22 02:03:40 [api_server.py:978] args: Namespace(subparser='serve', model_tag='OPEA/Mistral-Small-3.1-24B-Instruct-2503-int4-AutoRound-awq-sym', config='', host=None, port=11435, uvicorn_log_level='info', allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, lora_modules=None, prompt_adapters=None, chat_template=None, chat_template_content_format='auto', response_role='assistant', ssl_keyfile=None, ssl_certfile=None, ssl_ca_certs=None, enable_ssl_refresh=False, ssl_cert_reqs=0, root_path=None, middleware=[], return_tokens_as_token_ids=False, disable_frontend_multiprocessing=False, enable_request_id_headers=False, enable_aut...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: 3.1-24B-Instruct-2503-int4-AutoRound-awq-sym --tensor-parallel-size 4 --config-format mistral --load-format mistral --limit-mm-per-prompt 'image=4' --max-model-len 8192 --port 11435 --quantization awq --tokenizer-mode m...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: PEA/Mistral-Small-3.1-24B-Instruct-2503-int4-AutoRound-awq-sym error bug;stale ### Your current environment ### 🐛 Describe the bug CUDA_VISIBLE_DEVICES=0,1,4,7 vllm serve OPEA/Mistral-Small-3.1-24B-Instruct-2503-int4-Au...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: d platform cuda. INFO 03-22 02:03:40 [api_server.py:977] vLLM API server version 0.8.1 INFO 03-22 02:03:40 [api_server.py:978] args: Namespace(subparser='serve', model_tag='OPEA/Mistral-Small-3.1-24B-Instruct-2503-int4-...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: [Bug]: OPEA/Mistral-Small-3.1-24B-Instruct-2503-int4-AutoRound-awq-sym error bug;stale ### Your current environment ### 🐛 Describe the bug CUDA_VISIBLE_DEVICES=0,1,4,7 vllm serve OPEA/Mistral-Small-3.1-24B-Instruct-2503...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: dtype='auto', kv_cache_dtype='auto', max_model_len=8192, guided_decoding_backend='xgrammar', logits_processor_pattern=None, model_impl='auto', distributed_executor_backend=None, pipeline_parallel_size=1, tensor_parallel...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
