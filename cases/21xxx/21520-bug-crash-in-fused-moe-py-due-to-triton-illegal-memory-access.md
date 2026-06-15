# vllm-project/vllm#21520: [Bug]: Crash in fused_moe.py due to Triton illegal memory access

| 字段 | 值 |
| --- | --- |
| Issue | [#21520](https://github.com/vllm-project/vllm/issues/21520) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;kernel;moe;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Crash in fused_moe.py due to Triton illegal memory access

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ```text vllm serve deepseek-ai/DeepSeek-V2-Lite-Chat --trust-remote-code -tp 1 --served-model-name deepseek-r1 DeepSeek-R1 --gpu-memory-utilization 0.8 --enforce-eager --port 30000 curl --location 'http://127.0.0.1:30000/v1/chat/completions' --header 'Content-Type: application/json' --data '{ "stream":false, "messages": [ { "role": "user", "content": "hi" } ], "model": "deepseek-r1" }' ``` ```text INFO 07-24 11:08:25 [core.py:194] init engine (profile, create kv cache, warmup model) took 33.27 seconds INFO 07-24 11:08:26 [loggers.py:141] Engine 000: vllm cache_config_info with initialization after num_gpu_blocks is: 42180 WARNING 07-24 11:08:26 [config.py:1529] Default sampling parameters have been overridden by the model's Hugging Face generation config recommended from the model creator. If this is not intended, please relaunch vLLM instance with `--generation-config vllm`. INFO 07-24 11:08:26 [serving_responses.py:89] Using default chat sampling params from model: {'temperature': 0.3, 'top_p': 0.95} INFO 07-24 11:08:26 [serving_chat.py:125] Using default chat sampling params from model: {'temperature': 0.3, 'top_p': 0.95} INFO...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: trics, Methods: GET INFO: Started server process [2684567] INFO: Waiting for application startup. INFO: Application startup complete. INFO 07-24 11:08:40 [chat_utils.py:473] Detected the chat template content format to...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: e: /v1/models, Methods: GET INFO 07-24 11:08:26 [launcher.py:37] Route: /version, Methods: GET INFO 07-24 11:08:26 [launcher.py:37] Route: /v1/responses, Methods: POST INFO 07-24 11:08:26 [launcher.py:37] Route: /v1/res...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: : /v2/rerank, Methods: POST INFO 07-24 11:08:26 [launcher.py:37] Route: /scale_elastic_ep, Methods: POST INFO 07-24 11:08:26 [launcher.py:37] Route: /is_scaling_elastic_ep, Methods: POST INFO 07-24 11:08:26 [launcher.py...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: [Bug]: Crash in fused_moe.py due to Triton illegal memory access bug ### Your current environment ### 🐛 Describe the bug ```text vllm serve deepseek-ai/DeepSeek-V2-Lite-Chat --trust-remote-code -tp 1 --served-model-name...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 4: [Bug]: Crash in fused_moe.py due to Triton illegal memory access bug ### Your current environment ### 🐛 Describe the bug ```text vllm serve deepseek-ai/DeepSeek-V2-Lite-Chat --trust-remote-code -tp 1 --served-model-name...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
