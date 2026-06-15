# vllm-project/vllm#16259: [Bug]: vLLM still runs after Ray workers crash

| 字段 | 值 |
| --- | --- |
| Issue | [#16259](https://github.com/vllm-project/vllm/issues/16259) |
| 状态 | closed |
| 标签 | bug;ray;stale |
| 评论 | 14; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;fp8;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;crash;import_error;nan_inf;oom;slowdown |
| 根因提示 | dtype;env_dependency;memory_layout;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vLLM still runs after Ray workers crash

### Issue 正文摘录

### Your current environment I came up with some issue regarding 0.8.x in serving some models for instance Llama 3.3 70B , Llama 3.1 405B models, Mixtral-8x7B ### 🐛 Describe the bug In the instances of 0.8.1, 0.8.2 the issue we're mainly in the CUDA out of memory that I can add the details also in this ticket, the main problem is also in 0.8.3 where is more stable on the CUDA. I started a model The model load properly with no issue, getting to the end to start the FastAPI At the first request the Ray workers go down while the FastAPI is still on, handling the requests from users, keeping them in waiting until the request is done, which leaves them hanging. Full detail output ```bash INFO 04-08 03:47:19 [__init__.py:239] Automatically detected platform cuda. INFO 04-08 03:47:24 [api_server.py:1034] vLLM API server version 0.8.3 INFO 04-08 03:47:24 [api_server.py:1035] args: Namespace(host='0.0.0.0', port=8000, uvicorn_log_level='info', disable_uvicorn_access_log=False, allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, lora_modules=None, prompt_adapters=None, chat_template='/vllm-workspace/examples/tool_chat_template_llama3.1...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: platform cuda. INFO 04-08 03:47:24 [api_server.py:1034] vLLM API server version 0.8.3 INFO 04-08 03:47:24 [api_server.py:1035] args: Namespace(host='0.0.0.0', port=8000, uvicorn_log_level='info', disable_uvicorn_access_...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 7: [Bug]: vLLM still runs after Ray workers crash bug;ray;stale ### Your current environment I came up with some issue regarding 0.8.x in serving some models for instance Llama 3.3 70B , Llama 3.1 405B models, Mixtral-8x7B...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 6: e, tool_call_parser='llama3_json', tool_parser_plugin='', model='hugging-quants/Meta-Llama-3.1-405B-Instruct-AWQ-INT4', task='auto', tokenizer=None, hf_config_path=None, skip_tokenizer_init=False, revision=None, code_re...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 5: dtype='auto', kv_cache_dtype='auto', max_model_len=None, guided_decoding_backend='xgrammar', logits_processor_pattern=None, model_impl='auto', distributed_executor_backend='ray', pipeline_parallel_size=1, tensor_paralle...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: environment I came up with some issue regarding 0.8.x in serving some models for instance Llama 3.3 70B , Llama 3.1 405B models, Mixtral-8x7B ### 🐛 Describe the bug In the instances of 0.8.1, 0.8.2 the issue we're mainl...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
