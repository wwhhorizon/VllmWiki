# vllm-project/vllm#28407: [Feature]: Improve DCP error messages

| 字段 | 值 |
| --- | --- |
| Issue | [#28407](https://github.com/vllm-project/vllm/issues/28407) |
| 状态 | open |
| 标签 | good first issue;feature request;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Improve DCP error messages

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Currently if a backend doesn't support DCP we get the following error message ``` AssertionError: DCP requires attention impls to return the softmax lse for decode, but the impl FlashInferImpl does not return the softmax lse for decode. ``` It would good to suggest to the user to try an alternative backend using `VLLM_ATTENTION_BACKEND` ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Feature]: Improve DCP error messages good first issue;feature request;stale ### 🚀 The feature, motivation and pitch Currently if a backend doesn't support DCP we get the following error message ``` AssertionError: DCP...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: re request;stale ### 🚀 The feature, motivation and pitch Currently if a backend doesn't support DCP we get the following error message ``` AssertionError: DCP requires attention impls to return the softmax lse for decod...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: ``` AssertionError: DCP requires attention impls to return the softmax lse for decode, but the impl FlashInferImpl does not return the softmax lse for decode. ``` It would good to suggest to the user to try an alternati...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
