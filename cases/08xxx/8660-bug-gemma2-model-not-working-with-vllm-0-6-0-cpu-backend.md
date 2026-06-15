# vllm-project/vllm#8660: [Bug]: Gemma2 model not working with vLLM 0.6.0 CPU backend

| 字段 | 值 |
| --- | --- |
| Issue | [#8660](https://github.com/vllm-project/vllm/issues/8660) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits |
| 子分类 | env_compat |
| Operator 关键词 | attention;cuda;quantization;triton |
| 症状 | crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Gemma2 model not working with vLLM 0.6.0 CPU backend

### Issue 正文摘录

### Your current environment - vLLM CPU : v0.6.0 - Hardware: Intel(R) Xeon(R) Platinum 8480+ CPU - Model: google/gemma-2-2b ### 🐛 Describe the bug vLLM v0.6.0 (cpu) is throwing below error on loading Gemma2 model. Run vLLM: ``` docker run -p 8000:8000 -e HUGGING_FACE_HUB_TOKEN= -e VLLM_CPU_KVCACHE_SPACE=40 -v /mnt/models:/root/.cache/huggingface:rw cpu/vllm:v0.6.0 --model=google/gemma-2-2b --dtype=float32 --max-model-len=2048 ``` ``` INFO 09-20 08:05:38 importing.py:10] Triton not installed; certain GPU-related functions will not be available. INFO 09-20 08:05:40 api_server.py:495] vLLM API server version 0.6.0 INFO 09-20 08:05:40 api_server.py:496] args: Namespace(host=None, port=8000, uvicorn_log_level='info', allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, lora_modules=None, prompt_adapters=None, chat_template=None, response_role='assistant', ssl_keyfile=None, ssl_certfile=None, ssl_ca_certs=None, ssl_cert_reqs=0, root_path=None, middleware=[], return_tokens_as_token_ids=False, disable_frontend_multiprocessing=False, enable_auto_tool_choice=False, tool_call_parser=None, model='google/gemma-2-2b', tokenizer=None, skip_t...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 8: [Bug]: Gemma2 model not working with vLLM 0.6.0 CPU backend bug;stale ### Your current environment - vLLM CPU : v0.6.0 - Hardware: Intel(R) Xeon(R) Platinum 8480+ CPU - Model: google/gemma-2-2b ### 🐛 Describe the bug vL...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: .0 (cpu) is throwing below error on loading Gemma2 model. Run vLLM: ``` docker run -p 8000:8000 -e HUGGING_FACE_HUB_TOKEN= -e VLLM_CPU_KVCACHE_SPACE=40 -v /mnt/models:/root/.cache/huggingface:rw cpu/vllm:v0.6.0 --model=...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 6: :/root/.cache/huggingface:rw cpu/vllm:v0.6.0 --model=google/gemma-2-2b --dtype=float32 --max-model-len=2048 ``` ``` INFO 09-20 08:05:38 importing.py:10] Triton not installed; certain GPU-related functions will not be av...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: [Bug]: Gemma2 model not working with vLLM 0.6.0 CPU backend bug;stale ### Your current environment - vLLM CPU : v0.6.0 - Hardware: Intel(R) Xeon(R) Platinum 8480+ CPU - Model: google/gemma-2-2b ### 🐛 Describe the bug vL...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: [Bug]: Gemma2 model not working with vLLM 0.6.0 CPU backend bug;stale ### Your current environment - vLLM CPU : v0.6.0 - Hardware: Intel(R) Xeon(R) Platinum 8480+ CPU - Model: google/gemma-2-2b ### 🐛 Describe the bug vL...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
