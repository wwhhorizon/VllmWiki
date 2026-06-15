# vllm-project/vllm#12902: [Bug]: Failure to run Qwen2.5-VL-72B-Instruct-bnb-4bit

| 字段 | 值 |
| --- | --- |
| Issue | [#12902](https://github.com/vllm-project/vllm/issues/12902) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;quantization |
| 子分类 | latency_reg |
| Operator 关键词 | attention;cuda;operator;quantization |
| 症状 | crash;slowdown |
| 根因提示 | dtype;env_dependency;memory_layout;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Failure to run Qwen2.5-VL-72B-Instruct-bnb-4bit

### Issue 正文摘录

### Your current environment I am trying to run `unsloth/Qwen2.5-VL-72B-Instruct-bnb-4bit` with 2 A100-80GB on modal. ``` subprocess.Popen([ "vllm", "serve", f"{MODELS_DIR}/{MODEL_NAME}", "--host", "127.0.0.1", "--port", "8000", "--max-model-len", "32767", "--tensor-parallel-size", "1", "--gpu-memory-utilization", "0.90", "--trust-remote-code", "--quantization", "bitsandbytes", "--load-format", "bitsandbytes", ]) ``` ### 🐛 Describe the bug Feb 07 21:57:25.839 | INFO 02-07 13:57:25 api_server.py:841] args: Namespace(subparser='serve', model_tag='/pointer/unsloth/Qwen2.5-VL-72B-Instruct-bnb-4bit', config='', host='127.0.0.1', port=8000, uvicorn_log_level='info', allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key='[API_KEY]', lora_modules=None, prompt_adapters=None, chat_template=None, chat_template_content_format='auto', response_role='assistant', ssl_keyfile=None, ssl_certfile=None, ssl_ca_certs=None, ssl_cert_reqs=0, root_path=None, middleware=[], return_tokens_as_token_ids=False, disable_frontend_multiprocessing=False, enable_request_id_headers=False, enable_auto_tool_choice=False, enable_reasoning=False, reasoning_parser=None, t...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: kwargs=None, pooler_config=None, compilation_config={"splitting_ops":[],"compile_sizes":[],"cudagraph_capture_sizes":[256,248,240,232,224,216,208,200,192,184,176,168,160,152,144,136,128,120,112,104,96,88,80,72,64,56,48,...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: u-memory-utilization", "0.90", "--trust-remote-code", "--quantization", "bitsandbytes", "--load-format", "bitsandbytes", ]) ``` ### 🐛 Describe the bug Feb 07 21:57:25.839 | INFO 02-07 13:57:25 api_server.py:841] args: N...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: Failure to run Qwen2.5-VL-72B-Instruct-bnb-4bit bug ### Your current environment I am trying to run `unsloth/Qwen2.5-VL-72B-Instruct-bnb-4bit` with 2 A100-80GB on modal. ``` subprocess.Popen([ "vllm", "serve", f"{
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: okens_as_token_ids=False, disable_frontend_multiprocessing=False, enable_request_id_headers=False, enable_auto_tool_choice=False, enable_reasoning=False, reasoning_parser=None, tool_call_parser=None, tool_parser_plugin=...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 4: nstruct-bnb-4bit bug ### Your current environment I am trying to run `unsloth/Qwen2.5-VL-72B-Instruct-bnb-4bit` with 2 A100-80GB on modal. ``` subprocess.Popen([ "vllm", "serve", f"{MODELS_DIR}/{MODEL_NAME}", "--host",...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
