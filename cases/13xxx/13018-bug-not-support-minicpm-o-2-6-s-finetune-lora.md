# vllm-project/vllm#13018: [Bug]: Not support MiniCPM-o 2.6 ‘s finetune lora

| 字段 | 值 |
| --- | --- |
| Issue | [#13018](https://github.com/vllm-project/vllm/issues/13018) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | activation_norm;attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Not support MiniCPM-o 2.6 ‘s finetune lora

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I use LLama-factory to make a SFT finetune lora based on MiniCPM-o-2.6,and merge it into the base model,the merged one cannot run but the original one can run very well My command is: ``` vllm serve /root/test/MiniCPM-o-2_6-lora --trust-remote-code --gpu_memory_utilization 0.8 --max-model-len 8192 --dtype auto ``` Vllm 's log is ``` DEBUG 02-10 15:42:08 __init__.py:28] No plugins for group vllm.platform_plugins found. INFO 02-10 15:42:08 __init__.py:190] Automatically detected platform cuda. DEBUG 02-10 15:42:09 scripts.py:141] Setting VLLM_WORKER_MULTIPROC_METHOD to 'spawn' INFO 02-10 15:42:09 api_server.py:840] vLLM API server version 0.7.2 INFO 02-10 15:42:09 api_server.py:841] args: Namespace(subparser='serve', model_tag='/root/test/MiniCPM-o-2_6-lora', config='', host=None, port=8000, uvicorn_log_level='info', allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, lora_modules=None, prompt_adapters=None, chat_template=None, chat_template_content_format='auto', response_role='assistant', ssl_keyfile=None, ssl_certfile=None, ssl_ca_certs=None, ssl_cert_reqs=0, root_path=None...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 7: [Bug]: Not support MiniCPM-o 2.6 ‘s finetune lora bug;stale ### Your current environment ### 🐛 Describe the bug I use LLama-factory to make a SFT finetune lora based on MiniCPM-o-2.6,and merge it into the base model,the...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 5: dtype='auto', kv_cache_dtype='auto', max_model_len=8192, guided_decoding_backend='xgrammar', logits_processor_pattern=None, model_impl='auto', distributed_executor_backend=None, pipeline_parallel_size=1, tensor_parallel...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: METHOD to 'spawn' INFO 02-10 15:42:09 api_server.py:840] vLLM API server version 0.7.2 INFO 02-10 15:42:09 api_server.py:841] args: Namespace(subparser='serve', model_tag='/root/test/MiniCPM-o-2_6-lora', config='', host...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: --trust-remote-code --gpu_memory_utilization 0.8 --max-model-len 8192 --dtype auto ``` Vllm 's log is ``` DEBUG 02-10 15:42:08 __init__.py:28] No plugins for group vllm.platform_plugins found. INFO 02-10 15:42:08 __init...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: bug;stale ### Your current environment ### 🐛 Describe the bug I use LLama-factory to make a SFT finetune lora based on MiniCPM-o-2.6,and merge it into the base model,the merged one cannot run but the original one can ru...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
