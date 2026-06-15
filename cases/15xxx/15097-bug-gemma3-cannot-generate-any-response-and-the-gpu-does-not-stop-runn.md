# vllm-project/vllm#15097: [Bug]: Gemma3 cannot generate any response, and the GPU does not stop running. Please check the screenshot.

| 字段 | 值 |
| --- | --- |
| Issue | [#15097](https://github.com/vllm-project/vllm/issues/15097) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | activation_norm;attention_kv_cache;distributed_parallel;frontend_api;model_support;multimodal_vlm;quantization;sampling_logits;scheduler_memory |
| 子分类 | throughput |
| Operator 关键词 | attention;cache;cuda;quantization;sampling;triton |
| 症状 | slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Gemma3 cannot generate any response, and the GPU does not stop running. Please check the screenshot.

### Issue 正文摘录

### Your current environment ![Image](https://github.com/user-attachments/assets/90c067e3-441c-438d-926b-07c10be141ed) ### 🐛 Describe the bug ``` python -m vllm.entrypoints.openai.api_server --served-model-name gemma-3-12b-it --model /home/drc-whlab/.cache/modelscope/hub/LL M-Research/gemma-3-12b-it --tensor-parallel-size 2 --dtype=half --max-model-len 8192 --gpu_memory_utilization 0.99 --max_num_seqs 2 --trust-remote-code --enforce-eager --port=7777 INFO 03-19 14:17:59 [__init__.py:256] Automatically detected platform cuda. INFO 03-19 14:18:03 [api_server.py:977] vLLM API server version 0.8.0 INFO 03-19 14:18:03 [api_server.py:978] args: Namespace(host=None, port=7777, uvicorn_log_level='info', allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], ap i_key=None, lora_modules=None, prompt_adapters=None, chat_template=None, chat_template_content_format='auto', response_role='assistant', ssl_keyfile=None, ssl_certfile=None, ssl_ca_certs=None, enable_ ssl_refresh=False, ssl_cert_reqs=0, root_path=None, middleware=[], return_tokens_as_token_ids=False, disable_frontend_multiprocessing=False, enable_request_id_headers=False, enable_auto_tool_choic...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 7: [Bug]: Gemma3 cannot generate any response, and the GPU does not stop running. Please check the screenshot. bug ### Your current environment ![Image](https://github.com/user-attachments/assets/90c067e3-441c-438d-926b-07...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: M-Research/gemma-3-12b-it --tensor-parallel-size 2 --dtype=half --max-model-len 8192 --gpu_memory_utilization 0.99 --max_num_seqs 2 --trust-remote-code --enforce-eager --port=7777 INFO 03-19 14:17:59 [__init__.py:256] A...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: okens_as_token_ids=False, disable_frontend_multiprocessing=False, enable_request_id_headers=False, enable_auto_tool_choice=Fa lse, tool_call_parser=None, tool_parser_plugin='', model='/home/drc-whlab/.cache/modelscope/h...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: d platform cuda. INFO 03-19 14:18:03 [api_server.py:977] vLLM API server version 0.8.0 INFO 03-19 14:18:03 [api_server.py:978] args: Namespace(host=None, port=7777, uvicorn_log_level='info', allow_credentials=False, all...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: /drc-whlab/.cache/modelscope/hub/LL M-Research/gemma-3-12b-it --tensor-parallel-size 2 --dtype=half --max-model-len 8192 --gpu_memory_utilization 0.99 --max_num_seqs 2 --trust-remote-code --enforce-eager --port=7777 INF...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
