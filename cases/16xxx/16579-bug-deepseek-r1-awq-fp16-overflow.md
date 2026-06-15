# vllm-project/vllm#16579: [Bug]: deepseek-r1 awq fp16 overflow

| 字段 | 值 |
| --- | --- |
| Issue | [#16579](https://github.com/vllm-project/vllm/issues/16579) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: deepseek-r1 awq fp16 overflow

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I found https://github.com/vllm-project/vllm/pull/14809 . Is there a plan to address the overflow issue during fp16 inference? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ce? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: deepseek-r1 awq fp16 overflow bug;stale ### Your current environment ### 🐛 Describe the bug I found https://github.com/vllm-project/vllm/pull/14809 . Is there a plan to address the overflow issue during fp16 infe...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
