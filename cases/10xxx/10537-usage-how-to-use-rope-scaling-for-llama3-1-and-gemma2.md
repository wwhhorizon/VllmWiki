# vllm-project/vllm#10537: [Usage]: How to use ROPE scaling for llama3.1 and gemma2?

| 字段 | 值 |
| --- | --- |
| Issue | [#10537](https://github.com/vllm-project/vllm/issues/10537) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 26; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;distributed_parallel;frontend_api;model_support;quantization;scheduler_memory |
| 子分类 | kernel_eff |
| Operator 关键词 | attention;cache;cuda;operator;quantization |
| 症状 | crash |
| 根因提示 | dtype;env_dependency;memory_layout;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: How to use ROPE scaling for llama3.1 and gemma2?

### Issue 正文摘录

### Your current environment ```text vllm-0.6.4.post1 ``` ### How would you like to use vllm I am using the latest vllm version, i need to apply rope scaling to llama3.1-8b and gemma2-9b to extend the the max context length from 8k up to 128k. I using this command: ``` python -m vllm.entrypoints.openai.api_server --model NousResearch/Meta-Llama-3.1-8B-Instruct --max-model-len 12000 --gpu-memory-utilization 0.95 --rope-scaling '{"factor": 8.0, "type": "dynamic"}' ``` I don't know how to use/tune these args `--rope-scaling ` and `--rope-theta` to be assure that i can serve 128k tokens per requests (or context length is extended to 128k tokens). what do they mean? ***Hardware A10 GPU with 24G RAM*** btw I got this error: ``` $ python -m vllm.entrypoints.openai.api_server --model NousResearch/Meta-Llama-3.1-8B-Instruct --max-model-len 120000 --gpu-memory-utilization 0.95 --rope-scaling '{"factor": 8.0, "type": "dynamic"}' INFO 11-21 13:28:24 api_server.py:585] vLLM API server version 0.6.4.post1 INFO 11-21 13:28:24 api_server.py:586] args: Namespace(host=None, port=8000, uvicorn_log_level='info', allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: [Usage]: How to use ROPE scaling for llama3.1 and gemma2? usage;stale ### Your current environment ```text vllm-0.6.4.post1 ``` ### How would you like to use vllm I am using the latest vllm version, i need to apply rope...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: [Usage]: How to use ROPE scaling for llama3.1 and gemma2? usage;stale ### Your current environment ```text vllm-0.6.4.post1 ``` ### How would you like to use vllm I am using the latest vllm version, i need to apply rope...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ost1 ``` ### How would you like to use vllm I am using the latest vllm version, i need to apply rope scaling to llama3.1-8b and gemma2-9b to extend the the max context length from 8k up to 128k. I using this command: ``...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: media_path=None, download_dir=None, load_format='auto', config_format= , dtype='auto', kv_cache_dtype='auto', quantization_param_path=None, max_model_len=120000, guided_decoding_backend='outlines', distributed_executor_...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 4: pace(host=None, port=8000, uvicorn_log_level='info', allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, lora_modules=None, prompt_adapters=None, chat_template=Non...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
