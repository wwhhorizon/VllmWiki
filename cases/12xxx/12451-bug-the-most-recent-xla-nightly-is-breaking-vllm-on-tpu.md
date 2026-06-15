# vllm-project/vllm#12451: [Bug]: the most recent xla nightly is breaking vllm on TPU

| 字段 | 值 |
| --- | --- |
| Issue | [#12451](https://github.com/vllm-project/vllm/issues/12451) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: the most recent xla nightly is breaking vllm on TPU

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug The [recent change](https://github.com/vllm-project/vllm/commit/324960a95c00112ce6b9b858d9311da1597cfb8b) to `20250124` is causing vllm to break - ``` $ vllm serve "meta-llama/Meta-Llama-3.1-8B" --download_dir /dev/shm --num-scheduler-steps 4 --swap-space 16 --disable-log-requests --tensor_parallel_size=8 --max-model-len=256 --dtype=bfloat16 INFO 01-26 17:51:40 __init__.py:187] No platform detected, vLLM is running on UnspecifiedPlatform INFO 01-26 17:51:41 api_server.py:786] vLLM API server version 0.6.6.post2.dev384+gaa2cd2c4 INFO 01-26 17:51:41 api_server.py:787] args: Namespace(subparser='serve', model_tag='meta-llama/Meta-Llama-3.1-8B', config='', host=None, port=8000, uvicorn_log_level='info', allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, lora_modules=None, prompt_adapters=None, chat_template=None, chat_template_content_format='auto', response_role='assistant', ssl_keyfile=None, ssl_certfile=None, ssl_ca_certs=None, ssl_cert_reqs=0, root_path=None, middleware=[], return_tokens_as_token_ids=False, disable_frontend_multiprocessin...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: 17:51:40 __init__.py:187] No platform detected, vLLM is running on UnspecifiedPlatform INFO 01-26 17:51:41 api_server.py:786] vLLM API server version 0.6.6.post2.dev384+gaa2cd2c4 INFO 01-26 17:51:41 api_server.py:787] a...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: 16 --disable-log-requests --tensor_parallel_size=8 --max-model-len=256 --dtype=bfloat16 INFO 01-26 17:51:40 __init__.py:187] No platform detected, vLLM is running on UnspecifiedPlatform INFO 01-26 17:51:41 api_server.py...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: nightly is breaking vllm on TPU bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug The [recent change](https://github.com/vllm-project/vllm/commit/324960a95c00112ce6b9b858d9311da...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: vllm serve "meta-llama/Meta-Llama-3.1-8B" --download_dir /dev/shm --num-scheduler-steps 4 --swap-space 16 --disable-log-requests --tensor_parallel_size=8 --max-model-len=256 --dtype=bfloat16 INFO 01-26 17:51:40 __init__...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: ='', host=None, port=8000, uvicorn_log_level='info', allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, lora_modules=None, prompt_adapters=None, chat_template=Non...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
