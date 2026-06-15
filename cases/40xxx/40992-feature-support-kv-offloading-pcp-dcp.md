# vllm-project/vllm#40992: [Feature]: Support KV offloading + PCP/DCP

| 字段 | 值 |
| --- | --- |
| Issue | [#40992](https://github.com/vllm-project/vllm/issues/40992) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Support KV offloading + PCP/DCP

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Currently, PCP/DCP does not work with `--kv-offloading-size` (using the offloading connector). See https://github.com/vllm-project/vllm/issues/40259#issuecomment-4325036379 for example. Investigate whether we can extend support for that. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: [Feature]: Support KV offloading + PCP/DCP feature request ### 🚀 The feature, motivation and pitch Currently, PCP/DCP does not work with `--kv-offloading-size` (using the offloading connector). See https://github.com/vl...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature]: Support KV offloading + PCP/DCP feature request ### 🚀 The feature, motivation and pitch Currently, PCP/DCP does not work with `--kv-offloading-size` (using the offloading connector). See https://github.com/vl...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
