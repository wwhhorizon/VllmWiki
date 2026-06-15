# vllm-project/vllm#36729: [Feature]: Fast KV Compaction via Attention Matching (50x compression)

| 字段 | 值 |
| --- | --- |
| Issue | [#36729](https://github.com/vllm-project/vllm/issues/36729) |
| 状态 | open |
| 标签 | feature request |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Fast KV Compaction via Attention Matching (50x compression)

### Issue 正文摘录

### 🚀 The feature, motivation and pitch I'm just forwarding a research paper i stumbled upon. https://arxiv.org/abs/2602.16284 This is the abstract: > Scaling language models to long contexts is often bottlenecked by the size of the key-value (KV) cache. In deployed settings, long contexts are typically managed through compaction in token space via summarization. However, summarization can be highly lossy, substantially harming downstream performance. Recent work on Cartridges has shown that it is possible to train highly compact KV caches in latent space that closely match full-context performance, but at the cost of slow and expensive end-to-end optimization. This work describes an approach for fast context compaction in latent space through Attention Matching, which constructs compact keys and values to reproduce attention outputs and preserve attention mass at a per-KV-head level. We show that this formulation naturally decomposes into simple subproblems, some of which admit efficient closed-form solutions. Within this framework, we develop a family of methods that significantly push the Pareto frontier of compaction time versus quality, achieving up to 50x compaction in secon...

## 候选优化模式

- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: through Attention Matching, which constructs compact keys and values to reproduce attention outputs and preserve attention mass at a per-KV-head level. We show that this formulation naturally decomposes into simple subp...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: on naturally decomposes into simple subproblems, some of which admit efficient closed-form solutions. Within this framework, we develop a family of methods that significantly push the Pareto frontier of compaction time...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: quest ### 🚀 The feature, motivation and pitch I'm just forwarding a research paper i stumbled upon. https://arxiv.org/abs/2602.16284 This is the abstract: > Scaling language models to long contexts is often bottlenecked...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: work on Cartridges has shown that it is possible to train highly compact KV caches in latent space that closely match full-context performance, but at the cost of slow and expensive end-to-end optimization. This work de...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ps://arxiv.org/abs/2602.16284 This is the abstract: > Scaling language models to long contexts is often bottlenecked by the size of the key-value (KV) cache. In deployed settings, long contexts are typically managed thr...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
