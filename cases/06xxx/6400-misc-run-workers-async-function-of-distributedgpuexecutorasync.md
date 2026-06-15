# vllm-project/vllm#6400: [Misc]: _run_workers_async function of DistributedGPUExecutorAsync

| 字段 | 值 |
| --- | --- |
| Issue | [#6400](https://github.com/vllm-project/vllm/issues/6400) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Misc]: _run_workers_async function of DistributedGPUExecutorAsync

### Issue 正文摘录

I am confused why _run_workers_async function of DistributedGPUExecutorAsync is removed since v0.4.3? New implementation starts a loop for every worker which will restrict worker from doing other things such as transfering kv cache in prefill/decode disaggregation. I use _run_workers_async to transfer kv cache before without any problems but it will execute only when the loops of workers are stopped currently. I am sorry that I am not familiar with asyncio in python. I want to know what the benefits of the new implementation are? And how to allow the workers to transfer kv asynchronously during generation?

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Misc]: _run_workers_async function of DistributedGPUExecutorAsync stale I am confused why _run_workers_async function of DistributedGPUExecutorAsync is removed since v0.4.3? New implementation starts a loop for every w...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: rkers are stopped currently. I am sorry that I am not familiar with asyncio in python. I want to know what the benefits of the new implementation are? And how to allow the workers to transfer kv asynchronously during ge...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: r which will restrict worker from doing other things such as transfering kv cache in prefill/decode disaggregation. I use _run_workers_async to transfer kv cache before without any problems but it will execute only when...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
