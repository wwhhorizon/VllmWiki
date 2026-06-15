# vllm-project/vllm#8330: [Bug]:  vLLM v0.6.0 (CPU) server failed to start on setting VLLM_CPU_OMP_THREADS_BIND

| 字段 | 值 |
| --- | --- |
| Issue | [#8330](https://github.com/vllm-project/vllm/issues/8330) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;quantization;triton |
| 症状 | crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]:  vLLM v0.6.0 (CPU) server failed to start on setting VLLM_CPU_OMP_THREADS_BIND

### Issue 正文摘录

### Your current environment vLLM version: v0.6.0 (CPU) CPU: AMD EPYC 9654 ### 🐛 Describe the bug vLLM v0.6.0 (CPU) server failed to start on setting VLLM_CPU_OMP_THREADS_BIND as shown below: ``` docker run --name vllm -p 8000:8000 -e HUGGING_FACE_HUB_TOKEN=-e VLLM_CPU_KVCACHE_SPACE=40 -e VLLM_CPU_OMP_THREADS_BIND=0-29 -v /mnt/models:/root/.cache/huggingface:rw 121701826775.dkr.ecr.us-east-1.amazonaws.com/cpu/vllm:v0.6.0 --model=microsoft/Phi-3.5-mini-instruct --dtype=bfloat16 --max-model-len=2048 ``` vLLM Error Log: ``` INFO 09-10 08:18:53 importing.py:10] Triton not installed; certain GPU-related functions will not be available. INFO 09-10 08:18:55 api_server.py:495] vLLM API server version 0.6.0 INFO 09-10 08:18:55 api_server.py:496] args: Namespace(host=None, port=8000, uvicorn_log_level='info', allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, lora_modules=None, prompt_adapters=None, chat_template=None, response_role='assistant', ssl_keyfile=None, ssl_certfile=None, ssl_ca_certs=None, ssl_cert_reqs=0, root_path=None, middleware=[], return_tokens_as_token_ids=False, disable_frontend_multiprocessing=False, enable_auto_to...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: setting VLLM_CPU_OMP_THREADS_BIND bug ### Your current environment vLLM version: v0.6.0 (CPU) CPU: AMD EPYC 9654 ### 🐛 Describe the bug vLLM v0.6.0 (CPU) server failed to start on setting VLLM_CPU_OMP_THREADS_BIND as sh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: e, max_prompt_adapters=1, max_prompt_adapter_token=0, device='auto', num_scheduler_steps=1, scheduler_delay_factor=0.0, enable_chunked_prefill=None, speculative_model=None, speculative_model_quantization=None, num_specu...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: .amazonaws.com/cpu/vllm:v0.6.0 --model=microsoft/Phi-3.5-mini-instruct --dtype=bfloat16 --max-model-len=2048 ``` vLLM Error Log: ``` INFO 09-10 08:18:53 importing.py:10] Triton not installed; certain GPU-related functio...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: N=-e VLLM_CPU_KVCACHE_SPACE=40 -e VLLM_CPU_OMP_THREADS_BIND=0-29 -v /mnt/models:/root/.cache/huggingface:rw 121701826775.dkr.ecr.us-east-1.amazonaws.com/cpu/vllm:v0.6.0 --model=microsoft/Phi-3.5-mini-instruct --dtype=bf...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: -len=2048 ``` vLLM Error Log: ``` INFO 09-10 08:18:53 importing.py:10] Triton not installed; certain GPU-related functions will not be available. INFO 09-10 08:18:55 api_server.py:495] vLLM API server version 0.6.0 INFO...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
