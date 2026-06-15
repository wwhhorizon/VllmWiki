# vllm-project/vllm#13946: [Bug]: When deploying LLM with Docker, the following error occurs: RuntimeError: Failed to infer device type

| 字段 | 值 |
| --- | --- |
| Issue | [#13946](https://github.com/vllm-project/vllm/issues/13946) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: When deploying LLM with Docker, the following error occurs: RuntimeError: Failed to infer device type

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When I try to run ```bash docker run --name qwen2.5-32b-instruct --runtime nvidia --gpus '"device=0,1,2,3"' -v /home/ics/workspace/llm-models/qwen/Qwen2___5-32B-Instruct:/qwen/Qwen2___5-32B-Instruct -p 8000:8000 --ipc=host vllm/vllm-openai:v0.6.5 --model /qwen/Qwen2___5-32B-Instruct --tensor_parallel_size 4 --served-model-name qwen2.5-32b-instruct ``` When deploying LLM, the following error occurred ```bash INFO 02-26 21:04:24 api_server.py:651] vLLM API server version 0.6.5 INFO 02-26 21:04:24 api_server.py:652] args: Namespace(host=None, port=8000, uvicorn_log_level='info', allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, lora_modules=None, prompt_adapters=None, chat_template=None, chat_template_content_format='auto', response_role='assistant', ssl_keyfile=None, ssl_certfile=None, ssl_ca_certs=None, ssl_cert_reqs=0, root_path=None, middleware=[], return_tokens_as_token_ids=False, disable_frontend_multiprocessing=False, enable_auto_tool_choice=False, tool_call_parser=None, tool_parser_plugin='', model='/qwen/Qwen2___5-32B-Instruct', task='auto', tokenizer=None, skip_toke...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: he following error occurs: RuntimeError: Failed to infer device type bug;stale ### Your current environment ### 🐛 Describe the bug When I try to run ```bash docker run --name qwen2.5-32b-instruct --runtime nvidia --gpus...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: [Bug]: When deploying LLM with Docker, the following error occurs: RuntimeError: Failed to infer device type bug;stale ### Your current environment ### 🐛 Describe the bug When I try to run ```bash docker run --name qwen...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: ### 🐛 Describe the bug When I try to run ```bash docker run --name qwen2.5-32b-instruct --runtime nvidia --gpus '"device=0,1,2,3"' -v /home/ics/workspace/llm-models/qwen/Qwen2___5-32B-Instruct:/qwen/Qwen2___5-32B-Instru...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: pace(host=None, port=8000, uvicorn_log_level='info', allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, lora_modules=None, prompt_adapters=None, chat_template=Non...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: auto', quantization_param_path=None, max_model_len=None, guided_decoding_backend='xgrammar', logits_processor_pattern=None, distributed_executor_backend=None, worker_use_ray=False, pipeline_parallel_size=1, tensor_paral...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
