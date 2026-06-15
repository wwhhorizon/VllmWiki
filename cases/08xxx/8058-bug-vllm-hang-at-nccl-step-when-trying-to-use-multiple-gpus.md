# vllm-project/vllm#8058: [Bug]: vLLM hang at nccl step when trying to use multiple GPUs

| 字段 | 值 |
| --- | --- |
| Issue | [#8058](https://github.com/vllm-project/vllm/issues/8058) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | latency_reg |
| Operator 关键词 | cuda;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;crash;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vLLM hang at nccl step when trying to use multiple GPUs

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When trying to run `VLLM_LOGGING_LEVEL=DEBUG CUDA_LAUNCH_BLOCKING=1 NCCL_DEBUG=TRACE VLLM_TRACE_FUNCTION=1 CUDA_VISIBLE_DEVICES=0,1 vllm serve Qwen/Qwen2-72B-Instruct-AWQ --max-model-len=20480 --max-num-seqs=1 --gpu-memory-utilization=0.98 --trust-remote-code --tensor-parallel-size 2`, output of the program shows: ``` /scratch/banghao2/miniforge3/envs/spin/lib/python3.10/site-packages/transformers/utils/hub.py:127: FutureWarning: Using `TRANSFORMERS_CACHE` is deprecated and will be removed in v5 of Transformers. Use `HF_HOME` instead. warnings.warn( INFO 08-31 09:50:38 api_server.py:440] vLLM API server version 0.5.5 INFO 08-31 09:50:38 api_server.py:441] args: Namespace(model_tag='Qwen/Qwen2-72B-Instruct-AWQ', host=None, port=8000, uvicorn_log_level='info', allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, lora_modules=None , prompt_adapters=None, chat_template=None, response_role='assistant', ssl_keyfile=None, ssl_certfile=None, ssl_ca_certs=None, ssl_cert_reqs=0, root_path=None, middleware=[], return_tokens_as_token_ids=False, disable_frontend_multiprocessing=False, mod...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: , max_prompt_adapters=1, max_prompt_adapter_token =0, device='auto', num_scheduler_steps=1, scheduler_delay_factor=0.0, enable_chunked_prefill=None, speculative_model=None, speculative_model_quantization=None, num_specu...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: CL_DEBUG=TRACE VLLM_TRACE_FUNCTION=1 CUDA_VISIBLE_DEVICES=0,1 vllm serve Qwen/Qwen2-72B-Instruct-AWQ --max-model-len=20480 --max-num-seqs=1 --gpu-memory-utilization=0.98 --trust-remote-code --tensor-parallel-size 2`, ou...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: warnings.warn( INFO 08-31 09:50:38 api_server.py:440] vLLM API server version 0.5.5 INFO 08-31 09:50:38 api_server.py:441] args: Namespace(model_tag='Qwen/Qwen2-72B-Instruct-AWQ', host=None, port=8000, uvicorn_log_level...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: to', quantization_param_path=No ne, max_model_len=20480, guided_decoding_backend='outlines', distributed_executor_backend=None, worker_use_ray=False, pipeline_parallel_size=1, tensor_parallel_size=2, max_parallel_loadin...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: e='auto', trust_remote_code=True, download_dir=None, load_format='auto', dtype='auto', kv_cache_dtype='auto', quantization_param_path=No ne, max_model_len=20480, guided_decoding_backend='outlines', distributed_executor_...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
