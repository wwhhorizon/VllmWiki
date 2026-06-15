# vllm-project/vllm#16092: [Bug]: vllm server stops after torch.compile step for multi-gpu setup 

| 字段 | 值 |
| --- | --- |
| Issue | [#16092](https://github.com/vllm-project/vllm/issues/16092) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vllm server stops after torch.compile step for multi-gpu setup 

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ``` mistral="mistralai/Mistral-7B-Instruct-v0.3" starcoder="bigcode/starcoder2-7b" qwen7b="Qwen/Qwen2.5-7B-Instruct" qwen14b="Qwen/Qwen2.5-14B-Instruct" qwen32b="Qwen/Qwen2.5-32B-Instruct" qwen70b="Qwen/Qwen2.5-70B-Instruct" llama8b="meta-llama/Llama-3.1-8B-Instruct" llama1b="meta-llama/Llama-3.2-1B" deepseek="deepseek-ai/DeepSeek-R1-Distill-Qwen-7B" CUDA_VISIBLE_DEVICES=0,1 vllm serve $qwen32b -tp 2 ``` Using this code I get the following log: ``` bash server_llm.sh INFO 04-05 22:13:02 [__init__.py:239] Automatically detected platform cuda. INFO 04-05 22:13:07 [api_server.py:981] vLLM API server version 0.8.2 INFO 04-05 22:13:07 [api_server.py:982] args: Namespace(subparser='serve', model_tag='Qwen/Qwen2.5-32B-Instruct', config='', host=None, port=8000, uvicorn_log_level='info', disable_uvicorn_access_log=False, allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, lora_modules=None, prompt_adapters=None, chat_template=None, chat_template_content_format='auto', response_role='assistant', ssl_keyfile=None, ssl_certfile=None, ssl_ca_certs=None, enable_ssl_refresh=False, ssl_cer...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 7: ug]: vllm server stops after torch.compile step for multi-gpu setup bug;stale ### Your current environment ### 🐛 Describe the bug ``` mistral="mistralai/Mistral-7B-Instruct-v0.3" starcoder="bigcode/starcoder2-7b" qwen7b...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: l="mistralai/Mistral-7B-Instruct-v0.3" starcoder="bigcode/starcoder2-7b" qwen7b="Qwen/Qwen2.5-7B-Instruct" qwen14b="Qwen/Qwen2.5-14B-Instruct" qwen32b="Qwen/Qwen2.5-32B-Instruct" qwen70b="Qwen/Qwen2.5-70B-Instruct" llam...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 5: dtype='auto', kv_cache_dtype='auto', max_model_len=None, guided_decoding_backend='xgrammar', logits_processor_pattern=None, model_impl='auto', distributed_executor_backend=None, pipeline_parallel_size=1, tensor_parallel...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: [Bug]: vllm server stops after torch.compile step for multi-gpu setup bug;stale ### Your current environment ### 🐛 Describe the bug ``` mistral="mistralai/Mistral-7B-Instruct-v0.3" starcoder="bigcode/starcoder2-7b" qwen...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: media_path=None, download_dir=None, load_format='auto', config_format= , dtype='auto', kv_cache_dtype='auto', max_model_len=None, guided_decoding_backend='xgrammar', logits_processor_pattern=None, model_impl='auto', dis...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
