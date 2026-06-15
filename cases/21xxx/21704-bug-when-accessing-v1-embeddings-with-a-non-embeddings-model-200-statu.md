# vllm-project/vllm#21704: [Bug]: When accessing /v1/embeddings with a non-embeddings model, 200 status code is returned

| 字段 | 值 |
| --- | --- |
| Issue | [#21704](https://github.com/vllm-project/vllm/issues/21704) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: When accessing /v1/embeddings with a non-embeddings model, 200 status code is returned

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When the model being started is not an embedding model, attempting to access the `/v1/embeddings` api returns 200 status code: ```console (vllm-dev) root@kebe-gpu-dev-0:~/vllm# curl http://127.0.0.1:8000/v1/embeddings -H 'accept: application/json' -H 'Content-Type: application/json' -d '{"model": "abc", "input": "test"}' -v * Trying 127.0.0.1:8000... * Connected to 127.0.0.1 (127.0.0.1) port 8000 (#0) > POST /v1/embeddings HTTP/1.1 > Host: 127.0.0.1:8000 > User-Agent: curl/7.81.0 > accept: application/json > Content-Type: application/json > Content-Length: 33 > * Mark bundle as not supporting multiuse < HTTP/1.1 200 OK < date: Mon, 28 Jul 2025 03:43:13 GMT < server: uvicorn < content-length: 121 < content-type: application/json < * Connection #0 to host 127.0.0.1 left intact {"object":"error","message":"The model does not support Embeddings API","type":"BadRequestError","param":null,"code":400} ``` vllm log: ``` INFO: 127.0.0.1:51396 - "POST /v1/embeddings HTTP/1.1" 200 OK ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of t...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: /embeddings with a non-embeddings model, 200 status code is returned bug;stale ### Your current environment ### 🐛 Describe the bug When the model being started is not an embedding model, attempting to access the `/v1/em...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency Your current environment
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Bug]: When accessing /v1/embeddings with a non-embeddings model, 200 status code is returned bug;stale ### Your current environment ### 🐛 Describe the bug When the model being started is not an embedding model, attempt...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
