# vllm-project/vllm#3759: TTFT in openllm with vllm backend VS vllm 

| 字段 | 值 |
| --- | --- |
| Issue | [#3759](https://github.com/vllm-project/vllm/issues/3759) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> TTFT in openllm with vllm backend VS vllm 

### Issue 正文摘录

### Your current environment I have the following two setups, and I am using the benchmark_serving.py to check the ttft for the same request of fixed length. 1. First setup: Openllm with vllm backend * ` vllm version :'0.2.7'` * I print the chunk if the ttft condition is meet: * `chunk: b'data: {"choices":[{"index":0,"delta":{"role":"assistant","content":null},"finish_reason":null}],"model":"MYMODEL","object":"chat.completion.chunk","id":"chatcmpl-4857ac5939864d449af8fbfc9e6e0bc7","created":18869,"usage":null}\n' ` 2. Second setup: VLLM service with fastapi * ` vllm version :'0.3.0'` * I print the chunk when ttft is occurred in the benchmark script: * chunk: `b'data: {"id":"cmpl-97ed2be2dbf24d8b9a6555be25e24bc6","object":"chat.completion.chunk","created":19140,"model":"path/to/mymodel","choices":[{"index":0,"delta":{"role":"assistant"},"finish_reason":null}]}\n'` I was surprized that the output length of the generated text, TPOT, latency all are the same, but there is gap between two TTFT in both setups!!! * Openllm with vllm backend: TTFT is 0.005 * VLLM service: TTFT is 0.214 Why is this difference? what config should be play role in TTFT? or maybe the different version of VLLM...

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: current environment I have the following two setups, and I am using the benchmark_serving.py to check the ttft for the same request of fixed length. 1. First setup: Openllm with vllm backend * ` vllm version :'0.2.7'` *...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: x":0,"delta":{"role":"assistant","content":null},"finish_reason":null}],"model":"MYMODEL","object":"chat.completion.chunk","id":"chatcmpl-4857ac5939864d449af8fbfc9e6e0bc7","created":18869,"usage":null}\n' ` 2. Second se...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: TTFT in openllm with vllm backend VS vllm bug ### Your current environment I have the following two setups, and I am using the benchmark_serving.py to check the ttft for the same request of fixed length. 1. First setup:...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: est of fixed length. 1. First setup: Openllm with vllm backend * ` vllm version :'0.2.7'` * I print the chunk if the ttft condition is meet: * `chunk: b'data: {"choices":[{"index":0,"delta":{"role":"assistant","content"...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: , and I am using the benchmark_serving.py to check the ttft for the same request of fixed length. 1. First setup: Openllm with vllm backend * ` vllm version :'0.2.7'` * I print the chunk if the ttft condition is meet: *...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
