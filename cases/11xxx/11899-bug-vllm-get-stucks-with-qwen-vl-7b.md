# vllm-project/vllm#11899: [Bug]: VLLM get stucks with Qwen VL 7B

| 字段 | 值 |
| --- | --- |
| Issue | [#11899](https://github.com/vllm-project/vllm/issues/11899) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | activation_norm;attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;multimodal_vlm;quantization |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;fp8;kernel;quantization |
| 症状 | oom |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: VLLM get stucks with Qwen VL 7B

### Issue 正文摘录

### Your current environment I'm using ["v0.6.5"] of VLLM. When I try to launch Qwen VL 7B with 100% of the GPU (24GB VRAM) it's ok. Then even if the model is only 4GB when I reduce to a little bit less the launch of VLLM is getting stuck by printing an endless: 'INFO: 127.0.0.6:XXX - "GET /metrics HTTP/1.1" 200 OK' I'm confused because I know that I have enough space for the model. ``` vllm serve Qwen/Qwen2-VL-7B-Instruct-AWQ --trust-remote-code --enable-chunked-prefill --max_model_len 4096 --quantization awq_marlin --gpu_memory_utilization=0.8 --max-num-batched-tokens 4097 --kv-cache-dtype fp8_e4m3 ``` ### Model Input Dumps _No response_ ### 🐛 Describe the bug INFO 01-09 06:23:59 api_server.py:651] vLLM API server version 0.6.5 INFO 01-09 06:23:59 api_server.py:652] args: Namespace(subparser='serve', model_tag='Qwen/Qwen2-VL-7B-Instruct-AWQ', config='', host=None, port=8000, uvicorn_log_level='info', allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, lora_modules=None, prompt_adapters=None, chat_template=None, chat_template_content_format='auto', response_role='assistant', ssl_keyfile=None, ssl_certfile=None, ssl_ca_certs=...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 7: [Bug]: VLLM get stucks with Qwen VL 7B bug ### Your current environment I'm using ["v0.6.5"] of VLLM. When I try to launch Qwen VL 7B with 100% of the GPU (24GB VRAM) it's ok. Then even if the model is only 4GB when I r...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: Describe the bug INFO 01-09 06:23:59 api_server.py:651] vLLM API server version 0.6.5 INFO 01-09 06:23:59 api_server.py:652] args: Namespace(subparser='serve', model_tag='Qwen/Qwen2-VL-7B-Instruct-AWQ', config='', host=...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: serve Qwen/Qwen2-VL-7B-Instruct-AWQ --trust-remote-code --enable-chunked-prefill --max_model_len 4096 --quantization awq_marlin --gpu_memory_utilization=0.8 --max-num-batched-tokens 4097 --kv-cache-dtype fp8_e4m3 ``` ##...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 5: awq_marlin --gpu_memory_utilization=0.8 --max-num-batched-tokens 4097 --kv-cache-dtype fp8_e4m3 ``` ### Model Input Dumps _No response_ ### 🐛 Describe the bug INFO 01-09 06:23:59 api_server.py:651] vLLM API server versi...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: e4m3', quantization_param_path=None, max_model_len=4096, guided_decoding_backend='xgrammar', logits_processor_pattern=None, distributed_executor_backend=None, worker_use_ray=False, pipeline_parallel_size=1, tensor_paral...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
