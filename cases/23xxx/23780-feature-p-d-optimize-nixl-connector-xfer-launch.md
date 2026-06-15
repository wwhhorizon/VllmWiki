# vllm-project/vllm#23780: [Feature][P/D]: Optimize NIXL Connector xfer Launch

| 字段 | 值 |
| --- | --- |
| Issue | [#23780](https://github.com/vllm-project/vllm/issues/23780) |
| 状态 | closed |
| 标签 | help wanted;good first issue;feature request;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature][P/D]: Optimize NIXL Connector xfer Launch

### Issue 正文摘录

### 🚀 The feature, motivation and pitch NIXL Connector takes ~3ms to launch a transfer per request due to the `_get_block_desc_ids` We can optimize this by leveraging the numpy bindings for nixl ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: Optimize NIXL Connector xfer Launch help wanted;good first issue;feature request;stale ### 🚀 The feature, motivation and pitch NIXL Connector takes ~3ms to launch a transfer per request due to the `_get_block_desc_ids`...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: L Connector takes ~3ms to launch a transfer per request due to the `_get_block_desc_ids` We can optimize this by leveraging the numpy bindings for nixl ### Alternatives _No response_ ### Additional context _No response_...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
