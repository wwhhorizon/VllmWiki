# vllm-project/vllm#17292: [Feature]: support reasoning output when offline batched inference

| 字段 | 值 |
| --- | --- |
| Issue | [#17292](https://github.com/vllm-project/vllm/issues/17292) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: support reasoning output when offline batched inference

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Does enable-reasoning support in offline batched inference? if no, is there a plan to support? https://docs.vllm.ai/en/latest/getting_started/quickstart.html#offline-batched-inference https://docs.vllm.ai/en/stable/features/reasoning_outputs.html ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: eature]: support reasoning output when offline batched inference feature request;stale ### 🚀 The feature, motivation and pitch Does enable-reasoning support in offline batched inference? if no, is there a plan to suppor...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: nference? if no, is there a plan to support? https://docs.vllm.ai/en/latest/getting_started/quickstart.html#offline-batched-inference https://docs.vllm.ai/en/stable/features/reasoning_outputs.html ### Alternatives _No r...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
