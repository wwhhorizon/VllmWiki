# vllm-project/vllm#1677: API Server Performance

| 字段 | 值 |
| --- | --- |
| Issue | [#1677](https://github.com/vllm-project/vllm/issues/1677) |
| 状态 | closed |
| 标签 | performance |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> API Server Performance

### Issue 正文摘录

During benchmarking, we discovered there are performance gaps in both the API server and AsyncLLM engine where the request latency and throughput do not match a hand written gRPC server. I'm planning to investigate this. The clues are: * Slowdown in the asyncio loop due to implementation to support streaming * Blocking call in the asyncio loop, which have trouble offloading requests, this should be resolved by the threading PR. #1628 but we should benchmark it. * The FastAPI + uvicorn is single threaded. cc @WoosukKwon @zhuohan123

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: API Server Performance performance During benchmarking, we discovered there are performance gaps in both the API server and AsyncLLM engine where the request latency and throughput do not match a hand written gRPC serve...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: I'm planning to investigate this. The clues are: * Slowdown in the asyncio loop due to implementation to support streaming * Blocking call in the asyncio loop, which have trouble offloading requests, this should be reso...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: upport streaming * Blocking call in the asyncio loop, which have trouble offloading requests, this should be resolved by the threading PR. #1628 but we should benchmark it. * The FastAPI + uvicorn is single threaded. cc...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: lowdown in the asyncio loop due to implementation to support streaming * Blocking call in the asyncio loop, which have trouble offloading requests, this should be resolved by the threading PR. #1628 but we should benchm...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: re performance gaps in both the API server and AsyncLLM engine where the request latency and throughput do not match a hand written gRPC server. I'm planning to investigate this. The clues are: * Slowdown in the asyncio...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
