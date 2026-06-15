# vllm-project/vllm#2669: Ray worker out of memory

| 字段 | 值 |
| --- | --- |
| Issue | [#2669](https://github.com/vllm-project/vllm/issues/2669) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Ray worker out of memory

### Issue 正文摘录

Trying to spin a server with an asyncengine, with 'use_ray' on true. after a few hours, i get the following error: Memory on the node (IP: 169.254.181.2, ID: 708c7baf966d59aa3f08299830c349ca055293ebb1c33d8e72cd3336) where the task (actor ID: 0dab4ab45f6c947201afac6d01000000, name=RayWorkerVllm.__init__, pid=308, memory used=11.15GB) was running was 12.49GB / 13.15GB (0.950003), which exceeds the memory usage threshold of 0.95. Ray killed this worker (ID: 79a553ea91fe46f95e8384ddf8a8f0a01e3418a975ecd0af983c7bb2) because it was the most recently scheduled task; to see more information about memory usage on this node, use `ray logs raylet.out -ip 169.254.181.2`. To see the logs of the worker, use `ray logs worker-79a553ea91fe46f95e8384ddf8a8f0a01e3418a975ecd0af983c7bb2*out -ip 169.254.181.2. Top 10 memory users: ... Refer to the documentation on how to address the out of memory issue: https://docs.ray.io/en/latest/ray-core/scheduling/ray-oom-prevention.html. Consider provisioning more memory on this node or reducing task parallelism by requesting more CPUs per task. Set max_restarts and max_task_retries to enable retry when the task crashes due to OOM. To adjust the kill threshold, s...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: Ray worker out of memory stale Trying to spin a server with an asyncengine, with 'use_ray' on true. after a few hours, i get the following error: Memory on the node (IP: 169.254.181.2, ID: 708c7baf966d59aa3f08299830c349...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: m-prevention.html. Consider provisioning more memory on this node or reducing task parallelism by requesting more CPUs per task. Set max_restarts and max_task_retries to enable retry when the task crashes due to OOM. To...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: Consider provisioning more memory on this node or reducing task parallelism by requesting more CPUs per task. Set max_restarts and max_task_retries to enable retry when the task crashes due to OOM. To adjust the kill th...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: t of memory issue: https://docs.ray.io/en/latest/ray-core/scheduling/ray-oom-prevention.html. Consider provisioning more memory on this node or reducing task parallelism by requesting more CPUs per task. Set max_restart...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: 983c7bb2) because it was the most recently scheduled task; to see more information about memory usage on this node, use `ray logs raylet.out -ip 169.254.181.2`. To see the logs of the worker, use `ray logs worker-79a553...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
