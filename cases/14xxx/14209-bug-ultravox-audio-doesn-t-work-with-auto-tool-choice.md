# vllm-project/vllm#14209: [Bug]: Ultravox audio doesn't work with auto tool choice

| 字段 | 值 |
| --- | --- |
| Issue | [#14209](https://github.com/vllm-project/vllm/issues/14209) |
| 状态 | closed |
| 标签 | bug;stale;tool-calling |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;crash;mismatch;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Ultravox audio doesn't work with auto tool choice

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When I run ultravox v5 via: ``` $ VLLM_USE_V1=1 vllm serve fixie-ai/ultravox-v0_5-llama-3_3-70b --tensor-parallel-size 8 --download-dir /app/data/models --trust-remote-code --enable-auto-tool-choice --chat-template-content-format openai --chat-template /app/vllm/examples/tool_chat_template_llama3.1_json.jinja --tool-call-parser llama3_json --enable-chunked-prefill --max-model-len 9000 INFO 03-03 18:56:52 [__init__.py:207] Automatically detected platform rocm. INFO 03-03 18:57:09 [api_server.py:912] vLLM API server version 0.7.4.dev181+gf35f8e22.d20250303 INFO 03-03 18:57:09 [api_server.py:913] args: Namespace(subparser='serve', model_tag='fixie-ai/ultravox-v0_5-llama-3_3-70b', config='', host=None, port=8000, uvicorn_log_level='info', allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, lora_modules=None, prompt_adapters=None, chat_template='/app/vllm/examples/tool_chat_template_llama3.1_json.jinja', chat_template_content_format='openai', response_role='assistant', ssl_keyfile=None, ssl_certfile=None, ssl_ca_certs=None, enable_ssl_refresh=False, ssl_cert_reqs=0, root_path=Non...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 8: [Bug]: Ultravox audio doesn't work with auto tool choice bug;stale;tool-calling ### Your current environment ### 🐛 Describe the bug When I run ultravox v5 via: ``` $ VLLM_USE_V1=1 vllm serve fixie-ai/ultravox-v0_5-llama...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 7: n ultravox v5 via: ``` $ VLLM_USE_V1=1 vllm serve fixie-ai/ultravox-v0_5-llama-3_3-70b --tensor-parallel-size 8 --download-dir /app/data/models --trust-remote-code --enable-auto-tool-choice --chat-template-content-forma...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: d platform rocm. INFO 03-03 18:57:09 [api_server.py:912] vLLM API server version 0.7.4.dev181+gf35f8e22.d20250303 INFO 03-03 18:57:09 [api_server.py:913] args: Namespace(subparser='serve', model_tag='fixie-ai/ultravox-v...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: 0 INFO 03-03 18:56:52 [__init__.py:207] Automatically detected platform rocm. INFO 03-03 18:57:09 [api_server.py:912] vLLM API server version 0.7.4.dev181+gf35f8e22.d20250303 INFO 03-03 18:57:09 [api_server.py:913] args...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: e, download_dir='/app/data/models', load_format='auto', config_format= , dtype='auto', kv_cache_dtype='auto', max_model_len=9000, guided_decoding_backend='xgrammar', logits_processor_pattern=None, model_impl='auto', dis...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
