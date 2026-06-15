# vllm-project/vllm#22019: [Usage]: How to do KV cache transfer between a CPU instance and a GPU instance

| 字段 | 值 |
| --- | --- |
| Issue | [#22019](https://github.com/vllm-project/vllm/issues/22019) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: How to do KV cache transfer between a CPU instance and a GPU instance

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm If there are two vllm instances, one with a GPU backend and the other with a CPU, is it currently possible to transfer the KV cache between the two? Can the current kv_transfer do this? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ld you like to use vllm If there are two vllm instances, one with a GPU backend and the other with a CPU, is it currently possible to transfer the KV cache between the two? Can the current kv_transfer do this? ### Befor...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: is? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: [Usage]: How to do KV cache transfer between a CPU instance and a GPU instance usage;stale ### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm If there are t...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: to do KV cache transfer between a CPU instance and a GPU instance usage;stale ### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm If there are two vllm insta...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
