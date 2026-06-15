# vllm-project/vllm#8819: [Bug]: Later version have degradation based on `vllm:time_to_first_token_seconds_sum` metric

| 字段 | 值 |
| --- | --- |
| Issue | [#8819](https://github.com/vllm-project/vllm/issues/8819) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Later version have degradation based on `vllm:time_to_first_token_seconds_sum` metric

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I've noticed a degradation after vllm v0.5.3.post1. For example for a simple model `facebook/opt-125m` start server with: ```python python3 -m vllm.entrypoints.openai.api_server --model facebook/opt-125m ``` send a request and query metrics: ```bash ### curl http://127.0.0.1:8000/metrics INFO: 127.0.0.1:55690 - "GET /metrics HTTP/1.1" 200 OK # HELP python_gc_objects_collected_total Objects collected during gc # TYPE python_gc_objects_collected_total counter python_gc_objects_collected_total{generation="0"} 11541.0 python_gc_objects_collected_total{generation="1"} 10139.0 python_gc_objects_collected_total{generation="2"} 2032.0 # HELP python_gc_objects_uncollectable_total Uncollectable objects found during GC # TYPE python_gc_objects_uncollectable_total counter python_gc_objects_uncollectable_total{generation="0"} 0.0 python_gc_objects_uncollectable_total{generation="1"} 0.0 python_gc_objects_uncollectable_total{generation="2"} 0.0 # HELP python_gc_collections_total Number of times this generation was collected # TYPE python_gc_collections_total counter python_gc_collections_total{generation="0"...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: vllm.entrypoints.openai.api_server --model facebook/opt-125m ``` send a request and query metrics: ```bash ### curl http://127.0.0.1:8000/metrics INFO: 127.0.0.1:55690 - "GET /metrics HTTP/1.1" 200 OK # HELP python_gc_o...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 4: info gauge vllm:cache_config_info{block_size="16",cache_dtype="auto",cpu_offload_gb="0",enable_prefix_caching="False",gpu_memory_utilization="0.9",num_cpu_blocks="7281",num_gpu_blocks="76416",num_gpu_blocks_override="No...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: first_token_seconds_sum` metric bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I've noticed a degradation after vllm v0.5.3.post1. For example for a simple model `facebook/op...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: l_name="facebook/opt-125m"} 0.007464408874511719 # HELP vllm:e2e_request_latency_seconds Histogram of end to end request latency in seconds. # TYPE vllm:e2e_request_latency_seconds histogram vllm:e2e_request_latency_sec...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [Bug]: Later version have degradation based on `vllm:time_to_first_token_seconds_sum` metric bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I've noticed a degradation after v...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
