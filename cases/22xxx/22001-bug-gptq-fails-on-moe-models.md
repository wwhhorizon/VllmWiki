# vllm-project/vllm#22001: [Bug]: GPTQ fails on MoE models

| 字段 | 值 |
| --- | --- |
| Issue | [#22001](https://github.com/vllm-project/vllm/issues/22001) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;kernel;moe;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: GPTQ fails on MoE models

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug vllm fails to start when serving GPTQ quantized Qwen3 MoE models. What's weird is that serving GPTQ Qwen3 dense model is OK. Or, serving Qwen3 MoE model without quantization is also OK. INFO 07-31 08:25:38 [__init__.py:241] Automatically detected platform rocm. (APIServer pid=296) INFO 07-31 08:25:42 [api_server.py:1774] vLLM API server version 0.10.1.dev235+g055bd3978 (APIServer pid=296) INFO 07-31 08:25:42 [utils.py:326] non-default args: {'model_tag': '/models/Qwen3-30B-A3B-GPTQ-Int4/', 'model': '/models/Qwen3-30B-A3B-GPTQ-Int4/', 'max_model_len': 8192} (APIServer pid=296) INFO 07-31 08:25:50 [config.py:713] Resolved architecture: Qwen3MoeForCausalLM (APIServer pid=296) INFO 07-31 08:25:50 [config.py:1716] Using max model len 8192 (APIServer pid=296) WARNING 07-31 08:25:50 [config.py:1171] gptq quantization is not fully optimized yet. The speed can be slower than non-quantized models. (APIServer pid=296) INFO 07-31 08:25:51 [config.py:2542] Chunked prefill is enabled with max_num_batched_tokens=2048. INFO 07-31 08:25:56 [__init__.py:241] Automatically detected platform rocm. INFO 07-31 08:25:59 [core.py:605] Waiting for init m...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: [Bug]: GPTQ fails on MoE models bug;stale ### Your current environment ### 🐛 Describe the bug vllm fails to start when serving GPTQ quantized Qwen3 MoE models. What's weird is that serving GPTQ Qwen3 dense model is OK....
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: Server pid=296) INFO 07-31 08:25:42 [api_server.py:1774] vLLM API server version 0.10.1.dev235+g055bd3978 (APIServer pid=296) INFO 07-31 08:25:42 [utils.py:326] non-default args: {'model_tag': '/models/Qwen3-30B-A3B-GPT...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: onment ### 🐛 Describe the bug vllm fails to start when serving GPTQ quantized Qwen3 MoE models. What's weird is that serving GPTQ Qwen3 dense model is OK. Or, serving Qwen3 MoE model without quantization is also OK. INF...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: kv_cache_dtype=auto, device_config=cuda, decoding_config=DecodingConfig(backend='auto', disable_fallback=False, disable_any_whitespace=False, disable_additional_properties=False, reasoning_backend=''), observability_con...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: GPTQ fails on MoE models bug;stale ### Your current environment ### 🐛 Describe the bug vllm fails to start when serving GPTQ quantized Qwen3 MoE models. What's weird is that serving GPTQ Qwen3 dense model is OK....

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
