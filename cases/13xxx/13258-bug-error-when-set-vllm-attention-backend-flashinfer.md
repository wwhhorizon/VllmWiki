# vllm-project/vllm#13258: [Bug]: error when set  VLLM_ATTENTION_BACKEND=FLASHINFER

| 字段 | 值 |
| --- | --- |
| Issue | [#13258](https://github.com/vllm-project/vllm/issues/13258) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;fp8;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: error when set  VLLM_ATTENTION_BACKEND=FLASHINFER

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I set `export VLLM_ATTENTION_BACKEND=FLASHINFER` and my start commend here `vllm serve sophosympatheia/Midnight-Miqu-70B-v1.0 --tensor-parallel-size 8 --gpu-memory-utilization .94 --max-model-len 16384 --enable-prefix-caching --kv-cache-dtype fp8 --dtype bfloat16 --max-num-seqs 128 --block-size 32 --enable-chunked-prefill --max-num-batched-tokens 8192` error Appeared `INFO 02-14 03:50:41 api_server.py:528] vLLM API server version 0.6.3.post1 INFO 02-14 03:50:41 api_server.py:529] args: Namespace(subparser='serve', model_tag='sophosympatheia/Midnight-Miqu-70B-v1.0', config='', host=None, port=8000, uvicorn_log_level='info', allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, lora_modules=None, prompt_adapters=None, chat_template=None, response_role='assistant', ssl_keyfile=None, ssl_certfile=None, ssl_ca_certs=None, ssl_cert_reqs=0, root_path=None, middleware=[], return_tokens_as_token_ids=False, disable_frontend_multiprocessing=False, enable_auto_tool_choice=False, tool_call_parser=None, tool_parser_plugin='', model='sophosympatheia/Midnight-Miqu-70B-v1.0', tokenizer=None, s...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 7: fp8 --dtype bfloat16 --max-num-seqs 128 --block-size 32 --enable-chunked-prefill --max-num-batched-tokens 8192` error Appeared `INFO 02-14 03:50:41 api_server.py:528] vLLM API server version 0.6.3.post1 INFO 02-14 03:50...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: utilization .94 --max-model-len 16384 --enable-prefix-caching --kv-cache-dtype fp8 --dtype bfloat16 --max-num-seqs 128 --block-size 32 --enable-chunked-prefill --max-num-batched-tokens 8192` error Appeared `INFO 02-14 0...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: [Bug]: error when set VLLM_ATTENTION_BACKEND=FLASHINFER bug ### Your current environment ### 🐛 Describe the bug I set `export VLLM_ATTENTION_BACKEND=FLASHINFER` and my start commend here `vllm serve sophosympatheia/Midn...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: error Appeared `INFO 02-14 03:50:41 api_server.py:528] vLLM API server version 0.6.3.post1 INFO 02-14 03:50:41 api_server.py:529] args: Namespace(subparser='serve', model_tag='sophosympatheia/Midnight-Miqu-70B-v1.0', co...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 4: u-memory-utilization .94 --max-model-len 16384 --enable-prefix-caching --kv-cache-dtype fp8 --dtype bfloat16 --max-num-seqs 128 --block-size 32 --enable-chunked-prefill --max-num-batched-tokens 8192` error Appeared `INF...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
