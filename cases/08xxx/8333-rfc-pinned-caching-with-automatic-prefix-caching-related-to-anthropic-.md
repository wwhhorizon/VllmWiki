# vllm-project/vllm#8333: [RFC]: Pinned Caching with Automatic Prefix Caching (Related to Anthropic Prompt Caching API)

| 字段 | 值 |
| --- | --- |
| Issue | [#8333](https://github.com/vllm-project/vllm/issues/8333) |
| 状态 | closed |
| 标签 | RFC;stale |
| 评论 | 16; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Pinned Caching with Automatic Prefix Caching (Related to Anthropic Prompt Caching API)

### Issue 正文摘录

### Motivation. - When using automatic prefix caching that manages blocks in an LRU (Least Recently Used) manner, it would be useful to add a pinned caching feature, where blocks are retained until a Time to Live (TTL) expires or a specific duration is reached. - The Anthropic API supports [prompt caching](https://docs.anthropic.com/en/docs/build-with-claude/prompt-caching) with TTL, which refreshes as prompts and their corresponding blocks are reused. This functionality is currently not possible in vLLM, as prefix caching operates solely in LRU mode. - Adding pinned caching would enhance the control logic for caching by allowing additional flexibility. I am considering features such as TTL, fixed expiration times, and manual expiration for pinned caching. ### Proposed Change. - Managing pinned caching at the block level can be complex. I believe managing it at the sequence level would suffice. Therefore, a `PinnedCachingManager` will handle pinned caching sequences, placed directly under the `Scheduler`. - To reduce implementation complexity, pinned caching will only be supported for GPU memory and will not allow swapping into CPU memory. Pinned caching will be restricted to the...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: h Automatic Prefix Caching (Related to Anthropic Prompt Caching API) RFC;stale ### Motivation. - When using automatic prefix caching that manages blocks in an LRU (Least Recently Used) manner, it would be useful to add...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: re, where blocks are retained until a Time to Live (TTL) expires or a specific duration is reached. - The Anthropic API supports [prompt caching](https://docs.anthropic.com/en/docs/build-with-claude/prompt-caching) with...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 334 ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: uce implementation complexity, pinned caching will only be supported for GPU memory and will not allow swapping into CPU memory. Pinned caching will be restricted to the prefill stage to prevent swapping into CPU memory...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: tale ### Motivation. - When using automatic prefix caching that manages blocks in an LRU (Least Recently Used) manner, it would be useful to add a pinned caching feature, where blocks are retained until a Time to Live (...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
