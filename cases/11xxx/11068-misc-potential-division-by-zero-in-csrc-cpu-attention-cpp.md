# vllm-project/vllm#11068: [Misc]: Potential division by zero in csrc/cpu/attention.cpp

| 字段 | 值 |
| --- | --- |
| Issue | [#11068](https://github.com/vllm-project/vllm/issues/11068) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Misc]: Potential division by zero in csrc/cpu/attention.cpp

### Issue 正文摘录

### Anything you want to discuss about vllm. Our scanners picked this one up, just as a potential issue: https://github.com/vllm-project/vllm/blob/9b9cef3145381721fa950c89718fe71849ac2a55/csrc/cpu/attention.cpp#L97 and https://github.com/vllm-project/vllm/blob/9b9cef3145381721fa950c89718fe71849ac2a55/csrc/cpu/attention.cpp#L129 both have the potential to divide by zero, though this would only ever happen if sum happens to be zero, which would only ever seem to be possible in an extreme edge case. I can draft up a PR if it seems worth fixing. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ng. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: hich would only ever seem to be possible in an extreme edge case. I can draft up a PR if it seems worth fixing. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked th...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
