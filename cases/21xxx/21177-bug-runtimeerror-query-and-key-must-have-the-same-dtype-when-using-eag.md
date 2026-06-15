# vllm-project/vllm#21177: [Bug]: RuntimeError: query and key must have the same dtype when using Eagle3 speculative decoding with kv-cache-dtype fp8

| 字段 | 值 |
| --- | --- |
| Issue | [#21177](https://github.com/vllm-project/vllm/issues/21177) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;frontend_api;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;fp8;operator;quantization;sampling |
| 症状 | build_error;crash;mismatch |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: RuntimeError: query and key must have the same dtype when using Eagle3 speculative decoding with kv-cache-dtype fp8

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When using Eagle3 speculative decoding and kv-cache-dtype fp8, inference requests fail with a 500 error. The logs show: ``` RuntimeError: query and key must have the same dtype ``` The stack trace references `torch.ops.vllm.unified_attention_with_output` and `flash_attn_varlen_func`. **Environment:** - vllm/vllm-openai:v0.9.2 - Command: ``` docker run --gpus all vllm/vllm-openai:v0.9.2 --model meta-llama/Llama-3.1-8B-Instruct --max-model-len 10000 --swap-space 4 --dtype auto --enable-chunked-prefill --disable-log-requests --enable-prefix-caching --port 8081 --max-num-seqs 72 --quantization fp8 --max-num-batched-tokens 1024 --kv-cache-dtype fp8 --speculative-config '{"method": "eagle3", "model": "yuhuili/EAGLE3-LLaMA3.1-Instruct-8B", "num_speculative_tokens": 5, "draft_tensor_parallel_size": 1}' ``` **Full logs and context:** ``` INFO: Started server process [1] INFO: Waiting for application startup. INFO: Application startup complete. INFO: 172.17.0.1:58176 - "POST /v1/completions HTTP/1.1" 400 Bad Request INFO: 172.17.0.1:45166 - "POST /v1/completions HTTP/1.1" 400 Bad Request ERROR 07-18 03:16:02 [dump_input.py:69] Dumping inpu...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 8: : RuntimeError: query and key must have the same dtype when using Eagle3 speculative decoding with kv-cache-dtype fp8 bug;stale ### Your current environment ### 🐛 Describe the bug When using Eagle3 speculative decoding...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: en_func`. **Environment:** - vllm/vllm-openai:v0.9.2 - Command: ``` docker run --gpus all vllm/vllm-openai:v0.9.2 --model meta-llama/Llama-3.1-8B-Instruct --max-model-len 10000 --swap-space 4 --dtype auto --enable-chunk...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: [Bug]: RuntimeError: query and key must have the same dtype when using Eagle3 speculative decoding with kv-cache-dtype fp8 bug;stale ### Your current environment ### 🐛 Describe the bug When using Eagle3 speculative deco...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: 0.9.2 - Command: ``` docker run --gpus all vllm/vllm-openai:v0.9.2 --model meta-llama/Llama-3.1-8B-Instruct --max-model-len 10000 --swap-space 4 --dtype auto --enable-chunked-prefill --disable-log-requests --enable-pref...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: kv_cache_dtype=fp8, device_config=cuda, decoding_config=DecodingConfig(backend='auto', disable_fallback=False, disable_any_whitespace=False, disable_additional_properties=False, reasoning_backend=''), observability_conf...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
