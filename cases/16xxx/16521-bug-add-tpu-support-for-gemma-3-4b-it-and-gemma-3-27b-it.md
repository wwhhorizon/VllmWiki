# vllm-project/vllm#16521: [Bug]: Add TPU support for gemma-3-4b-it and gemma-3-27b-it

| 字段 | 值 |
| --- | --- |
| Issue | [#16521](https://github.com/vllm-project/vllm/issues/16521) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 17; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;gemm;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Add TPU support for gemma-3-4b-it and gemma-3-27b-it

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Attempting to load gemma-3-4b-it or gemma-3-27b-it leads to vLLM engine crashing with below error. Comparing the model configs against gemma-3-1b-it (which currently works), the architecture looks different at I don't see head_dim key value on the former models. Gemma3ForConditionalGeneration (4b/27b) vs Gemma3ForCausalLM (1b) ``` VLLM_USE_V1=1 vllm serve 'google/gemma-3-4b-it' --port 8080 --disable-log-requests --seed 42 --max-model-len 2048 --gpu-memory-utilization 0.95 INFO 04-12 01:01:02 [__init__.py:239] Automatically detected platform tpu. INFO 04-12 01:01:06 [api_server.py:1034] vLLM API server version 0.7.4.dev1067+g93195146e INFO 04-12 01:01:06 [api_server.py:1035] args: Namespace(subparser='serve', model_tag='google/gemma-3-4b-it', config='', host=None, port=8080, uvicorn_log_level='info', disable_uvicorn_access_log=False, allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, lora_modules=None, prompt_adapters=None, chat_template=None, chat_template_content_format='auto', response_role='assistant', ssl_keyfile=None, ssl_certfile=None, ssl_ca_certs=None, enable_ssl_re...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 7: [Bug]: Add TPU support for gemma-3-4b-it and gemma-3-27b-it bug;stale ### Your current environment ### 🐛 Describe the bug Attempting to load gemma-3-4b-it or gemma-3-27b-it leads to vLLM engine crashing with below error...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: d platform tpu. INFO 04-12 01:01:06 [api_server.py:1034] vLLM API server version 0.7.4.dev1067+g93195146e INFO 04-12 01:01:06 [api_server.py:1035] args: Namespace(subparser='serve', model_tag='google/gemma-3-4b-it', con...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: media_path=None, download_dir=None, load_format='auto', config_format= , dtype='auto', kv_cache_dtype='auto', max_model_len=2048, guided_decoding_backend='auto', logits_processor_pattern=None, model_impl='auto', distrib...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 5: =None, port=8080, uvicorn_log_level='info', disable_uvicorn_access_log=False, allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, lora_modules=None, prompt_adapter...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: [Bug]: Add TPU support for gemma-3-4b-it and gemma-3-27b-it bug;stale ### Your current environment ### 🐛 Describe the bug Attempting to load gemma-3-4b-it or gemma-3-27b-it leads to vLLM engine crashing with below error...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
