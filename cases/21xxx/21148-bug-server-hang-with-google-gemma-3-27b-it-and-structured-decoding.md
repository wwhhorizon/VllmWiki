# vllm-project/vllm#21148: [Bug]: Server hang with google/gemma-3-27b-it and structured decoding

| 字段 | 值 |
| --- | --- |
| Issue | [#21148](https://github.com/vllm-project/vllm/issues/21148) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | activation_norm;attention_kv_cache;distributed_parallel;frontend_api;model_support;moe;multimodal_vlm;quantization;sampling_logits;scheduler_memory |
| 子分类 | cold_start |
| Operator 关键词 | activation;attention;cache;cuda;quantization;sampling |
| 症状 | slowdown |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Server hang with google/gemma-3-27b-it and structured decoding

### Issue 正文摘录

### Your current environment (see repro info below) ### 🐛 Describe the bug With the `google/gemma-3-27b-it` model, if I request a JSON formatted response, only a couple of tokens are generated before the request hangs. Subsequent requests to the server then all hang as well even after cancelling the first hung request (and vLLM logging that it aborted the request). To reproduce, simply run the server: ``` vllm serve google/gemma-3-27b-it --max-model-len 32000 --max-num-seqs 16 --enforce-eager ``` and send a request with JSON structured output: ``` curl --request POST 'http://localhost:8000/v1/chat/completions' -H 'Content-Type: application/json' -H 'Accept: application/json' --data-raw '{ "model": "google/gemma-3-27b-it", "stream": true, "response_format": {"type": "json_object"}, "messages": [ { "role": "user", "content": [ { "type": "text", "text": "Generate a sample JSON document." } ] } ] }' ``` I ran the repro against recent past versions of vLLM (and deps) as well and found: - this worked fine back in v0.8.4 - in v0.8.5 and v0.8.5.post1, the response streams empty tokens and logs an interesting warning indicating that there are no tokens that match the guide: > ERROR 07-17 2...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: Server hang with google/gemma-3-27b-it and structured decoding bug;stale ### Your current environment (see repro info below) ### 🐛 Describe the bug With the `google/gemma-3-27b-it` model, if I request a JSON form...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: > ERROR 07-17 22:03:54 [backend_xgrammar.py:167] Failed to advance FSM for request chatcmpl-78eca22187e24416a39e4c12c73dad75 for tokens 0. Please file an issue. - for v0.9.0 and later, it streams 1 token and then hangs...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: Bug]: Server hang with google/gemma-3-27b-it and structured decoding bug;stale ### Your current environment (see repro info below) ### 🐛 Describe the bug With the `google/gemma-3-27b-it` model, if I request a JSON forma...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: } ] } ] }' ``` I ran the repro against recent past versions of vLLM (and deps) as well and found: - this worked fine back in v0.8.4 - in v0.8.5 and v0.8.5.post1, the response streams empty tokens and logs an interesting...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: cache;distributed_parallel;frontend_api;model_support;moe;multimodal_vlm;quantization;sampling_logits;scheduler_memory activation;attention;cache;cuda;quantization;sampling slowdown dtype;env_dependency;shape Your curre...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
