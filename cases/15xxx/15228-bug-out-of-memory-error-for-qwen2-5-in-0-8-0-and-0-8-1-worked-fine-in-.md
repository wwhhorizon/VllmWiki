# vllm-project/vllm#15228: [Bug]: Out of Memory error for Qwen2.5 in 0.8.0 and 0.8.1. Worked fine in the previous versions

| 字段 | 值 |
| --- | --- |
| Issue | [#15228](https://github.com/vllm-project/vllm/issues/15228) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 26; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | activation_norm;attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;quantization;sampling_logits;scheduler_memory |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;kernel;quantization;sampling;triton |
| 症状 | build_error;crash;mismatch;oom |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Out of Memory error for Qwen2.5 in 0.8.0 and 0.8.1. Worked fine in the previous versions

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I start the inference server by the following command `python -m vllm.entrypoints.openai.api_server --dtype auto --api-key token-abc123 --tensor-parallel-size 2 --host 0.0.0.0 --port 8004 --model Qwen2.5-72B-Instruct-GPTQ-Int4 --gpu-memory-utilization 0.9 --max-model-len 16000` **Here's the log during the service start-up in the version 0.7.2** ``` INFO 03-20 16:00:54 __init__.py:190] Automatically detected platform cuda. INFO 03-20 16:00:54 api_server.py:840] vLLM API server version 0.7.2 INFO 03-20 16:00:54 api_server.py:841] args: Namespace(host='0.0.0.0', port=8004, uvicorn_log_level='info', allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key='token-abc123', lora_modules=None, prompt_adapters=None, chat_template=None, chat_template_content_format='auto', response_role='assistant', ssl_keyfile=None, ssl_certfile=None, ssl_ca_certs=None, ssl_cert_reqs=0, root_path=None, middleware=[], return_tokens_as_token_ids=False, disable_frontend_multiprocessing=False, enable_request_id_headers=False, enable_auto_tool_choice=False, enable_reasoning=False, reasoning_parser=None, tool_call_pa...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 8: for Qwen2.5 in 0.8.0 and 0.8.1. Worked fine in the previous versions bug;stale ### Your current environment ### 🐛 Describe the bug I start the inference server by the following command `python -m vllm.entrypoints.openai...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: Memory error for Qwen2.5 in 0.8.0 and 0.8.1. Worked fine in the previous versions bug;stale ### Your current environment ### 🐛 Describe the bug I start the inference server by the following command `python -m vllm.entry...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: by the following command `python -m vllm.entrypoints.openai.api_server --dtype auto --api-key token-abc123 --tensor-parallel-size 2 --host 0.0.0.0 --port 8004 --model Qwen2.5-72B-Instruct-GPTQ-Int4 --gpu-memory-utilizat...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: Out of Memory error for Qwen2.5 in 0.8.0 and 0.8.1. Worked fine in the previous versions bug;stale ### Your current environment ### 🐛 Describe the bug I start the inference server by the following command `python...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: type='auto', kv_cache_dtype='auto', max_model_len=16000, guided_decoding_backend='xgrammar', logits_processor_pattern=None, model_impl='auto', distributed_executor_backend=None, pipeline_parallel_size=1, tensor_parallel...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
