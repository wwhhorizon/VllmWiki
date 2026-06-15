# vllm-project/vllm#17076: [RFC]: Implement structural_tag support in structured output

| 字段 | 值 |
| --- | --- |
| Issue | [#17076](https://github.com/vllm-project/vllm/issues/17076) |
| 状态 | closed |
| 标签 | structured-output;RFC |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Implement structural_tag support in structured output

### Issue 正文摘录

### Motivation. Xgrammar introduced `structural_tag` support. vLLM users would benefit from adding support for this feature. Xgrammar implementation: https://github.com/mlc-ai/xgrammar/pull/162 ### Proposed Change. Implement structural_tag support along with support in each structured output backend that can support it. ### Feedback Period. _No response_ ### CC List. _No response_ ### Any Other Things. _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ment structural_tag support along with support in each structured output backend that can support it. ### Feedback Period. _No response_ ### CC List. _No response_ ### Any Other Things. _No response_ ### Before submitti...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
