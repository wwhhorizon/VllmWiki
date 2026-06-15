# vllm-project/vllm#12554: [Bug]: Engine fails to start when running Qwen2.5 Deepseek r1

| 字段 | 值 |
| --- | --- |
| Issue | [#12554](https://github.com/vllm-project/vllm/issues/12554) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | activation_norm;attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Engine fails to start when running Qwen2.5 Deepseek r1

### Issue 正文摘录

### Your current environment ### Model Input Dumps N/a ### 🐛 Describe the bug I have been running vllm for some time using docker, and I recently pulled the latest version to try a new model. The engine fails to start after loading the model with much room to spare memory wise. Here is the entrypoint in my docker-compose ``` entrypoint: ["python3", "-m", "vllm.entrypoints.openai.api_server", "--model", "/models/DeepSeek-R1-Distill-Qwen-32B", "--dtype", "float16", "-tp", "2", "--chat-template", "/chat_templates/qwen2.5-instruct.jinja", "--max-model-len", "1000", "--gpu-memory-utilization", "0.9", "--swap-space", "36", "--guided-decoding-backend", "lm-format-enforcer"] ``` Here is the full log from the container ```bash INFO 01-29 07:13:04 __init__.py:183] Automatically detected platform cuda. INFO 01-29 07:13:05 api_server.py:835] vLLM API server version 0.7.0 INFO 01-29 07:13:05 api_server.py:836] args: Namespace(host=None, port=8000, uvicorn_log_level='info', allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, lora_modules=None, prompt_adapters=None, chat_template='/chat_templates/qwen2.5-instruct.jinja', chat_template_conte...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 7: okens_as_token_ids=False, disable_frontend_multiprocessing=False, enable_request_id_headers=False, enable_auto_tool_choice=False, tool_call_parser=None, tool_parser_plugin='', model='/models/DeepSeek-R1-Distill-Qwen-32B...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: /a ### 🐛 Describe the bug I have been running vllm for some time using docker, and I recently pulled the latest version to try a new model. The engine fails to start after loading the model with much room to spare memor...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: penai.api_server", "--model", "/models/DeepSeek-R1-Distill-Qwen-32B", "--dtype", "float16", "-tp", "2", "--chat-template", "/chat_templates/qwen2.5-instruct.jinja", "--max-model-len", "1000", "--gpu-memory-utilization",...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: Engine fails to start when running Qwen2.5 Deepseek r1 bug ### Your current environment ### Model Input Dumps N/a ### 🐛 Describe the bug I have been running vllm for some time using docker, and I recently pulled...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: gpu-memory-utilization", "0.9", "--swap-space", "36", "--guided-decoding-backend", "lm-format-enforcer"] ``` Here is the full log from the container ```bash INFO 01-29 07:13:04 __init__.py:183] Automatically detected pl...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
