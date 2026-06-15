# vllm-project/vllm#17392: [Bug]: Failed to run model Qwen3-30B-A3B on DGX V100x4

| 字段 | 值 |
| --- | --- |
| Issue | [#17392](https://github.com/vllm-project/vllm/issues/17392) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 40; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization;scheduler_memory;speculative_decoding |
| 子分类 | cold_start |
| Operator 关键词 | attention;cuda;moe;operator;quantization;triton |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Failed to run model Qwen3-30B-A3B on DGX V100x4

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug command ```shell docker run --gpus all -v ~/.cache/huggingface:/root/.cache/huggingface -p 8000:8000 --ipc=host vllm/vllm-openai:v0.8.5 --model Qwen/Qwen3-30B-A3B --tensor-parallel-size 4 --dtype=half --enable-reasoning --reasoning-parser deepseek_r1 --max-model-len 32768 --enforce-eager ``` Output: ```shell NFO 04-29 06:17:33 [__init__.py:239] Automatically detected platform cuda. INFO 04-29 06:17:38 [api_server.py:1043] vLLM API server version 0.8.5 INFO 04-29 06:17:38 [api_server.py:1044] args: Namespace(host=None, port=8000, uvicorn_log_level='info', disable_uvicorn_access_log=False, allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, lora_modules=None, prompt_adapters=None, chat_template=None, chat_template_content_format='auto', response_role='assistant', ssl_keyfile=None, ssl_certfile=None, ssl_ca_certs=None, enable_ssl_refresh=False, ssl_cert_reqs=0, root_path=None, middleware=[], return_tokens_as_token_ids=False, disable_frontend_multiprocessing=False, enable_request_id_headers=False, enable_auto_tool_choice=False, tool_call_parser=None, tool_parser_plugin='', model...

## 现有链接修复摘要

#29889 [Bugfix] respect user-defined flash attention version in ViT attentions

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: [Bug]: Failed to run model Qwen3-30B-A3B on DGX V100x4 bug ### Your current environment ### 🐛 Describe the bug command ```shell docker run --gpus all -v ~/.cache/huggingface:/root/.cache/huggingface -p 8000:8000 --ipc=h...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: ## Your current environment ### 🐛 Describe the bug command ```shell docker run --gpus all -v ~/.cache/huggingface:/root/.cache/huggingface -p 8000:8000 --ipc=host vllm/vllm-openai:v0.8.5 --model Qwen/Qwen3-30B-A3B --ten...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: vllm-openai:v0.8.5 --model Qwen/Qwen3-30B-A3B --tensor-parallel-size 4 --dtype=half --enable-reasoning --reasoning-parser deepseek_r1 --max-model-len 32768 --enforce-eager ``` Output: ```shell NFO 04-29 06:17:33 [__init...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 4: =None, port=8000, uvicorn_log_level='info', disable_uvicorn_access_log=False, allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, lora_modules=None, prompt_adapter...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: okens_as_token_ids=False, disable_frontend_multiprocessing=False, enable_request_id_headers=False, enable_auto_tool_choice=False, tool_call_parser=None, tool_parser_plugin='', model='Qwen/Qwen3-30B-A3B', task='auto', to...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#29889](https://github.com/vllm-project/vllm/pull/29889) | closes_keyword | 0.95 | [Bugfix] respect user-defined flash attention version in ViT attentions | fix #27103, #25143, #17392, #28903 in better way. ## Test Plan Run `Qwen/Qwen3-VL-32B-Instruct` successfully with the default FA backend on H100. ```bash vllm serve Qwen/Qwen3-V |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
