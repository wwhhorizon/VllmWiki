# vllm-project/vllm#5804: [Usage]: AttributeError: '_OpNamespace' '_C' object has no attribute 'rms_norm'

| 字段 | 值 |
| --- | --- |
| Issue | [#5804](https://github.com/vllm-project/vllm/issues/5804) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | activation_norm;attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;quantization |
| 子分类 |  |
| Operator 关键词 | activation;attention;cuda;operator;quantization |
| 症状 | build_error;crash;import_error |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: AttributeError: '_OpNamespace' '_C' object has no attribute 'rms_norm'

### Issue 正文摘录

### Your current environment **When I send the cl:** ``` python -m vllm.entrypoints.openai.api_server --model Qwen/Qwen2-1.5B-Instruct --served-model-name Qwen2-7B-Instruct-lora --max-model-len=2048 --dtype=half ``` **Then Response:** WARNING 06-24 21:44:48 _custom_ops.py:14] Failed to import from vllm._C with ImportError('libcudart.so.12: cannot open shared object file: No such file or directory') INFO 06-24 21:44:54 api_server.py:177] vLLM API server version 0.5.0.post1 INFO 06-24 21:44:54 api_server.py:178] args: Namespace(host=None, port=8000, uvicorn_log_level='info', allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, lora_modules=None, chat_template=None, response_role='assistant', ssl_keyfile=None, ssl_certfile=None, ssl_ca_certs=None, ssl_cert_reqs=0, root_path=None, middleware=[], model='Qwen/Qwen2-1.5B-Instruct', tokenizer=None, skip_tokenizer_init=False, revision=None, code_revision=None, tokenizer_revision=None, tokenizer_mode='auto', trust_remote_code=False, download_dir=None, load_format='auto', dtype='half', kv_cache_dtype='auto', quantization_param_path=None, max_model_len=2048, guided_decoding_backend='outli...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: **Then Response:** WARNING 06-24 21:44:48 _custom_ops.py:14] Failed to import from vllm._C with ImportError('libcudart.so.12: cannot open shared object file: No such file or directory') INFO 06-24 21:44:54 api_server.py...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: struct --served-model-name Qwen2-7B-Instruct-lora --max-model-len=2048 --dtype=half ``` **Then Response:** WARNING 06-24 21:44:48 _custom_ops.py:14] Failed to import from vllm._C with ImportError('libcudart.so.12: canno...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: When I send the cl:** ``` python -m vllm.entrypoints.openai.api_server --model Qwen/Qwen2-1.5B-Instruct --served-model-name Qwen2-7B-Instruct-lora --max-model-len=2048 --dtype=half ``` **Then Response:** WARNING 06-24 2...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: ssor=None, image_processor_revision=None, disable_image_processor=False, scheduler_delay_factor=0.0, enable_chunked_prefill=False, speculative_model=None, num_speculative_tokens=None, speculative_max_model_len=None, spe...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: 48 _custom_ops.py:14] Failed to import from vllm._C with ImportError('libcudart.so.12: cannot open shared object file: No such file or directory') INFO 06-24 21:44:54 api_server.py:177] vLLM API server version 0.5.0.pos...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
