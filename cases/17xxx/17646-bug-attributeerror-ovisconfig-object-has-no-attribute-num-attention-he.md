# vllm-project/vllm#17646: [Bug]: AttributeError: 'OvisConfig' object has no attribute 'num_attention_heads'

| 字段 | 值 |
| --- | --- |
| Issue | [#17646](https://github.com/vllm-project/vllm/issues/17646) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: AttributeError: 'OvisConfig' object has no attribute 'num_attention_heads'

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug vllm serve code ``` CUDA_VISIBLE_DEVICES=3,1,0,2 \ VLLM_USE_V1=1 \ VLLM_WORKER_MULTIPROC_METHOD=spawn \ TRANSFORMERS_OFFLINE=1 \ HF_DATASETS_OFFLINE=1 \ vllm serve /root/HuggingFaceCache/Ovis2-16B \ --trust-remote-code --served-model-name gpt-4o gpt-4 gpt-3.5-turbo o1 o1-mini o3-mini \ --gpu-memory-utilization 0.98 --tensor-parallel-size 4 \ --port 8000 --api-key sk-123456 ``` error ``` INFO 05-05 16:27:52 [__init__.py:239] Automatically detected platform cuda. INFO 05-05 16:27:57 [api_server.py:1043] vLLM API server version 0.8.5.post1 INFO 05-05 16:27:57 [api_server.py:1044] args: Namespace(subparser='serve', model_tag='/root/HuggingFaceCache/Ovis2-16B', config='', host=None, port=8000, uvicorn_log_level='info', disable_uvicorn_access_log=False, allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key='sk-123456', lora_modules=None, prompt_adapters=None, chat_template=None, chat_template_content_format='auto', response_role='assistant', ssl_keyfile=None, ssl_certfile=None, ssl_ca_certs=None, enable_ssl_refresh=False, ssl_cert_reqs=0, root_path=None, middleware=[], return_tokens_as_to...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: uteError: 'OvisConfig' object has no attribute 'num_attention_heads' bug;stale ### Your current environment ### 🐛 Describe the bug vllm serve code ``` CUDA_VISIBLE_DEVICES=3,1,0,2 \ VLLM_USE_V1=1 \ VLLM_WORKER_MULTIPROC...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: platform cuda. INFO 05-05 16:27:57 [api_server.py:1043] vLLM API server version 0.8.5.post1 INFO 05-05 16:27:57 [api_server.py:1044] args: Namespace(subparser='serve', model_tag='/root/HuggingFaceCache/Ovis2-16B', confi...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: e, model_loader_extra_config={}, use_tqdm_on_load=True, config_format= , dtype='auto', max_model_len=None, guided_decoding_backend='auto', reasoning_parser=None, logits_processor_pattern=None, model_impl='auto', distrib...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: AttributeError: 'OvisConfig' object has no attribute 'num_attention_heads' bug;stale ### Your current environment ### 🐛 Describe the bug vllm serve code ``` CUDA_VISIBLE_DEVICES=3,1,0,2 \ VLLM_USE_V1=1 \ VLLM_WOR...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: True, config_format= , dtype='auto', max_model_len=None, guided_decoding_backend='auto', reasoning_parser=None, logits_processor_pattern=None, model_impl='auto', distributed_executor_backend=None, pipeline_parallel_size...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
