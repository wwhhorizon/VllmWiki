# vllm-project/vllm#13499: [V1] Support rejection sampling for non-greedy requests

| 字段 | 值 |
| --- | --- |
| Issue | [#13499](https://github.com/vllm-project/vllm/issues/13499) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [V1] Support rejection sampling for non-greedy requests

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Currently, the V1 rejection sampler only supports greedy sampling. We need to expand it to random sampling. I think we can do this in three steps: 1. Support the case when greedy sampling (w/ spec decoding) and random sampling (w/o spec decoding) are mixed 2. Support spec decoding with random sampling ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [V1] Support rejection sampling for non-greedy requests feature request ### 🚀 The feature, motivation and pitch Currently, the V1 rejection sampler only supports greedy sampling. We need to expand it to random sampling....
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
