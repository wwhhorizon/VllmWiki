# vllm-project/vllm#39579: Support SentenceTransformer Dense projection layers for embedding models (stella_en_1.5B_v5)

| 字段 | 值 |
| --- | --- |
| Issue | [#39579](https://github.com/vllm-project/vllm/issues/39579) |
| 状态 | open |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Support SentenceTransformer Dense projection layers for embedding models (stella_en_1.5B_v5)

### Issue 正文摘录

## Summary `stella_en_1.5B_v5` (and other SentenceTransformer models with a `2_Dense_*` projection layer) cannot be served correctly via vLLM's `--runner pooling` mode. vLLM only loads weights from the root `model.safetensors` and ignores the `modules.json` / `2_Dense_*` subdirectories that SentenceTransformer models use for linear projection layers. ## Impact stella_en_1.5B_v5 is the highest-performing open embedding model in the 1–2B parameter range on MTEB retrieval (nDCG@10: 61.01 — beats text-embedding-004's 55.70 and e5-mistral-7b's 56.89). It's widely used for RAG/semantic search pipelines. Without the projection layer, vLLM returns raw 1536-dim mean-pool vectors instead of the correct normalized 1024-dim embeddings. This produces embeddings that do not match sentence-transformers output and likely degrades retrieval quality significantly. ## Reproduction ```bash vllm serve dunzhang/stella_en_1.5B_v5 \ --runner pooling \ --trust-remote-code \ --dtype bfloat16 \ --override-pooler-config '{"pooling_type": "MEAN"}' ``` The server starts and returns embeddings, but they are 1536-dim instead of 1024-dim, and do not match sentence-transformers output because `2_Dense_1024/model.s...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: ang/stella_en_1.5B_v5 \ --runner pooling \ --trust-remote-code \ --dtype bfloat16 \ --override-pooler-config '{"pooling_type": "MEAN"}' ``` The server starts and returns embeddings, but they are 1536-dim instead of 1024...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: Support SentenceTransformer Dense projection layers for embedding models (stella_en_1.5B_v5) ## Summary `stella_en_1.5B_v5` (and other SentenceTransformer models with a `2_Dense_*` projection layer) cannot be served cor...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: nmerged PR attempting to add generic ST Dense projection loading (closed stale, Nov 2025) ## Workaround Currently the only correct way to serve stella is via sentence-transformers directly or [Infinity](https://github.c...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: performing open embedding model in the 1–2B parameter range on MTEB retrieval (nDCG@10: 61.01 — beats text-embedding-004's 55.70 and e5-mistral-7b's 56.89). It's widely used for RAG/semantic search pipelines. Without th...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: -volume pipelines. ## Request Either: 1. Revive and merge a cleaned-up version of #22614 2. Add a `SentenceTransformerDensePooler` to the vLLM pooling infrastructure that reads `modules.json` and loads projection layers...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
