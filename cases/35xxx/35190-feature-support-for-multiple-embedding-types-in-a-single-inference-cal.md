# vllm-project/vllm#35190: [Feature]: Support for multiple embedding types in a single inference call

| 字段 | 值 |
| --- | --- |
| Issue | [#35190](https://github.com/vllm-project/vllm/issues/35190) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Support for multiple embedding types in a single inference call

### Issue 正文摘录

### 🚀 The feature, motivation and pitch With the recent release 0.15, vLLM added support for multi-vector retrieval (e.g., ColBERT-style token embeddings). However, current usage requires making one API call per vector type. For users requiring multiple representations (like dense and sparse vectors from a single model), this design is inefficient. It doubles the indexing overhead and requires two separate inference calls to the same embedding model. I would like vLLM to support returning multiple vector types in a single inference call, similar to the implementation found in specialized images like flag-embeddings. The API should allow a single request to return all supported embedding outputs (e.g., dense, sparse, colbert) simultaneously to minimize latency and redundant computation. ### Alternatives Current Workaround: Making two separate calls, which is not ideal for production due to doubled inference costs and increased network overhead. External Frameworks: Using custom model implementations (like flag-embeddings), but this prevents us from leveraging vLLM's optimized serving engine and PagedAttention for large-scale embedding tasks. ### Additional context This feature is c...

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: With the recent release 0.15, vLLM added support for multi-vector retrieval (e.g., ColBERT-style token embeddings). However, current usage requires making one API call per vector type. For users requiring multiple repre...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: Support for multiple embedding types in a single inference call feature request;stale ### 🚀 The feature, motivation and pitch With the recent release 0.15, vLLM added support for multi-vector retrieval (e.g., ColBERT-st...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: like dense and sparse vectors from a single model), this design is inefficient. It doubles the indexing overhead and requires two separate inference calls to the same embedding model. I would like vLLM to support return...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: leveraging vLLM's optimized serving engine and PagedAttention for large-scale embedding tasks. ### Additional context This feature is critical for high-performance RAG pipelines that use hybrid search (dense + sparse) o...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: feature is critical for high-performance RAG pipelines that use hybrid search (dense + sparse) or late interaction models (ColBERT). Efficiently retrieving all vector types in one pass would significantly improve indexi...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
