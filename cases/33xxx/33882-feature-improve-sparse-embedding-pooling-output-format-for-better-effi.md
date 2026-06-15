# vllm-project/vllm#33882: [Feature]: Improve sparse embedding pooling output format for better efficiency and usability

| 字段 | 值 |
| --- | --- |
| Issue | [#33882](https://github.com/vllm-project/vllm/issues/33882) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Improve sparse embedding pooling output format for better efficiency and usability

### Issue 正文摘录

### 🚀 The feature, motivation and pitch This issue is about the current output format of the sparse embedding pooling interface and how it impacts performance and usability. For models that support sparse embeddings, we typically need to store, for each document, the mapping from **token → weight** so we can use it later during retrieval. Currently, the vLLM `pooling` API returns only the **per-token weights** for each position in the document. This leads to two potential issues: 1. **Duplicate tokens in the document are not aggregated** Since the pooling output is per-position, repeated tokens in the same document are returned multiple times. This has a few consequences: The response becomes larger than necessary. Serialization of the response takes more CPU time and can become a bottleneck for vLLM inference. Downstream systems that only need a sparse representation per unique token have to do extra work to aggregate duplicates. 1. **The user has to manually run the tokenizer to reconstruct the mapping** The pooling interface currently returns weights only. To build the sparse representation that retrieval systems typically want (token_id → weight), users must: Run the tokenizer...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [Feature]: Improve sparse embedding pooling output format for better efficiency and usability feature request ### 🚀 The feature, motivation and pitch This issue is about the current output format of the sparse embedding...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Feature]: Improve sparse embedding pooling output format for better efficiency and usability feature request ### 🚀 The feature, motivation and pitch This issue is about the current output format of the sparse embedding...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: , the mapping from **token → weight** so we can use it later during retrieval. Currently, the vLLM `pooling` API returns only the **per-token weights** for each position in the document. This leads to two potential issu...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: rt sparse embeddings, we typically need to store, for each document, the mapping from **token → weight** so we can use it later during retrieval. Currently, the vLLM `pooling` API returns only the **per-token weights**...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
