# vllm-project/vllm#458: Support embedding models

| 字段 | 值 |
| --- | --- |
| Issue | [#458](https://github.com/vllm-project/vllm/issues/458) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Support embedding models

### Issue 正文摘录

It would be nice if VLLM could serve Transformer-based embedding models (ex. BERT) as well. Having one host server that supports generative and embedding LLM APIs makes deployment of applications involving vector indexing easier (document retrieval and memory insertion into prompts). This may be related to #187 for BERT-derived models, since they are encoder-only.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: Support embedding models It would be nice if VLLM could serve Transformer-based embedding models (ex. BERT) as well. Having one host server that supports generative and embedding LLM APIs makes deployment of application...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ployment of applications involving vector indexing easier (document retrieval and memory insertion into prompts). This may be related to #187 for BERT-derived models, since they are encoder-only.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
