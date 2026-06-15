# vllm-project/vllm#11250: [Bug]: Hermes tool choice can not supprot format 'string'

| 字段 | 值 |
| --- | --- |
| Issue | [#11250](https://github.com/vllm-project/vllm/issues/11250) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 12; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Hermes tool choice can not supprot format 'string'

### Issue 正文摘录

### Your current environment ### Model Input Dumps vllm serve /model/models/calme-3.2-instruct-78b/ --guided-decoding-backend xgrammar --block-size 32 --max-num-seqs 100 --port xxxxxxxxxx --api-key xxxxxxxxxxxxxxxx -tp 8 --served-model-name Qwen2.5-72B-Instruct --dtype float16 --max-model-len 65536 --enable-chunked-prefill false --seed 818 --multi-step-stream-outputs true --enable-auto-tool-choice --tool-call-parser hermes --tokenizer-pool-size 50 ### 🐛 Describe the bug INFO 12-17 04:39:28 llm_engine.py:446] init engine (profile, create kv cache, warmup model) took 119.34 seconds INFO 12-17 04:39:28 api_server.py:578] Using supplied chat template: INFO 12-17 04:39:28 api_server.py:578] None INFO 12-17 04:39:28 serving_chat.py:74] "auto" tool choice has been enabled please note that while the parallel_tool_calls client option is preset for compatibility reasons, it will be ignored. INFO 12-17 04:39:28 launcher.py:19] Available routes are: INFO 12-17 04:39:28 launcher.py:27] Route: /openapi.json, Methods: GET, HEAD INFO 12-17 04:39:28 launcher.py:27] Route: /docs, Methods: GET, HEAD INFO 12-17 04:39:28 launcher.py:27] Route: /docs/oauth2-redirect, Methods: GET, HEAD INFO 12-17 04:39...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: te: /v1/models, Methods: GET INFO 12-17 04:39:28 launcher.py:27] Route: /version, Methods: GET INFO 12-17 04:39:28 launcher.py:27] Route: /v1/chat/completions, Methods: POST INFO 12-17 04:39:28 launcher.py:27] Route: /v...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: Hermes tool choice can not supprot format 'string' bug;stale ### Your current environment ### Model Input Dumps vllm serve /model/models/calme-3.2-instruct-78b/ --guided-decoding-backend xgrammar --block-size 32...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Bug]: Hermes tool choice can not supprot format 'string' bug;stale ### Your current environment ### Model Input Dumps vllm serve /model/models/calme-3.2-instruct-78b/ --guided-decoding-backend xgrammar --block-size 32...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: del/models/calme-3.2-instruct-78b/ --guided-decoding-backend xgrammar --block-size 32 --max-num-seqs 100 --port xxxxxxxxxx --api-key xxxxxxxxxxxxxxxx -tp 8 --served-model-name Qwen2.5-72B-Instruct --dtype float16 --max-...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: umps vllm serve /model/models/calme-3.2-instruct-78b/ --guided-decoding-backend xgrammar --block-size 32 --max-num-seqs 100 --port xxxxxxxxxx --api-key xxxxxxxxxxxxxxxx -tp 8 --served-model-name Qwen2.5-72B-Instruct --d...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
