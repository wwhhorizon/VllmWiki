# vllm-project/vllm#12823: [Bug]: Error in inspecting model architecture 'MiniCPMO'

| 字段 | 值 |
| --- | --- |
| Issue | [#12823](https://github.com/vllm-project/vllm/issues/12823) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Error in inspecting model architecture 'MiniCPMO'

### Issue 正文摘录

### Your current environment Using docker CPU image. ### 🐛 Describe the bug > INFO 02-06 10:20:41 __init__.py:190] Automatically detected platform cpu. INFO 02-06 10:20:42 api_server.py:840] vLLM API server version 0.7.3.dev2+gcefd56ee INFO 02-06 10:20:42 api_server.py:841] args: Namespace(host=None, port=8000, uvicorn_log_level='info', allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, lora_modules=None, prompt_adapters=None, chat_template=None, chat_template_content_format='auto', response_role='assistant', ssl_keyfile=None, ssl_certfile=None, ssl_ca_certs=None, ssl_cert_reqs=0, root_path=None, middleware=[], return_tokens_as_token_ids=False, disable_frontend_multiprocessing=False, enable_request_id_headers=False, enable_auto_tool_choice=False, enable_reasoning=False, reasoning_parser=None, tool_call_parser=None, tool_parser_plugin='', model='openbmb/MiniCPM-o-2_6-int4', task='auto', tokenizer=None, skip_tokenizer_init=False, revision=None, code_revision=None, tokenizer_revision=None, tokenizer_mode='auto', trust_remote_code=True, allowed_local_media_path=None, download_dir=None, load_format='auto', config_format= , dtype=...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: [Bug]: Error in inspecting model architecture 'MiniCPMO' bug;stale ### Your current environment Using docker CPU image. ### 🐛 Describe the bug > INFO 02-06 10:20:41 __init__.py:190] Automatically detected platform cpu....
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: [Bug]: Error in inspecting model architecture 'MiniCPMO' bug;stale ### Your current environment Using docker CPU image. ### 🐛 Describe the bug > INFO 02-06 10:20:41 __init__.py:190] Automatically detected platform cpu....
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: el architecture 'MiniCPMO' bug;stale ### Your current environment Using docker CPU image. ### 🐛 Describe the bug > INFO 02-06 10:20:41 __init__.py:190] Automatically detected platform cpu. INFO 02-06 10:20:42 api_server...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: ol_call_parser=None, tool_parser_plugin='', model='openbmb/MiniCPM-o-2_6-int4', task='auto', tokenizer=None, skip_tokenizer_init=False, revision=None, code_revision=None, tokenizer_revision=None, tokenizer_mode='auto',...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: pace(host=None, port=8000, uvicorn_log_level='info', allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, lora_modules=None, prompt_adapters=None, chat_template=Non...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
