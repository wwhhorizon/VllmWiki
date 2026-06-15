# vllm-project/vllm#16713: [Bug]: Loading bnb-community/Llama-4-Scout-17B-16E-Instruct-bnb-4bit error `FusedMoE` quant_method is None

| 字段 | 值 |
| --- | --- |
| Issue | [#16713](https://github.com/vllm-project/vllm/issues/16713) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;moe;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Loading bnb-community/Llama-4-Scout-17B-16E-Instruct-bnb-4bit error `FusedMoE` quant_method is None

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I'm trying to load this model: [bnb-community/Llama-4-Scout-17B-16E-Instruct-bnb-4bit](https://huggingface.co/bnb-community/Llama-4-Scout-17B-16E-Instruct-bnb-4bit) The model is quantized model of llama 4 scout in 4 bit quantized using bitsandbytes. Here is how I run the model: ```bash vllm serve models/llama4-17Bx16E-Instruct-bnb-4bit --host 0.0.0.0 --port 8000 --max-model-len 8192 --load-format bitsandbytes --quantization bitsandbytes --override-generation-config='{"attn_temperature_tuning": true}' ``` But, I got this error: ``` INFO 04-16 16:34:25 [__init__.py:239] Automatically detected platform cuda. INFO 04-16 16:34:27 [api_server.py:1034] vLLM API server version 0.8.4 INFO 04-16 16:34:27 [api_server.py:1035] args: Namespace(subparser='serve', model_tag='models/llama4-17Bx16E-Instruct-bnb-4bit', config='', host='0.0.0.0', port=8000, uvicorn_log_level='info', disable_uvicorn_access_log=False, allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, lora_modules=None, prompt_adapters=None, chat_template=None, chat_template_content_format='auto', response_role='assistant', ssl...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: [Bug]: Loading bnb-community/Llama-4-Scout-17B-16E-Instruct-bnb-4bit error `FusedMoE` quant_method is None bug ### Your current environment ### 🐛 Describe the bug I'm trying to load this model: [bnb-community/Llama-4-Sc...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: platform cuda. INFO 04-16 16:34:27 [api_server.py:1034] vLLM API server version 0.8.4 INFO 04-16 16:34:27 [api_server.py:1035] args: Namespace(subparser='serve', model_tag='models/llama4-17Bx16E-Instruct-bnb-4bit', conf...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: g bnb-community/Llama-4-Scout-17B-16E-Instruct-bnb-4bit error `FusedMoE` quant_method is None bug ### Your current environment ### 🐛 Describe the bug I'm trying to load this model: [bnb-community/Llama-4-Scout-17B-16E-I...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: dtype='auto', kv_cache_dtype='auto', max_model_len=8192, guided_decoding_backend='auto', logits_processor_pattern=None, model_impl='auto', distributed_executor_backend=None, pipeline_parallel_size=1, tensor_parallel_siz...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: okens_as_token_ids=False, disable_frontend_multiprocessing=False, enable_request_id_headers=False, enable_auto_tool_choice=False, tool_call_parser=None, tool_parser_plugin='', model='models/llama4-17Bx16E-Instruct-bnb-4...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
