# vllm-project/vllm#15942: [Bug]: Out of Memory in Concurrent Request v0.6.1 vs [v0.7.* and v0.8.*]

| 字段 | 值 |
| --- | --- |
| Issue | [#15942](https://github.com/vllm-project/vllm/issues/15942) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | activation_norm;attention_kv_cache;distributed_parallel;frontend_api;model_support;sampling_logits;scheduler_memory |
| 子分类 | memory |
| Operator 关键词 | cache;cuda |
| 症状 | build_error;crash;oom;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Out of Memory in Concurrent Request v0.6.1 vs [v0.7.* and v0.8.*]

### Issue 正文摘录

Hello, I started encountering out-of-memory (OOM) errors when processing a certain number of requests on versions 0.7.*, and 0.8.*. When this happens, the server crashes. It seems like the queueing mechanism is not working properly. I tested both V0 and V1 engines in these versions, but the issue persists. However, with the same model and generation parameters, v0.6.1 works flawlessly and queues incoming requests as expected. Details: Average Input Tokens: 2K-3K Average Output Tokens: 1K-3K GPU : 2xH100 Model Parameters: disable_log_requests: True enforce_eager: True distributed_executor_backend: ray gpu_memory_utilization: 0.99 max_model_len: 32768 max_num_seqs: 200 Could you provide any insights into why this is happening and if there are any potential fixes? Thanks! ### 🐛 Describe the bug **In v0.6.1** [2025-04-02 12:38:43] llm_service.py:420 INFO: Params: {'max_tokens': 3000, 'temperature': 0} [2025-04-02 12:38:43] uvicorn.access INFO: https://127.0.0.1:39490 - "POST /v3/generate HTTP/1.1" 200 [2025-04-02 12:38:43] llm_service.py:420 INFO: Params: {'max_tokens': 3000, 'temperature': 0} [2025-04-02 12:38:43] uvicorn.access INFO: https://127.0.0.1:39504 - "POST /v3/generate HTTP...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: t-of-memory (OOM) errors when processing a certain number of requests on versions 0.7.*, and 0.8.*. When this happens, the server crashes. It seems like the queueing mechanism is not working properly. I tested both V0 a...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Bug]: Out of Memory in Concurrent Request v0.6.1 vs [v0.7.* and v0.8.*] bug;stale Hello, I started encountering out-of-memory (OOM) errors when processing a certain number of requests on versions 0.7.*, and 0.8.*. When...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: When this happens, the server crashes. It seems like the queueing mechanism is not working properly. I tested both V0 and V1 engines in these versions, but the issue persists. However, with the same model and generation...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: .7.* and v0.8.*] bug;stale Hello, I started encountering out-of-memory (OOM) errors when processing a certain number of requests on versions 0.7.*, and 0.8.*. When this happens, the server crashes. It seems like the que...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ngines in these versions, but the issue persists. However, with the same model and generation parameters, v0.6.1 works flawlessly and queues incoming requests as expected. Details: Average Input Tokens: 2K-3K Average Ou...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
