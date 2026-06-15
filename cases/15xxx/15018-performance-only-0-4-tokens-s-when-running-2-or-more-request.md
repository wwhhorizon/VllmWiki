# vllm-project/vllm#15018: [Performance]: only 0.4 tokens/s when running 2 or more request

| 字段 | 值 |
| --- | --- |
| Issue | [#15018](https://github.com/vllm-project/vllm/issues/15018) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | activation_norm;attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf;oom;slowdown |
| 根因提示 | dtype;env_dependency;memory_layout;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Performance]: only 0.4 tokens/s when running 2 or more request

### Issue 正文摘录

### Proposal to improve performance _No response_ ### Report of performance regression _No response_ ### Misc discussion on performance I was tring to run DeepSeek-R1-Distill-Qwen-32B-Q4_K_M.gguf with 7900 XTX（24G) and it works,I have got 19.3 tokens/s when it run with one request.However，the throughput was only 0.4 tokens/s when it running two or more requsets.The GPU KV cache usage is enought,is there any parameters i have to set? INFO 03-18 08:46:00 [__init__.py:256] Automatically detected platform rocm. INFO 03-18 08:46:01 [api_server.py:912] vLLM API server version 0.7.4.dev442+gfd8e055f INFO 03-18 08:46:01 [api_server.py:913] args: Namespace(subparser='serve', model_tag='/app/model/DeepSeek-R1-Distill-Qwen-32B-GGUF/DeepSeek-R1-Distill-Qwen-32B-Q4_K_M.gguf', config='', host='0.0.0.0', port=8199, uvicorn_log_level='info', allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, lora_modules=None, prompt_adapters=None, chat_template=None, chat_template_content_format='auto', response_role='assistant', ssl_keyfile=None, ssl_certfile=None, ssl_ca_certs=None, enable_ssl_refresh=False, ssl_cert_reqs=0, root_path=None, middleware=[]...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: d platform rocm. INFO 03-18 08:46:01 [api_server.py:912] vLLM API server version 0.7.4.dev442+gfd8e055f INFO 03-18 08:46:01 [api_server.py:913] args: Namespace(subparser='serve', model_tag='/app/model/DeepSeek-R1-Distil...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 7: [Performance]: only 0.4 tokens/s when running 2 or more request performance;stale ### Proposal to improve performance _No response_ ### Report of performance regression _No response_ ### Misc discussion on performance I...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 6: media_path=None, download_dir=None, load_format='auto', config_format= , dtype='auto', kv_cache_dtype='auto', max_model_len=4096, guided_decoding_backend='xgrammar', logits_processor_pattern=None, model_impl='auto', dis...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 5: dtype='auto', kv_cache_dtype='auto', max_model_len=4096, guided_decoding_backend='xgrammar', logits_processor_pattern=None, model_impl='auto', distributed_executor_backend=None, pipeline_parallel_size=1, tensor_parallel...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: t? INFO 03-18 08:46:00 [__init__.py:256] Automatically detected platform rocm. INFO 03-18 08:46:01 [api_server.py:912] vLLM API server version 0.7.4.dev442+gfd8e055f INFO 03-18 08:46:01 [api_server.py:913] args: Namespa...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
