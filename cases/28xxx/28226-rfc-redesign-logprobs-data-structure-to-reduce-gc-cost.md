# vllm-project/vllm#28226: [RFC]: Redesign Logprobs data structure to reduce GC cost

| 字段 | 值 |
| --- | --- |
| Issue | [#28226](https://github.com/vllm-project/vllm/issues/28226) |
| 状态 | closed |
| 标签 | RFC;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Redesign Logprobs data structure to reduce GC cost

### Issue 正文摘录

# Motivation. ## High GC cost of list[dict[int, Logprob]] Currently, Logprobs are stored as list[dict[int, Logprob]], which means for each requests with logprobs enabled, it would create a lot of objects collected by GC - 1 list for each request - dictionaries for each position - * Logprob objects to store metadata So in total, there would be * + +1 objects allocated for a request and their lifecycle would last until the request finished. ## Background: GC costs By default, GC0 would be triggered every 700 objects allocation, GC1 would be triggered after every 10 GC0, GC2 would be triggered after every 10 GC1. For jobs that rely on logprobs, and especially for large batch size jobs, GC costs could be extremely high! # Proposed Change. ## Data Structure Proposal: FlattenLogprobs ### Structure: GC-friendly We're proposing a replacement of the list[dict[int, Logprob]], which flatten Logprob into a constant number of primitive type lists (i.e. FlattenLogprobs): - start_indices / end_indices: The range of indicies of logprobs for each position. - logprobs, token_ids, ranks, decoded_tokens: Flatten lists of logprob metadata With FlattenLogprobs, each requests would only introduce 6 obje...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [RFC]: Redesign Logprobs data structure to reduce GC cost RFC;stale # Motivation. ## High GC cost of list[dict[int, Logprob]] Currently, Logprobs are stored as list[dict[int, Logprob]], which means for each requests wit...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: h requests would only introduce 6 objects for GC, which is significantly smaller than * + +1 objects in the original list[dict] approach. ### Signature: Migration-friendly We're going to implement most of the list API t...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: be triggered after every 10 GC1. For jobs that rely on logprobs, and especially for large batch size jobs, GC costs could be extremely high! # Proposed Change. ## Data Structure Proposal: FlattenLogprobs ### Structure:...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: equest - dictionaries for each position - * Logprob objects to store metadata So in total, there would be * + +1 objects allocated for a request and their lifecycle would last until the request finished. ## Background:...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
