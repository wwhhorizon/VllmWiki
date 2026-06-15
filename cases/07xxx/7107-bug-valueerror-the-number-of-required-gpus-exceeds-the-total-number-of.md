# vllm-project/vllm#7107: [Bug]: ValueError: The number of required GPUs exceeds the total number of available GPUs in the cluster.

| 字段 | 值 |
| --- | --- |
| Issue | [#7107](https://github.com/vllm-project/vllm/issues/7107) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: ValueError: The number of required GPUs exceeds the total number of available GPUs in the cluster.

### Issue 正文摘录

### Your current environment [root@localhost wangjianqiang]# python -m vllm.entrypoints.openai.api_server --model /root/wangjianqiang/deepseek-moe/deepseek-coder-33b-base/ --tensor-parallel-size 8 --port 9010 --host 0.0.0.0 --served-model-name deep --gpu-memory-utilization 0.9 --host 0.0.0.0 INFO 08-03 15:45:33 api_server.py:219] vLLM API server version 0.5.3.post1 INFO 08-03 15:45:33 api_server.py:220] args: Namespace(host='0.0.0.0', port=9010, uvicorn_log_level='info', allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, lora_modules=None, prompt_adapters=None, chat_template=None, response_role='assistant', ssl_keyfile=None, ssl_certfile=None, ssl_ca_certs=None, ssl_cert_reqs=0, root_path=None, middleware=[], model='/root/wangjianqiang/deepseek-moe/deepseek-coder-33b-base/', tokenizer=None, skip_tokenizer_init=False, revision=None, code_revision=None, tokenizer_revision=None, tokenizer_mode='auto', trust_remote_code=False, download_dir=None, load_format='auto', dtype='auto', kv_cache_dtype='auto', quantization_param_path=None, max_model_len=None, guided_decoding_backend='outlines', distributed_executor_backend=None, worker_u...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: ired GPUs exceeds the total number of available GPUs in the cluster. bug;stale ### Your current environment [root@localhost wangjianqiang]# python -m vllm.entrypoints.openai.api_server --model /root/wangjianqiang/deepse...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: host='0.0.0.0', port=9010, uvicorn_log_level='info', allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, lora_modules=None, prompt_adapters=None, chat_template=Non...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: localhost wangjianqiang]# python -m vllm.entrypoints.openai.api_server --model /root/wangjianqiang/deepseek-moe/deepseek-coder-33b-base/ --tensor-parallel-size 8 --port 9010 --host 0.0.0.0 --served-model-name deep --gpu...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: ='auto', trust_remote_code=False, download_dir=None, load_format='auto', dtype='auto', kv_cache_dtype='auto', quantization_param_path=None, max_model_len=None, guided_decoding_backend='outlines', distributed_executor_ba...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: auto', quantization_param_path=None, max_model_len=None, guided_decoding_backend='outlines', distributed_executor_backend=None, worker_use_ray=False, pipeline_parallel_size=1, tensor_parallel_size=8, max_parallel_loadin...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
