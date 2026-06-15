# vllm-project/vllm#6928: [Feature]: Support rerank models

| 字段 | 值 |
| --- | --- |
| Issue | [#6928](https://github.com/vllm-project/vllm/issues/6928) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 19; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Support rerank models

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Rerank models are essential to RAG workflow. There are quite a few models available, such as jina-reranker-v2. Some inference frameworks already support rerank models, for example, https://inference.readthedocs.io/en/latest/models/builtin/rerank/index.html Do we have plans to add support for this? What are the main steps if someone tries to implement?

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Feature]: Support rerank models feature request ### 🚀 The feature, motivation and pitch Rerank models are essential to RAG workflow. There are quite a few models available, such as jina-reranker-v2. Some inference fram...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature]: Support rerank models feature request ### 🚀 The feature, motivation and pitch Rerank models are essential to RAG workflow. There are quite a few models available, such as jina-reranker-v2. Some inference fram...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: upport rerank models, for example, https://inference.readthedocs.io/en/latest/models/builtin/rerank/index.html Do we have plans to add support for this? What are the main steps if someone tries to implement?

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
