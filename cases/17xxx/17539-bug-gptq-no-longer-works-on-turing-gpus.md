# vllm-project/vllm#17539: [Bug]: GPTQ no longer works on Turing GPUs

| 字段 | 值 |
| --- | --- |
| Issue | [#17539](https://github.com/vllm-project/vllm/issues/17539) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory |
| 子分类 | precision |
| Operator 关键词 | cuda;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: GPTQ no longer works on Turing GPUs

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug It seems with the release of vllm 0.8.5 and and the introduction of bitblas in GPTQ quantization, GPTQ no longer works in Turing GPUs. I get the following error (when trying to use an existing model that works fine with `gptq_marlin` in 0.8.4) ``` INFO 05-01 16:02:32 [__init__.py:239] Automatically detected platform cuda. INFO 05-01 16:02:39 [api_server.py:1043] vLLM API server version 0.8.5 INFO 05-01 16:02:39 [api_server.py:1044[] args: Namespace(subparser='serve', model_tag='/data/model/base-model', config='', host=None, port=8000, uvicorn_log_level='info', disable_uvicorn_access_log=False, allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, lora_modules=[LoRAModulePath(name='mistral-7b-instruct-v0.2-ta-call-driver-lora', path='/data/model/gptq_call_driver_64r', base_model_name=None)], prompt_adapters=None, chat_template=None, chat_template_content_format='auto', response_role='assistant', ssl_keyfile=None, ssl_certfile=None, ssl_ca_certs=None, enable_ssl_refresh=False, ssl_cert_reqs=0, root_path=None, middleware=[], return_tokens_as_token_ids=False, disable_frontend_mult...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: platform cuda. INFO 05-01 16:02:39 [api_server.py:1043] vLLM API server version 0.8.5 INFO 05-01 16:02:39 [api_server.py:1044[] args: Namespace(subparser='serve', model_tag='/data/model/base-model', config='', host=None...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: True, config_format= , dtype='auto', max_model_len=8000, guided_decoding_backend='auto', reasoning_parser=None, logits_processor_pattern=None, model_impl='auto', distributed_executor_backend=None, pipeline_parallel_size...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: `` INFO 05-01 16:02:32 [__init__.py:239] Automatically detected platform cuda. INFO 05-01 16:02:39 [api_server.py:1043] vLLM API server version 0.8.5 INFO 05-01 16:02:39 [api_server.py:1044[] args: Namespace(subparser='...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: n Turing GPUs. I get the following error (when trying to use an existing model that works fine with `gptq_marlin` in 0.8.4) ``` INFO 05-01 16:02:32 [__init__.py:239] Automatically detected platform cuda. INFO 05-01 16:0...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: okens_as_token_ids=False, disable_frontend_multiprocessing=False, enable_request_id_headers=False, enable_auto_tool_choice=False, tool_call_parser=None, tool_parser_plugin='', model='/data/model/base-model', task='auto'...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
