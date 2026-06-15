# vllm-project/vllm#15530: [Bug][Triton MLA]: Some calculation errors about triton mla kernal

| 字段 | 值 |
| --- | --- |
| Issue | [#15530](https://github.com/vllm-project/vllm/issues/15530) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug][Triton MLA]: Some calculation errors about triton mla kernal

### Issue 正文摘录

### Your current environment None ### 🐛 Describe the bug I integrated the **triton mla kernel** of vllm and found that when the batch is larger than 1, the last sequence sometimes cannot get the correct result. I have done some experiments on simpler cases, such as kvcache is all 0, and the ideal output is also all 0, but the last sequence will get all nan. Hope to receive a response, thanks. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: [Bug][Triton MLA]: Some calculation errors about triton mla kernal bug;stale ### Your current environment None ### 🐛 Describe the bug I integrated the **triton mla kernel** of vllm and found that when the batch is large...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ks. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug][Triton MLA]: Some calculation errors about triton mla kernal bug;stale ### Your current environment None ### 🐛 Describe the bug I integrated the **triton mla kernel** of vllm and found that when the batch is large...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
