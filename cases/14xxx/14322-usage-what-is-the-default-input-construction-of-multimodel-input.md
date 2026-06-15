# vllm-project/vllm#14322: [Usage]: What is the default input construction of multimodel input?

| 字段 | 值 |
| --- | --- |
| Issue | [#14322](https://github.com/vllm-project/vllm/issues/14322) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: What is the default input construction of multimodel input?

### Issue 正文摘录

### Your current environment ```text skip because this may not important. ``` ### How would you like to use vllm Hi, when I use bench_serving.py to bench a multimodel server with the exampled dataset sharegpt4v. I want to test the max throughout of this server. I found it will be very hard to use all the gpu memory, even I set a very large max-num-seqs for server. I think it maybe because the script just send one single image and one prompt as input for one request? What if I construct input with multiple images and prompts as one request, will that improve the throughput performance of the server? Does bench_serving.py support we make batched request now? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: sage]: What is the default input construction of multimodel input? usage;stale ### Your current environment ```text skip because this may not important. ``` ### How would you like to use vllm Hi, when I use bench_servin...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: ench a multimodel server with the exampled dataset sharegpt4v. I want to test the max throughout of this server. I found it will be very hard to use all the gpu memory, even I set a very large max-num-seqs for server. I...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ge;stale ### Your current environment ```text skip because this may not important. ``` ### How would you like to use vllm Hi, when I use bench_serving.py to bench a multimodel server with the exampled dataset sharegpt4v...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ow? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: x throughout of this server. I found it will be very hard to use all the gpu memory, even I set a very large max-num-seqs for server. I think it maybe because the script just send one single image and one prompt as inpu...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
