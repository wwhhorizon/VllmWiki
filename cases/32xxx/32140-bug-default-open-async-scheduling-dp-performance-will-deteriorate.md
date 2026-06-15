# vllm-project/vllm#32140: [Bug]: Default open async_scheduling, DP performance will deteriorate

| 字段 | 值 |
| --- | --- |
| Issue | [#32140](https://github.com/vllm-project/vllm/issues/32140) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Default open async_scheduling, DP performance will deteriorate

### Issue 正文摘录

### Your current environment Use main branch code. ### 🐛 Describe the bug Current default open async_scheduling, but DP synchronizers cannot use nccl, it use cpu to synchronizers, performance will deteriorate. https://github.com/vllm-project/vllm/blob/19504ac07fda211744bd67e62c03ab6b32c92ab1/vllm/v1/worker/dp_utils.py#L29-L34 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: L34 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
