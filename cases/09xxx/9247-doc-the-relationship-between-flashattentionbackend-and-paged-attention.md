# vllm-project/vllm#9247: [Doc]: The relationship between FlashAttentionBackend and paged_attention_kernel

| 字段 | 值 |
| --- | --- |
| Issue | [#9247](https://github.com/vllm-project/vllm/issues/9247) |
| 状态 | closed |
| 标签 | documentation |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Doc]: The relationship between FlashAttentionBackend and paged_attention_kernel

### Issue 正文摘录

### 📚 The doc issue I read the [paged_attention_kernel ](https://docs.vllm.ai/en/latest/dev/kernel/paged_attention.html)part in the document, but I don’t know how FlashAttentionBackend is related to paged attention. hope to be able to explain the relationship between the two ### Suggest a potential alternative/fix _No response_ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: [Doc]: The relationship between FlashAttentionBackend and paged_attention_kernel documentation ### 📚 The doc issue I read the [paged_attention_kernel ](https://docs.vllm.ai/en/latest/dev/kernel/paged_attention.html)part...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Doc]: The relationship between FlashAttentionBackend and paged_attention_kernel documentation ### 📚 The doc issue I read the [paged_attention_kernel ](https://docs.vllm.ai/en/latest/dev/kernel/paged_attention.html)part...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: oc issue I read the [paged_attention_kernel ](https://docs.vllm.ai/en/latest/dev/kernel/paged_attention.html)part in the document, but I don’t know how FlashAttentionBackend is related to paged attention. hope to be abl...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
