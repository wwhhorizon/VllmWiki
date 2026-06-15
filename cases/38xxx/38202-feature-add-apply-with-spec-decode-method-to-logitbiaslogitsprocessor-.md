# vllm-project/vllm#38202: [Feature]: Add apply_with_spec_decode() method to LogitBiasLogitsProcessor for speculative decoding support

| 字段 | 值 |
| --- | --- |
| Issue | [#38202](https://github.com/vllm-project/vllm/issues/38202) |
| 状态 | open |
| 标签 | feature request |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Add apply_with_spec_decode() method to LogitBiasLogitsProcessor for speculative decoding support

### Issue 正文摘录

### 🚀 The feature, motivation and pitch LogitBiasLogitsProcessor is not supported during speculative decoding. We have added an `apply_with_spec_decode` function to LogitBiasLogitsProcessor, included corresponding test cases, and adjusted the current raise error condition. ### Alternatives Add apply_with_spec_decode() method to LogitBiasLogitsProcessor for speculative decoding support ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Feature]: Add apply_with_spec_decode() method to LogitBiasLogitsProcessor for speculative decoding support feature request ### 🚀 The feature, motivation and pitch LogitBiasLogitsProcessor is not supported during specul...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: pec_decode` function to LogitBiasLogitsProcessor, included corresponding test cases, and adjusted the current raise error condition. ### Alternatives Add apply_with_spec_decode() method to LogitBiasLogitsProcessor for s...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
