# vllm-project/vllm#17708: [Bug]: Qwen3-30B-A3B-FP8 fails to run on 2*3090

| 字段 | 值 |
| --- | --- |
| Issue | [#17708](https://github.com/vllm-project/vllm/issues/17708) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;distributed_parallel;frontend_api;gemm_linear;model_support;quantization;sampling_logits;scheduler_memory |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;fp8;quantization;sampling |
| 症状 | crash;mismatch |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Qwen3-30B-A3B-FP8 fails to run on 2*3090

### Issue 正文摘录

### Your current environment CUDA_VISIBLE_DEVICES=5,7 vllm serve Qwen3-30B-A3B-FP8 --api-key wanglei --host 0.0.0.0 --port 24445 --enable-reasoning --reasoning-parser deepseek_r1 --tensor-parallel-size 2 INFO 05-06 16:51:41 [__init__.py:239] Automatically detected platform cuda. INFO 05-06 16:51:43 [api_server.py:1034] vLLM API server version 0.8.4 INFO 05-06 16:51:43 [api_server.py:1035] args: Namespace(subparser='serve', model_tag='Qwen3-30B-A3B-FP8', config='', host='0.0.0.0', port=24445, uvicorn_log_level='info', disable_uvicorn_access_log=False, allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key='wanglei', lora_modules=None, prompt_adapters=None, chat_template=None, chat_template_content_format='auto', response_role='assistant', ssl_keyfile=None, ssl_certfile=None, ssl_ca_certs=None, enable_ssl_refresh=False, ssl_cert_reqs=0, root_path=None, middleware=[], return_tokens_as_token_ids=False, disable_frontend_multiprocessing=False, enable_request_id_headers=False, enable_auto_tool_choice=False, tool_call_parser=None, tool_parser_plugin='', model='Qwen3-30B-A3B-FP8', task='auto', tokenizer=None, hf_config_path=None, skip_tokenize...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 6: [Bug]: Qwen3-30B-A3B-FP8 fails to run on 2*3090 bug;stale ### Your current environment CUDA_VISIBLE_DEVICES=5,7 vllm serve Qwen3-30B-A3B-FP8 --api-key wanglei --host 0.0.0.0 --port 24445 --enable-reasoning --reasoning-p...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: [Bug]: Qwen3-30B-A3B-FP8 fails to run on 2*3090 bug;stale ### Your current environment CUDA_VISIBLE_DEVICES=5,7 vllm serve Qwen3-30B-A3B-FP8 --api-key wanglei --host 0.0.0.0 --port 24445 --enable-reasoning --reasoning-p...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: platform cuda. INFO 05-06 16:51:43 [api_server.py:1034] vLLM API server version 0.8.4 INFO 05-06 16:51:43 [api_server.py:1035] args: Namespace(subparser='serve', model_tag='Qwen3-30B-A3B-FP8', config='', host='0.0.0.0',...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: Qwen3-30B-A3B-FP8 fails to run on 2*3090 bug;stale ### Your current environment CUDA_VISIBLE_DEVICES=5,7 vllm serve Qwen3-30B-A3B-FP8 --api-key wanglei --host 0.0.0.0 --port 24445 --enable-reasoning --reasoning-p...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 5: ne_parallel_size=1, tensor_parallel_size=2, data_parallel_size=1, enable_expert_parallel=False, max_parallel_loading_workers=None, ray_workers_use_nsight=False, disable_custom_all_reduce=False, block_size=None, enable_p...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
