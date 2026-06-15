# vllm-project/vllm#9243: [Bug]: vllm0.6.2  Using FLASHINFER to start VLLM reported an error, enabling -- quantification gptq -- kv cache dtype fp8_e5m2

| 字段 | 值 |
| --- | --- |
| Issue | [#9243](https://github.com/vllm-project/vllm/issues/9243) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;distributed_parallel;frontend_api;model_support;quantization |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;fp8;quantization;triton |
| 症状 | crash;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vllm0.6.2  Using FLASHINFER to start VLLM reported an error, enabling -- quantification gptq -- kv cache dtype fp8_e5m2

### Issue 正文摘录

Using FLASHINFER to start VLLM reported an error, enabling -- quantification gptq -- kv cache dtype fp8_e5m2 Start command: python3 -m vllm.entrypoints.openai.api_server --host 0.0.0.0 --port 7807 --model /mnt/home/Qwen2.5-14B-Instruct-GPTQ-Int4 --trust-remote-code --served-model-name Qwen --gpu-memory-utilization 0.9 --tensor-parallel-size 2 --enforce-eager --max-model-len 8192 --quantization gptq --kv-cache-dtype fp8_e5m2 Can start, but remind me of the following information: ``` (VllmWorkerProcess pid=530898) INFO 10-10 11:12:03 selector.py:227] Cannot use FlashAttention-2 backend for FP8 KV cache. (VllmWorkerProcess pid=530898) WARNING 10-10 11:12:03 selector.py:229] Please use FlashInfer backend with FP8 KV Cache for better performance by setting environment variable VLLM_ATTENTION_BACKEND=FLASHINFER ``` So, there are the following settings: export VLLM_ATTENTION_BACKEND=FLASHINFER After setting, using the same command, an error occurs: ``` INFO 10-10 18:38:58 api_server.py:526] vLLM API server version 0.6.1.dev238+ge2c6e0a82 INFO 10-10 18:38:58 api_server.py:527] args: Namespace(host='0.0.0.0', port=7807, uvicorn_log_level='info', allow_credentials=False, allowed_origins=['*...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 8: an error, enabling -- quantification gptq -- kv cache dtype fp8_e5m2 bug;stale Using FLASHINFER to start VLLM reported an error, enabling -- quantification gptq -- kv cache dtype fp8_e5m2 Start command: python3 -m vllm....
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: vllm0.6.2 Using FLASHINFER to start VLLM reported an error, enabling -- quantification gptq -- kv cache dtype fp8_e5m2 bug;stale Using FLASHINFER to start VLLM reported an error, enabling -- quantification gptq -- kv ca...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 5: NFER to start VLLM reported an error, enabling -- quantification gptq -- kv cache dtype fp8_e5m2 bug;stale Using FLASHINFER to start VLLM reported an error, enabling -- quantification gptq -- kv cache dtype fp8_e5m2 Sta...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: [Bug]: vllm0.6.2 Using FLASHINFER to start VLLM reported an error, enabling -- quantification gptq -- kv cache dtype fp8_e5m2 bug;stale Using FLASHINFER to start VLLM reported an error, enabling -- quantification gptq -...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: rror occurs: ``` INFO 10-10 18:38:58 api_server.py:526] vLLM API server version 0.6.1.dev238+ge2c6e0a82 INFO 10-10 18:38:58 api_server.py:527] args: Namespace(host='0.0.0.0', port=7807, uvicorn_log_level='info', allow_c...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
