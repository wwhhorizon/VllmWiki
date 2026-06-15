# vllm-project/vllm#38651: [RFC]: Add `max_tokens_per_doc` support for rerank and scoring endpoints

| 字段 | 值 |
| --- | --- |
| Issue | [#38651](https://github.com/vllm-project/vllm/issues/38651) |
| 状态 | closed |
| 标签 | RFC |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Add `max_tokens_per_doc` support for rerank and scoring endpoints

### Issue 正文摘录

## Motivation vLLM's reranking and scoring endpoints currently have no mechanism to truncate documents before processing. When users send long documents that exceed the model's context window, requests fail or produce degraded results. Both the [Cohere Rerank API](https://docs.cohere.com/reference/rerank) and [Jina Reranker API](https://jina.ai/en-US/reranker/) support a `max_tokens_per_doc` (or equivalent) parameter that truncates each document to a specified token limit before scoring. This is a standard feature in production reranking APIs that vLLM should support. PR #33315 by @hustxiayang introduced an initial implementation of this feature. This RFC formalizes the design — particularly around offline support, `PoolingParams` integration, and score template compatibility — to align on the approach and move toward merging. ## Proposed Change Add a `max_tokens_per_doc` parameter to the rerank/score request schema that truncates each document's token representation before model inference. The implementation should support both **online** (HTTP API) and **offline** (`LLM.score()` / `LLM.embed()`) usage paths. ### API Surface **Online (HTTP):** Add `max_tokens_per_doc: Optional[in...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: _per_doc` (or equivalent) parameter that truncates each document to a specified token limit before scoring. This is a standard feature in production reranking APIs that vLLM should support. PR #33315 by @hustxiayang int...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ivation vLLM's reranking and scoring endpoints currently have no mechanism to truncate documents before processing. When users send long documents that exceed the model's context window, requests fail or produce degrade...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: uments before processing. When users send long documents that exceed the model's context window, requests fail or produce degraded results. Both the [Cohere Rerank API](https://docs.cohere.com/reference/rerank) and [Jin...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: . When users send long documents that exceed the model's context window, requests fail or produce degraded results. Both the [Cohere Rerank API](https://docs.cohere.com/reference/rerank) and [Jina Reranker API](https://...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ints/openai/protocol.py` | Add field to rerank/score request models | | `tests/models/language/pooling/` | Add tests for truncation with cross-encoders and bi-encoders | ### Compatibility This must work correctly with s...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
