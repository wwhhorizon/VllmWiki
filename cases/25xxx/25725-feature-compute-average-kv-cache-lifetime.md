# vllm-project/vllm#25725: [Feature]: Compute "average KV cache lifetime"

| 字段 | 值 |
| --- | --- |
| Issue | [#25725](https://github.com/vllm-project/vllm/issues/25725) |
| 状态 | closed |
| 标签 | good first issue;feature request |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Compute "average KV cache lifetime"

### Issue 正文摘录

### 🚀 The feature, motivation and pitch It would be useful to provide a measure how long each KV block/request stays in cache in average. This is to answer questions like "if a user returns in 10min they will expect a prefix cache and better experience". ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: [Feature]: Compute "average KV cache lifetime" good first issue;feature request ### 🚀 The feature, motivation and pitch It would be useful to provide a measure how long each KV block/request stays in cache in average. T...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: tion and pitch It would be useful to provide a measure how long each KV block/request stays in cache in average. This is to answer questions like "if a user returns in 10min they will expect a prefix cache and better ex...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature]: Compute "average KV cache lifetime" good first issue;feature request ### 🚀 The feature, motivation and pitch It would be useful to provide a measure how long each KV block/request stays in cache in average. T...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
