# vllm-project/vllm#11762: [Bug]: Failed to apply Qwen2VLProcessor when running vllm serve showlab/ShowUI-2B

| 字段 | 值 |
| --- | --- |
| Issue | [#11762](https://github.com/vllm-project/vllm/issues/11762) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency;memory_layout;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Failed to apply Qwen2VLProcessor when running vllm serve showlab/ShowUI-2B

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug [showlab/ShowUI-2B](https://huggingface.co/showlab/ShowUI-2B) is a GUI grounding model fine-tuned from Qwen/Qwen2-VL-2B. I had no problem using this model with `vllm serve` until a recent PR merge #11717, which caused the server hosting to fail. The version before this PR merge is working fine. Below is the error message when I try to run `vllm serve showlab/ShowUI-2B`. ``` INFO 01-06 15:35:04 api_server.py:764] vLLM API server version 0.6.6.post2.dev73+geed11ebe INFO 01-06 15:35:04 api_server.py:765] args: Namespace(subparser='serve', model_tag='showlab/ShowUI-2B', config='', host=None, port=8000, uvicorn_log_level='info', allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, lora_modules=None, prompt_adapters=None, chat_template=None, chat_template_content_format='auto', response_role='assistant', ssl_keyfile=None, ssl_certfile=None, ssl_ca_certs=None, ssl_cert_reqs=0, root_path=None, middleware=[], return_tokens_as_token_ids=False, disable_frontend_multiprocessing=False, enable_request_id_headers=False, enable_auto_tool_choice=False, tool...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 8: [Bug]: Failed to apply Qwen2VLProcessor when running vllm serve showlab/ShowUI-2B bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug [showlab/ShowUI-2B](https://huggingface.co/sh...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: l a recent PR merge #11717, which caused the server hosting to fail. The version before this PR merge is working fine. Below is the error message when I try to run `vllm serve showlab/ShowUI-2B`. ``` INFO 01-06 15:35:04...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: okens_as_token_ids=False, disable_frontend_multiprocessing=False, enable_request_id_headers=False, enable_auto_tool_choice=False, tool_call_parser=None, tool_parser_plugin='', model='showlab/ShowUI-2B', task='auto', tok...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: auto', quantization_param_path=None, max_model_len=None, guided_decoding_backend='xgrammar', logits_processor_pattern=None, distributed_executor_backend=None, worker_use_ray=False, pipeline_parallel_size=1, tensor_paral...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: media_path=None, download_dir=None, load_format='auto', config_format= , dtype='auto', kv_cache_dtype='auto', quantization_param_path=None, max_model_len=None, guided_decoding_backend='xgrammar', logits_processor_patter...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
