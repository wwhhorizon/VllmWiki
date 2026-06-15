# vllm-project/vllm#33115: [RFC]: Deprecate NCCL Connector?

| 字段 | 值 |
| --- | --- |
| Issue | [#33115](https://github.com/vllm-project/vllm/issues/33115) |
| 状态 | closed |
| 标签 | RFC;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Deprecate NCCL Connector?

### Issue 正文摘录

### Motivation. We now support the NIXL Connector and Mooncake Connector Additionally, the API is stable for 3rd party plugins. Is anyone using the NCCL connector? We get quite a few GH issues about it so Im wondering if we can simplify the number of connectors and make the set of choices smaller for users Im open to keeping it if its in use, but Im personally not aware of any major users leveraging this feature so Im curious ### Proposed Change. Remove NCCL connector ### Feedback Period. 2 weeks ### CC List. @Abatom who originally implemented it ### Any Other Things. _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: if we can simplify the number of connectors and make the set of choices smaller for users Im open to keeping it if its in use, but Im personally not aware of any major users leveraging this feature so Im curious ### Pro...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [RFC]: Deprecate NCCL Connector? RFC;stale ### Motivation. We now support the NIXL Connector and Mooncake Connector Additionally, the API is stable for 3rd party plugins. Is anyone using the NCCL connector? We get quite...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
