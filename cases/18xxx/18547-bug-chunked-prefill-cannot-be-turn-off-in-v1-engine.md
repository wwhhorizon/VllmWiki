# vllm-project/vllm#18547: [Bug]:  chunked_prefill cannot be turn off in V1 engine

| 字段 | 值 |
| --- | --- |
| Issue | [#18547](https://github.com/vllm-project/vllm/issues/18547) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]:  chunked_prefill cannot be turn off in V1 engine

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I try to turn off chunked_prefill in V1 engine. According to the results of the log print (chunked_prefill_enabled=True), it seems to have failed The script I used: ```bash export CUDA_VISIBLE_DEVICES=7 export VLLM_USE_V1=1 vllm serve /path/to/Qwen3-4B --enforce-eager \ --gpu-memory-utilization 0.97 --tensor-parallel-size 1 \ --port 34007 --served-model-name HengNao-r1 \ --swap-space 0 --block-size 16 --max-model-len 32000 \ --enable-prefix-caching --no-enable-chunked-prefill ``` The printed log: ```bash INFO 05-22 11:04:21 [__init__.py:239] Automatically detected platform cuda. INFO 05-22 11:04:25 [api_server.py:1043] vLLM API server version 0.8.5.post1 INFO 05-22 11:04:25 [api_server.py:1044] args: Namespace(subparser='serve', model_tag='/path/to/Qwen3-4B', config='', host=None, port=34007, uvicorn_log_level='info', disable_uvicorn_access_log=False, allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, lora_modules=None, prompt_adapters=None, chat_template=None, chat_template_content_format='auto', response_role='assistant', ssl_keyfile=None, ssl_certfile=None, ssl_ca_certs=...

## 现有链接修复摘要

#21645 [V1] Raise error if chunked prefill is explicitly disabled

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: platform cuda. INFO 05-22 11:04:25 [api_server.py:1043] vLLM API server version 0.8.5.post1 INFO 05-22 11:04:25 [api_server.py:1044] args: Namespace(subparser='serve', model_tag='/path/to/Qwen3-4B', config='', host=None...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 5: rue, config_format= , dtype='auto', max_model_len=32000, guided_decoding_backend='auto', reasoning_parser=None, logits_processor_pattern=None, model_impl='auto', distributed_executor_backend=None, pipeline_parallel_size...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: e, model_loader_extra_config={}, use_tqdm_on_load=True, config_format= , dtype='auto', max_model_len=32000, guided_decoding_backend='auto', reasoning_parser=None, logits_processor_pattern=None, model_impl='auto', distri...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: h export CUDA_VISIBLE_DEVICES=7 export VLLM_USE_V1=1 vllm serve /path/to/Qwen3-4B --enforce-eager \ --gpu-memory-utilization 0.97 --tensor-parallel-size 1 \ --port 34007 --served-model-name HengNao-r1 \ --swap-space 0 -...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: [Bug]: chunked_prefill cannot be turn off in V1 engine bug ### Your current environment ### 🐛 Describe the bug I try to turn off chunked_prefill in V1 engine. According to the results of the log print (chunked_prefill_e...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#21645](https://github.com/vllm-project/vllm/pull/21645) | mentioned | 0.6 | [V1] Raise error if chunked prefill is explicitly disabled | user it's not supported. Users have asked for this behaviour e.g. in [#18547](https://github.com/vllm-project/vllm/issues/18547#issuecomment-2920326178) ## Test Plan vllm serve: `… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
