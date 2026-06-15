# vllm-project/vllm#32659: [RFC]: Tracking follow-up progress on Encode–Prefill–Decode Disaggregation

| 字段 | 值 |
| --- | --- |
| Issue | [#32659](https://github.com/vllm-project/vllm/issues/32659) |
| 状态 | open |
| 标签 | RFC;unstale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Tracking follow-up progress on Encode–Prefill–Decode Disaggregation

### Issue 正文摘录

### Motivation. The EPD code #25233 has already been merged for a while. Since then, we have received some feedback and encountered issues in real-world scenarios. We hope to track these issues through RFCs, and we will continue to optimize and resolve them accordingly. ### Proposed Change. # Tasks - [x] Load encoder-only option (#30242) - [ ] Optimize the current EPD proxy implementation (#31017) - [x] Optimize remote cache checks in the scheduler (https://github.com/vllm-project/vllm/pull/32585) - [ ] [EPD] Support EC cache deallocation ([fake0fan/vllm#18](https://github.com/fake0fan/vllm/pull/18)) - [ ] MoonCake ECConnector (#30468) - [ ] Nixl ECConnector ([fake0fan/vllm#20](https://github.com/fake0fan/vllm/pull/20)) ### Feedback Period. _No response_ ### CC List. _No response_ ### Any Other Things. _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [RFC]: Tracking follow-up progress on Encode–Prefill–Decode Disaggregation RFC;unstale ### Motivation. The EPD code #25233 has already been merged for a while. Since then, we have received some feedback and encountered...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
