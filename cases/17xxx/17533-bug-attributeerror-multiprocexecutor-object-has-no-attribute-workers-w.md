# vllm-project/vllm#17533: [Bug]: AttributeError: 'MultiprocExecutor' object has no attribute 'workers' when VLLM_USE_V1=1 on rocm platform serve deepseek-r1 671B

| 字段 | 值 |
| --- | --- |
| Issue | [#17533](https://github.com/vllm-project/vllm/issues/17533) |
| 状态 | closed |
| 标签 | bug;rocm |
| 评论 | 13; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | activation_norm;attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;scheduler_memory;speculative_decoding |
| 子分类 | env_compat |
| Operator 关键词 | attention;cuda;fp8;operator;quantization;triton |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: AttributeError: 'MultiprocExecutor' object has no attribute 'workers' when VLLM_USE_V1=1 on rocm platform serve deepseek-r1 671B

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug With vllm 0.8.5(also the same issue with vllm 0.8.3, has not try 0.8.4, but most likely the same issue) , on a rocm platform(AMD Mi3** GPU), when v1 engine is enabled, when vllm serve deepseek-r1 671B，the vllm server could not start successfully due to ERROR 05-01 12:18:50 [multiproc_executor.py:435] AttributeError: 'GPUModelRunner' object has no attribute 'runner'. '''Python export VLLM_CONFIGURE_LOGGING=1 export VLLM_USE_V1=1 vllm serve /model/deepseek-r1 \ --enable-reasoning \ --reasoning-parser deepseek_r1 \ --tensor-parallel-size 8 \ --trust-remote-code ''' Below is the full error log: ``` INFO 05-01 12:17:52 [__init__.py:239] Automatically detected platform rocm. INFO 05-01 12:18:03 [api_server.py:1043] vLLM API server version 0.8.5.dev5+g41b85b6ed INFO 05-01 12:18:03 [api_server.py:1044] args: Namespace(subparser='serve', model_tag='/model/deepseek-r1', config='', host=None, port=8000, uvicorn_log_level='info', disable_uvicorn_access_log=False, allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, lora_modules=None, prompt_adapters=None, chat_template=None, chat_templat...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 6: e, model_loader_extra_config={}, use_tqdm_on_load=True, config_format= , dtype='auto', max_model_len=None, guided_decoding_backend='auto', reasoning_parser='deepseek_r1', logits_processor_pattern=None, model_impl='auto'...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: platform rocm. INFO 05-01 12:18:03 [api_server.py:1043] vLLM API server version 0.8.5.dev5+g41b85b6ed INFO 05-01 12:18:03 [api_server.py:1044] args: Namespace(subparser='serve', model_tag='/model/deepseek-r1', config=''...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: okens_as_token_ids=False, disable_frontend_multiprocessing=False, enable_request_id_headers=False, enable_auto_tool_choice=False, tool_call_parser=None, tool_parser_plugin='', model='/model/deepseek-r1', task='auto', to...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: ltiprocExecutor' object has no attribute 'workers' when VLLM_USE_V1=1 on rocm platform serve deepseek-r1 671B bug;rocm ### Your current environment ### 🐛 Describe the bug With vllm 0.8.5(also the same issue with vllm 0....
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 4: =None, port=8000, uvicorn_log_level='info', disable_uvicorn_access_log=False, allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, lora_modules=None, prompt_adapter...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
