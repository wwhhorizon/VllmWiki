# vllm-project/vllm#13451: [Bug]: With docker "ValueError: No supported config format found in"

| 字段 | 值 |
| --- | --- |
| Issue | [#13451](https://github.com/vllm-project/vllm/issues/13451) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;model_support;quantization |
| 子分类 | install |
| Operator 关键词 | cuda;quantization |
| 症状 | crash |
| 根因提示 | dtype |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: With docker "ValueError: No supported config format found in"

### Issue 正文摘录

### Your current environment Official latest docker image ### 🐛 Describe the bug I run a docker container with the commande line: "docker run --runtime nvidia --gpus all \ -v ~/.cache/huggingface:/root/.cache/huggingface \ --env "HUGGING_FACE_HUB_TOKEN= " \ -p 8000:8000 \ --ipc=host \ vllm/vllm-openai:latest \ --model mistralai/Mistral-7B-v0.1" A few hours ago, everything was working fine. However, when I try to run a model using the Docker image now, I encounter the following error: "ValueError: No supported config format found in" Below, you’ll find the full error message that appears when I run the command provided on the vLLM website. docker run --runtime nvidia --gpus all \ -v ~/.cache/huggingface:/root/.cache/huggingface \ --env "HUGGING_FACE_HUB_TOKEN= " \ -p 8000:8000 \ --ipc=host \ vllm/vllm-openai:latest \ --model mistralai/Mistral-7B-v0.1 INFO 02-17 19:14:31 __init__.py:190] Automatically detected platform cuda. INFO 02-17 19:14:31 api_server.py:840] vLLM API server version 0.7.2 INFO 02-17 19:14:31 api_server.py:841] args: Namespace(host=None, port=8000, uvicorn_log_level='info', allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: With docker "ValueError: No supported config format found in" bug ### Your current environment Official latest docker image ### 🐛 Describe the bug I run a docker container with the commande line: "docker run --ru...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: okens_as_token_ids=False, disable_frontend_multiprocessing=False, enable_request_id_headers=False, enable_auto_tool_choice=False, enable_reasoning=False, reasoning_parser=None, tool_call_parser=None, tool_parser_plugin=...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [Bug]: With docker "ValueError: No supported config format found in" bug ### Your current environment Official latest docker image ### 🐛 Describe the bug I run a docker container with the commande line: "docker run --ru...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: media_path=None, download_dir=None, load_format='auto', config_format= , dtype='auto', kv_cache_dtype='auto', max_model_len=None, guided_decoding_backend='xgrammar', logits_processor_pattern=None, model_impl='auto', dis...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: pace(host=None, port=8000, uvicorn_log_level='info', allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, lora_modules=None, prompt_adapters=None, chat_template=Non...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
