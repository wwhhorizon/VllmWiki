# vllm-project/vllm#1160: killed due to memory pressure (OOM), 0 Workers crashed due to other reasons at node

| 字段 | 值 |
| --- | --- |
| Issue | [#1160](https://github.com/vllm-project/vllm/issues/1160) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> killed due to memory pressure (OOM), 0 Workers crashed due to other reasons at node

### Issue 正文摘录

#033[2m#033[33m(raylet)#033[0m [DATE] (raylet) node_manager.cc:3007: 2 Workers (tasks / actors) killed due to memory pressure (OOM), 0 Workers crashed due to other reasons at node (ID: abd406d415bd2b74a5 e281968fd76aa200d56e4529fd1c1cd4373840, IP: 10.0.167.26) over the last time period. To see more information about th e Workers killed on this node, use `ray logs raylet.out -ip 10.0.167.26` #033[2m#033[33m(raylet)#033[0m #033[2m#033[33m(raylet)#033[0m Refer to the documentation on how to address the out of memory issue: https://docs.ra y.io/en/latest/ray-core/scheduling/ray-oom-prevention.html. Consider provisioning more memory on this node or reduci ng task parallelism by requesting more CPUs per task. To adjust the kill threshold, set the environment variable `RA Y_memory_usage_threshold` when starting Ray. To disable worker killing, set the environment variable `RAY_memory_mon itor_refresh_ms` to zero. I met this problem. How many memory with tensor_parallel_size=4 when infernce with a 1.3B model?

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: d1c1cd4373840, IP: 10.0.167.26) over the last time period. To see more information about th e Workers killed on this node, use `ray logs raylet.out -ip 10.0.167.26` #033[2m#033[33m(raylet)#033[0m #033[2m#033[33m(raylet)...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: m-prevention.html. Consider provisioning more memory on this node or reduci ng task parallelism by requesting more CPUs per task. To adjust the kill threshold, set the environment variable `RA Y_memory_usage_threshold`...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: onsider provisioning more memory on this node or reduci ng task parallelism by requesting more CPUs per task. To adjust the kill threshold, set the environment variable `RA Y_memory_usage_threshold` when starting Ray. T...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: killed due to memory pressure (OOM), 0 Workers crashed due to other reasons at node #033[2m#033[33m(raylet)#033[0m [DATE] (raylet) node_manager.cc:3007: 2 Workers (tasks / actors) killed due to memory pressure (OOM), 0...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: r provisioning more memory on this node or reduci ng task parallelism by requesting more CPUs per task. To adjust the kill threshold, set the environment variable `RA Y_memory_usage_threshold` when starting Ray. To disa...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
