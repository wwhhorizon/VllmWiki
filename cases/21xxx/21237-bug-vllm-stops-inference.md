# vllm-project/vllm#21237: [Bug]: vLLM stops inference

| 字段 | 值 |
| --- | --- |
| Issue | [#21237](https://github.com/vllm-project/vllm/issues/21237) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 12; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: vLLM stops inference

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug There is a batch of data that needs to be processed using vLLM, and each data item requires three rounds of inference. However, there's an issue: after processing a certain number of data items, vLLM stops performing inference. The GPU memory is still occupied, but the utilization drops to 0, and the program no longer proceeds. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ds. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: ing a certain number of data items, vLLM stops performing inference. The GPU memory is still occupied, but the utilization drops to 0, and the program no longer proceeds. ### Before submitting a new issue... - [x] Make...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: vLLM stops inference bug;stale ### Your current environment ### 🐛 Describe the bug There is a batch of data that needs to be processed using vLLM, and each data item requires three rounds of inference. However, t...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
