# vllm-project/vllm#18489: [Bug]: SharedStorageConnector does not load KV cache

| 字段 | 值 |
| --- | --- |
| Issue | [#18489](https://github.com/vllm-project/vllm/issues/18489) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: SharedStorageConnector does not load KV cache

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug We are currently evaluating the recently introduced KV Connector API V1. I verified that `LMCacheConnectorV1` is working correctly—offloading to local/remote fs successfully reduces TTFT. However, when switching to `SharedStorageConnector`, KV caches are written (using safetensor), but they are never loaded. Here is a snippet of the logs: ``` INFO 05-21 14:12:13 [async_llm.py:256] Added request chatcmpl-4e49e0c575f34e258eb96de5e16b9f57. INFO: 172.17.0.1:51484 - "GET /metrics HTTP/1.1" 200 OK INFO 05-21 14:12:18 [loggers.py:116] Engine 000: Avg prompt throughput: 0.0 tokens/s, Avg generation throughput: 20.4 tokens/s, Running: 1 reqs, Waiting: 0 reqs, GPU KV cache usage: 19.2%, Prefix cache hit rate: 0.0% INFO: 172.17.0.1:51484 - "GET /metrics HTTP/1.1" 200 OK INFO: 172.17.0.1:51484 - "GET /metrics HTTP/1.1" 200 OK INFO 05-21 14:12:28 [loggers.py:116] Engine 000: Avg prompt throughput: 7717.9 tokens/s, Avg generation throughput: 48.4 tokens/s, Running: 1 reqs, Waiting: 0 reqs, GPU KV cache usage: 26.0 %, Prefix cache hit rate: 0.0% INFO: 172.17.0.1:51484 - "GET /metrics HTTP/1.1" 200 OK WARNING 05-21 14:12:34 [shared_storage_conne...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: [Bug]: SharedStorageConnector does not load KV cache bug;stale ### Your current environment ### 🐛 Describe the bug We are currently evaluating the recently introduced KV Connector API V1. I verified that `LMCacheConnect...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: nswer lots of frequently asked questions. correctness attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization;sampling_logits;scheduler_memory;speculative_decoding a...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 3: [Bug]: SharedStorageConnector does not load KV cache bug;stale ### Your current environment ### 🐛 Describe the bug We are currently evaluating the recently introduced KV Connector API V1. I verified that `LMCacheConnect...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: ## Your current environment ### 🐛 Describe the bug We are currently evaluating the recently introduced KV Connector API V1. I verified that `LMCacheConnectorV1` is working correctly—offloading to local/remote fs success...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: ild;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization;sampling_logits;scheduler_memory;speculative_decoding attention;cache;cuda;operator;quantization;sampling;triton build_error;nan_inf;...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
