# vllm-project/vllm#17250: [Bug]: The same startup command works fine in version 0.8.2, but it throws an error in version 0.8.4.

| 字段 | 值 |
| --- | --- |
| Issue | [#17250](https://github.com/vllm-project/vllm/issues/17250) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 12; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm;quantization;scheduler_memory;speculative_decoding |
| 子分类 | memory |
| Operator 关键词 | attention;cuda;gemm;operator;quantization;triton |
| 症状 | build_error;crash;oom;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: The same startup command works fine in version 0.8.2, but it throws an error in version 0.8.4.

### Issue 正文摘录

``` python -m vllm.entrypoints.openai.api_server \ --served-model-name Qwen2___5-VL-32B-Instruct-AWQ \ --model /home/Qwen2___5-VL-32B-Instruct-AWQ \ --tensor-parallel-size 2 \ --dtype=half \ --max-model-len 20000 \ --gpu_memory_utilization 0.99 \ --max_num_seqs 2 \ --limit-mm-per-prompt "image=5" \ --enable-auto-tool-choice \ --tool-call-parser=llama3_json \ --trust-remote-code \ --enforce-eager \ --port=7777 ``` ![Image](https://github.com/user-attachments/assets/60bc17a8-7b57-43ba-b3be-22a866891ec5) ![Image](https://github.com/user-attachments/assets/23935bbe-0f06-4e19-a5b8-b0f910603976) ### 🐛 Describe the bug error log: ``` INFO 04-27 16:27:09 [__init__.py:239] Automatically detected platform cuda. INFO 04-27 16:27:10 [api_server.py:1034] vLLM API server version 0.8.4 INFO 04-27 16:27:10 [api_server.py:1035] args: Namespace(host=None, port=7777, uvicorn_log_level='info', disable_uvicorn_access_log=False, allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, lora_modules=None, prompt_adapters=None, chat_template=None, chat_template_content_format='auto', response_role='assistant', ssl_keyfile=None, ssl_certfile=None, ssl_ca_c...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 8: n 0.8.4. bug ``` python -m vllm.entrypoints.openai.api_server \ --served-model-name Qwen2___5-VL-32B-Instruct-AWQ \ --model /home/Qwen2___5-VL-32B-Instruct-AWQ \ --tensor-parallel-size 2 \ --dtype=half \ --max-model-len...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: model /home/Qwen2___5-VL-32B-Instruct-AWQ \ --tensor-parallel-size 2 \ --dtype=half \ --max-model-len 20000 \ --gpu_memory_utilization 0.99 \ --max_num_seqs 2 \ --limit-mm-per-prompt "image=5" \ --enable-auto-tool-choic...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [Bug]: The same startup command works fine in version 0.8.2, but it throws an error in version 0.8.4. bug ``` python -m vllm.entrypoints.openai.api_server \ --served-model-name Qwen2___5-VL-32B-Instruct-AWQ \ --model /h...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: okens_as_token_ids=False, disable_frontend_multiprocessing=False, enable_request_id_headers=False, enable_auto_tool_choice=True, tool_call_parser='llama3_json', tool_parser_plugin='', model='/home/drc-whlab/james/Qwen2_...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: `` INFO 04-27 16:27:09 [__init__.py:239] Automatically detected platform cuda. INFO 04-27 16:27:10 [api_server.py:1034] vLLM API server version 0.8.4 INFO 04-27 16:27:10 [api_server.py:1035] args: Namespace(host=None, p...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
