# vllm-project/vllm#20171: [Usage]: Getting logits of the first token to generate

| 字段 | 值 |
| --- | --- |
| Issue | [#20171](https://github.com/vllm-project/vllm/issues/20171) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Getting logits of the first token to generate

### Issue 正文摘录

### Your current environment v1 engine ### How would you like to use vllm I want the logits of the first-token-to-generate over the vocabulary. I can successfully get a hidden embedding. Am I supposed to multiply it with the `lm_head`? The vocab distribution I got in this way seems quite different from the logprobs I get from `generate`. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: e`. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
