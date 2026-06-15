# vllm-project/vllm#13131: [Bug]: Memory usage calculations are unstable on systems with unified memory (Jetson, GH200, etc.)

| 字段 | 值 |
| --- | --- |
| Issue | [#13131](https://github.com/vllm-project/vllm/issues/13131) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Memory usage calculations are unstable on systems with unified memory (Jetson, GH200, etc.)

### Issue 正文摘录

### Your current environment I have observed the issue on an NVIDIA Jetson Orin NX, but this could happen on any system with unified memory. ### 🐛 Describe the bug https://github.com/vllm-project/vllm/pull/9352 added logic [in memory usage calculations](https://github.com/vllm-project/vllm/blob/v0.7.2/vllm/worker/worker.py#L273-L283) that hopes other processes don't release GPU memory during the calculation process, aborting if they have. This may be an acceptable tradeoff on a traditional system with a dedicated GPU, but it is not viable on a system where the CPU and GPU share memory, such as on a Jetson or GH200. On such systems, it is highly probable that another process will release memory, causing this assertion to fail. Another solution needs to be found for these systems. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ms. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: llm/worker/worker.py#L273-L283) that hopes other processes don't release GPU memory during the calculation process, aborting if they have. This may be an acceptable tradeoff on a traditional system with a dedicated GPU,...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ns are unstable on systems with unified memory (Jetson, GH200, etc.) bug;stale ### Your current environment I have observed the issue on an NVIDIA Jetson Orin NX, but this could happen on any system with unified memory....
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
