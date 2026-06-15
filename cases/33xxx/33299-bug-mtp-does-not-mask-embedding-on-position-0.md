# vllm-project/vllm#33299: [Bug]: MTP does not mask embedding on position 0

| 字段 | 值 |
| --- | --- |
| Issue | [#33299](https://github.com/vllm-project/vllm/issues/33299) |
| 状态 | open |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: MTP does not mask embedding on position 0

### Issue 正文摘录

### 🐛 Describe the bug According to the report of deepseek v3, embedding on position 0 is dropped by left shifting instead of being set to 0. ```python # masking inputs at position 0, as not needed by MTP inputs_embeds = torch.where(positions.unsqueeze(-1) == 0, 0, inputs_embeds) ``` Codes like these do not follow the design of training. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ing. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), w...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
