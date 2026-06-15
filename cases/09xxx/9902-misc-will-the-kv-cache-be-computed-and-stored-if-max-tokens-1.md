# vllm-project/vllm#9902: [Misc]: Will the kv-cache be computed and stored if max_tokens=1?

| 字段 | 值 |
| --- | --- |
| Issue | [#9902](https://github.com/vllm-project/vllm/issues/9902) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Misc]: Will the kv-cache be computed and stored if max_tokens=1?

### Issue 正文摘录

### Anything you want to discuss about vllm. I have a specific use case where the output always consists of only one new token (i.e., max_tokens=1). This means that the model only goes through the prefill stage and never enters the decoding stage. Given this scenario, I have a few questions: - Computation of kv-cache: Will the kv-cache still be computed and stored even when max_tokens=1? - Optimization Opportunities: Are there any optimizations that can be applied to the kv-cache management in this specific use case to improve performance or reduce memory usage? Any insights or recommendations would be greatly appreciated! ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Misc]: Will the kv-cache be computed and stored if max_tokens=1? stale ### Anything you want to discuss about vllm. I have a specific use case where the output always consists of only one new token (i.e., max_tokens=1)...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: okens=1? stale ### Anything you want to discuss about vllm. I have a specific use case where the output always consists of only one new token (i.e., max_tokens=1). This means that the model only goes through the prefill...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ed! ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: [Misc]: Will the kv-cache be computed and stored if max_tokens=1? stale ### Anything you want to discuss about vllm. I have a specific use case where the output always consists of only one new token (i.e., max_tokens=1)...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: consists of only one new token (i.e., max_tokens=1). This means that the model only goes through the prefill stage and never enters the decoding stage. Given this scenario, I have a few questions: - Computation of kv-ca...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
