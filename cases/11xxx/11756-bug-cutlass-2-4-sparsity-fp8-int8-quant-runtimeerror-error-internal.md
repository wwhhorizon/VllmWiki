# vllm-project/vllm#11756: [Bug]: Cutlass 2:4 Sparsity + FP8/Int8 Quant RuntimeError: Error Internal

| 字段 | 值 |
| --- | --- |
| Issue | [#11756](https://github.com/vllm-project/vllm/issues/11756) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;model_support;quantization |
| 子分类 |  |
| Operator 关键词 | attention;cuda;fp8;operator;quantization |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Cutlass 2:4 Sparsity + FP8/Int8 Quant RuntimeError: Error Internal

### Issue 正文摘录

[root workflow_47400355 /ossfs/workspace] 一 1月 06 15:46:05 $CUDA_LAUNCH_BLOCKING=1 vllm serve /mntfn/yanyi/sparse/mntfn-FP8-Dynamic/ INFO 01-06 15:46:27 api_server.py:647] vLLM API server version 0.1.dev3896+ga491d6f.d20250103 INFO 01-06 15:46:27 api_server.py:648] args: Namespace(subparser='serve', model_tag='/mntfn/yanyi/sparse/mntfn-FP8-Dynamic/', config='', host=None, port=8000, uvicorn_log_level='info', allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, lora_modules=None, prompt_adapters=None, chat_template=None, chat_template_content_format='auto', response_role='assistant', ssl_keyfile=None, ssl_certfile=None, ssl_ca_certs=None, ssl_cert_reqs=0, root_path=None, middleware=[], return_tokens_as_token_ids=False, disable_frontend_multiprocessing=False, enable_auto_tool_choice=False, tool_call_parser=None, tool_parser_plugin='', model='/mntfn/yanyi/sparse/mntfn-FP8-Dynamic/', task='auto', tokenizer=None, skip_tokenizer_init=False, revision=None, code_revision=None, tokenizer_revision=None, tokenizer_mode='auto', trust_remote_code=False, allowed_local_media_path=None, download_dir=None, load_format='auto', config_format= ,...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: ntfn-FP8-Dynamic/ INFO 01-06 15:46:27 api_server.py:647] vLLM API server version 0.1.dev3896+ga491d6f.d20250103 INFO 01-06 15:46:27 api_server.py:648] args: Namespace(subparser='serve', model_tag='/mntfn/yanyi/sparse/mn...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: [Bug]: Cutlass 2:4 Sparsity + FP8/Int8 Quant RuntimeError: Error Internal bug [root workflow_47400355 /ossfs/workspace] 一 1月 06 15:46:05 $CUDA_LAUNCH_BLOCKING=1 vllm serve /mntfn/yanyi/sparse/mntfn-FP8-Dynamic/ INFO 01-...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: e, max_prompt_adapters=1, max_prompt_adapter_token=0, device='auto', num_scheduler_steps=1, multi_step_stream_outputs=True, scheduler_delay_factor=0.0, enable_chunked_prefill=None, speculative_model=None, speculative_mo...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: [Bug]: Cutlass 2:4 Sparsity + FP8/Int8 Quant RuntimeError: Error Internal bug [root workflow_47400355 /ossfs/workspace] 一 1月 06 15:46:05 $CUDA_LAUNCH_BLOCKING=1 vllm serve /mntfn/yanyi/sparse/mntfn-FP8-Dynamic/ INFO 01-...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 4: [root workflow_47400355 /ossfs/workspace] 一 1月 06 15:46:05 $CUDA_LAUNCH_BLOCKING=1 vllm serve /mntfn/yanyi/sparse/mntfn-FP8-Dynamic/ INFO 01-06 15:46:27 api_server.py:647] vLLM API server version 0.1.dev3896+ga491d6f.d2...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
