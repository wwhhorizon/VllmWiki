# vllm-project/vllm#15710: [Feature]: Support Cascade Attention for Sliding Window Attention

| 字段 | 值 |
| --- | --- |
| Issue | [#15710](https://github.com/vllm-project/vllm/issues/15710) |
| 状态 | closed |
| 标签 | help wanted;good first issue;feature request;stale |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Support Cascade Attention for Sliding Window Attention

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Currently, vLLM does not support cascade attention for sliding window attention: https://github.com/vllm-project/vllm/blob/3b00ff91380044fa409612401309b9cb6a82685f/vllm/v1/attention/backends/flash_attn.py#L352-L354 However, it is technically possible to use it in specific cases. For instance, when the context lengths of all requests in the batch do not exceed the sliding window size, it functions the same as global attention, making it suitable for cascade attention. As such, we should expand the coverage of cascade attention with sliding window. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ention for Sliding Window Attention help wanted;good first issue;feature request;stale ### 🚀 The feature, motivation and pitch Currently, vLLM does not support cascade attention for sliding window attention: https://git...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ect/vllm/blob/3b00ff91380044fa409612401309b9cb6a82685f/vllm/v1/attention/backends/flash_attn.py#L352-L354 However, it is technically possible to use it in specific cases. For instance, when the context lengths of all re...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: h_attn.py#L352-L354 However, it is technically possible to use it in specific cases. For instance, when the context lengths of all requests in the batch do not exceed the sliding window size, it functions the same as gl...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
