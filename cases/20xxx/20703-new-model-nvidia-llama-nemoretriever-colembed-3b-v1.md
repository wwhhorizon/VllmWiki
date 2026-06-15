# vllm-project/vllm#20703: [New Model]: nvidia/llama-nemoretriever-colembed-3b-v1

| 字段 | 值 |
| --- | --- |
| Issue | [#20703](https://github.com/vllm-project/vllm/issues/20703) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [New Model]: nvidia/llama-nemoretriever-colembed-3b-v1

### Issue 正文摘录

### The model to consider. The nvidia/llama-nemoretriever-colembed-3b-v1 is a late interaction embedding model fine-tuned for query-document retrieval. Users can input queries, which are text, or documents which are page images, to the model. The model outputs ColBERT-style multi-vector numerical representations for input queries and documents. It achieved 1st place on ViDoRe V1 (nDCG@5), ViDoRe V2 (nDCG@5) and MTEB VisualDocumentRetrieval (Rank Borda) (as of 27th June, 2025). ### The closest model vllm already supports. _No response_ ### What's your difficulty of supporting the model you want? _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: page images, to the model. The model outputs ColBERT-style multi-vector numerical representations for input queries and documents. It achieved 1st place on ViDoRe V1 (nDCG@5), ViDoRe V2 (nDCG@5) and MTEB VisualDocumentR...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [New Model]: nvidia/llama-nemoretriever-colembed-3b-v1 stale ### The model to consider. The nvidia/llama-nemoretriever-colembed-3b-v1 is a late interaction embedding model fine-tuned for query-document retrieval. Users...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: is a late interaction embedding model fine-tuned for query-document retrieval. Users can input queries, which are text, or documents which are page images, to the model. The model outputs ColBERT-style multi-vector nume...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [New Model]: nvidia/llama-nemoretriever-colembed-3b-v1 stale ### The model to consider. The nvidia/llama-nemoretriever-colembed-3b-v1 is a late interaction embedding model fine-tuned for query-document retrieval. Users...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
