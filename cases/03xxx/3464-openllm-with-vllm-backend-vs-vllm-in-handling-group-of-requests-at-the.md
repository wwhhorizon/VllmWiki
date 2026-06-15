# vllm-project/vllm#3464: Openllm with vLLM backend VS  vLLM in handling group of requests at the same time

| 字段 | 值 |
| --- | --- |
| Issue | [#3464](https://github.com/vllm-project/vllm/issues/3464) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 15; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Openllm with vLLM backend VS  vLLM in handling group of requests at the same time

### Issue 正文摘录

### Your current environment I am sending requests at the same time such as benchmark_serving to two services: Number of requests: 400 ### 🐛 Describe the bug I am sending requests at the same time such as benchmark_serving to two services: Number of requests: 400 1. first endpoint from running openllm start to my model with vLLM backend, I observed from the metrics logs that this service can handle more requests at the same time unlike vLLM service which enable openllm service to process them under high load more than vLLM which always I can see up to 3 request are running and 0 pending. > * vllm version :'0.2.7' logs: `INFO 03-18 12:34:52 llm_engine.py:706] Avg prompt throughput: 209.6 tokens/s, Avg generation throughput: 567.4 tokens/s, Running: 36 reqs, Swapped: 0 reqs, Pending: 78 reqs, GPU KV cache usage: 99.1%, CPU KV cache usage: 0.0% ` 2. vLLM service, I write endpoint as its mentioned in the vLLM [entrypoints](https://github.com/vllm-project/vllm/blob/main/vllm/entrypoints/api_server.py) > * vllm version :'0.3.2' logs: `(ServeReplica:default:OpenLLMDeployment pid=126565) INFO 03-18 12:58:24 metrics.py:161] Avg prompt throughput: 0.0 tokens/s, Avg generation throughput: 54...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: Openllm with vLLM backend VS vLLM in handling group of requests at the same time bug;stale ### Your current environment I am sending requests at the same time such as benchmark_serving to two services: Number of request...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: Your current environment I am sending requests at the same time such as benchmark_serving to two services: Number of requests: 400 ### 🐛 Describe the bug I am sending requests at the same time such as benchmark_serving...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: Openllm with vLLM backend VS vLLM in handling group of requests at the same time bug;stale ### Your current environment I am sending requests at the same time such as benchmark_serving to two services: Number of request...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: always I can see up to 3 request are running and 0 pending. > * vllm version :'0.2.7' logs: `INFO 03-18 12:34:52 llm_engine.py:706] Avg prompt throughput: 209.6 tokens/s, Avg generation throughput: 567.4 tokens/s, Runni...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: 567.4 tokens/s, Running: 36 reqs, Swapped: 0 reqs, Pending: 78 reqs, GPU KV cache usage: 99.1%, CPU KV cache usage: 0.0% ` 2. vLLM service, I write endpoint as its mentioned in the vLLM [entrypoints](https://github.com/...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
