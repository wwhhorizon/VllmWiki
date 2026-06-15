# vllm-project/vllm#35780: [RFC]: Remove Per-Block KV Transfer Error Handling

| 字段 | 值 |
| --- | --- |
| Issue | [#35780](https://github.com/vllm-project/vllm/issues/35780) |
| 状态 | open |
| 标签 | RFC |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Remove Per-Block KV Transfer Error Handling

### Issue 正文摘录

### Motivation. * logic is very complex to maintain and reason about * its making new features harder to land * its off by default ### Proposed Change. * remove it. handle errors at the request level (current default) ### Feedback Period. 1 week. ### CC List. cc @orozery @njhill @markmc @NickLucche @ApostaC @houseroad @sdavidbd - can you implement this as OOT if needed for your use case? ### Any Other Things. _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: [RFC]: Remove Per-Block KV Transfer Error Handling RFC ### Motivation. * logic is very complex to maintain and reason about * its making new features harder to land * its off by default ### Proposed Change. * remove it....
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: off by default ### Proposed Change. * remove it. handle errors at the request level (current default) ### Feedback Period. 1 week. ### CC List. cc @orozery @njhill @markmc @NickLucche @ApostaC @houseroad @sdavidbd - can...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
