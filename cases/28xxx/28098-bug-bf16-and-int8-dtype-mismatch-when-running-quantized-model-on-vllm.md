# vllm-project/vllm#28098: [Bug]: BF16 and INT8 dtype mismatch when running quantized model on vLLM

| 字段 | 值 |
| --- | --- |
| Issue | [#28098](https://github.com/vllm-project/vllm/issues/28098) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;fp8;kernel;moe;operator;quantization;sampling;triton |
| 症状 | build_error;crash;mismatch;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: BF16 and INT8 dtype mismatch when running quantized model on vLLM

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug **Command Used:-** `python -m vllm.entrypoints.openai.api_server \ --model deepseek-moe-16b-base-int8-Dynamic \ --no-enable-chunked-prefill \ --no-enable-prefix-caching \ --gpu-memory-utilization 0.9 \ --trust_remote_code ` **Description :-** I quantized the model deepseek-ai/deepseek-moe-16b-base using LLM Compressor with INT8 dynamic quantization. The quantization process completed successfully, and the quantized model directory was generated correctly. However, when I try to serve this quantized model using vllm.entrypoints.openai.api_server, I encounter a runtime error related to a data type mismatch between BF16 and INT8 operands. **Error Message** INFO 11-05 10:41:13 [__init__.py:216] Automatically detected platform cuda. (APIServer pid=429482) INFO 11-05 10:41:14 [api_server.py:1839] vLLM API server version 0.11.0 (APIServer pid=429482) INFO 11-05 10:41:14 [utils.py:233] non-default args: {'model': '/data/users/logesh/llm-compressor/examples/quantization_w8a8_fp8/deepseek-moe-16b-base-FP8-Dynamic', 'trust_remote_code': True, 'enable_prefix_caching': False, 'enable_chunked_prefill': False} (APIServer pid=429482) The argumen...

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 7: o, device_config=cuda, structured_outputs_config=StructuredOutputsConfig(backend='auto', disable_fallback=False, disable_any_whitespace=False, disable_additional_properties=False, reasoning_parser=''), observability_con...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 7: [Bug]: BF16 and INT8 dtype mismatch when running quantized model on vLLM bug;stale ### Your current environment ### 🐛 Describe the bug **Command Used:-** `python -m vllm.entrypoints.openai.api_server \ --model deepsee
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: ver pid=429482) INFO 11-05 10:41:14 [api_server.py:1839] vLLM API server version 0.11.0 (APIServer pid=429482) INFO 11-05 10:41:14 [utils.py:233] non-default args: {'model': '/data/users/logesh/llm-compressor/examples/q...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: ]: BF16 and INT8 dtype mismatch when running quantized model on vLLM bug;stale ### Your current environment ### 🐛 Describe the bug **Command Used:-** `python -m vllm.entrypoints.openai.api_server \ --model deepseek-moe-...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 4: ** `python -m vllm.entrypoints.openai.api_server \ --model deepseek-moe-16b-base-int8-Dynamic \ --no-enable-chunked-prefill \ --no-enable-prefix-caching \ --gpu-memory-utilization 0.9 \ --trust_remote_code ` **Descripti...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
