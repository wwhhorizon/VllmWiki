# vllm-project/vllm#6226: [RFC] Drop beam search support

| 字段 | 值 |
| --- | --- |
| Issue | [#6226](https://github.com/vllm-project/vllm/issues/6226) |
| 状态 | closed |
| 标签 | RFC |
| 评论 | 42; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC] Drop beam search support

### Issue 正文摘录

~~**TL;DR: To reduce system complexity and enable future optimizations, we propose discontinuing beam search support.**~~ **Due to strong pushback from the community, we have decided to reconsider this proposal. vLLM will continue to support beam search until further notice. Thanks everyone for the feedback!** ### Motivation. Currently, vLLM supports 3 types of sampling: greedy, random, and beam search. Beam search, which dynamically creates and removes top-k branches at each step, is the most complex of the three. Traditionally, beam search has been popular for NLP tasks like translation and summarization. However, in the LLM era, beam search has become less common. Major LLM APIs such as GPT, Gemini, and Claude do not support it. In vLLM, beam search initially motivated the idea of PagedAttention. Actually, vLLM excels at beam search compared to other inference engines, since PagedAttention can efficiently handle the dynamic nature of beam search and minimize its KV cache usage. Despite this, implementing beam search introduces significant system complexity, hindering potential optimizations. It complicates the system while being used rarely. To resolve this, we propose eliminat...

## 候选优化模式

- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: an efficiently handle the dynamic nature of beam search and minimize its KV cache usage. Despite this, implementing beam search introduces significant system complexity, hindering potential optimizations. It complicates...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ach step. This leads to synchronization between the model runner and the scheduler. Removing beam search will be the first step to allow them to operate asynchronously. 3. **Potential Future Removal of SequenceGroup** -...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: rch support.**~~ **Due to strong pushback from the community, we have decided to reconsider this proposal. vLLM will continue to support beam search until further notice. Thanks everyone for the feedback!** ### Motivati...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: [RFC] Drop beam search support RFC ~~**TL;DR: To reduce system complexity and enable future optimizations, we propose discontinuing beam search support.**~~ **Due to strong pushback from the community, we have decided t...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: ampling, and this will greatly simplify the code. 2. **More Predictable Block Table** - Beam search causes the block table for PagedAttention to change dynamically at each step. This leads to synchronization between the...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
