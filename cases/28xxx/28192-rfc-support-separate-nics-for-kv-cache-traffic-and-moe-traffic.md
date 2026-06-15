# vllm-project/vllm#28192: [RFC]: Support separate NICs for KV cache traffic and MoE traffic

| 字段 | 值 |
| --- | --- |
| Issue | [#28192](https://github.com/vllm-project/vllm/issues/28192) |
| 状态 | closed |
| 标签 | RFC;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Support separate NICs for KV cache traffic and MoE traffic

### Issue 正文摘录

### Motivation. In MoE models with large KV caches, KV cache all-to-all and MoE expert communication share the same RNIC, causing congestion and degrading performance. Using dedicated NICs for each traffic type can improve bandwidth utilization and reduce interference. ### Proposed Change. Does vLLM currently support routing KV cache traffic and MoE traffic through different NICs? ### Feedback Period. _No response_ ### CC List. _No response_ ### Any Other Things. _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: [RFC]: Support separate NICs for KV cache traffic and MoE traffic RFC;stale ### Motivation. In MoE models with large KV caches, KV cache all-to-all and MoE expert communication share the same RNIC, causing congestion an...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: reduce interference. ### Proposed Change. Does vLLM currently support routing KV cache traffic and MoE traffic through different NICs? ### Feedback Period. _No response_ ### CC List. _No response_ ### Any Other Things....
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: [RFC]: Support separate NICs for KV cache traffic and MoE traffic RFC;stale ### Motivation. In MoE models with large KV caches, KV cache all-to-all and MoE expert communication share the same RNIC, causing congestion an...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: s for KV cache traffic and MoE traffic RFC;stale ### Motivation. In MoE models with large KV caches, KV cache all-to-all and MoE expert communication share the same RNIC, causing congestion and degrading performance. Us...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
