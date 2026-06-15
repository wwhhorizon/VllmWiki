# vllm-project/vllm#14628: [Bug]: Multi GPU inference using two RTX 5090s(TP=2)

| 字段 | 值 |
| --- | --- |
| Issue | [#14628](https://github.com/vllm-project/vllm/issues/14628) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Multi GPU inference using two RTX 5090s(TP=2)

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Hello, I’m trying to run vLLM on a machine with two RTX 5090 GPUs, specifically using tensor parallelism with a size of 2. Inference on a single 5090 works fine, but I’m having trouble with two GPUs. Forcing NCCL_P2P_DISABLE=1 did not help to resolve the issue. Below is the error log: ``` INFO 03-11 17:07:44 [__init__.py:256] Automatically detected platform cuda. INFO 03-11 17:07:45 [api_server.py:912] vLLM API server version 0.7.4.dev254+ged6ea065.d20250311 INFO 03-11 17:07:45 [api_server.py:913] args: Namespace(subparser='serve', model_tag='Qwen/Qwen2-1.5B-Instruct', config='', host=None, port=8000, uvicorn_log_level='info', allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, lora_modules=None, prompt_adapters=None, chat_template=None, chat_template_content_format='auto', response_role='assistant', ssl_keyfile=None, ssl_certfile=None, ssl_ca_certs=None, enable_ssl_refresh=False, ssl_cert_reqs=0, root_path=None, middleware=[], return_tokens_as_token_ids=False, disable_frontend_multiprocessing=False, enable_request_id_headers=False, enable_auto_tool_choice=False, tool_call_p...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 7: [Bug]: Multi GPU inference using two RTX 5090s(TP=2) bug;stale ### Your current environment ### 🐛 Describe the bug Hello, I’m trying to run vLLM on a machine with two RTX 5090 GPUs, specifically using tensor parallelism...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: Hello, I’m trying to run vLLM on a machine with two RTX 5090 GPUs, specifically using tensor parallelism with a size of 2. Inference on a single 5090 works fine, but I’m having trouble with two GPUs. Forcing NCCL_P2P_DI...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: media_path=None, download_dir=None, load_format='auto', config_format= , dtype='auto', kv_cache_dtype='auto', max_model_len=4096, guided_decoding_backend='xgrammar', logits_processor_pattern=None, model_impl='auto', dis...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: FO 03-11 17:07:45 [api_server.py:913] args: Namespace(subparser='serve', model_tag='Qwen/Qwen2-1.5B-Instruct', config='', host=None, port=8000, uvicorn_log_level='info', allow_credentials=False, allowed_origins=['*'], a...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [Bug]: Multi GPU inference using two RTX 5090s(TP=2) bug;stale ### Your current environment ### 🐛 Describe the bug Hello, I’m trying to run vLLM on a machine with two RTX 5090 GPUs, specifically using tensor parallelism...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
