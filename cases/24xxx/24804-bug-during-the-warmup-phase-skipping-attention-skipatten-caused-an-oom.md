# vllm-project/vllm#24804: [Bug]: During the warmup phase, skipping attention (skipatten) caused an OOM (Out of Memory) error later.

| 字段 | 值 |
| --- | --- |
| Issue | [#24804](https://github.com/vllm-project/vllm/issues/24804) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: During the warmup phase, skipping attention (skipatten) caused an OOM (Out of Memory) error later.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug chunked_prefill_workspace_size itself is a relatively large hyperparameter, which causes NPU memory usage to increase during runtime. It is unreasonable that the community’s current warmup phase does not account for the workspace occupied by attention (atten). ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: n). ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: [Bug]: During the warmup phase, skipping attention (skipatten) caused an OOM (Out of Memory) error later. bug ### Your current environment ### 🐛 Describe the bug chunked_prefill_workspace_size itself is a relatively lar...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: er. bug ### Your current environment ### 🐛 Describe the bug chunked_prefill_workspace_size itself is a relatively large hyperparameter, which causes NPU memory usage to increase during runtime. It is unreasonable that t...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
