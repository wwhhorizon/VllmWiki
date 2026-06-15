# vllm-project/vllm#8816: [Usage]: How does VLLM allocate memory

| 字段 | 值 |
| --- | --- |
| Issue | [#8816](https://github.com/vllm-project/vllm/issues/8816) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: How does VLLM allocate memory

### Issue 正文摘录

### Your current environment Running VLLM like` vllm serve /models/Meta-Llama-3-8B/ --disable-log-requests` uses almost all available space on my H100. How is that possible? An 8b model should take about 16GB - How does VLLM use all the GPU memory? ### How would you like to use vllm I am trying to understand VLLM memory usage ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: a-3-8B/ --disable-log-requests` uses almost all available space on my H100. How is that possible? An 8b model should take about 16GB - How does VLLM use all the GPU memory? ### How would you like to use vllm I am trying...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: usage;stale ### Your current environment Running VLLM like` vllm serve /models/Meta-Llama-3-8B/ --disable-log-requests` uses almost all available space on my H100. How is that possible? An 8b model should take about 16G...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Usage]: How does VLLM allocate memory usage;stale ### Your current environment Running VLLM like` vllm serve /models/Meta-Llama-3-8B/ --disable-log-requests` uses almost all available space on my H100. How is that poss...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: possible? An 8b model should take about 16GB - How does VLLM use all the GPU memory? ### How would you like to use vllm I am trying to understand VLLM memory usage ### Before submitting a new issue... - [X] Make sure yo...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
