# vllm-project/vllm#26762: [Usage]: about curl http://ip:8000/metrics

| 字段 | 值 |
| --- | --- |
| Issue | [#26762](https://github.com/vllm-project/vllm/issues/26762) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: about curl http://ip:8000/metrics

### Issue 正文摘录

### Your current environment When I run this command, I get the following results: # HELP python_gc_objects_collected_total Objects collected during gc # TYPE python_gc_objects_collected_total counter python_gc_objects_collected_total{generation="0"} 12286.0 python_gc_objects_collected_total{generation="1"} 1244.0 python_gc_objects_collected_total{generation="2"} 1326.0 # HELP python_gc_objects_uncollectable_total Uncollectable objects found during GC # TYPE python_gc_objects_uncollectable_total counter python_gc_objects_uncollectable_total{generation="0"} 0.0 python_gc_objects_uncollectable_total{generation="1"} 0.0 python_gc_objects_uncollectable_total{generation="2"} 0.0 # HELP python_gc_collections_total Number of times this generation was collected # TYPE python_gc_collections_total counter python_gc_collections_total{generation="0"} 1378.0 python_gc_collections_total{generation="1"} 124.0 python_gc_collections_total{generation="2"} 9.0 # HELP python_info Python platform information # TYPE python_info gauge python_info{implementation="CPython",major="3",minor="12",patchlevel="11",version="3.12.11"} 1.0 # HELP process_virtual_memory_bytes Virtual memory size in bytes. # TYPE p...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: ython_info{implementation="CPython",major="3",minor="12",patchlevel="11",version="3.12.11"} 1.0 # HELP process_virtual_memory_bytes Virtual memory size in bytes. # TYPE process_virtual_memory_bytes gauge process_virtual...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: llections_total{generation="2"} 9.0 # HELP python_info Python platform information # TYPE python_info gauge python_info{implementation="CPython",major="3",minor="12",patchlevel="11",version="3.12.11"} 1.0 # HELP process...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Usage]: about curl http://ip:8000/metrics usage;stale ### Your current environment When I run this command, I get the following results: # HELP python_gc_objects_collected_total Objects collected during gc # TYPE pytho...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: none"} 1.7604160309445088e+09 # HELP http_request_duration_highr_seconds Latency with many buckets but no API specific labels. Made for more accurate percentile calculations. # TYPE http_request_duration_highr_seconds h...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: lm. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
