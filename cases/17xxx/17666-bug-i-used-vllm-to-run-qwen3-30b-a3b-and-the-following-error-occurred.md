# vllm-project/vllm#17666: [Bug]: I used vllm to run Qwen3-30B-A3B and the following error occurred

| 字段 | 值 |
| --- | --- |
| Issue | [#17666](https://github.com/vllm-project/vllm/issues/17666) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;distributed_parallel;frontend_api;model_support;moe;quantization;scheduler_memory |
| 子分类 | memory |
| Operator 关键词 | attention;cuda;kernel;moe;operator;quantization;triton |
| 症状 | build_error;crash;oom |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: I used vllm to run Qwen3-30B-A3B and the following error occurred

### Issue 正文摘录

### Your current environment `(vllm) sun@sun-AI:~/anaconda3/envs/vllm/lib/python3.11/site-packages/vllm/model_executor/layers/fused_moe/configs$ vllm serve /home/sun/models/Qwen3-30B-A3B --no-enable-expert-parallel --host 0.0.0.0 --port 8088 --tensor-parallel-size 4 --gpu-memory-utilization 1 --dtype float16 --max-model-len 4096 --max-num-seqs 16 --served-model-name Qwen3-30B-A3B INFO 05-05 23:51:03 [__init__.py:239] Automatically detected platform cuda. INFO 05-05 23:51:09 [api_server.py:1043] vLLM API server version 0.8.5.post1 INFO 05-05 23:51:09 [api_server.py:1044] args: Namespace(subparser='serve', model_tag='/home/sun/models/Qwen3-30B-A3B', config='', host='0.0.0.0', port=8088, uvicorn_log_level='info', disable_uvicorn_access_log=False, allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, lora_modules=None, prompt_adapters=None, chat_template=None, chat_template_content_format='auto', response_role='assistant', ssl_keyfile=None, ssl_certfile=None, ssl_ca_certs=None, enable_ssl_refresh=False, ssl_cert_reqs=0, root_path=None, middleware=[], return_tokens_as_token_ids=False, disable_frontend_multiprocessing=False, enable_r...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: platform cuda. INFO 05-05 23:51:09 [api_server.py:1043] vLLM API server version 0.8.5.post1 INFO 05-05 23:51:09 [api_server.py:1044] args: Namespace(subparser='serve', model_tag='/home/sun/models/Qwen3-30B-A3B', config=...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: .0 --port 8088 --tensor-parallel-size 4 --gpu-memory-utilization 1 --dtype float16 --max-model-len 4096 --max-num-seqs 16 --served-model-name Qwen3-30B-A3B INFO 05-05 23:51:03 [__init__.py:239] Automatically detected pl...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: I used vllm to run Qwen3-30B-A3B and the following error occurred bug;stale ### Your current environment `(vllm) sun@sun-AI:~/anaconda3/envs/vllm/lib/python3.11/site-packages/vllm/model_executor/layers/fused_moe/...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: ]: I used vllm to run Qwen3-30B-A3B and the following error occurred bug;stale ### Your current environment `(vllm) sun@sun-AI:~/anaconda3/envs/vllm/lib/python3.11/site-packages/vllm/model_executor/layers/fused_moe/conf...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 4: /envs/vllm/lib/python3.11/site-packages/vllm/model_executor/layers/fused_moe/configs$ vllm serve /home/sun/models/Qwen3-30B-A3B --no-enable-expert-parallel --host 0.0.0.0 --port 8088 --tensor-parallel-size 4 --gpu-memor...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
