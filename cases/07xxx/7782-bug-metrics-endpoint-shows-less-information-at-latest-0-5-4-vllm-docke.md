# vllm-project/vllm#7782: [Bug]: /metrics endpoint shows less information at latest (0.5.4) vllm docker container.

| 字段 | 值 |
| --- | --- |
| Issue | [#7782](https://github.com/vllm-project/vllm/issues/7782) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: /metrics endpoint shows less information at latest (0.5.4) vllm docker container.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug /metrics endpoint from docker with version 0.5.1 contain all data about vllm server. For example 'gpu_cache_usage_perc' metric. Here is example of /metrics endpoint(# deleted): > HELP python_gc_objects_collected_total Objects collected during gc > TYPE python_gc_objects_collected_total counter > python_gc_objects_collected_total{generation="0"} 7902.0 > python_gc_objects_collected_total{generation="1"} 4609.0 > python_gc_objects_collected_total{generation="2"} 1618.0 > HELP python_gc_objects_uncollectable_total Uncollectable objects found during GC > TYPE python_gc_objects_uncollectable_total counter > python_gc_objects_uncollectable_total{generation="0"} 0.0 > python_gc_objects_uncollectable_total{generation="1"} 0.0 > python_gc_objects_uncollectable_total{generation="2"} 0.0 > HELP python_gc_collections_total Number of times this generation was collected > TYPE python_gc_collections_total counter > python_gc_collections_total{generation="0"} 956.0 > python_gc_collections_total{generation="1"} 85.0 > python_gc_collections_total{generation="2"} 79.0 > HELP python_info Python platform information > TYPE python_info gauge > python_...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: /metrics endpoint shows less information at latest (0.5.4) vllm docker container. bug ### Your current environment ### 🐛 Describe the bug /metrics endpoint from docker with version 0.5.1 contain all data about vl...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [Bug]: /metrics endpoint shows less information at latest (0.5.4) vllm docker container. bug ### Your current environment ### 🐛 Describe the bug /metrics endpoint from docker with version 0.5.1 contain all data about vl...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: sliding_window="None",swap_space_bytes="4294967296"} 1.0 > HELP vllm:num_requests_running Number of requests currently running on GPU. > TYPE vllm:num_requests_running gauge > vllm:num_requests_running{model_name="caspe...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: [Bug]: /metrics endpoint shows less information at latest (0.5.4) vllm docker container. bug ### Your current environment ### 🐛 Describe the bug /metrics endpoint from docker with version 0.5.1 contain all data about vl...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: m:cache_config_info gauge > vllm:cache_config_info{block_size="16",cache_dtype="auto",enable_prefix_caching="True",gpu_memory_utilization="0.94",num_cpu_blocks="819",num_gpu_blocks="7093",num_gpu_blocks_override="None",...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
