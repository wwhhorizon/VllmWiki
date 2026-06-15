# vllm-project/vllm#16368: [Usage]: vllm serve: how to get KV cache percentage on CPU and GPU?

| 字段 | 值 |
| --- | --- |
| Issue | [#16368](https://github.com/vllm-project/vllm/issues/16368) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: vllm serve: how to get KV cache percentage on CPU and GPU?

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm Like benchmark_throughput.py and benchmark_ latency.py that show KV cache usage on GPU and CPU. How can I get the same stats with vlm serve? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: of `python collect_env.py` ``` ### How would you like to use vllm Like benchmark_throughput.py and benchmark_ latency.py that show KV cache usage on GPU and CPU. How can I get the same stats with vlm serve? ### Before s...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ve? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: [Usage]: vllm serve: how to get KV cache percentage on CPU and GPU? usage;stale ### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm Like benchmark_throughput...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: at show KV cache usage on GPU and CPU. How can I get the same stats with vlm serve? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bott...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: Usage]: vllm serve: how to get KV cache percentage on CPU and GPU? usage;stale ### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm Like benchmark_throughput....

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
