# vllm-project/vllm#13827: [Feature]: Support for ColBERT (Late-Interaction Retrieval) in vLLM

| 字段 | 值 |
| --- | --- |
| Issue | [#13827](https://github.com/vllm-project/vllm/issues/13827) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Support for ColBERT (Late-Interaction Retrieval) in vLLM

### Issue 正文摘录

### 🚀 The feature, motivation and pitch We would like to request adding support for the ColBERT family of models (e.g., [colbert-ir/colbertv2.0](https://huggingface.co/colbert-ir/colbertv2.0)) in vLLM. ColBERT (“Contextualized Late Interaction over BERT”) is a retrieval model originally developed at Stanford. Unlike decoder-based LLMs (e.g., GPT, LLaMA) used for text generation, ColBERT is specifically designed for document retrieval with a “late-interaction” mechanism. At indexing time, documents are tokenized into multiple embedding vectors; at query time, ColBERT encodes the query tokens and does a specialized MaxSim scoring step against the document embeddings. This approach often achieves higher retrieval accuracy and better domain generalization than many dense-retrieval methods.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: pitch We would like to request adding support for the ColBERT family of models (e.g., [colbert-ir/colbertv2.0](https://huggingface.co/colbert-ir/colbertv2.0)) in vLLM. ColBERT (“Contextualized Late Interaction over BERT...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: ature]: Support for ColBERT (Late-Interaction Retrieval) in vLLM feature request;stale ### 🚀 The feature, motivation and pitch We would like to request adding support for the ColBERT family of models (e.g., [colbert-ir/...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [Feature]: Support for ColBERT (Late-Interaction Retrieval) in vLLM feature request;stale ### 🚀 The feature, motivation and pitch We would like to request adding support for the ColBERT family of models (e.g., [colbert-...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: t the document embeddings. This approach often achieves higher retrieval accuracy and better domain generalization than many dense-retrieval methods.
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: er-based LLMs (e.g., GPT, LLaMA) used for text generation, ColBERT is specifically designed for document retrieval with a “late-interaction” mechanism. At indexing time, documents are tokenized into multiple embedding v...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
