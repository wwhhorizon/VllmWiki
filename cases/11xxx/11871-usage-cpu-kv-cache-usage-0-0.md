# vllm-project/vllm#11871: [Usage]: 为什么CPU KV cache usage一直为0.0%

| 字段 | 值 |
| --- | --- |
| Issue | [#11871](https://github.com/vllm-project/vllm/issues/11871) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: 为什么CPU KV cache usage一直为0.0%

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm. 我用的是L40，发现GPU KV cache在使用中，但是CPU KV cache一直为0，想利用起这部分资源，请问大佬们该如何配置呀？ INFO 01-09 09:53:39 metrics.py:351] Avg prompt throughput: 0.0 tokens/s, Avg generation throughput: 18.5 tokens/s, Running: 1 reqs, Swapped: 0 reqs, Pending: 0 reqs, GPU KV cache usage: 20.0%, CPU KV cache usage: 0.0%. INFO: 10.38.115.100:51522 - "GET /metrics HTTP/1.1" 200 OK INFO 01-09 09:53:44 metrics.py:351] Avg prompt throughput: 0.0 tokens/s, Avg generation throughput: 18.5 tokens/s, Running: 1 reqs, Swapped: 0 reqs, Pending: 0 reqs, GPU KV cache usage: 20.0%, CPU KV cache usage: 0.0%. INFO: 10.38.115.100:51522 - "GET /metrics HTTP/1.1" 200 OK INFO 01-09 09:53:49 metrics.py:351] Avg prompt throughput: 0.0 tokens/s, Avg generation throughput: 18.4 tokens/s, Running: 1 reqs, Swapped: 0 reqs, Pending: 0 reqs, GPU KV cache usage: 20.0%, CPU KV cache usage: 0.0%. INFO: 10.38.115.100:51522 - "GET /metrics HTTP/1.1" 200 OK INFO 01-09 09:53:54 metrics.py:351] Avg prompt throughput: 0.0 tokens/s, Avg...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: `` ### How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm. 我用的是L40，发现GPU KV cache在使用中，但是CPU KV cache一直为0，想利用起这部分资源，请问大佬们该如何配置呀？ INFO 0...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: 0，想利用起这部分资源，请问大佬们该如何配置呀？ INFO 01-09 09:53:39 metrics.py:351] Avg prompt throughput: 0.0 tokens/s, Avg generation throughput: 18.5 tokens/s, Running: 1 reqs, Swapped: 0 reqs, Pending: 0 reqs, GPU KV cache usage: 20.0%, C...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 0%. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: [Usage]: 为什么CPU KV cache usage一直为0.0% usage;stale ### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm I want to run inference of a [specific model](put link...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: # How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm. 我用的是L40，发现GPU KV cache在使用中，但是CPU KV cache一直为0，想利用起这部分资源，请问大佬们该如何配置呀？ INFO 01-09...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
