# vllm-project/vllm#23892: [RFC]: Remove LoRA bias

| 字段 | 值 |
| --- | --- |
| Issue | [#23892](https://github.com/vllm-project/vllm/issues/23892) |
| 状态 | closed |
| 标签 | good first issue;RFC |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Remove LoRA bias

### Issue 正文摘录

### Motivation. #5733 introduced LoRA bias(by using `enable_lora_bias` arg). We have some doubts about this implementation and have also discussed it with the author on Slack, see [lora bias thread](https://vllm-dev.slack.com/archives/C07V3D6F493/p1732803748800689). Considering that LoRA bias has been introduced for about 10 months now, there are almost no issues related to it and this feature appears to be rarely used, so we are considering deleting the LoRA bias-related code. ### Proposed Change. Divided into 2 stages: - [x] Add deprecation warning for `enable_lora_bias`, https://github.com/vllm-project/vllm/pull/24339 - [ ] After keeping the warning for a period of time, delete related code. ### Feedback Period. one week ### CC List. @njhill @followumesh ### Any Other Things. _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: h the author on Slack, see [lora bias thread](https://vllm-dev.slack.com/archives/C07V3D6F493/p1732803748800689). Considering that LoRA bias has been introduced for about 10 months now, there are almost no issues relate...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
