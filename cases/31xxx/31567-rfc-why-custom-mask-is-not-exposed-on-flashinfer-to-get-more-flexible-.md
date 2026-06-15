# vllm-project/vllm#31567: [RFC]: Why custom_mask is not exposed on FlashInfer to get more flexible use case?

| 字段 | 值 |
| --- | --- |
| Issue | [#31567](https://github.com/vllm-project/vllm/issues/31567) |
| 状态 | closed |
| 标签 | RFC;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Why custom_mask is not exposed on FlashInfer to get more flexible use case?

### Issue 正文摘录

### Motivation. Like what tensorrt-llm does https://github.com/NVIDIA/TensorRT-LLM/blob/6c1abf2d45c77d04121ebe10f6b29abf89373c60/tensorrt_llm/_torch/attention_backend/flashinfer.py#L411C17-L411C28 ### Proposed Change. expose the custom_weight to support use case like relative attention bias ### Feedback Period. _No response_ ### CC List. _No response_ ### Any Other Things. _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: [RFC]: Why custom_mask is not exposed on FlashInfer to get more flexible use case? RFC;stale ### Motivation. Like what tensorrt-llm does https://github.com/NVIDIA/TensorRT-LLM/blob/6c1abf2d45c77d04121ebe10f6b29abf89373c...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: tom_mask is not exposed on FlashInfer to get more flexible use case? RFC;stale ### Motivation. Like what tensorrt-llm does https://github.com/NVIDIA/TensorRT-LLM/blob/6c1abf2d45c77d04121ebe10f6b29abf89373c60/tensorrt_ll...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
