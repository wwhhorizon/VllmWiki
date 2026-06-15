# vllm-project/vllm#11828: [Bug]: Using  "response_format": { "type": "json_object" } with /v1/chat/completions is terminating the engine

| 字段 | 值 |
| --- | --- |
| Issue | [#11828](https://github.com/vllm-project/vllm/issues/11828) |
| 状态 | closed |
| 标签 | bug;structured-output;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | throughput |
| Operator 关键词 | cache;cuda;operator;sampling |
| 症状 | build_error;crash;slowdown |
| 根因提示 | env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Using  "response_format": { "type": "json_object" } with /v1/chat/completions is terminating the engine

### Issue 正文摘录

### Your current environment ### Model Input Dumps API Request: POST: localhost/v1/chat/completions { "model": "meta-llama/Meta-Llama-3-8B-Instruct", "messages": [ { "role": "system", "content": "You are a JSON Response AI assistant. You are assisting the customer with their Mobile Number Verification journey for the Personal Loan product. You always have to generate only a mentioned JSON response based on the flow. The JSON format should always be: {'status':'','mobile_no':''}. All these JSON response parameters are decided based on the conversation. The JSON keys for: status will be either SUCCESS or OTHER. When the customer provides a response, follow these steps: First, check if the response contains a mobile number or anything similar. If the response includes digits, even with spaces between them, extract the entire number. Assign the extracted number to the mobile_no variable and set the status to SUCCESS. Remember that for each and every query you should always provide the exact only a mentioned JSON format as response dont add any extra words like Here is the JSON response: need only json which contains all the fields : {'status':'','mobile_no':''}. " } ], "temperature":...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: ith /v1/chat/completions is terminating the engine bug;structured-output;stale ### Your current environment ### Model Input Dumps API Request: POST: localhost/v1/chat/completions { "model": "meta-llama/Meta-Llama-3-8B-I...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: : {'status':'','mobile_no':''}. All these JSON response parameters are decided based on the conversation. The JSON keys for: status will be either SUCCESS or OTHER. When the customer provides a response, follow these st...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: Using "response_format": { "type": "json_object" } with /v1/chat/completions is terminating the engine bug;structured-output;stale ### Your current environment ### Model Input Dumps API Request: POST: localhost/v...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: "type": "json_object" }, "top_p": 1, "n": 1, "stream": false, "max_tokens": 30, "presence_penalty": 0, "frequency_penalty": 0 } Logs : INFO 01-08 03:22:32 metrics.py:345] Avg prompt throughput: 0.0 tokens/s, Avg generat...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: e heartbeat thread (RayWorkerWrapper pid=10020) [W108 02:51:49.764772246 CUDAAllocatorConfig.h:28] Warning: expandable_segments not supported on this platform (function operator()) [repeated 2x across cluster] (RayWorke...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
